from accounts.models.user_profile import UserProfile
from django.db import models
from .exchange import Exchange
from .base_currency import BaseCurrency
import ccxt
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
            exchange=exchange,
            base_currency=base_currency
        )
        return account


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

    def trader_account_update(self, account_name, api_key,kucoin_password, okex_password, api_secret, exchange, base_currency):
        self.account_name = account_name
        self.exchange = exchange
        self.base_currency = base_currency
        self.api_key = api_key
        self.api_secret = api_secret
        self.save()

        if kucoin_password:
            kucoin_pass = KucoinPassword.objects.filter(trader_account=self).first()
            if kucoin_pass is not None:
                kucoin_pass.password = kucoin_password
                kucoin_pass.save()
        if okex_password:
            okex_pass = OkexPassword.objects.filter(trader_account=self).first()
            if okex_pass is not None:
                okex_pass.password = okex_password
                okex_pass.save()


    @classmethod
    def update_trader_account(cls, trader_id, account_name, api_key,kucoin_password, okex_password, api_secret, exchange_id, base_currency_id):
        trader_account = cls.objects.filter(pk=trader_id).first()

        if trader_account is not None:
            account_exist = cls.check_account_name_exist(account_name=account_name)
            if account_exist:
                res = "exist"
                response = "Account name already Taken"
            else:
                exchange, currency = cls.get_exchange_and_currency(exchange=exchange_id,base_currency=base_currency_id)

                res, response = cls.verify_updated_exchange(trader_account,account_name=account_name,api_key=api_key,api_secret=api_secret,kucoin_password=kucoin_password,
                                            okex_password=okex_password,exchange=exchange, base_currency=currency)

            return res, response


    @classmethod
    def verify_updated_exchange(cls,api_key, api_secret,trader_account,base_currency,account_name, kucoin_password, okex_password, exchange):

        if exchange.name == "FTX":
            response, message = cls.verify_API_AND_SECRET_FTX(api_key, api_secret)
            if message:
                cls.trader_account_update(trader_account, account_name=account_name,api_key=api_key,
                                          kucoin_password=kucoin_password,okex_password=okex_password,
                                          api_secret=api_secret,exchange=exchange,base_currency=base_currency)
                res = "saved"
            else:
                res = "error"

        if exchange.name == "BINANCE":
            response, message = cls.verify_API_AND_SECRET_BINANCE(api_key, api_secret)
            if message:
                cls.trader_account_update(trader_account, account_name=account_name, api_key=api_key,
                                          kucoin_password=kucoin_password, okex_password=okex_password,
                                          api_secret=api_secret, exchange=exchange, base_currency=base_currency)
                res = "saved"
            else:
                res = "error"

        if exchange.name == "KUCOIN":
            response, message = cls.verify_API_AND_SECRET_KUCOIN(api_key, api_secret, kucoin_password)
            if message:
                cls.trader_account_update(trader_account, account_name=account_name, api_key=api_key,
                                          kucoin_password=kucoin_password, okex_password=okex_password,
                                          api_secret=api_secret, exchange=exchange, base_currency=base_currency)
                res = "saved"
            else:
                res = "error"

        if exchange.name == "BINANCE-FUTURE":
            response, message = cls.verify_API_AND_SECRET_BINANCE(api_key, api_secret)
            if message:
                cls.trader_account_update(trader_account, account_name=account_name, api_key=api_key,
                                          kucoin_password=kucoin_password, okex_password=okex_password,
                                          api_secret=api_secret, exchange=exchange, base_currency=base_currency)
                res = "saved"
            else:
                res = "error"

        if exchange.name == "FTX-US":
            response, message = cls.verify_API_AND_SECRET_FTX(api_key, api_secret)
            if message:
                cls.trader_account_update(trader_account, account_name=account_name, api_key=api_key,
                                          kucoin_password=kucoin_password, okex_password=okex_password,
                                          api_secret=api_secret, exchange=exchange, base_currency=base_currency)
                res = "saved"
            else:
                res = "error"

        if exchange.name == "BYBIT":
            response, message = cls.verify_API_AND_SECRET_BYBIT(api_key, api_secret)
            if message:
                cls.trader_account_update(trader_account, account_name=account_name, api_key=api_key,
                                          kucoin_password=kucoin_password, okex_password=okex_password,
                                          api_secret=api_secret, exchange=exchange, base_currency=base_currency)
                res = "saved"
            else:
                res = "error"

        if exchange.name == "HITBTC":
            response, message = cls.verify_API_AND_SECRET_HITBTC(api_key, api_secret)
            if message:
                cls.trader_account_update(trader_account, account_name=account_name, api_key=api_key,
                                          kucoin_password=kucoin_password, okex_password=okex_password,
                                          api_secret=api_secret, exchange=exchange, base_currency=base_currency)
                res = "saved"
            else:
                res = "error"

        if exchange.name == "KRAKEN":
            response, message = cls.verify_API_AND_SECRET_KRAKEN(api_key, api_secret)
            if message:

                res = "saved"
            else:
                res = "error"

        if exchange.name == "OKEX":
            response, message = cls.verify_API_AND_SECRET_OKEX(api_key, api_secret, okex_password)
            if message:
                cls.trader_account_update(trader_account, account_name=account_name, api_key=api_key,
                                          kucoin_password=kucoin_password, okex_password=okex_password,
                                          api_secret=api_secret, exchange=exchange, base_currency=base_currency)
                res = "saved"
            else:
                res = "error"

        if exchange.name == "DERIBIT":
            response, message = cls.verify_API_AND_SECRET_DERIBIT(api_key, api_secret)
            if message:
                cls.trader_account_update(trader_account, account_name=account_name, api_key=api_key,
                                          kucoin_password=kucoin_password, okex_password=okex_password,
                                          api_secret=api_secret, exchange=exchange, base_currency=base_currency)
                res = "saved"
            else:
                res = "error"

        return res, response

    @classmethod
    def get_or_create_trader_account(cls, trader, account_name, api_key,kucoin_password, okex_password, api_secret, exchange, base_currency
                                     ):
        get_exchange = Exchange.objects.filter(pk=exchange).first()
        get_currency = BaseCurrency.objects.filter(pk=base_currency).first()

        trader_account = cls.objects.filter(account_name=account_name).first()

        if trader_account is not None:
            res = "exist"
            response = "Account Name Already Taken"
        else:
            if get_exchange.name == "FTX":
                response, message = cls.verify_API_AND_SECRET_FTX(api_key, api_secret)
                if message:
                    cls.create_trader_account(trader, account_name, api_key, get_exchange, get_currency)
                    res = "saved"
                else:
                    res = "error"

            if get_exchange.name == "BINANCE":
                response, message = cls.verify_API_AND_SECRET_BINANCE(api_key, api_secret)
                if message:
                    cls.create_trader_account(trader, account_name, api_key, get_exchange, get_currency)
                    res = "saved"
                else:
                    res = "error"

            if get_exchange.name == "KUCOIN":
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

            if get_exchange.name == "BINANCE-FUTURE":
                response, message = cls.verify_API_AND_SECRET_BINANCE(api_key, api_secret)
                if message:
                    cls.create_trader_account(trader, account_name, api_key, get_exchange, get_currency)
                    res = "saved"
                else:
                    res = "error"

            if get_exchange.name == "FTX-US":
                response, message = cls.verify_API_AND_SECRET_FTX(api_key, api_secret)
                if message:
                    cls.create_trader_account(trader, account_name, api_key, get_exchange, get_currency)
                    res = "saved"
                else:
                    res = "error"

            if get_exchange.name == "BYBIT":
                response, message = cls.verify_API_AND_SECRET_BYBIT(api_key, api_secret)
                if message:
                    cls.create_trader_account(trader, account_name, api_key, get_exchange, get_currency)
                    res = "saved"
                else:
                    res = "error"

            if get_exchange.name == "HITBTC":
                response, message = cls.verify_API_AND_SECRET_HITBTC(api_key, api_secret)
                if message:
                    cls.create_trader_account(trader, account_name, api_key, get_exchange, get_currency)
                    res = "saved"
                else:
                    res = "error"

            if get_exchange.name == "KRAKEN":
                response, message = cls.verify_API_AND_SECRET_KRAKEN(api_key, api_secret)
                if message:
                    cls.create_trader_account(trader, account_name, api_key,api_secret, get_exchange, get_currency)
                    res = "saved"
                else:
                    res = "error"

            if get_exchange.name == "OKEX":
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

            if get_exchange.name == "DERIBIT":
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
            exchange_id = 'binance'
            exchange_class = getattr(ccxt, exchange_id)
            exchange = exchange_class({
                'apiKey': 'YOUR_API_KEY',
                'secret': 'YOUR_SECRET',
                'timeout': 30000,
                'enableRateLimit': True,
            })

            fetch_balance = exchange.fetch_balance()

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




