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
        fin = parametre.get('end')

        evenement = ProductionPlan.objects.filter(date_created__gte=debut,
                                                  date_created__lte=fin)
        event_arr = []
        for i in evenement:
            event_sub_arr = {}
            event_sub_arr['title'] = i.ref + "\n" + str(i.qte)
            event_sub_arr['start'] = i.date_created
            event_sub_arr['end'] = i.date_created
            event_arr.append(event_sub_arr)
        print(event_arr)
        return HttpResponse(json.dumps(event_arr))


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
                instance = form.save(commit=False)
                instance.save()
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
