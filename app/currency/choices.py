from django.utils.translation import gettext_lazy as _
from django.db import models


class RateCurrencyChoices(models.IntegerChoices):
    USD = 1, _("US Dollar")
    EUR = 2, _("Euro")
    UAH = 3, _("Hryvnia")
