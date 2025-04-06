from rest_framework import serializers
from .models import User, Cohort, CohortMembership

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_teacher']
        extra_kwargs = {
            'is_teacher': {'read_only': True}  # Prevent users from setting themselves as teachers
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_teacher']

class CohortSerializer(serializers.ModelSerializer):
    teacher = UserSerializer(read_only=True)
    
    class Meta:
        model = Cohort
        fields = ['id', 'name', 'description', 'created_at', 'teacher']

class CohortDetailSerializer(CohortSerializer):
    members = serializers.SerializerMethodField()
    
    class Meta(CohortSerializer.Meta):
        fields = CohortSerializer.Meta.fields + ['members']
    
    def get_members(self, obj):
        from cohorts.serializers import UserSerializer
        members = obj.members.all()
        return UserSerializer(members, many=True).data

class CohortMembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    cohort = CohortSerializer(read_only=True)
    
    class Meta:
        model = CohortMembership
        fields = ['id', 'user', 'cohort', 'joined_at']

class AddStudentToCohortSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()