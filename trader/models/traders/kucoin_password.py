from django.db import models


class KucoinPassword(models.Model):
    trader_account = models.OneToOneField("trader.TraderAccounts", on_delete=models.CASCADE)
    password = models.CharField(max_length=100, null=True, blank=True)