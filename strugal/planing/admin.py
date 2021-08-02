from django.contrib import admin
from .models import *


class FilterProductionPlan(admin.ModelAdmin):
    list_display = ('id', 'ref', 'qte', 'date_created', 'get_ref')

    def get_ref(self, obj):
        return obj.typeP.typeP

    get_ref.admin_order_field = 'typeP'  #Allows column order sorting
    get_ref.short_description = 'typeP'  #Renames column head


class FilterTypePlaning(admin.ModelAdmin):
    list_display = ('id', 'typeP')


admin.site.register(ProductionPlan, FilterProductionPlan)
admin.site.register(TypePlaning, FilterTypePlaning)