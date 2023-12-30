from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.main, name="main-page"),
    path("", include("register.urls")),
    path("", include("login.urls")),
    path("", include("menu.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
