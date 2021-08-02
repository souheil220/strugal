from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductFormset
from .models import *
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required
import json


def renderFormset(request, url):
    print('renderFormset')
    formset = ProductFormset()
    formset = ProductFormset(request.POST or None)

    print(request.method)
    if request.method == 'POST':
        print("request post renderFormset")
        if formset.is_valid():
            print("formset.is_valid renderFormset")
            for form in formset:
                is_there = None
                try:
                    is_there = ProductionPlan.objects.get(
                        ref=form.cleaned_data['ref'],
                        typeP=TypePlaning.objects.get(
                            form.cleaned_data['typeP']),
                        date_created=form.cleaned_data['date_created'])
                except:
                    print(is_there)
                    instance = form.save(commit=False)
                    instance.save()

        else:
            print(formset.errors)
            print('not valid')

    return render(request, "planing/" + url + ".html")


@login_required(login_url='login')
def planing(request):
    return renderFormset(request, "index")


@login_required(login_url='login')
def anodisation(request):
    return renderFormset(request, "anodisation")


@login_required(login_url='login')
def laquageBlanc(request):
    return renderFormset(request, "laquageBlanc")


@login_required(login_url='login')
def laquageCouleur(request):
    return renderFormset(request, "laquageCouleur")


@login_required(login_url='login')
def rpt(request):
    return renderFormset(request, "rpt")


def getEventList(debut, fin, typeM, typeP):
    evenement = typeM.objects.filter(
        date_created__gte=debut,
        date_created__lte=fin,
        typeP=TypePlaning.objects.get(typeP=typeP),
        planned=True)

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
    events = ProductionPlan.objects.filter(
        date_created=date, typeP=TypePlaning.objects.get(typeP=typeP))
    print("events", events)
    event_arr = []
    for i in events:
        event_sub_arr = {}
        event_sub_arr['title'] = i.ref
        event_arr.append(event_sub_arr)
    print(type(event_arr))
    return HttpResponse(json.dumps(event_arr, cls=DjangoJSONEncoder))
