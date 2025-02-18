from django.db import models
import os
from django.contrib.auth.models import User

# if useing image field so first install this library must 'pip install Pillow'


def post_image(instance, filename):                      # create directory for each seperae student
    return os.path.join('socialmedia_app/media/', instance.name, filename)


class Post(models.Model):
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=post_image, default=None, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description[:10] + "..." if len(self.description) > 10 else self.description

