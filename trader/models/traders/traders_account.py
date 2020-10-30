from accounts.models.user_profile import UserProfile
from django.db import models
from .exchange import Exchange
from .base_currency import BaseCurrency
import ccxt
from django.contrib import messages


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
    def get_or_create_trader_account(cls, trader, account_name, api_key,kucoin_password, api_secret, exchange, base_currency
                                     ):
        get_exchange = Exchange.objects.filter(pk=exchange).first()
        get_currency = BaseCurrency.objects.filter(pk=base_currency).first()

        trader_account = cls.objects.filter(account_name=account_name).first()

        if trader_account is not None:
            response = "exist"
        else:
            if exchange == "FTX":
                cls.verify_API_AND_SECRET_BINANCE()
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

    @staticmethod
    def verify_API_AND_SECRET_FTX(self, api_key, api_secret):
        try:
            ftx = ccxt.ftx({
                'apiKey': api_key,
                'secret': api_secret
            })

            fetch_balance = ftx.fetch_balance()
            message = True

            response = fetch_balance
        except Exception as e:
            message = False

            response = "An error occured: {}".format(e)

        return response, message

    @staticmethod
    def verify_API_AND_SECRET_KUCOIN(self, api_key, api_secret, kucoin_password):
        try:
            kucoin = ccxt.kucoin({
                'apiKey': api_key,
                'secret': api_secret,
                'password': kucoin_password
            })

            fetch_balance = kucoin.fetch_balance()

            message = "success"

            response = fetch_balance

        except Exception as e:
            message = "failed"

            response = "An error occured: {}".format(e)

        return response, message

    @staticmethod
    def verify_API_AND_SECRET_BINANCE(self, api_key, api_secret):
        try:
            binance = ccxt.binance({
                'apiKey': api_key,
                'secret': api_secret
            })

            fetch_balance = binance.fetch_balance()

            message = "success"

            response = fetch_balance

        except Exception as e:
            message = "failed"

            response = "An error occured: {}".format(e)

        return response, message

    @staticmethod
    def verify_API_AND_SECRET_KRAKEN(self, api_key, api_secret):
        try:
            kraken = ccxt.kraken({
                'apiKey': api_key,
                'secret': api_secret
            })

            fetch_balance = kraken.fetch_balance()

            message = "success"

            response = fetch_balance

        except Exception as e:
            message = "failed"

            response = "An error occured: {}".format(e)

        return response, message

    @staticmethod
    def verify_API_AND_SECRET_BYBIT(self, api_key, api_secret):
        try:
            bybit = ccxt.bybit({
                'apiKey': api_key,
                'secret': api_secret
            })

            fetch_balance = bybit.fetch_balance()

            message = "success"

            response = fetch_balance

        except Exception as e:
            message = "failed"

            response = "An error occured: {}".format(e)

        return response, message

    @staticmethod
    def verify_API_AND_SECRET_OKEX(self, api_key, api_secret, orex_password):
        try:
            okex = ccxt.okex({
                'apiKey': api_key,
                'secret': api_secret,
                'password': orex_password
            })

            fetch_balance = okex.fetch_balance()

            message = "success"

            response = fetch_balance

        except Exception as e:
            message = "failed"

            response = "An error occured: {}".format(e)

        return response, message

    @staticmethod
    def verify_API_AND_SECRET_HITBTC(self, api_key, api_secret):
        try:
            hitbtc = ccxt.hitbtc({
                'apiKey': api_key,
                'secret': api_secret
            })

            fetch_balance = hitbtc.fetch_balance()

            message = "success"

            response = fetch_balance

        except Exception as e:
            message = "failed"

            response = "An error occured: {}".format(e)

        return response, message




