from django.urls import path

from . import views

urlpatterns = [
    path("", views.rapport, name="rapport"),
    path("rapport/rapportAujourdui", views.index, name="rapportAujourdui"),
    path("rapport/<str:typeR>/<str:dateC>", views.rapportJ, name="rapportJ"),
    path("saveRapport", views.saveRapport, name="saveRapport"),
]
