from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, CreateView, UpdateView, DetailView
from django.contrib.auth import login
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.views import View

from .forms import PostForm, RegistrationForm, ProfileUpdateForm
from .models import Post, Profile


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
from .models import Post
from .forms import PostForm





def home(request):
    return render(request, 'index.html')

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'  # Pass profile data to the template

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])  # Allow viewing any profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user=self.object.user).order_by('-created_at')  # Get user's posts
        context['can_edit'] = self.request.user.is_authenticated and self.request.user == self.object.user  # Check if logged-in user owns the profile
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profile_edit.html'

    def get_object(self):
        return self.request.user.profile  # Only allow users to edit their own profile

    def form_valid(self, form):
        messages.success(self.request, "Profile updated successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})  # Redirect to profile page after update


class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Registration successful!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Registration failed! Please try again later.")
        return self.render_to_response(self.get_context_data(form=form))
    

class CustomLoginView(LoginView):
    def form_invalid(self, form):
        messages.error(self.request, "Invalid username/email or password. Please try again!")
        return super().form_invalid(form)
    
    def form_valid(self, form):
        messages.success(self.request, "Login successful! Welcome back.")
        return super().form_valid(form)