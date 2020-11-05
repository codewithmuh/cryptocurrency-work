from django.db import models
from .traders_account import TraderAccounts


class AccountInfo(models.Model):
    trader_account = models.OneToOneField(TraderAccounts, on_delete=models.CASCADE)
    