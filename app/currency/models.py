from django.db import models
from django.core.validators import MinValueValidator
from .choices import RateCurrencyChoices, RequestMethodChoices
from django.utils.translation import gettext_lazy as _


class Rate(models.Model):
    buy = models.DecimalField(
        max_digits=8, decimal_places=2, default=0, validators=[MinValueValidator(0)]
    )
    sell = models.DecimalField(
        max_digits=8, decimal_places=2, default=0, validators=[MinValueValidator(0)]
    )

    currency = models.PositiveSmallIntegerField(
        _("Currency"),
        max_length=3,
        choices=RateCurrencyChoices.choices,
        default=RateCurrencyChoices.USD,
    )

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
    request_method = models.PositiveSmallIntegerField(
        _("RequestMethod"),
        max_length=1,
        choices=RequestMethodChoices.choices,
        default=RequestMethodChoices.GET,
    )
    time = models.IntegerField()

    def __str__(self):
        return f"{self.request_method} | {self.path[0:10]} at {self.time}"
