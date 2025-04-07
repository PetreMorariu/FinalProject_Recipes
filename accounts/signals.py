#This will dispatch a signal to create a new profile for a newly created user.

from django.db.models.signals import post_save #post_save is a signal that gets activated when an object is saved
from django.contrib.auth.models import User #this is the sender
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()