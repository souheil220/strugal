from django.contrib import admin
from .models import ProductionPlan


class Filter(admin.ModelAdmin):
    list_display = ('id', 'ref', 'qte', 'date_created', 'typeP')


admin.site.register(ProductionPlan, Filter)