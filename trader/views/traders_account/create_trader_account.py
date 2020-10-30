from trader.models.traders import TraderAccounts
import ccxt
from django.contrib.auth.models import User
from accounts.models.user_profile import UserProfile
from django.contrib.auth.decorators import login_required


@login_required(login_url="login_view/")
def create_trader_account(request):
    pass
