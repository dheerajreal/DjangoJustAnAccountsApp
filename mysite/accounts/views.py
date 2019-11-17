from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import RegistrationForm, LoginForm


def register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")

    context = {
        "form": form
    }
    return render(request, "accounts/register.html", context)


def login(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("index")

    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("index")
