from django.db import models
from django.contrib.auth.models import User


class Rate(models.Model):
    
    buy = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    sell = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    currency = models.CharField(max_length=3, unique=True, blank=False, null=False)
    source = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"For {self.currency} --> Buy: {self.buy} | Sell: {self.sell}"


class ContuctUs(models.Model):
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    email_from = models.EmailField(blank=False, null=False)
    subject = models.CharField(max_length=255, blank=False, null=False)
    message = models.TextField(max_length=2500)
    
    def __str__(self):
        return f"{self.subject} | {self.message} | by {self.email_from}"


