# Django
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

# First Party
from tableservice.api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("chat/", include("chat.urls")),
]
