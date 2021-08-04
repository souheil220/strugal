from django.urls import path

from . import views

urlpatterns = [
    path("rapportR/<str:typeR>", views.rediger_rapport, name="rapport"),
    path("rapportA/rapportAujourdui",
         views.rapportAujourdui,
         name="rapportAujourdui"),
    path("rapport/<str:typeR>/<str:dateC>", views.rapportJ, name="rapportJ"),
    path("saveRapport/<str:typeR>", views.saveRapport, name="saveRapport"),
    path("updateObjectif", views.update_obj, name="updateObjectif"),
]
