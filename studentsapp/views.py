from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from . import forms
from . import models
from .forms import SignUpForm

def home(request):
    return render(request, 'home.html')

def details(request):
    return render(request, 'details.html')

def userLogin(request):
    return render(request, 'login.html')  

def create(request):
    return render(request, 'create_update.html')  

def ownStudents(request):
    return render(request, 'own_students.html')


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)  # ফর্মের পূর্বের ডাটা ধরে রাখার জন্য
#         if form.is_valid():
#             user = form.save()
#             login(request, user)    # user login directly when complete registratoin
#             messages.success(request, 'আপনার রেজিস্ট্রেশন সফল হয়েছে!')
#             return redirect('home')
#         else:
#             for field, errors in form.errors.items():
#                 for error in errors:
#                     messages.error(request, f" {form.fields[field].label}: {error}")
#     else:
#         form = SignUpForm()  # নতুন ফর্ম তৈরি

#     return render(request, 'login.html', {'form': form, 'signup': True})  # ফর্ম পাঠানো হচ্ছে

class signup(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)   # user login directly when complete registratoin
        messages.success(self.request, 'Registratoin successfully!!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        for field, errors in field.errors.items():
            for error in errors:
                messages.error(self.request, f"❌ {form.fields[field].label}: {error}")
    
    




