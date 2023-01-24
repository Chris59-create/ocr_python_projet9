from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from authentication.models import User, UserFollows

from . import forms


def login_page(request):

    form = forms.LoginForm()
    message = ""

    if request.method == "POST":
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"]
            )

            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
                # to check with the template Home
                return redirect("feed:home")
            else:
                message = 'Identifiants invalides.'

    return render(
        request,
        'authentication/login.html',
        context={'form': form, 'message': message}
    )


def logout_view(request):

    logout(request)

    return redirect("authentication:login")


def signup_page(request):

    form = forms.SignupForm()

    if request.method == "POST":
        form = forms.SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request,
                  "authentication/signup.html",
                  context={"form": form}
                  )


def follows(request):

    form = forms.UserFollowsForm()
    message = ""

    if request.method == "POST":
        form = forms.UserFollowsForm(request.POST)

        if form.is_valid():

            followed_name = form.cleaned_data["followed_name"]
            usernames = User.objects.filter(username=followed_name)

            if usernames:

                followed_id = User.objects.get(username=followed_name).id

                new_userfollows = UserFollows(request.user.id, followed_id)

                new_userfollows.save()

                message = f"{followed_id} ajouté à vos suivis !"

                # return redirect("authentication:follows", message)

            else:

                message = "Pas de membre avec cet identifiant"

                # return redirect("authentication:follows", message)

    return render(request,
                  "authentication/follows.html",
                  {"form": form, "message": message}
                  )
