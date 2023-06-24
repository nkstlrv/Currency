from django.db import models


class Rate(models.Model):
    
    buy = models.DecimalField(max_digits=8, decimal_places=2)
    sell = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=3)
    source = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)


class ContuctUs(models.Model):
    pass


