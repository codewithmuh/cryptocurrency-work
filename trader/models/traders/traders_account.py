from accounts.models.user_profile import UserProfile
from django.db import models
from .exchange import Exchange
from .base_currency import BaseCurrency
import ccxt
import shrimpy
from .kucoin_password import KucoinPassword
from .okex_password import OkexPassword
from trading import settings
from .account_info import AccountInfo


class TraderAccounts(models.Model):

    trader = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=200, null=True, blank=True)
    account_name = models.CharField(max_length=100, null=True, blank=True)
    shrimpy_api_key = models.CharField(max_length=500, null=True, blank=True)
    shrimpy_secret_key = models.CharField(max_length=500, null=True, blank=True)
    password = models.CharField(max_length=250, null=True, blank=True)
    api_key = models.CharField(max_length=500, null=True, blank=True)
    api_secret = models.CharField(max_length=500, null=True, blank=True)
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    base_currency = models.ForeignKey(BaseCurrency, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    @staticmethod
    def shrimpy_client():
        client = shrimpy.ShrimpyApiClient(settings.SHRIMPY_API_KEY, settings.SHRIMPY_API_SECRET)

        return client

    @classmethod
    def create_trader_account(cls, trader, account_name, api_key, api_secret, exchange, base_currency, password=None):

        exchange, currency = cls.get_exchange_and_currency(exchange,base_currency)

        account_exist = cls.check_account_name_exist(account_name=account_name)

        if account_exist:
            res = 'exist'
            response = "Account name already exist"
        else:
            try:
                client = cls.shrimpy_client()

                create_user_response = client.create_user(account_name)
                create_user_data = create_user_response['error'][34:]
                print(create_user_data)

                user_id = create_user_data

                if user_id:
                    user_api_keys = client.create_api_keys(user_id)

                    exchange_name = exchange.name

                    passphrase = None if password is None else password

                    link_account_response = client.link_account(user_id, exchange_name.lower(), api_key,
                                                                api_secret, passphrase)

                    print(link_account_response)
                    account_id = link_account_response['id']

                    shrimpy_api_key = user_api_keys['publicKey']
                    shrimpy_secret = user_api_keys['privateKey']

                    account = cls.objects.create(
                        trader=trader,
                        user_id=user_id,
                        shrimpy_api_key=shrimpy_api_key,
                        shrimpy_secret_kry=shrimpy_secret,
                        password=passphrase,
                        api_key=api_key,
                        api_secret=api_secret,
                        exchange=exchange,
                        base_currency=base_currency
                    )
                    AccountInfo.objects.create(
                        trader_account=account,
                        account_id=account_id
                    )
                    res = "success"
                    response = "Account successfull created"
            except Exception as e:
                res = "error"
                response = "An Error occured {}".format(e)

        return res, response


    @staticmethod
    def get_exchange_and_currency(exchange, base_currency):
        exchange = Exchange.objects.filter(pk=exchange).first()
        currency = BaseCurrency.objects.filter(pk=base_currency).first()

        return exchange, currency

    @classmethod
    def check_account_name_exist(cls, account_name):

        trader_account = cls.objects.filter(account_name=account_name).first()

        if trader_account is not None:
            account_exist = True
        else:
            account_exist = False

        return account_exist

