from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import RegistrationForm, LoginForm, ProfileEditForm, PasswordEditForm
User = get_user_model()
# TODO : fix password change view


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
    if request.user.is_authenticated:
        user = request.user
        user = User.objects.get(username=user)
        print(user)
        form = ProfileEditForm(request.POST or None, instance=user)
        print(form)
        if form.is_valid():
            print(form)
            #user.username = form.cleaned_data["username"]
            #user.email = form.cleaned_data["email"]
            #user.first_name = form.cleaned_data["first_name"]
            #user.last_name = form.cleaned_data["last_name"]
            form.save()
            msg = messages.success(request, "Successfully updated")
            return redirect("profile_overview")
        context = {
            "form": form
        }
        return render(request, "accounts/profile_edit.html", context)
    else:
        msg = messages.warning(request, "not logged in")
        return redirect("login")


def profile_passwd_edit(request):
   # return HttpResponse("passwd")
    if request.user.is_authenticated:
        user = request.user
        user = User.objects.get(username=user)
        print(user)
        form = PasswordEditForm(request.POST or None)
        print(form)
        if form.is_valid():
            print("valid")
            msg = messages.success(request, "Successfully updated")
            return redirect("profile_overview")
        context = {
            "form": form
        }
        return render(request, "accounts/password_edit.html", context)
    else:
        msg = messages.warning(request, "not logged in")
        return redirect("login")
