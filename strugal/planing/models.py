from django.db import models


class ProductionPlanE(models.Model):
    id = models.AutoField(primary_key=True)
    ref = models.CharField(blank=True, max_length=255)
    qte = models.FloatField()
    typeP = models.CharField(default='extrusion', max_length=255)
    date_created = models.CharField(blank=True, max_length=255)

    def __str__(self):
        # return "{} {} {}".format(self.ref, self.qte, self.date_created)
        return "{} {} {} ".format(self.ref, self.qte, self.date_created)


class ProductionPlanLB(models.Model):
    id = models.AutoField(primary_key=True)
    ref = models.CharField(blank=True, max_length=255)
    qte = models.FloatField()
    typeP = models.CharField(default='Laquage blan', max_length=255)
    date_created = models.CharField(blank=True, max_length=255)

    def __str__(self):
        # return "{} {} {}".format(self.ref, self.qte, self.date_created)
        return "{} {} {} ".format(self.ref, self.qte, self.date_created)


class ProductionPlanLC(models.Model):
    id = models.AutoField(primary_key=True)
    ref = models.CharField(blank=True, max_length=255)
    qte = models.FloatField()
    ral = models.CharField(default='0M', max_length=255)
    typeP = models.CharField(default='laquage couleurs', max_length=255)
    date_created = models.CharField(blank=True, max_length=255)

    def __str__(self):
        # return "{} {} {}".format(self.ref, self.qte, self.date_created)
        return "{} {} {} ".format(self.ref, self.qte, self.date_created)


class ProductionPlanRPT(models.Model):
    id = models.AutoField(primary_key=True)
    ref01 = models.CharField(blank=True, max_length=255)
    ref02 = models.CharField(blank=True, max_length=255)
    ral01 = models.CharField(blank=True, max_length=255)
    ral02 = models.CharField(blank=True, max_length=255)
    qte = models.FloatField()
    typeP = models.CharField(default='RTP', max_length=255)
    date_created = models.CharField(blank=True, max_length=255)

    def __str__(self):
        # return "{} {} {}".format(self.ref, self.qte, self.date_created)
        return "{} {} {} ".format(self.ref01, self.qte, self.date_created)


class ProductionPlanA(models.Model):
    id = models.AutoField(primary_key=True)
    ref = models.CharField(blank=True, max_length=255)
    ral = models.CharField(blank=True, max_length=255)
    qte = models.FloatField()
    typeP = models.CharField(default='Anodisation', max_length=255)
    date_created = models.CharField(blank=True, max_length=255)

    def __str__(self):
        # return "{} {} {}".format(self.ref, self.qte, self.date_created)
        return "{} {} {} ".format(self.ref, self.qte, self.date_created)