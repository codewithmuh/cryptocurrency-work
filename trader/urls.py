from django.urls import path
from trader.views.settings import settings_view, user_profile_settings, user_update_description
from trader.views.dashboard import dashboard
from trader.views.marketplace import marketplace
from trader.views.crypto_trading import copy_trading
from trader.views.profile import profile
from .views.traders_account.trader_account_view import  trader_account_view
from .views.traders_account import create_trader_account, delete_trader_account, update_trader_account



urlpatterns = [
    path('dashboard/',dashboard,name="dashboard"),
    path('marketplace/',marketplace,name="marketplace"),
    path('copyTrading/',copy_trading,name="copyTrading"),
    path('profile/',profile,name="profile"),
    path('settings/', settings_view, name="settings"),
    path('settings/trader_account_view/', trader_account_view, name="trader_account_view"),
    path('settings/update_description/', user_update_description, name="user_update_description"),
    path('settings/user_update/', user_profile_settings , name='user_update'),
    path('settings/create_trader_account/', create_trader_account, name="create_trader_Account"),
    path('settings/update_trader_account/<int:trader_id>/', update_trader_account, name="update_trader_Account"),
    path('settings/delete_trader_account/<int:trader_id>/', delete_trader_account, name="delete_trader_Account")
]