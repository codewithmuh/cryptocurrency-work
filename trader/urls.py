from django.urls import path
from trader.views.settings import settings_view, user_profile_settings
from trader.views.dashboard import dashboard
from trader.views.marketplace import marketplace
from trader.views.crypto_trading import copy_trading
from trader.views.profile import profile



urlpatterns = [
    path('dashboard/',dashboard,name="dashboard"),
    path('marketplace/',marketplace,name="marketplace"),
    path('copyTrading/',copy_trading,name="copyTrading"),
    path('profile/',profile,name="profile"),
    path('settings/', settings_view, name="settings")
]