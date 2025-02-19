from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from  . import views
from .views import RegisterView, CustomLoginView, ProfileDetailView, CreatePostView, ProfileUpdateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:username>/', ProfileDetailView.as_view(), name='profile'),
    path('profile/<str:username>/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('create-post/', CreatePostView.as_view(), name='create_post'),
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    

    path('register/', RegisterView.as_view(), name='register'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)