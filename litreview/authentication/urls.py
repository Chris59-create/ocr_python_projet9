from django.urls import path
from authentication import views
from django.contrib.auth.views import LogoutView

app_name = "authentication"

urlpatterns = [
    path("signup/", views.signup_page, name="signup"),
    path("", views.login_page, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("follows", views.follows, name="follows")
]