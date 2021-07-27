from django.forms import modelformset_factory
from .models import ProductionPlan

ProductFormset = modelformset_factory(
    ProductionPlan,
    fields=('ref', 'qte', 'date_created', 'typeP'),
)
