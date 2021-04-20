from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductFormsetE, ProductFormsetLB, ProductFormsetLC, ProductFormsetRPT, ProductFormsetA
from .models import ProductionPlanE, ProductionPlanLB, ProductionPlanLC, ProductionPlanRPT, ProductionPlanA
from django.core.serializers.json import DjangoJSONEncoder
import json


def events(request):
    if request.method == 'GET':
        parametre = request.GET
        debut = parametre.get('start')
        fin = parametre.get('end')

        evenement = ProductionPlanE.objects.filter(date_created__gte=debut,
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


def events2(request):
    if request.method == 'GET':
        parametre = request.GET
        debut = parametre.get('start')
        fin = parametre.get('end')

        evenement = ProductionPlanLB.objects.filter(date_created__gte=debut,
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


def events3(request):
    if request.method == 'GET':
        parametre = request.GET
        debut = parametre.get('start')
        fin = parametre.get('end')

        evenement = ProductionPlanRPT.objects.filter(date_created__gte=debut,
                                                     date_created__lte=fin)
        event_arr = []
        for i in evenement:
            event_sub_arr = {}
            event_sub_arr['id'] = i.id
            event_sub_arr['title'] = i.ref01 + "\n" + str(i.qte)
            event_sub_arr['start'] = i.date_created
            event_sub_arr['end'] = i.date_created
            event_arr.append(event_sub_arr)
        # print(type(event_arr))
        return HttpResponse(json.dumps(event_arr))


def events4(request):
    if request.method == 'GET':
        parametre = request.GET
        debut = parametre.get('start')
        fin = parametre.get('end')

        evenement = ProductionPlanA.objects.filter(date_created__gte=debut,
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


def events5(request):
    if request.method == 'GET':
        parametre = request.GET
        debut = parametre.get('start')
        fin = parametre.get('end')

        evenement = ProductionPlanLC.objects.filter(date_created__gte=debut,
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
        form = ProductFormsetE(request.POST)
        if form.is_valid():
            elem = ProductionPlanE.objects.get(id=int(pk))
            elem.qte = int(form.cleaned_data[0]['qte'])
            elem.ref = form.cleaned_data[0]['ref']
            elem.save()
            return render(request, "planing/index.html")


def delete(request, pk):
    if request.method == 'POST':
        elem = ProductionPlanE.objects.get(id=int(pk))
        elem.delete()
        return HttpResponse("Deleted")


def getDate(request, date):
    events = ProductionPlanE.objects.filter(date_created=date)
    event_arr = []
    for i in events:
        event_sub_arr = {}
        event_sub_arr['title'] = i.ref
        event_arr.append(event_sub_arr)
    print(type(event_arr))
    return HttpResponse(json.dumps(event_arr, cls=DjangoJSONEncoder))


def laquageBlanc(request):
    formset = ProductFormsetLB()
    formset = ProductFormsetLB(request.POST or None)

    product = ProductionPlanLB.objects.values()
    list_result = [entry for entry in product]

    if request.method == 'POST':
        if formset.is_valid():

            for form in formset:
                is_there = None
                try:
                    is_there = ProductionPlanLB.objects.get(
                        ref=form.cleaned_data['ref'],
                        date_created=form.cleaned_data['date_created'])
                except:
                    print(is_there)
                    instance = form.save(commit=False)
                    instance.save()

        else:
            print(formset.errors)
            print('not valid')
        return HttpResponse('Hola')
    return render(
        request, "planing/laquageBlanc.html", {
            'formset': formset,
            'product': json.dumps(list_result, cls=DjangoJSONEncoder)
        })


def anodisation(request):
    formset = ProductFormsetA()
    formset = ProductFormsetA(request.POST or None)

    product = ProductionPlanA.objects.values()
    list_result = [entry for entry in product]
    print('list format {}'.format(list_result))
    print('request {}'.format(request))

    if request.method == 'POST':
        if formset.is_valid():

            for form in formset:
                is_there = None
                try:
                    is_there = ProductionPlanA.objects.get(
                        ref=form.cleaned_data['ref'],
                        ral=form.cleaned_data['ral'],
                        date_created=form.cleaned_data['date_created'])
                except:
                    print(is_there)
                    instance = form.save(commit=False)
                    instance.save()

        else:
            print(formset.errors)
            print('not valid')
        return HttpResponse('Hola')
    return render(
        request, "planing/anodisation.html", {
            'formset': formset,
            'product': json.dumps(list_result, cls=DjangoJSONEncoder)
        })


def laquageCouleur(request):
    formset = ProductFormsetLC()
    formset = ProductFormsetLC(request.POST or None)

    product = ProductionPlanLC.objects.values()
    list_result = [entry for entry in product]
    print('list format {}'.format(list_result))
    print('request {}'.format(request))

    if request.method == 'POST':
        if formset.is_valid():

            for form in formset:
                is_there = None
                try:
                    is_there = ProductionPlanLC.objects.get(
                        ref=form.cleaned_data['ref'],
                        ral=form.cleaned_data['ral'],
                        date_created=form.cleaned_data['date_created'])
                except:
                    print(is_there)
                    instance = form.save(commit=False)
                    instance.save()

        else:
            print(formset.errors)
            print('not valid')
        return HttpResponse('Hola')
    return render(
        request, "planing/laquageCouleur.html", {
            'formset': formset,
            'product': json.dumps(list_result, cls=DjangoJSONEncoder)
        })


def rpt(request):
    formset = ProductFormsetRPT()
    formset = ProductFormsetRPT(request.POST or None)

    product = ProductionPlanRPT.objects.values()
    list_result = [entry for entry in product]
    print('list format {}'.format(list_result))
    print('request {}'.format(request))

    if request.method == 'POST':
        if formset.is_valid():

            for form in formset:
                is_there = None
                try:
                    is_there = ProductionPlanRPT.objects.get(
                        ref01=form.cleaned_data['ref01'],
                        ref02=form.cleaned_data['ref02'],
                        ral01=form.cleaned_data['ral01'],
                        ral02=form.cleaned_data['ral02'],
                        date_created=form.cleaned_data['date_created'])
                except:
                    print(is_there)
                    instance = form.save(commit=False)
                    instance.save()

        else:
            print(formset.errors)
            print('not valid')
        return HttpResponse('Hola')
    return render(
        request, "planing/rpt.html", {
            'formset': formset,
            'product': json.dumps(list_result, cls=DjangoJSONEncoder)
        })


def planing(request):
    formset = ProductFormsetE()
    formset = ProductFormsetE(request.POST or None)

    product = ProductionPlanE.objects.values()
    list_result = [entry for entry in product]
    print('list format {}'.format(list_result))
    print('request {}'.format(request))

    if request.method == 'POST':
        if formset.is_valid():

            for form in formset:
                is_there = None
                try:
                    is_there = ProductionPlanE.objects.get(
                        ref=form.cleaned_data['ref'],
                        date_created=form.cleaned_data['date_created'])
                except:
                    print(is_there)
                    instance = form.save(commit=False)
                    instance.save()

        else:
            print(formset.errors)
            print('not valid')
        return HttpResponse('Hola')
    return render(
        request, "planing/index.html", {
            'formset': formset,
            'product': json.dumps(list_result, cls=DjangoJSONEncoder)
        })
