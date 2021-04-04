from django.shortcuts import render, redirect
from .models import ProductionPlan
from django.forms import modelformset_factory


def planing(request):
    ProductFormset = modelformset_factory(
        ProductionPlan,
        fields=(
            'ref',
            'qte',
            'longueur',
        ),
    )
    formset = ProductFormset(request.POST or None)

    # print formset data if it is valid
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)

    return render(request, "planing/index.html",
                  {'ProductFormset': ProductFormset})
