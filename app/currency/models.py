from django.db import models
from django.core.validators import MinValueValidator

# from django.contrib.auth.models import User


class Rate(models.Model):
    buy = models.DecimalField(max_digits=8, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    sell = models.DecimalField(max_digits=8, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    currency = models.CharField(max_length=4)
    source = models.CharField(max_length=255, default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"For {self.currency} --> Buy: {self.buy} | Sell: {self.sell}"


class ContactUs(models.Model):
    email_from = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=2500)

    def __str__(self):
        return f"{self.subject} | {self.message} | by {self.email_from}"


class Source(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} | {self.url}"
