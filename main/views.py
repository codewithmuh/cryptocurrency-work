from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect


def home(request):
    context = {

    }
    return render(request, 'home.html', context)
