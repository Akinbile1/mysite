from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    # Additional fields can be added here if needed
    pass

class Tutor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='tutor_profile')
    # Additional tutor-specific fields
    qualification = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.user

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    grade = models.CharField(max_length=50)  # Adjusted max_length to accommodate longer grade names
    subject = models.CharField(max_length=100)  # Added field for the subject the student is trying to learn

    def __str__(self):
        return self.user
    