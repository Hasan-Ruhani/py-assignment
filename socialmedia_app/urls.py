from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from  . import views
from .views import home, RegisterView, CustomLoginView, ProfileDetailView, ProfileUpdateView, ProfilePostCreateView, ProfilePostUpdateView
from django.contrib.auth import views as auth_views

urlpatterns = [


    path('profile/<str:username>/post/create/', ProfilePostCreateView.as_view(), name='profile_post_create'),
    path('profile/<str:username>/post/edit/<int:pk>/', ProfilePostUpdateView.as_view(), name='profile_post_edit'),


    path('', home.as_view(), name='home'),
    path('profile/<str:username>/', ProfileDetailView.as_view(), name='profile'),
    path('profile/<str:username>/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    

    path('register/', RegisterView.as_view(), name='register'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)