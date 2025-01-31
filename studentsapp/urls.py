from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('login/', views.UserLoginView.as_view(next_page='home'), name='userLogin'),
    path('signup/', views.signup.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page='userLogin'), name='user_logout'),


    path('', views.studentList.as_view(), name='home'),
    path('own/', views.ownStudents.as_view(), name='own'),
    path('details/<int:pk>/', views.studentDetails.as_view(), name='details'),
    path('create/', views.studentCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.studentUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.studentDelete.as_view(), name='delete')



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
