from django.contrib import admin
from .models import ProductionPlan


class Filter(admin.ModelAdmin):
    list_display = ('ref', 'qte', 'date_created')


admin.site.register(ProductionPlan, Filter)
