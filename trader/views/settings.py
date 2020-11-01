from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models.user_profile import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from trader.models.traders import TraderAccounts
from trader.models.traders import Exchange, BaseCurrency


@login_required(login_url="login_view/")
def user_update_description(request):
    if request.method == "POST":
        base_currencies = BaseCurrency.objects.filter()
        exchanges = Exchange.objects.filter()

        context = {
            "base_currencies": base_currencies,
            "exchanges": exchanges
        }
        template_name = "settings.html"
        body = request.POST

        description = body.get('description', '')

        user = User.objects.get(pk=request.user.id)
        user_profile = UserProfile.objects.filter(user=user).first()

        if user:
            user_profile.description = description
            user_profile.save()
            context['user_profile'] = user_profile
            print(user_profile.description)
            messages.success(request, "Description Updated successful")
        return render(request, template_name=template_name, context=context)


@login_required(login_url="login_view/")
def user_profile_settings(request):
    if request.method == "POST":
        base_currencies = BaseCurrency.objects.filter()
        exchanges = Exchange.objects.filter()

        context = {
            "base_currencies": base_currencies,
            "exchanges": exchanges
        }
        template_name = "settings.html"
        body = request.POST

        user = User.objects.get(pk=request.user.id)
        user_profile = UserProfile.objects.filter(user=user).first()

        first_name = body.get('first_name', '')
        last_name = body.get('last_name', '')

        if user:
            user_profile.user.first_name = first_name
            user_profile.user.last_name = last_name

            user_profile.user.save()
            user_profile.save()

            context['user_profile'] = user_profile

            messages.success(request, "Updated successfully")

        return render(request, template_name=template_name, context=context)


@login_required(login_url="login_view/")
def settings_view(request):

    base_currencies = BaseCurrency.objects.filter()
    exchanges = Exchange.objects.filter()

    context = {
        "base_currencies": base_currencies,
        "exchanges": exchanges
    }

    user = User.objects.filter(pk=request.user.id).first()
    user_profile = UserProfile.objects.filter(user=user).first()

    if user is not None:
        trader_accounts = TraderAccounts.objects.filter(trader=user_profile)
        user_profile = UserProfile.objects.get(user=user)
        template_name = "settings.html"
        context['user_profile'] = user_profile
        context['trader_accounts'] = trader_accounts
        return render(request, template_name=template_name, context=context)
    else:
        template_name = "login.html"

        return render(request, template_name=template_name, context=context)
