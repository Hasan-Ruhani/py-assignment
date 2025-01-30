from django.db import models
import os
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.conf import settings

def student_directory_name(instance, filename):
    """Save image inside the media folder within the app with student name"""

    # Ensure MEDIA_ROOT is used as the base directory
    base_media_path = settings.MEDIA_ROOT  # This ensures all files are stored within MEDIA_ROOT

    # Create a student-specific folder
    student_folder = os.path.join(base_media_path, instance.name)

    # Ensure the directory exists
    os.makedirs(student_folder, exist_ok=True)  # Safer way to create folder

    # Return the path where the image will be saved
    return os.path.join(instance.name, filename)  # This ensures Django uses MEDIA_ROOT as base

def validate_image_file(value):
    """Validate uploaded image file size and format"""
    filesize = value.size
    ext = os.path.splitext(value.name)[1].lower()
    allowed_extensions = ['.jpg', '.jpeg', '.png']

    if filesize > 5 * 1024 * 1024:  # Restrict file size to max 5MB
        raise ValidationError("❌ Uploaded file size cannot exceed 5MB!")

    if ext not in allowed_extensions:  # Allow only specific image formats
        raise ValidationError("❌ Only JPG, JPEG, and PNG files are allowed!")

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    course = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    photo = models.ImageField(
        upload_to=student_directory_name, 
        validators=[validate_image_file], 
        blank=True,  # Existing students without photos remain valid
        null=True,   # Allow existing database records without images
        default=None # No default image, but required during updates
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
