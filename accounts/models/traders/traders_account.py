from accounts.models.user_profile import UserProfile
from django.db import models
from .exchange import Exchange
from accounts.models.traders.base_currency import BaseCurrency


class TraderAccounts(models.Model):
    trader = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100, null=True, blank=True)
    api_key = models.CharField(max_length=500, null=True, blank=True)
    api_secret = models.CharField(max_length=500, null=True, blank=True)
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    base_currency = models.ForeignKey(BaseCurrency, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
