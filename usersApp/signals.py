from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#this functions shall be fired every time a user is created to give them a default profile
#so when a user is saved send the signal "post_save" to this receiver and trigger the create_profile function
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()