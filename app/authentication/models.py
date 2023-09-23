from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Custom User model
    """

    # phone_number = models.CharField(_("phone number"), max_length=15, unique=True)
    email = models.EmailField(_("email address"), max_length=50, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ()
