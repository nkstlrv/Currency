from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Custom User model
    """

    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ()

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = str(uuid4())

        # if self.email:
        #     self.email = self.email.lower()

        super().save(*args, **kwargs)
