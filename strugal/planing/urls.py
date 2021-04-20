from django.urls import path

from . import views

urlpatterns = [
    path("", views.planing, name="planing"),
    path("laquageBlanc", views.laquageBlanc, name="laquageBlanc"),
    path("anodisation", views.anodisation, name="anodisation"),
    path("laquageCouleur", views.laquageCouleur, name="laquageCouleur"),
    path("rpt", views.rpt, name="rpt"),
    path("events", views.events, name="events"),
    path("events2", views.events2, name="events2"),
    path("events3", views.events3, name="events3"),
    path("events4", views.events4, name="events4"),
    path("events5", views.events5, name="events5"),
    path("update/<str:pk>", views.update, name="update"),
    path("delete/<str:pk>", views.delete, name="delete"),
    path("getdate/<str:date>", views.getDate, name="getdate"),
]
