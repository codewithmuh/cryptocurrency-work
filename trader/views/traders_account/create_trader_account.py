from trader.models.traders import TraderAccounts
import ccxt
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models.user_profile import UserProfile
from django.contrib.auth.decorators import login_required


@login_required(login_url="login_view/")
def create_trader_account(request):
    if request.method == "POST":
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

        )
