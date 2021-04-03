from django.db import models

class ProductionPlan(models.Model):
    ref = models.CharField(max_length=255,blank=True)
    qte = models.FloatField()
    longueur = models.FloatField()
    ral = models.FloatField()

    def __str__(self):
        return self.ref

