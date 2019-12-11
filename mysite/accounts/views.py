from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import (LoginForm, PasswordEditForm, ProfileEditForm,
                    RegistrationForm)

User = get_user_model()


def register(request):
    if request.user.is_authenticated:
        msg = messages.success(request, "Already logged in")
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
        msg = messages.success(request, "Already logged in")
        return redirect("index")
    form = LoginForm(request, data=request.POST or None)
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            msg = messages.success(request, f"Login successful as {username}")
            return redirect("index")
        else:
            msg = messages.warning(request, "Login failed")
    if request.POST and not form.is_valid():
        msg = messages.warning(request, *form.get_invalid_login_error())
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        msg = messages.success(request, "Logout successful")
        return redirect("login")
    else:
        msg = messages.warning(request, "Not logged in")
        return redirect("login")


def profile_overview(request):
    if request.user.is_authenticated:
        user = request.user
        user = User.objects.get(username=user)
    else:
        msg = messages.warning(request, "Not logged in")
        return redirect("login")
    context = {
        "user": user
    }
    return render(request, "accounts/profile_overview.html", context)


def profile_edit(request):
    if request.user.is_authenticated:
        user = request.user
        user = User.objects.get(username=user)
        # print(user)
        form = ProfileEditForm(request.POST or None, instance=user)
        # print(form)
        if form.is_valid():
            # print(form)
            #user.username = form.cleaned_data["username"]
            #user.email = form.cleaned_data["email"]
            #user.first_name = form.cleaned_data["first_name"]
            #user.last_name = form.cleaned_data["last_name"]
            form.save()
            msg = messages.success(request, "Successfully updated Profile")
            return redirect("profile_overview")
        context = {
            "form": form
        }
        return render(request, "accounts/profile_edit.html", context)
    else:
        msg = messages.warning(request, "Not logged in")
        return redirect("login")


def profile_passwd_edit(request):
    if request.user.is_authenticated:
        user = request.user
        user = User.objects.get(username=user)
        form = PasswordEditForm(request.user, request.POST or None)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            msg = messages.success(request, "Successfully Changed Password ")
            return redirect("profile_overview")
        context = {
            "form": form
        }
        return render(request, "accounts/password_edit.html", context)
    else:
        msg = messages.warning(request, "Not logged in")
        return redirect("login")
