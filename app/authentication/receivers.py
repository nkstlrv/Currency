from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import User
from uuid import uuid4


@receiver(pre_save, sender=User)
def user_lower_email(instance, *args, **kwargs):
    if instance.email:
        instance.email = instance.email.lower()


@receiver(post_save, sender=User)
def user_set_username(instance, created, *args, **kwargs):
    if created and not instance.username:
        instance.username = str(uuid4())
