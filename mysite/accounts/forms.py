from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
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


class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(label="Username",
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "Username", "class": "form-control"
                                   }
                               )
                               )
    email = forms.CharField(label="Email",
                            widget=forms.EmailInput(
                                attrs={
                                    "placeholder": "Email", "class": "form-control"
                                }
                            )
                            )
    first_name = forms.CharField(label="First Name",
                                 widget=forms.TextInput(
                                     attrs={
                                       "placeholder": "First Name", "class": "form-control"
                                     }
                                 )
                                 )
    last_name = forms.CharField(label="Last Name",
                                widget=forms.TextInput(
                                    attrs={
                                        "placeholder": "Last Name", "class": "form-control"
                                    }
                                )
                                )

    class Meta:
        model = User
        #exclude = []
        fields = ["email", "username", "first_name", "last_name"]


class PasswordEditForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old Password",
                                   widget=forms.PasswordInput(
                                       attrs={
                                           "placeholder": "Old Password", "class": "form-control"
                                       }
                                   )
                                   )
    new_password1 = forms.CharField(label="New Password",
                                    widget=forms.PasswordInput(
                                        attrs={
                                            "placeholder": "New Password", "class": "form-control"
                                        }
                                    )
                                    )
    new_password2 = forms.CharField(label="Confirm New Password",
                                    widget=forms.PasswordInput(
                                        attrs={
                                            "placeholder": "Confirm New Password", "class": "form-control"
                                        }
                                    )
                                    )
