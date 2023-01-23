from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

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

    if request.method == "POST":
        form = forms.UserFollowsForm(request.POST)
        form.cleaned_data["user"] = request.user

        if form.is_valid():

            form.save()
            return redirect("feed:home")

    return render(request,
                  "authentication/follows.html",
                  locals()
                  )
