from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from . import forms
from . import models
from .forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class studentList(ListView):
    model = models.Student
    template_name = 'home.html'
    context_object_name = 'students'

class ownStudents(LoginRequiredMixin, ListView):
    model = models.Student
    template_name = 'own_students.html'
    context_object_name = 'students'

    def get_queryset(self):
        return models.Student.objects.filter(user=self.request.user)
    
class studentDetails(DetailView):
    model = models.Student
    template_name = 'details.html'
    context_object_name = 'student'
    

class studentCreate(LoginRequiredMixin, CreateView):
    form_class = forms.StudentForm
    success_url = reverse_lazy('home')
    template_name = 'create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create'] = True 
        return context

    def form_valid(self, form):
        student = form.save(commit=False)
        student.user = self.request.user
        student.save()
        messages.add_message(self.request, messages.SUCCESS, 'Student create successfully.')
        return super().form_valid(form)
    
from django.core.exceptions import PermissionDenied

class studentUpdate(LoginRequiredMixin, UpdateView):
    """Update student details - Only allow the owner to edit"""
    model = models.Student
    form_class = forms.StudentForm
    template_name = 'create_update.html'
    success_url = reverse_lazy('own')

    def get_object(self, queryset=None):
        """Ensure only the student owner can edit"""
        obj = super().get_object(queryset)
        
        if obj.user != self.request.user:  # Check if the logged-in user is the owner
            raise PermissionDenied("You are not allowed to edit this student!")  # Restrict access
        
        return obj

    def form_valid(self, form):
        """Show success message on successful update"""
        messages.success(self.request, "Student updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        """Show error messages on form errors"""
        messages.error(self.request, "❌ Something went wrong! Please check the form.")
        return self.render_to_response(self.get_context_data(form=form))
    

class studentDelete(LoginRequiredMixin, DeleteView):
    """Allow only the owner to delete their students"""
    model = models.Student
    template_name = 'create_update.html'
    success_url = reverse_lazy('own')

    def get_object(self, queryset=None):
        """Ensure only the student owner can delete"""
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied("You are not allowed to delete this student!")
        return obj

    def delete(self, request, *args, **kwargs):
        """Show success message on successful delete"""
        messages.success(self.request, "Student deleted successfully!")
        return super().delete(request, *args, **kwargs)


class signup(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'login.html'
    success_url = reverse_lazy('userLogin')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['signup'] = True 
        return context

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)   # user login directly when complete registratoin
        messages.success(self.request, 'Registratoin successfully!!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"❌ {form.fields[field].label}: {error}")
        return self.render_to_response(self.get_context_data(form=form))
    
class UserLoginView(LoginView):
    template_name = "login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Login successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        if 'username' in form.errors:
            messages.error(self.request, "❌ Username or Email is incorrect!")
        if 'password' in form.errors:
            messages.error(self.request, "❌ Password is incorrect!")

        if form.non_field_errors():
            for error in form.non_field_errors():
                messages.error(self.request, f"❌ {error}")

        return self.render_to_response(self.get_context_data(form=form))
    
    

    

        
        
        
    
    
    




