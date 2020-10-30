from accounts.models.user_profile import UserProfile
from django.db import models
from .exchange import Exchange
from .base_currency import BaseCurrency
import ccxt
from django.contrib import messages
from .kucoin_password import KucoinPassword
from .okex_password import OkexPassword


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
    def create_trader_account(cls, trader, account_name, api_key, api_secret, exchange, base_currency):

        account = cls.objects.create(
            trader=trader,
            account_name=account_name,
            api_key=api_key,
            api_secret=api_secret,
            exchange=get_exchange,
            base_currency=get_currency
        )
        return account

    @classmethod
    def get_or_create_trader_account(cls, trader, account_name, api_key,kucoin_password, okex_password, api_secret, exchange, base_currency
                                     ):
        get_exchange = Exchange.objects.filter(pk=exchange).first()
        get_currency = BaseCurrency.objects.filter(pk=base_currency).first()

        trader_account = cls.objects.filter(account_name=account_name).first()

        if trader_account is not None:
            res = "exist"
        else:
            if get_exchange == "FTX":
                response, message = cls.verify_API_AND_SECRET_FTX(api_key, api_secret)
                if message:
                    cls.create_trader_account(trader, account_name, api_key, get_exchange, get_currency)
                    res = "saved"
                else:
                    res = "error"

            if get_exchange == "BINANCE":
                response, message = cls.verify_API_AND_SECRET_BINANCE(api_key, api_secret)
                if message:
                    cls.create_trader_account(trader, account_name, api_key, get_exchange, get_currency)
                    res = "saved"
                else:
                    res = "error"

            if get_exchange == "KUCOIN":
                response, message = cls.verify_API_AND_SECRET_KUCOIN(api_key, api_secret, kucoin_password)
                if message:
                    account = cls.create_trader_account(trader, account_name, api_key, get_exchange, get_currency)
                    KucoinPassword.objects.create(
                        trader_account=account,
                        password=kucoin_password
                    )
                    res = "saved"
                else:
                    res = "error"

            if get_exchange == "BINANCE-FUTURE":
                response, message = cls.verify_API_AND_SECRET_BINANCE(api_key, api_secret)
                if message:
                    cls.create_trader_account(trader, account_name, api_key, get_exchange, get_currency)
                    res = "saved"
                else:
                    res = "error"

            if get_exchange == "FTX-US":
                response, message = cls.verify_API_AND_SECRET_FTX(api_key, api_secret)
                if message:
                    cls.create_trader_account(trader, account_name, api_key, get_exchange, get_currency)
                    res = "saved"
                else:
                    res = "error"

            if get_exchange == "BYBIT":
                response, message = cls.verify_API_AND_SECRET_BYBIT(api_key, api_secret)
                if message:
                    cls.create_trader_account(trader, account_name, api_key, get_exchange, get_currency)
                    res = "saved"
                else:
                    res = "error"

            if get_exchange == "HITBTC":
                response, message = cls.verify_API_AND_SECRET_HITBTC(api_key, api_secret)
                if message:
                    cls.create_trader_account(trader, account_name, api_key, get_exchange, get_currency)
                    res = "saved"
                else:
                    res = "error"

            if get_exchange == "KRAKEN":
                response, message = cls.verify_API_AND_SECRET_KRAKEN(api_key, api_secret)
                if message:
                    cls.create_trader_account(trader, account_name, api_key, get_exchange, get_currency)
                    res = "saved"
                else:
                    res = "error"

            if get_exchange == "OKEX":
                response, message = cls.verify_API_AND_SECRET_OKEX(api_key, api_secret, okex_password)
                if message:
                    account = cls.create_trader_account(trader, account_name, api_key, get_exchange, get_currency)
                    OkexPassword.objects.create(
                        trader_account=account,
                        password=okex_password
                    )
                    res = "saved"
                else:
                    res = "error"

            if get_exchange == "DERIBIT":
                response, message = cls.verify_API_AND_SECRET_DERIBIT(api_key, api_secret)
                if message:
                    cls.create_trader_account(trader, account_name, api_key, get_exchange, get_currency)
                    res = "saved"
                else:
                    res = "error"
            
        return res, response

    @staticmethod
    def verify_API_AND_SECRET_FTX(api_key, api_secret):
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
    def verify_API_AND_SECRET_KUCOIN(api_key, api_secret, kucoin_password):
        try:
            kucoin = ccxt.kucoin({
                'apiKey': api_key,
                'secret': api_secret,
                'password': kucoin_password
            })

            fetch_balance = kucoin.fetch_balance()

            message = True

            response = fetch_balance

        except Exception as e:
            message = False

            response = "An error occured: {}".format(e)

        return response, message

    @staticmethod
    def verify_API_AND_SECRET_BINANCE(api_key, api_secret):
        try:
            binance = ccxt.binance({
                'apiKey': api_key,
                'secret': api_secret
            })

            fetch_balance = binance.fetch_balance()

            message = True

            response = fetch_balance

        except Exception as e:
            message = False

            response = "An error occured: {}".format(e)

        return response, message

    @staticmethod
    def verify_API_AND_SECRET_KRAKEN(api_key, api_secret):
        try:
            kraken = ccxt.kraken({
                'apiKey': api_key,
                'secret': api_secret
            })

            fetch_balance = kraken.fetch_balance()

            message = True

            response = fetch_balance

        except Exception as e:
            message = False

            response = "An error occured: {}".format(e)

        return response, message

    @staticmethod
    def verify_API_AND_SECRET_BYBIT(api_key, api_secret):
        try:
            bybit = ccxt.bybit({
                'apiKey': api_key,
                'secret': api_secret
            })

            fetch_balance = bybit.fetch_balance()

            message = True

            response = fetch_balance

        except Exception as e:
            message = False

            response = "An error occured: {}".format(e)

        return response, message

    @staticmethod
    def verify_API_AND_SECRET_OKEX(api_key, api_secret, orex_password):
        try:
            okex = ccxt.okex({
                'apiKey': api_key,
                'secret': api_secret,
                'password': orex_password
            })

            fetch_balance = okex.fetch_balance()

            message = True

            response = fetch_balance

        except Exception as e:
            message = False

            response = "An error occured: {}".format(e)

        return response, message

    @staticmethod
    def verify_API_AND_SECRET_HITBTC(api_key, api_secret):
        try:
            hitbtc = ccxt.hitbtc({
                'apiKey': api_key,
                'secret': api_secret
            })

            fetch_balance = hitbtc.fetch_balance()

            message = True

            response = fetch_balance

        except Exception as e:
            message = False

            response = "An error occured: {}".format(e)

        return response, message

    @staticmethod
    def verify_API_AND_SECRET_DERIBIT(api_key, api_secret):
        try:
            deribit = ccxt.deribit({
                'apiKey': api_key,
                'secret': api_secret
            })

            fetch_balance = deribit.fetch_balance()

            message = True

            response = fetch_balance

        except Exception as e:
            message = False

            response = "An error occured: {}".format(e)

        return response, message




