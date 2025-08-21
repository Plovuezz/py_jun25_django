from typing import Type

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def my_handler(instance: User, **kwargs):
    if instance.is_active and not hasattr(instance, "profile"):
        Profile.objects.create(user=instance)
