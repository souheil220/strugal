from django.db import models
from planing.models import ProductionPlan


class RapportJournalier(models.Model):
    id = models.AutoField(primary_key=True)
    ref = models.ForeignKey(ProductionPlan, on_delete=models.CASCADE)
    prod_physique = models.FloatField()
    prod_conforme = models.FloatField()
    prod_non_conforme = models.FloatField()
    deche_geometrique = models.FloatField()
    nbr_barre = models.FloatField()
    n_of = models.FloatField()

    def __str__(self):
        return "{}".format(self.ref)
