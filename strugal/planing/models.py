from django.db import models


class ProductionPlan(models.Model):
    id = models.AutoField(primary_key=True)
    ref = models.CharField(max_length=255)
    qte = models.FloatField()
    longueur = models.FloatField()
    ral = models.FloatField()

    def __str__(self):
        return self.ref
