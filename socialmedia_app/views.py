from django.shortcuts import render
from django.http import HttpResponse

from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import login
from .forms import RegistrationForm


def home(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')


def login(request):
    return render(request, 'login.html')

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