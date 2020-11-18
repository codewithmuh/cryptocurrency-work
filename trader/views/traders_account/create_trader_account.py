from trader.models.traders import TraderAccounts
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models.user_profile import UserProfile
from django.contrib.auth.decorators import login_required
from trader.models.traders import Exchange, BaseCurrency, KucoinPassword, OkexPassword


@login_required(login_url="login_view/")
def get_trader_account(request, trader_id):
    template_name = "get_trader_account.html"
    trader_account = TraderAccounts.objects.get(pk=trader_id)
    base_currencies = BaseCurrency.objects.filter()
    exchanges = Exchange.objects.filter()

    context = {
        "trader_account": trader_account,
        "base_currencies": base_currencies,
        "exchanges": exchanges
    }

    kucoin_pass = KucoinPassword.objects.filter(trader_account=trader_account).first()
    okex_pass = OkexPassword.objects.filter(trader_account=trader_account).first()

    if kucoin_pass is not None:
        context['kucoin_pass'] = kucoin_pass
    if okex_pass is not None:
        context['okex_pass'] = okex_pass

    return render(request, template_name=template_name, context=context)


@login_required(login_url="login_view/")
def delete_trader_account(request, trader_id):
    template_name = "settings.html"
    context = {}

    user_profile = UserProfile.objects.get(user=request.user)

    trader_accounts = TraderAccounts.objects.filter(trader=user_profile)

    trader_account = TraderAccounts.objects.filter(pk=trader_id).first()
    trader_account.delete()

    context['trader_accounts'] = trader_accounts

    return render(request, template_name=template_name, context=context)


@login_required(login_url="login_view/")
def update_trader_account(request, trader_id):
    template_name = "trader_account.html"
    base_currencies = BaseCurrency.objects.filter()
    exchanges = Exchange.objects.filter()

    if request.method == "POST":
        template_name = "settings.html"
        context = {
            "base_currencies": base_currencies,
            "exchanges": exchanges
        }

        user_profile = UserProfile.objects.get(user=request.user)

        trader_accounts = TraderAccounts.objects.filter(trader=user_profile)

        account_name = request.POST.get('account_name', '')
        api_key = request.POST.get('api_key', '')
        api_secret = request.POST.get('secret', '')
        kucoin_password = request.POST.get('kucoin_password', '')
        okex_password = request.POST.get('okex_password', '')
        exchange = request.POST.get('exchange', '')
        base_currency = request.POST.get('currency', '')

        res, response = TraderAccounts.update_trader_account(
            trader_id=trader_id,
            account_name=account_name,
            api_key=api_key,
            api_secret=api_secret,
            kucoin_password=kucoin_password,
            okex_password=okex_password,
            exchange_id=exchange,
            base_currency_id=base_currency
        )

        if res == "exist":
            messages.error(request, response)
        if res == "error":
            messages.error(request, response)
        if res == "saved":
            context['response'] = response

            messages.success(request, "Account updated successfullly")

            context['trader_accounts'] = trader_accounts

        return render(request, template_name=template_name, context=context)
    return render(request, template_name=template_name, context=context)


@login_required(login_url="login_view/")
def create_trader_account(request):
    template_name = "trader_account.html"
    base_currencies = BaseCurrency.objects.filter()
    exchanges = Exchange.objects.filter()

    if request.method == "POST":
        context = {
            "base_currencies": base_currencies,
            "exchanges": exchanges
        }

        user_profile = UserProfile.objects.get(user=request.user)

        trader_accounts = TraderAccounts.objects.filter(trader=user_profile)

        account_name = request.POST.get('account_name','')
        api_key = request.POST.get('api_key','')
        api_secret = request.POST.get('secret', '')
        kucoin_password = request.POST.get('kucoin_password', '')
        okex_password = request.POST.get('okex_password', '')
        exchange = request.POST.get('exchange','')
        base_currency = request.POST.get('currency', '')

        user = User.objects.get(pk=request.user.id)

        user_profile = UserProfile.objects.get(user=user)

        res, response = TraderAccounts.get_or_create_trader_account(
            trader=user_profile,
            api_key=api_key,
            api_secret=api_secret,
            account_name=account_name,
            exchange=exchange,
            base_currency=base_currency,
            kucoin_password=kucoin_password,
            okex_password=okex_password
        )

        if res == "exist":
            template_name = "trader_account.html"
            messages.error(request, response)
        if res == "error":
            template_name = "trader_account.html"
            messages.error(request, response)
        if res == "saved":
            template_name = "settings.html"
            context['response'] = response
            print(response)
            messages.success(request, "Account created successfullly")
            context['trader_accounts'] = trader_accounts

        return render(request, template_name=template_name, context=context)
    return render(request, template_name=template_name, context=context)
