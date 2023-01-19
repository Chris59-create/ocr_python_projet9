from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

import authentication.views
import feed.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", authentication.views.login_page, name="login"),
    path("signup/", authentication.views.signup_page, name="signup"),
    path("home", feed.views.home_page, name="home"),
    path("logout", LogoutView.as_view(), name="logout"),
]
