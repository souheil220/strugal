from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductFormset
from .models import ProductionPlan
from django.core.serializers.json import DjangoJSONEncoder
import json


def events(request):
    if request.method == 'GET':
        parametre = request.GET
        debut = parametre.get('start')
        print(debut)
        # fin = parametre['end']
        evenement = ProductionPlan.objects.filter(date_created=debut)
        return HttpResponse(evenement)


def planing(request):
    formset = ProductFormset()
    formset = ProductFormset(request.POST or None)

    product = ProductionPlan.objects.values()
    list_result = [entry for entry in product]

    # print formset data if it is valid
    if request.method == 'POST':
        if formset.is_valid():
            print('valid')
            for form in formset:
                # instance = form.save(commit=False)
                # instance.save()
                print(form.cleaned_data)
            # formset.save()

        else:
            print(formset.errors)
            print('not valid')
        return HttpResponse('Hola')

    return render(
        request, "planing/index.html", {
            'formset': formset,
            'product': json.dumps(list_result, cls=DjangoJSONEncoder)
        })
