from django.db import models
import os
from django.contrib.auth.models import User

def student_directory_name(instance, filename):                      # create directory for each seperae student
    return os.path.join('students/media/', instance.name, filename)

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    course = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    photo = models.ImageField(upload_to=student_directory_name, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
