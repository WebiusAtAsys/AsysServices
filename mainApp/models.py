from django.db import models
from PIL import Image
from django.urls import reverse
from PIL import Image
#from usersApp.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

#Tuple Lists for select widgets:
#the tuples are in the form ('key', 'display')
LASER_SOURCES = [
    ('Innolas Blizz', 'Innolas Blizz'),
    ('Eolite', 'Eolite'),
    ('CO2', 'CO2')
]

MACHINE_CHOICES = [
    ('Divisio 9000', 'Divisio 9000'),
    ('Insignum 2000', 'Insignum 2000')
]

# Create your models here.
class Report(models.Model):
    #all reports have an associated author/user, when the user is deleted dont delete the reports
    author = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT, related_name="reports") #this will allow to query: thisUser.reports.all()
    date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=3000)
    laserSource = models.CharField(default="CO2", max_length=100, choices=LASER_SOURCES)
    machine = models.CharField(default="Divisio 9000", max_length=100, choices=MACHINE_CHOICES)
    image = models.ImageField(upload_to='report_pics')

    #this is the function which django tries to call after the submission of a post
    #reverse will return a path as a string so the view knows where to go
    def get_absolute_url(self):
        return reverse('report-detail', kwargs={'pk': self.pk})


    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)
    #     img.save(self.image.path)

    # def __str__(self):
    #     return f'{self.user.username} profile'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)