from django.db import models

# class TypePlaning(models.Model):
#     id = models.AutoField(primary_key=True)
#     typeP = models.CharField(max_length=255)


class ProductionPlan(models.Model):
    id = models.AutoField(primary_key=True)
    ref = models.CharField(blank=True, max_length=255)
    qte = models.FloatField()
    typeP = models.CharField(max_length=255)
    # typeP = models.ForeignKey(TypePlaning, on_delete=models.CASCADE)
    date_created = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return "{} {} {} ".format(self.ref, self.qte, self.date_created)
