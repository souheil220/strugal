from django.forms.models import modelformset_factory
from .models import ProductionPlan

ProductFormSet = modelformset_factory(ProductionPlan,
                                      fields=[
                                          'ref',
                                          'qte',
                                          'longueur',
                                      ],
                                      exclude=(),
                                      extra=1,
                                      can_delete=True)
