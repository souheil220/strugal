from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductFormset
from .models import ProductionPlan
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
import json


def renderFormset(request):
    print('renderFormset')
    formset = ProductFormset()
    formset = ProductFormset(request.POST or None)

    product = ProductionPlan.objects.values()
    list_result = [entry for entry in product]
    print('list format {}'.format(list_result))
    data = []
    if request.method == 'POST':
        print("request post renderFormset")
        if formset.is_valid():
            print("formset.is_valid renderFormset")
            for form in formset:
                is_there = None
                try:
                    is_there = ProductionPlan.objects.get(
                        ref=form.cleaned_data['ref'],
                        typeP=form.cleaned_data['typeP'],
                        date_created=form.cleaned_data['date_created'])
                except:
                    print(is_there)
                    instance = form.save(commit=False)
                    instance.save()

        else:
            print(formset.errors)
            print('not valid')
    data.append(formset)
    data.append(list_result)
    return data


@login_required(login_url='login')
def planing(request):
    data = renderFormset(request)
    formset = data[0]
    list_result = data[1]
    return render(
        request, "planing/index.html", {
            'formset': formset,
            'product': json.dumps(list_result, cls=DjangoJSONEncoder)
        })


@login_required(login_url='login')
def anodisation(request):
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
                        typeP=form.cleaned_data['typeP'],
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


@login_required(login_url='login')
def laquageBlanc(request):
    formset = ProductFormset()
    formset = ProductFormset(request.POST or None)

    product = ProductionPlan.objects.values()
    list_result = [entry for entry in product]

    if request.method == 'POST':
        if formset.is_valid():

            for form in formset:
                is_there = None
                try:
                    is_there = ProductionPlan.objects.get(
                        ref=form.cleaned_data['ref'],
                        typeP=form.cleaned_data['typeP'],
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


@login_required(login_url='login')
def laquageCouleur(request):
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
                        typeP=form.cleaned_data['typeP'],
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


@login_required(login_url='login')
def rpt(request):
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
                        typeP=form.cleaned_data['typeP'],
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


def getEventList(debut, fin, typeM, typeP):
    evenement = typeM.objects.filter(date_created__gte=debut,
                                     date_created__lte=fin,
                                     typeP=typeP)

    event_arr = []
    for i in evenement:
        event_sub_arr = {}
        event_sub_arr['id'] = i.id
        event_sub_arr['title'] = i.ref + "\n" + str(i.qte)
        event_sub_arr['start'] = i.date_created
        event_sub_arr['end'] = i.date_created
        event_arr.append(event_sub_arr)

    return event_arr


def events(request):
    if request.method == 'GET':
        parametre = request.GET
        debut = parametre.get('start')
        typeP = parametre.get('palning')

        typeP = typeP[:-7]
        if typeP == "":
            typeP = 'extrusion'
        fin = parametre.get('end')
        event_arr = getEventList(debut, fin, ProductionPlan, typeP)
        return HttpResponse(json.dumps(event_arr))


def updateForALC(request, PPFT, PPMT, pk):
    form = PPFT(request.POST)
    if form.is_valid():
        elem = PPMT.objects.get(id=int(pk))
        elem.qte = int(form.cleaned_data[0]['qte'])
        elem.ref = form.cleaned_data[0]['ref']
        elem.ral = form.cleaned_data[0]['ral']
        elem.save()


def updateForRpt(request, pk):
    form = ProductFormsetRPT(request.POST)
    if form.is_valid():
        elem = ProductionPlanRPT.objects.get(id=int(pk))
        elem.qte = int(form.cleaned_data[0]['qte'])
        elem.ref01 = form.cleaned_data[0]['ref01']
        elem.ref02 = form.cleaned_data[0]['ref02']
        elem.ral01 = form.cleaned_data[0]['ral01']
        elem.ral02 = form.cleaned_data[0]['ral02']
        elem.save()


def update(request, pk):
    print('rani fel update')
    if request.method == 'POST':
        form = ProductFormset(request.POST)
        if form.is_valid():
            print('valid')
            elem = ProductionPlan.objects.get(id=int(pk))
            elem.qte = int(form.cleaned_data[0]['qte'])
            print(elem.qte)
            elem.ref = form.cleaned_data[0]['ref']
            print(elem.ref)
            elem.save()
        else:
            print("form not valid")
            print(form.errors)
        return HttpResponse("success")


def delete(request, pk):
    if request.method == 'POST':

        elem = ProductionPlan.objects.get(id=int(pk))
        elem.delete()

        return HttpResponse("Deleted")


def getDate(request, date, typeP):
    events = ProductionPlan.objects.filter(date_created=date, typeP=typeP)
    event_arr = []
    for i in events:
        event_sub_arr = {}
        event_sub_arr['title'] = i.ref
        event_arr.append(event_sub_arr)
    print(type(event_arr))
    return HttpResponse(json.dumps(event_arr, cls=DjangoJSONEncoder))
