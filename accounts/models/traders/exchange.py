from django.db import models


class Exchange(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
