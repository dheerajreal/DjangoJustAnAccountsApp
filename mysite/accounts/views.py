from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import RegistrationForm, LoginForm


def register(request):
    if request.user.is_authenticated:
        msg = messages.success(request, "already logged in")
        return redirect("index")
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        msg = messages.success(request, "User Created, can login now")
        return redirect("login")

    context = {
        "form": form
    }
    return render(request, "accounts/register.html", context)


def login(request):
    if request.user.is_authenticated:
        msg = messages.success(request, "already logged in")
        return redirect("index")
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            msg = messages.success(request, "login success")
            return redirect("index")
        else:
            msg = messages.warning(request, "login fail")

    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        msg = messages.success(request, "logout successful")
        return redirect("login")
    else:
        msg = messages.warning(request, "not logged in")
        return redirect("login")
