from django.db import models
from django.db import models

# Create your models here.
class Filltexts(models.Model):
    title = models.CharField(max_length=100)
    fillText = models.TextField(max_length=3000)