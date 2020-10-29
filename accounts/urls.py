from django.urls import path
from .views.account import signup, signup_view, login, login_view, logout

urlpatterns = [
    path('signup_view/', signup_view, name="signup_view"),
    path('signup/', signup, name="signup"),
    path('login_view/', login_view, name="login_view"),
    path('login/dashboard/', login, name="login"),
    path('logout/',logout,name="logout"),
    # path('login/',signin,name="login"),
    # path('loginpro/',signinpro,name="loginpro"),
    # path('signup/',signup,name="signup"),
    # path('signuppro/',signuppro,name="signuppro"),
    # path('verify/<str:code>/',verify,name="verify"),
    # path('forgot/',forgot,name="forgot"),
    # path('sendrescode/',sendrescode,name="sendrescode"),
    # path('resetpass/<str:code>/',resetpass,name="resetpass"),
    # path('resetpasspro/<str:code>/',resetpasspro,name="resetpasspro"),
    # path('account/',account,name="account"),
    # path('change_account_settings/<str:type>/',change_account_settings,name="change_account_settings"),
    # path('change_account_email/',change_account_email,name="change_account_email"),
    # path('verify_new_email/<str:code>/',verify_new_email,name="verify_new_email"),
    # path('checkemail/',checkemail,name="checkemail"),
]
