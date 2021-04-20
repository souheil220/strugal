from django.forms import modelformset_factory
from .models import ProductionPlanE, ProductionPlanLB, ProductionPlanLC, ProductionPlanRPT, ProductionPlanA

ProductFormsetE = modelformset_factory(
    ProductionPlanE,
    fields=(
        'ref',
        'qte',
        'date_created',
    ),
)

ProductFormsetLB = modelformset_factory(
    ProductionPlanLB,
    fields=(
        'ref',
        'qte',
        'date_created',
    ),
)

ProductFormsetLC = modelformset_factory(
    ProductionPlanLC,
    fields=(
        'ref',
        'qte',
        'ral',
        'date_created',
    ),
)

ProductFormsetRPT = modelformset_factory(
    ProductionPlanRPT,
    fields=(
        'ref01',
        'ref02',
        'ral01',
        'ral02',
        'qte',
        'date_created',
    ),
)

ProductFormsetA = modelformset_factory(
    ProductionPlanA,
    fields=(
        'ref',
        'ral',
        'qte',
        'date_created',
    ),
)
