from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout as user_logout, login as user_login
from django.contrib import messages
from accounts.models.user_profile import UserProfile
from django.contrib.auth.models import User

import ccxt


def logout(request):
    template_name = "login.html"
    context = {}
    user_logout(request)

    return render(request, template_name=template_name, context=context)


def login_view(request):
    template_name = "login.html"
    context = {}

    return render(request, template_name=template_name, context=context)


def login(request):
    if request.method == "POST":
        context = {}
        body = request.POST
        email = body.get('email', '')
        password = body.get('password', '')

        user = authenticate(request, username=email, password=password)

        if user:
            user_profile = UserProfile.objects.get(user=user)
            user_login(request, user)
            template_name = "dashboard.html"
            context['user_profile'] = user_profile
        else:
            template_name = "login.html"
            messages.error(request, "Invalid credentials")

        return render(request, template_name=template_name, context=context)
    else:
        context = {}
        user = User.objects.filter(pk=request.user.id).first()
        if user is not None:
            user_profile = UserProfile.objects.get(user=user)
            template_name = "dashboard.html"
            context['user_profile'] = user_profile
            return render(request, template_name=template_name, context=context)
        else:

            return login_view(request)


def signup_view(request):
    template_name = "signup.html"
    context = {}

    return render(request, template_name=template_name, context=context)


def signup(request):
    template_name = 'signup.html'
    context = {}
    if request.method == "POST":

        body = request.POST
        first_name = body.get('fname', '')
        last_name = body.get('lname', '')
        email = body.get('email', '')
        password = body.get('password', '')

        if confirm_password(request):
            response = UserProfile.create_user_and_send_email(first_name=first_name,
                                                              last_name=last_name, email=email,
                                                              password=password)

            if response == "Exist":
                messages.error(request, "User Already exist")
            if response == "Success":
                messages.success(request, "User created successfully")
        else:
            messages.error(request, "password do not match")

    return render(request, template_name=template_name, context=context)


def confirm_password(request):
    if request.method == "POST":
        body = request.POST
        password = body.get('password', '')
        confirm = body.get('repass', '')

        if str(password) == str(confirm):
            return True
        else:
            return False
