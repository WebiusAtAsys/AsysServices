from django.db import models
from PIL import Image

# Create your models here.
class Report(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=3000)
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