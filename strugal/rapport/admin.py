from django.contrib import admin
from .models import *


# Register your models here.
class FilterE(admin.ModelAdmin):
    list_display = ('ref', 'prod_physique', 'prod_conforme',
                    'prod_non_conforme', 'deche_geometrique', 'nbr_barre',
                    'n_of', 'date_created', 'realise')


class FilterALR(admin.ModelAdmin):
    list_display = ('ref', 'prod_physique_p_r', 'prod_physique',
                    'prod_conforme', 'prod_non_conforme', 'n_of',
                    'date_created', 'realise')

    # def get_ref(self, obj):
    #     return obj.ref.ref

    # get_ref.admin_order_field = 'ref'  #Allows column order sorting
    # get_ref.short_description = 'ref Name'  #Renames column head


admin.site.register(RapportJournalierE, FilterE)
admin.site.register(RapportJournalierA, FilterALR)
admin.site.register(RapportJournalierLB, FilterALR)
admin.site.register(RapportJournalierLC, FilterALR)
admin.site.register(RapportJournalierRPT, FilterALR)
