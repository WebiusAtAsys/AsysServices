from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(unique=True, null=True, max_length=20)
    has_reports = models.BooleanField(default=False)