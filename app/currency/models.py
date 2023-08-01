from django.db import models
from django.core.validators import MinValueValidator
from .choices import RateCurrencyChoices
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Rate(models.Model):
    buy = models.DecimalField(
        max_digits=8, decimal_places=2, default=0, validators=[MinValueValidator(0)]
    )
    sell = models.DecimalField(
        max_digits=8, decimal_places=2, default=0, validators=[MinValueValidator(0)]
    )

    currency = models.PositiveSmallIntegerField(
        _("Currency"),
        choices=RateCurrencyChoices.choices,
        default=RateCurrencyChoices.USD,
    )

    created = models.DateTimeField(auto_now_add=True)
    source = models.ForeignKey("currency.Source", on_delete=models.CASCADE, related_name='rates')

    def __str__(self):
        return f"For {self.currency} --> Buy: {self.buy} | Sell: {self.sell}"


class ContactUs(models.Model):
    email_from = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=2500)

    def __str__(self):
        return f"{self.subject} | {self.message} | by {self.email_from}"

    class Meta:
        verbose_name = "ContactUs"
        verbose_name_plural = "ContactUs"


class Source(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} | {self.url}"


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10, default="GET")
    status_code = models.IntegerField(default=200)
    created = models.DateTimeField(default=timezone.now, blank=True)

    # Changed from Integer to Float because middleware time is usually < 0
    time = models.DecimalField(decimal_places=3, max_digits=6)

    def __str__(self):
        return f"{self.method} | {self.path[0:10]} at {self.created} for {self.time}"
