from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()


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


class LoginForm(forms.Form):
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
