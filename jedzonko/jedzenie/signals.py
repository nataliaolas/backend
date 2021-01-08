from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Wlasciciel

@receiver(post_save, sender=User)
def create_user_wlasciciel(sender, instance, created, **kwargs):
    if created:
        Wlasciciel.objects.create(user=instance)
    instance.wlasciciel.save()
