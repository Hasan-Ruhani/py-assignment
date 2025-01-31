from django.db import models
import os
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.conf import settings

def student_directory_name(instance, filename):
    """Save image inside the current Django app's media folder with student name"""
    
    # Get the app name dynamically (assuming the app is inside BASE_DIR)
    app_name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))  # Get the current app name

    # Define app-specific media directory
    app_media_folder = os.path.join(settings.BASE_DIR, app_name, "media")

    # Create a folder for each student inside the app's media directory
    student_folder = os.path.join(app_media_folder, instance.name)

    # Ensure the directory exists
    if not os.path.exists(student_folder):
        os.makedirs(student_folder)  # Create folder if it doesn't exist

    # Return the path where the image will be saved
    return os.path.join(student_folder, filename)

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
