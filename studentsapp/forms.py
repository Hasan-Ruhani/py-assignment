from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import re
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        exclude = ['user']

    def clean_email(self):
        """Ensure email is unique (ignoring current student) and is a valid email address."""
        email = self.cleaned_data.get('email')

        # Validate email format
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("Enter a valid email address.")

        # Check uniqueness
        if models.Student.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError("This email already exists!")

        return email

    def clean_phone(self):
        """Ensure phone number is unique and valid"""
        phone = self.cleaned_data.get('phone')

        # Remove spaces and dashes to normalize input
        phone = phone.replace(" ", "").replace("-", "")

        # Check if the phone number starts with +880 or 01
        if phone.startswith("+880"):
            phone = phone[4:]  # Remove '+880' and keep the rest
        elif phone.startswith("880"):
            phone = phone[3:]  # Remove '880' and keep the rest

        # Ensure the number now starts with a valid BD prefix
        if not re.match(r'^(013|014|015|016|017|018|019)\d{8}$', phone):
            raise ValidationError("Invalid phone number format!")

        # Check if the number is already used by another student
        if models.Student.objects.filter(phone=phone).exclude(pk=self.instance.pk).exists():
            raise ValidationError("This phone number is already in use by another student!")

        return phone
    
    def clean_photo(self):
        """Ensure photo is required for new students and during update if missing"""
        photo = self.cleaned_data.get('photo')

        # If this is a new student and no file is uploaded, show error
        if not self.instance.pk and not photo:
            raise ValidationError("A profile photo is required for new students!")

        # If existing student is updating and has no photo, they must upload one
        if self.instance.pk and not self.instance.photo and not photo:
            raise ValidationError("You must upload a profile photo before updating your information!")

        return photo

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full border rounded-xl p-3'}))

    def clean(self):
        cleaned_data = super().clean()
        username_or_email = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user = None


        if User.objects.filter(email=username_or_email).exists():
            user = User.objects.get(email=username_or_email) 
        elif User.objects.filter(username=username_or_email).exists():
            user = User.objects.get(username=username_or_email) 

        if user is None:
            raise forms.ValidationError("❌ User does not exist!") 

        cleaned_data["username"] = user.username 
        return cleaned_data