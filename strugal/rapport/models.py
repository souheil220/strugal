from django.db import models
from planing.models import *
import time


class Objectif(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.FloatField()

    def __str__(self):
        return "{}".format(self.value)


class RapportJournalierE(models.Model):
    id = models.AutoField(primary_key=True)
    ref = models.ForeignKey(ProductionPlan, on_delete=models.CASCADE)
    obj = models.ForeignKey(Objectif, on_delete=models.CASCADE)
    prod_physique = models.FloatField()
    prod_conforme = models.FloatField()
    prod_non_conforme = models.FloatField()
    deche_geometrique = models.FloatField()
    nbr_barre = models.FloatField()
    n_of = models.CharField(max_length=255)
    date_created = models.CharField(default=time.strftime(
        "%Y-%m-%d", time.localtime()),
                                    max_length=255)
    realise = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.ref)


class TypeRapport(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.value)


class RapportJournalierALR(models.Model):
    id = models.AutoField(primary_key=True)
    # ref = models.ForeignKey(ProductionPlan,
    #                         on_delete=models.CASCADE,
    #                         blank=True,
    #                         null=True)
    ref = models.CharField(max_length=255, null=True)
    obj = models.ForeignKey(Objectif, on_delete=models.CASCADE)
    prod_physique_p_r = models.FloatField(default=0)
    prod_physique = models.FloatField()
    prod_conforme = models.FloatField()
    prod_non_conforme = models.FloatField()
    n_of = models.CharField(max_length=255)
    typeR = models.ForeignKey(TypeRapport, on_delete=models.CASCADE)
    date_created = models.CharField(default=time.strftime(
        "%Y-%m-%d", time.localtime()),
                                    max_length=255)
    realise = models.BooleanField()

    def __str__(self):
        return "{}".format(self.ref)
