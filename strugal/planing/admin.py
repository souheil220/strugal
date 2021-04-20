from django.contrib import admin
from .models import ProductionPlanE, ProductionPlanLB, ProductionPlanLC, ProductionPlanA, ProductionPlanRPT


class Filter(admin.ModelAdmin):
    list_display = ('ref', 'qte', 'date_created', 'typeP')


admin.site.register(ProductionPlanE, Filter)
admin.site.register(ProductionPlanLB, Filter)
admin.site.register(ProductionPlanLC, Filter)
admin.site.register(ProductionPlanA, Filter)
admin.site.register(ProductionPlanRPT, )
