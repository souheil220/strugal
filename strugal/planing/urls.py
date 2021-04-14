from django.urls import path

from . import views

urlpatterns = [
    path("", views.planing, name="planing"),
    path("events", views.events, name="events"),
    path("update/<str:pk>", views.update, name="update"),
]
