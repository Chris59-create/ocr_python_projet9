from django.urls import path
from authentication import views

app_name = "authentication"

urlpatterns = [
    path("signup/", views.signup_page, name="signup"),
    path("", views.login_page, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("follows/", views.follows, name="follows"),
    path('clearfollowed/<int:followed_id>', views.clear_followed,
         name='clear_followed')
]