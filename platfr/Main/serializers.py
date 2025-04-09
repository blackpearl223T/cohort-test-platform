from rest_framework import serializers
from .models import CustomUser
from Cohort.models import Cohort
from Tests.models import Test, Question 
from django.contrib.auth import get_user_model


User = get_user_model()

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields =["id", "username", "email", "password","Cohort"]


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_teacher']
        

    def create(self, validated_data):
        if validated_data.get("is_teacher",False):
            user = User.objects.create_superuser(
                username=validated_data['username'],
                email=validated_data.get('email', ''),
                password=validated_data['password'],
                is_teacher=True
                )
            
        else:
            user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            
        )
        return user
        


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    Cohort = serializers.BooleanField()

    


class CohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cohort
        fields = ['id', 'name']
        

class questionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'choices', 'correct_answer']



class TestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'title', 'Cohort', 'questions']