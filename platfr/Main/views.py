
from django.contrib.auth import authenticate, login, logout
from .form import RegisterForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from .serializers import RegisterSerializer, LoginSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



@method_decorator(csrf_exempt, name='dispatch')
class RegisterAPI(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@method_decorator(csrf_exempt, name='dispatch')
class LoginAPI(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            Cohort = serializer.validated_data["Cohort"]
            user = authenticate(username=username, password=password, Cohort=Cohort)
            if user:
                login(request, user)
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











#def home(request):
    #return HttpResponse("Welcome to the homepage!")
    

#def login(request):
   # if request.method == "POST":
        #form = AuthenticationForm(request, data=request.POST)
       # if form.isvalid():
         #   print("cool")
           # username = form.cleaned_data.get("username")
           # password = form.cleaned_data.get("password")
           # Cohort   = form.cleaned_data.get("Cohort")
           # (username, password, Cohort)
            #user = authenticate(username=username,password=password,Cohort=Cohort)
           # if user is not None:
               # login(request,user)
              #  return redirect('home')
           # else:
           #     print("Authentication failed")
             #   form.add_error(None, "Invalid username or password or Cohort")

    #else:
      #  form = AuthenticationForm()

   # return render(request, 'registration/login.html', {'form': form})

#def register(request):
   # if request.method == "POST":
     #   form = RegisterForm(request.POST)
     #   print("Form submitted")
       # if form.is_valid():
        #    print("Form is Valid")
         #   user = form.save()
          #  print(f"User created: {user.username}")
          #  login(request, user)
          #  return redirect("/home")
      #  else:
        #    print("Form errors:", form.errors)

    #else:
     #   form = RegisterForm()
   # return render(request, "register/register.html", {"form": form})








# Create your views here.
