from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    
    @property
    def is_student(self):
        return not self.is_teacher
    
    def __str__(self):
        return f"{self.username} ({'Teacher' if self.is_teacher else 'Student'})"

class Cohort(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taught_cohorts')
    
    def __str__(self):
        return self.name

class CohortMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cohort_memberships')
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='members')
    joined_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'cohort')
    
    def __str__(self):
        return f"{self.user.username} in {self.cohort.name}"