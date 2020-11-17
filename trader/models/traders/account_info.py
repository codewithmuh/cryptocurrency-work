from django.db import models


class AccountInfo(models.Model):
    trader_account = models.OneToOneField('trader.TraderAccounts', on_delete=models.CASCADE)
    account_id = models.IntegerField(null=True, blank=True)
    account_balance = models.FloatField(null=True, blank=True)