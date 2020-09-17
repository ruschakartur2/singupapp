from django.db import models
from django.contrib.auth.models import AbstractUser
import os


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    surname = models.CharField(null=True, blank=True, max_length=200)
    profile_image =  models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
