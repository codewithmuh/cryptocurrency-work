from django.db import models


class BaseCurrency(models.Model):
    currency = models.CharField(max_length=30, null=True, blank=True)