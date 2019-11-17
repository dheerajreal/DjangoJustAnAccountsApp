from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="Username",
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "Username", "class": "form-control"
                                   }
                               )
                               )
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput(
                                    attrs={
                                        "placeholder": "Password", "class": "form-control"
                                    }
                                )
                                )
    password2 = forms.CharField(label="Confirm Password",
                                widget=forms.PasswordInput(
                                    attrs={
                                        "placeholder": "Confirm Password", "class": "form-control"
                                    }
                                )
                                )

    class Meta:
        model = User
        #exclude = []
        fields = ["username", "password1", "password2", ]


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username",
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "Username", "class": "form-control"
                                   }
                               )
                               )
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(
                                   attrs={
                                       "placeholder": "Password", "class": "form-control"
                                   }
                               )
                               )
