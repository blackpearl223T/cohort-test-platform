from rest_framework import serializers
from .models import UserModel
from Cohort.models import Cohort
from Tests.models import Test, Question 
from django.contrib.auth import get_user_model

User = get_user_model

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields =["id", "username", "email", "password","Cohort"]


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