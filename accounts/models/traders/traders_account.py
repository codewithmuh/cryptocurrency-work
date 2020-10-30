from accounts.models.user_profile import UserProfile
from django.db import models
from .exchange import Exchange
from .base_currency import BaseCurrency


class TraderAccounts(models.Model):
    trader = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100, null=True, blank=True)
    api_key = models.CharField(max_length=500, null=True, blank=True)
    api_secret = models.CharField(max_length=500, null=True, blank=True)
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    base_currency = models.ForeignKey(BaseCurrency, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    @classmethod
    def get_or_create_trader_account(cls, trader, account_name, api_key, api_secret, exchange, base_currency
                                     ):
        get_exchange = Exchange.objects.filter(pk=exchange).first()
        get_currency = BaseCurrency.objects.filter(pk=base_currency).first()

        trader_account = cls.objects.filter(account_name=account_name).first()

        if trader_account is not None:
            response = "exist"
        else:
            cls.objects.create(
                trader=trader,
                account_name=account_name,
                api_key=api_key,
                api_secret=api_secret,
                exchange=get_exchange,
                base_currency=get_currency
            )

            response = "saved"
            
        return response

