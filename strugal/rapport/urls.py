from django.urls import path

from . import views

urlpatterns = [
    path("", views.rapport, name="rapport"),
    path("rapport/<str:date>", views.rapportJ, name="rapportJ"),
    path("saveRapport", views.saveRapport, name="saveRapport"),
]
