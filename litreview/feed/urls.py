from django.urls import path
from feed import views

app_name = "feed"

urlpatterns = [
    path("home", views.home_page, name="home"),
]