from django.shortcuts import render, redirect
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
            event_sub_arr['id'] = i.id
            event_sub_arr['title'] = i.ref + "\n" + str(i.qte)
            event_sub_arr['start'] = i.date_created
            event_sub_arr['end'] = i.date_created
            event_arr.append(event_sub_arr)
        # print(type(event_arr))
        return HttpResponse(json.dumps(event_arr))


def update(request, pk):
    if request.method == 'POST':
        form = ProductFormset(request.POST)
        if form.is_valid():
            elem = ProductionPlan.objects.get(id=int(pk))
            elem.qte = int(form.cleaned_data[0]['qte'])
            elem.ref = form.cleaned_data[0]['ref']
            elem.save()
            return render(request, "planing/index.html")


def delete(request, pk):
    if request.method == 'POST':
        elem = ProductionPlan.objects.get(id=int(pk))
        elem.delete()
        return HttpResponse("Deleted")


def getDate(request, date):
    events = ProductionPlan.objects.filter(date_created=date)
    event_arr = []
    for i in events:
        event_sub_arr = {}
        event_sub_arr['title'] = i.ref
        event_arr.append(event_sub_arr)
    print(type(event_arr))
    return HttpResponse(json.dumps(event_arr, cls=DjangoJSONEncoder))


def planing(request):
    formset = ProductFormset()
    formset = ProductFormset(request.POST or None)

    product = ProductionPlan.objects.values()
    list_result = [entry for entry in product]
    print('list format {}'.format(list_result))
    print('request {}'.format(request))

    if request.method == 'POST':
        if formset.is_valid():

            for form in formset:
                is_there = None
                try:
                    is_there = ProductionPlan.objects.get(
                        ref=form.cleaned_data['ref'],
                        date_created=form.cleaned_data['date_created'])
                except:
                    print(is_there)
                    instance = form.save(commit=False)
                    instance.save()

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
