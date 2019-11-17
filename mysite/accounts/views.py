from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import RegistrationForm, LoginForm
User = get_user_model()


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


def profile_overview(request):
    if request.user.is_authenticated:
        user = request.user
        user = User.objects.get(username=user)
    else:
        msg = messages.warning(request, "not logged in")
        return redirect("login")
    context = {
        "user": user
    }
    return render(request, "accounts/profile_overview.html", context)


def profile_edit(request):
    return HttpResponse("edit")


def profile_passwd_edit(request):
    return HttpResponse("passwd")
