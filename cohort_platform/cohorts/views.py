from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from .models import Cohort, CohortMembership
from .serializers import (
    UserRegistrationSerializer, UserSerializer, 
    CohortSerializer, CohortDetailSerializer,
    CohortMembershipSerializer, AddStudentToCohortSerializer
)
from .permissions import IsTeacher, IsStudent, IsCohortTeacher, IsCohortMember

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def register(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user).data,
            'message': 'User created successfully'
        }, status=status.HTTP_201_CREATED)

class CohortViewSet(viewsets.ModelViewSet):
    queryset = Cohort.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CohortDetailSerializer
        return CohortSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'add_student']:
            permission_classes = [IsTeacher]
        elif self.action in ['join']:
            permission_classes = [IsStudent]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)
    
    @action(detail=True, methods=['post'])
    def join(self, request, pk=None):
        cohort = self.get_object()
        if CohortMembership.objects.filter(user=request.user, cohort=cohort).exists():
            return Response({'detail': 'Already a member'}, status=status.HTTP_400_BAD_REQUEST)
        
        CohortMembership.objects.create(user=request.user, cohort=cohort)
        return Response({'detail': 'Joined cohort successfully'}, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['post'], permission_classes=[IsTeacher])
    def add_student(self, request, pk=None):
        cohort = self.get_object()
        serializer = AddStudentToCohortSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            user = User.objects.get(id=serializer.validated_data['user_id'])
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if CohortMembership.objects.filter(user=user, cohort=cohort).exists():
            return Response({'detail': 'User already in cohort'}, status=status.HTTP_400_BAD_REQUEST)
        
        CohortMembership.objects.create(user=user, cohort=cohort)
        return Response({'detail': 'Student added to cohort successfully'}, status=status.HTTP_201_CREATED)
    
    @action(detail=False)
    def my_cohorts(self, request):
        if request.user.is_teacher:
            cohorts = self.queryset.filter(teacher=request.user)
            serializer = self.get_serializer(cohorts, many=True)
        else:
            memberships = CohortMembership.objects.filter(user=request.user)
            serializer = CohortMembershipSerializer(memberships, many=True)
        return Response(serializer.data)

class CohortMembershipViewSet(viewsets.ModelViewSet):
    queryset = CohortMembership.objects.all()
    serializer_class = CohortMembershipSerializer
    permission_classes = [IsTeacher]