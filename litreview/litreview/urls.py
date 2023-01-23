from django.contrib import admin
from django.urls import path, include

import feed.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("authentication.urls")),
    path("", include("feed.urls")),


]
