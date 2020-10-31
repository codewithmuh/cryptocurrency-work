from accounts.models.user_profile import UserProfile
from django.shortcuts import render, redirect, HttpResponse
from trader.models.traders import Exchange, BaseCurrency
from django.contrib.auth.decorators import login_required


@login_required(login_url="login_view/")
def trader_account_view(request):
    template_name = "trader_account.html"

    base_currencies = BaseCurrency.objects.filter()
    exchanges = Exchange.objects.filter()

    context = {
        "base_currencies":base_currencies,
        "exchanges":exchanges
    }
    print(len(context['exchanges']))

    return render(request, template_name=template_name, context=context)