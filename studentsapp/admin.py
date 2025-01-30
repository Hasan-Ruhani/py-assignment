from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'phone', 'course', 'description', 'photo', 'created_at')  # Display in admin panel
    search_fields = ('name', 'email')  # Search functionality
    list_filter = ('course',)  # Filter option
    ordering = ('name',)  # Order the results

    def save_model(self, request, obj, form, change):
        if not obj.user:  # যদি `user` না থাকে, তাহলে `request.user` সেট করবো
            obj.user = request.user
        obj.save()

admin.site.register(Student, StudentAdmin)
