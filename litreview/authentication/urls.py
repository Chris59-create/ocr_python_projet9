from django.urls import path
from authentication import views

app_name = "authentication"

urlpatterns = [
    path("signup/", views.signup_page, name="signup"),
    path("", views.login_page, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("follows/", views.follows, name="follows"),
    path('follows/<int:followed_id>/remove', views.remove_followed,
         name='remove_followed')
]