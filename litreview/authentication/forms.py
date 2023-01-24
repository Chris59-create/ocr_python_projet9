from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from authentication.models import UserFollows
from django import forms


class SignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username",)
        labels = {"username": "Identifiant", }
        help_texts = {"username": "63 caractères max."}


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Identifiant")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput,
                               label="Mot de passe")


class UserFollowsForm(forms.Form):
    followed_name = forms.CharField(
        max_length=150,
        label="Identifiant du membre à suivre",
    )
