from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ProductionPlan
from django import forms
from django.forms import modelformset_factory


def planing(request):
    ProductFormset = modelformset_factory(
        ProductionPlan,
        fields=(
            'id',
            'ref',
            'qte',
            'longueur',
        ),
        widgets={
            'ref':
            forms.TextInput(attrs={
                'class': 'form-control',
                'required': "true"
            }),
            'qte':
            forms.TextInput(attrs={
                'class': 'form-control',
                'required': "true"
            }),
            'longueur':
            forms.TextInput(attrs={
                'class': 'form-control',
                'required': "true"
            })
        })
    formset = ProductFormset(request.POST or None)

    # print formset data if it is valid
    if request.method == 'POST':
        if formset.is_valid():
            print('valid')
            for form in formset:
                print(form.cleaned_data)
        else:
            print(formset.errors)
            print('not valid')
        return HttpResponse('Hola')
    else:
        return render(request, "planing/index.html",
                      {'ProductFormset': ProductFormset})
