from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/', views.details, name='details'),
    path('login/', views.userLogin, name='userLogin'),
    path('create/', views.create, name='create'),
    path('own/', views.ownStudents, name='own'),


    path('signup/', views.signup, name='signup'),
]
