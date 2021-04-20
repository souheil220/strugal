from django.contrib import admin
from .models import RapportJournalier
import time


# Register your models here.
class Filter(admin.ModelAdmin):
    list_display = ('get_ref', 'prod_physique', 'prod_conforme',
                    'prod_non_conforme', 'deche_geometrique', 'nbr_barre',
                    'n_of', 'date_created', 'realise')

    def get_ref(self, obj):
        return obj.ref.ref

    get_ref.admin_order_field = 'ref'  #Allows column order sorting
    get_ref.short_description = 'ref Name'  #Renames column head


admin.site.register(RapportJournalier, Filter)
