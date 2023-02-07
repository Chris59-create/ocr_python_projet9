from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from authentication.models import User

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
                return redirect("feed:home")

            else:
                message = "Identifiant ou mot de passe invalides !"
                form = forms.LoginForm()

    return render(
        request,
        'authentication/login.html',
        context={'form': form, 'message': message}
        )


@login_required
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


@login_required
def follows(request):

    add_followed_form = forms.AddFollowedForm()

    followed = request.user.followed_members.all()
    followers = request.user.following_by.all().order_by('user')

    message = ""

    if request.method == "POST":

        if "add_followed" in request.POST:
            add_followed_form = forms.AddFollowedForm(request.POST)

            if add_followed_form.is_valid():

                followed_name = add_followed_form.cleaned_data["followed_name"]

                try:
                    followed_user = User.objects.get(username=followed_name)
                    user = request.user
                    user.followed_members.add(followed_user.id)

                    message = f"{followed_user.username} ajouté à vos suivis !"

                    add_followed_form = forms.AddFollowedForm()

                    # return redirect("authentication:follows")

                except IndexError:

                    message = "Pas de membre avec cet identifiant"

                    # return redirect("authentication:follows")

    context = {
        "add_followed_form": add_followed_form,
        "followed": followed,
        "followers": followers,
        "message": message
    }

    return render(
        request,
        "authentication/follows.html",
        context=context
    )


@login_required
def remove_followed(request, followed_id=None):
    to_remove = get_object_or_404(User, pk=followed_id)
    request.user.followed_members.remove(to_remove)

    return redirect('authentication:follows')
