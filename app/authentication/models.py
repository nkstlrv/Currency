from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


# Custom User model
class User(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()
    
    def save(self, *args, **kwargs):
        if not self.username:
            pass
        
        super().save(*args, **kwargs)
        
    
