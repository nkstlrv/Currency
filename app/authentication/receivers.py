from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import User


@receiver(pre_save, sender=User)
def user_pre_save(instance, *args, **kwargs):
    if instance.email:
        instance.email = instance.email.lower()

    ...
