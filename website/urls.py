from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.main, name="main-page"),
    path("", include("register.urls")),
    path("", include("login.urls")),
    path("", include("menu.urls")),
]
