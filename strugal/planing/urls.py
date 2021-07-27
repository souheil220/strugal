from django.urls import path

from . import views

urlpatterns = [
    path("", views.planing, name="planing"),
    path("anodisation", views.anodisation, name="anodisation"),
    path("laquageBlanc", views.laquageBlanc, name="laquageBlanc"),
    path("laquageCouleur", views.laquageCouleur, name="laquageCouleur"),
    path("rpt", views.rpt, name="rpt"),
    # path("events", views.events, name="events"),
    path("a", views.events, name="events"),
    path("update/<str:pk>", views.update, name="update"),
    path("delete/<str:pk>", views.delete, name="delete"),
    path("getdate/<str:date>/<str:typeP>", views.getDate, name="getdate"),
]
