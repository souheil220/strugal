from django.db import models


class ProductionPlan(models.Model):
    id = models.AutoField(primary_key=True)
    ref = models.CharField(blank=True, max_length=255)
    qte = models.FloatField()
    date_created = models.CharField(blank=True, max_length=255)

    def __str__(self):
        # return "{} {} {}".format(self.ref, self.qte, self.date_created)
        return "{} {} {} ".format(self.ref, self.qte, self.date_created)
