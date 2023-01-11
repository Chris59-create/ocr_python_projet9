from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

import authentication.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
        name="login"
        ),
    path("signup/", authentication.views.signup_page, name="signup")
]
