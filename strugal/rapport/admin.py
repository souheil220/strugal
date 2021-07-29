from django.contrib import admin
from .models import *


# Register your models here.
class FilterE(admin.ModelAdmin):
    list_display = ('id', 'ref', 'prod_physique', 'prod_conforme',
                    'prod_non_conforme', 'deche_geometrique', 'nbr_barre',
                    'n_of', 'date_created', 'realise')


class FilterALR(admin.ModelAdmin):
    list_display = ('id', 'ref', 'prod_physique_p_r', 'prod_physique',
                    'prod_conforme', 'prod_non_conforme', 'n_of',
                    'date_created', 'realise', 'typeR')


class FilterTypeR(admin.ModelAdmin):
    list_display = ('id', 'value')


class FilterObjectif(admin.ModelAdmin):
    list_display = ('id', 'value')

    # def get_ref(self, obj):
    #     return obj.ref.ref

    # get_ref.admin_order_field = 'ref'  #Allows column order sorting
    # get_ref.short_description = 'ref Name'  #Renames column head


admin.site.register(RapportJournalierE, FilterE)
admin.site.register(RapportJournalierALR, FilterALR)
admin.site.register(TypeRapport, FilterTypeR)
admin.site.register(Objectif, FilterObjectif)