from django.db import models
from django.contrib.auth.models import AbstractUser
from Cohort.models import Cohort

class CustomUser(AbstractUser):
    Cohort= models.ForeignKey(Cohort, on_delete=models.SET_NULL, null=True, blank=True)
    is_teacher = models.BooleanField()

    def __str__(self):
        return self.username 

    


    
    




# Create your models here.
