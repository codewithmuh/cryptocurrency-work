from django.urls import path
from trader.views.settings import settings_view, user_profile_settings, user_update_description
from trader.views.dashboard import dashboard
from trader.views.marketplace import marketplace
from trader.views.crypto_trading import copy_trading
from trader.views.profile import profile



urlpatterns = [
    path('dashboard/',dashboard,name="dashboard"),
    path('marketplace/',marketplace,name="marketplace"),
    path('copyTrading/',copy_trading,name="copyTrading"),
    path('profile/',profile,name="profile"),
    path('settings/', settings_view, name="settings"),
    path('settings/update_description/', user_update_description, name="user_update_description"),
    path('settings/user_update/', user_profile_settings , name='user_update')
]