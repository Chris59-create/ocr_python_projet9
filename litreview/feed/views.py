from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from . import forms, models


@login_required
def home_page(request):
    return render(request, "feed/home.html")
