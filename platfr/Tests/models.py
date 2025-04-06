from django.db import models
from Cohort.models import Cohort


class Question(models.Model):
    text = models.TextField()
    choices = models.JSONField()
    correct_answer = models.CharField(max_length=100)


    def __str__(self):
        return self.text[:50]
    
class Test(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title

# Create your models here.
