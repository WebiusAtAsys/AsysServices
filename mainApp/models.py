from django.db import models
from PIL import Image
#from usersApp.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

#Tuple Lists for select widgets:
#the tuples are in the form ('key', 'display')
LASER_SOURCES = [
    ('Innolas Blizz', 'Innolas Blizz'),
    ('Eolite', 'Eolite'),
    ('CO2', 'CO2')
]

# Create your models here.
class Report(models.Model):
    #all reports have an associated author/user, when the user is deleted dont delete the reports
    author = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT, related_name="reports") #this will allow to query: thisUser.reports.all()
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=3000)
    laserSource = models.CharField(default="CO2", max_length=100, choices=LASER_SOURCES)
    image = models.ImageField(default='report.png', upload_to='report_pics')



    # def __str__(self):
    #     return f'{self.user.username} profile'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)