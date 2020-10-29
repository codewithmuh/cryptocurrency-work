from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models.user_profile import UserProfile
from django.contrib.auth.decorators import login_required


@login_required(login_url="login_view/")
def copy_trading(request):
    context = {}

    user = User.objects.filter(pk=request.user.id).first()

    if user is not None:
        user_profile = UserProfile.objects.get(user=user)
        template_name = "copyTrading.html"
        context['user_profile'] = user_profile
        return render(request, template_name=template_name, context=context)
    else:
        template_name = "login.html"

        return render(request, template_name=template_name, context=context)
