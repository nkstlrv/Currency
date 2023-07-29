from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


class User(AbstractUser):
    """
    Custom User model
    """
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()
    
    def save(self, *args, **kwargs):
        
        if not self.username:
            self.username = str(uuid4())
        
        super().save(*args, **kwargs)
        
    
