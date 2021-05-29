from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("pages.urls")),
    path("planing/", include("planing.urls")),
    path("rapport/", include("rapport.urls")),
]
