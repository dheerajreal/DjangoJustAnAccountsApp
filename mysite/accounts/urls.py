from django.contrib import admin
from django.urls import path, include
from .views import register, login, logout, profile_overview, profile_edit, profile_passwd_edit

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('profile/', profile_overview, name="profile_overview"),
    path('profile_edit/', profile_edit, name="profile_edit"),
    path('profile_passwd_edit/', profile_passwd_edit, name="profile_passwd_edit"),


]
