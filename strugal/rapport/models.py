from django.db import models
from planing.models import *
import time


class RapportJournalierE(models.Model):
    id = models.AutoField(primary_key=True)
    ref = models.ForeignKey(ProductionPlan, on_delete=models.CASCADE)
    obj = models.FloatField(default=7)
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


class RapportJournalierA(models.Model):
    id = models.AutoField(primary_key=True)
    ref = models.ForeignKey(ProductionPlan, on_delete=models.CASCADE)
    obj = models.FloatField(default=0.2)
    prod_physique_p_r = models.FloatField(default=0)
    prod_physique = models.FloatField()
    prod_conforme = models.FloatField()
    prod_non_conforme = models.FloatField()
    n_of = models.CharField(max_length=255)
    date_created = models.CharField(default=time.strftime(
        "%Y-%m-%d", time.localtime()),
                                    max_length=255)
    realise = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.ref)


class RapportJournalierLB(models.Model):
    id = models.AutoField(primary_key=True)
    ref = models.ForeignKey(ProductionPlan, on_delete=models.CASCADE)
    obj = models.FloatField(default=1.5)
    prod_physique_p_r = models.FloatField(default=0)
    prod_physique = models.FloatField()
    prod_conforme = models.FloatField()
    prod_non_conforme = models.FloatField()
    n_of = models.CharField(max_length=255)
    date_created = models.CharField(default=time.strftime(
        "%Y-%m-%d", time.localtime()),
                                    max_length=255)
    realise = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.ref)


class RapportJournalierLC(models.Model):
    id = models.AutoField(primary_key=True)
    ref = models.ForeignKey(ProductionPlan, on_delete=models.CASCADE)
    obj = models.FloatField(default=0.35)
    prod_physique_p_r = models.FloatField(default=0)
    prod_physique = models.FloatField()
    prod_conforme = models.FloatField()
    prod_non_conforme = models.FloatField()
    n_of = models.CharField(max_length=255)
    date_created = models.CharField(default=time.strftime(
        "%Y-%m-%d", time.localtime()),
                                    max_length=255)
    realise = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.ref)


class RapportJournalierRPT(models.Model):
    id = models.AutoField(primary_key=True)
    ref = models.ForeignKey(ProductionPlan, on_delete=models.CASCADE)
    obj = models.FloatField(default=0.15)
    prod_physique_p_r = models.FloatField(default=0)
    prod_physique = models.FloatField()
    prod_conforme = models.FloatField()
    prod_non_conforme = models.FloatField()
    n_of = models.CharField(max_length=255)
    date_created = models.CharField(default=time.strftime(
        "%Y-%m-%d", time.localtime()),
                                    max_length=255)
    realise = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.ref)
