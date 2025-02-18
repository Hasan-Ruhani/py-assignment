from django.urls import path
from  . import views
from .views import RegisterView

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('userlogin/', views.login, name='login'),


    path('register/', RegisterView.as_view(), name='register'),
]
