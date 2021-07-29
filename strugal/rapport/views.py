from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from planing.models import *
import time
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from datetime import date
import json
from django.db.models import Sum

# Create your views here.


def checkRepport(ProductionPlan, reportM, typeR):

    data = ProductionPlan.objects.filter(
        Q(date_created=time.strftime("%Y-%m-%d", time.localtime())),
        typeP=typeR.lower())
    print('data ', data)
    test = []
    try:
        for plan in data:
            repport = reportM.objects.filter(ref=plan).values()
            test.append(repport)

        i = 0

        for t in test:
            # print(t)
            if i < len(test):

                if typeR == 'Extrusion':

                    data[i].deche_geometrique = t[0]['deche_geometrique']
                    # print(data[i].deche_geometrique)
                    data[i].nbr_barre = t[0]['nbr_barre']
                else:
                    data[i].prod_physique_p_r = t[0]['prod_physique_p_r']

                data[i].prod_physique = t[0]['prod_physique']
                data[i].obj = t[0]['obj']
                data[i].prod_conforme = t[0]['prod_conforme']
                data[i].prod_non_conforme = t[0]['prod_non_conforme']
                data[i].n_of = t[0]['n_of']
                data[i].realise = t[0]['realise']

            i += 1
            # print("data : ", t[i].realise)
        print("data : ", data)
        return data
    except:
        return data


@login_required(login_url='login')
def rediger_rapport(request, typeR):
    if typeR == 'Extrusion':
        test = 0
        data = checkRepport(ProductionPlan, RapportJournalierE, typeR)
        if data is not None:
            test = len(data)
        context = {'data': data, 'list': test, "typeR": typeR}
        return render(request, 'rapport/rediget_rapportE.html', context)
    else:

        data = checkRepport(ProductionPlan, RapportJournalierALR, typeR)

        test = 0

        if data is not None:
            test = len(data)
        print(data)
        context = {'data': data, 'list': test, "typeR": typeR}
        return render(request, 'rapport/rediget_rapport.html', context)


@login_required(login_url='login')
def rapportAujourdui(request):
    aujourdhui = date.today().strftime("%Y-%m-%d")

    # try:
    typeR = TypeRapport.objects.get(value='Anodisation')
    print("typeR ", typeR)
    data = RapportJournalierALR.objects.filter(date_created=aujourdhui,
                                               typeR=typeR)
    if (len(data) > 0):
        data[0].prod_physique = RapportJournalierALR.objects.filter(
            date_created=aujourdhui).aggregate(Sum('prod_physique_p_r'))
        totalPC, totalPCP, totalPNC, totalPNCP = 0, 0, 0, 0
        for i in range(len(data)):
            data[0].prod_physique_pou = round(
                ((data[0].prod_physique['prod_physique_p_r__sum'] * 100 /
                  data[0].obj.value)), 2)
            data[i].prod_conforme_pou = round(
                ((data[i].prod_physique_p_r * 100 /
                  data[i].prod_physique_p_r)), 2)
            data[i].prod_non_conforme_pou = 100 - data[i].prod_conforme_pou
            totalPC = totalPC + data[i].prod_conforme
            totalPCP = totalPCP + data[i].prod_conforme_pou
            totalPNC = totalPNC + data[i].prod_non_conforme
            totalPNCP = totalPNCP + data[i].prod_non_conforme_pou
        totalPCP = totalPCP / (i + 1)
        totalPNCP = totalPNCP / (i + 1)
        context = {
            "data": data,
            "totalPC": totalPC,
            "totalPCP": totalPCP,
            "totalPNC": totalPNC,
            "totalPNCP": totalPNCP
        }
        return render(request, 'rapport/rapportAujourdui.html', context)
    else:
        context = {
            "data": data,
            "totalPC": "",
            "totalPCP": "",
            "totalPNC": "",
            "totalPNCP": ""
        }
        return render(request, 'rapport/rapportAujourdui.html', context)

    # # except Exception as e:
    #     print(e)
    #     return HttpResponse(e)


def rapportJ(request, typeR, dateC):
    print(typeR)
    if request.is_ajax and request.method == 'GET':
        try:
            if typeR == 'Extrusion':
                data = RapportJournalierE.objects.filter(date_created=dateC)
            else:
                rapport = RapportJournalierALR
                typeRap = TypeRapport.objects.get(value=typeR)
                data = RapportJournalierALR.objects.filter(date_created=dateC,
                                                           typeR=typeRap)

            if typeR == 'Extrusion':
                totalPP = RapportJournalierE.objects.filter(
                    date_created=dateC).aggregate(Sum('prod_physique'))
                totalPC = RapportJournalierE.objects.filter(
                    date_created=dateC).aggregate(Sum('prod_conforme'))
                totalPNCP = RapportJournalierE.objects.filter(
                    date_created=dateC).aggregate(Sum('prod_non_conforme'))
                totalDG = RapportJournalierE.objects.filter(
                    date_created=dateC).aggregate(Sum('deche_geometrique'))
                totalNBR = RapportJournalierE.objects.filter(
                    date_created=dateC).aggregate(Sum('nbr_barre'))
                print("data", data)
                for i in range(len(data)):
                    if data[i].prod_physique == 0:
                        data[i].prod_physique_pou = 0
                        data[i].prod_conforme_pou = 0
                        data[i].prod_conforme = 0
                        data[i].prod_non_conforme = 0
                        data[i].prod_non_conforme_pou = 0
                        data[i].deche_geometrique = 0
                        data[i].deche_geometrique_pou = 0
                        data[i].nbr_barre = 0

                    else:

                        data[i].prod_physique_pou = round(
                            ((data[i].prod_conforme + data[i].prod_non_conforme
                              + data[i].deche_geometrique) * 100 /
                             data[i].obj.value), 2)

                        data[i].prod_conforme_pou = round(
                            ((data[i].prod_conforme * 100 /
                              data[i].prod_physique)), 2)
                        data[i].prod_non_conforme_pou = round(
                            ((data[i].prod_non_conforme * 100 /
                              data[i].prod_physique)), 2)
                        data[i].deche_geometrique_pou = round(
                            ((data[i].deche_geometrique * 100 /
                              data[i].prod_physique)), 2)
                        print(data[i].prod_physique_pou)
                        print(data[i].prod_conforme, data[i].prod_non_conforme,
                              data[i].deche_geometrique)
                final_data = {}

                i = 0
                for j in data:
                    final_data[i] = {}
                    print("j.ref ", j.ref)
                    final_data[i]['ref'] = j.ref
                    final_data[i]['obj'] = j.obj.value
                    final_data[i]['prod_physique'] = j.prod_physique
                    final_data[i]['prod_physique_pou'] = data[
                        i].prod_physique_pou
                    final_data[i]['prod_conforme'] = j.prod_conforme
                    final_data[i]['prod_conforme_pou'] = j.prod_conforme_pou
                    final_data[i]['prod_non_conforme'] = j.prod_non_conforme
                    final_data[i][
                        'prod_non_conforme_pou'] = j.prod_non_conforme_pou
                    final_data[i]['deche_geometrique'] = j.deche_geometrique
                    final_data[i][
                        'deche_geometrique_pou'] = j.deche_geometrique_pou
                    final_data[i]['nbr_barre'] = j.nbr_barre
                    final_data[i]['n_of'] = j.n_of
                    final_data[i]['date_created'] = j.date_created
                    i += 1
                print("final_data ", final_data)
                totalPPP = round(
                    totalPP['prod_physique__sum'] * 100 / data[0].obj.value, 2)
                totalPPC = round(
                    totalPC['prod_conforme__sum'] * 100 /
                    totalPP['prod_physique__sum'], 2)
                totalPPNC = round(
                    totalPNCP['prod_non_conforme__sum'] * 100 /
                    totalPP['prod_physique__sum'], 2)
                totalDGP = round(
                    totalDG['deche_geometrique__sum'] * 100 /
                    totalPP['prod_physique__sum'], 2)
                context = {
                    "final_data": final_data,
                    "totalPP": totalPP['prod_physique__sum'],
                    "totalPC": totalPC['prod_conforme__sum'],
                    "totalPNC": totalPNCP['prod_non_conforme__sum'],
                    "totalDG": totalDG['deche_geometrique__sum'],
                    "totalNBR": totalNBR['nbr_barre__sum'],
                    "totalPPP": totalPPP,
                    "totalPPC": totalPPC,
                    "totalPPNC": totalPPNC,
                    "totalDGP": totalDGP,
                    "len": len(data)
                }
            else:
                data[0].prod_physique = rapport.objects.filter(
                    date_created=dateC,
                    typeR=typeRap).aggregate(Sum('prod_physique_p_r'))
                print('je suis fel else')
                totalPC, totalPCP, totalPNC, totalPNCP = 0, 0, 0, 0
                for i in range(len(data)):
                    if data[i].prod_physique == 0:
                        data[i].prod_physique_pou = 0
                        data[i].prod_physique_p_r = 0
                        data[i].prod_conforme_pou = 0
                        data[i].prod_conforme = 0
                        data[i].prod_non_conforme = 0
                        data[i].prod_non_conforme_pou = 0
                    else:
                        data[0].prod_physique_pou = round(
                            ((data[0].prod_physique * 100 /
                              data[0].obj.value)), 2)
                        data[i].prod_conforme_pou = round(
                            ((data[i].prod_physique_p_r * 100 /
                              data[i].prod_physique_p_r)), 2)
                        data[i].prod_non_conforme_pou = 100 - data[
                            i].prod_conforme_pou

                        totalPC = totalPC + data[i].prod_conforme
                        totalPCP = totalPCP + data[i].prod_conforme_pou
                        totalPNC = totalPNC + data[i].prod_non_conforme
                        totalPNCP = totalPNCP + data[i].prod_non_conforme_pou
                totalPCP = totalPCP / (i + 1)
                totalPNCP = totalPNCP / (i + 1)
                print(totalPC, totalPCP, totalPNC, totalPNCP)
                final_data = {}
                i = 0
                for j in data:
                    final_data[i] = {}
                    final_data[i]['ref'] = j.ref
                    final_data[i]['obj'] = j.obj.value
                    final_data[i]['prod_physique'] = j.prod_physique
                    final_data[i][
                        'prod_physique_par_ref'] = j.prod_physique_p_r
                    final_data[i]['prod_physique_pou'] = data[
                        0].prod_physique_pou
                    final_data[i]['prod_conforme'] = j.prod_conforme
                    final_data[i]['prod_conforme_pou'] = j.prod_conforme_pou
                    final_data[i]['prod_non_conforme'] = j.prod_non_conforme
                    final_data[i][
                        'prod_non_conforme_pou'] = j.prod_non_conforme_pou
                    final_data[i]['n_of'] = j.n_of
                    final_data[i]['date_created'] = j.date_created
                    i += 1
                    print("final_data ", final_data)
                context = {
                    "final_data": final_data,
                    "totalPC": totalPC,
                    "totalPCP": totalPCP,
                    "totalPNC": totalPNC,
                    "totalPNCP": totalPNCP,
                    "len": len(data)
                }

        except Exception as e:
            print(e)
            context = {"final_data": {}}

        return HttpResponse(json.dumps(context),
                            content_type="application/json")
    else:
        raise Http404


def sauvegarder(rapportExistant, deche_geometrique, nbr_barre, prod_physique,
                prod_conforme, prod_non_conforme, n_of, realise,
                prod_physique_p_r, typeR, obj):

    if deche_geometrique != None and nbr_barre != None:
        rapportExistant.deche_geometrique = deche_geometrique
        rapportExistant.nbr_barre = nbr_barre
    else:
        rapportExistant.prod_physique_p_r = prod_physique_p_r
        rapportExistant.typeR = typeR
    rapportExistant.prod_physique = prod_physique
    rapportExistant.prod_conforme = prod_conforme
    rapportExistant.prod_non_conforme = prod_non_conforme
    rapportExistant.n_of = n_of
    rapportExistant.realise = realise
    rapportExistant.obj = obj
    rapportExistant.save()


def rapportEALR(request, typeR, data, datalength):
    if typeR == 'Extrusion':
        RapportJournalierConcerner = RapportJournalierE
    else:
        RapportJournalierConcerner = RapportJournalierALR

    for i in range(1, int(datalength) + 1):
        ref = request.POST['ref-{}'.format(i)]
        id = request.POST.get('id-{}'.format(i))
        prod_physique = request.POST['prod_physique-{}'.format(i)]
        prod_conforme = request.POST['prod_conforme-{}'.format(i)]
        prod_non_conforme = request.POST['prod_non_conforme-{}'.format(i)]
        n_of = request.POST['n_of-{}'.format(i)]
        realise = request.POST.get('realise-{}'.format(i))
        if realise == 'on':
            realise = 'True'
        else:
            realise = 'False'
        try:
            rapportExistant = RapportJournalierConcerner.objects.select_related(
            ).filter(ref=id)

            print('existe  ?: ', len(rapportExistant) > 0)
            if typeR == "Extrusion":
                obj = Objectif.objects.get(id=1)
            elif typeR == 'LaquageBlanc':
                type_du_rap = TypeRapport.objects.get(value='LaquageBlanc')
                obj = Objectif.objects.get(id=2)
            elif typeR == 'LaquageCouleur':
                type_du_rap = TypeRapport.objects.get(value='LaquageCouleur')
                obj = Objectif.objects.get(id=3)
            elif typeR == 'Anodisation':
                type_du_rap = TypeRapport.objects.get(value='Anodisation')
                print(type(type_du_rap))
                obj = Objectif.objects.get(id=4)
            else:
                type_du_rap = TypeRapport.objects.get(value='RPT')
                obj = Objectif.objects.get(id=5)

            if len(rapportExistant) > 0:
                if typeR == "Extrusion":
                    deche_geometrique = request.POST[
                        'deche_geometrique-{}'.format(i)]
                    nbr_barre = request.POST['nbr_barr-{}'.format(i)]
                    print(rapportExistant[0])
                    sauvegarder(rapportExistant[0], deche_geometrique,
                                nbr_barre, prod_physique, prod_conforme,
                                prod_non_conforme, n_of, realise, None, None,
                                obj)
                else:
                    prod_physique_p_r = request.POST[
                        'prod_physique_p_r-{}'.format(i)]
                    sauvegarder(rapportExistant[0], None, None, prod_physique,
                                prod_conforme, prod_non_conforme, n_of,
                                realise, prod_physique_p_r, type_du_rap, obj)

            else:
                if typeR == "Extrusion":
                    deche_geometrique = request.POST[
                        'deche_geometrique-{}'.format(i)]
                    nbr_barre = request.POST['nbr_barr-{}'.format(i)]

                    rapport = RapportJournalierConcerner(
                        ref=ref,
                        prod_physique=prod_physique,
                        prod_conforme=prod_conforme,
                        prod_non_conforme=prod_non_conforme,
                        deche_geometrique=deche_geometrique,
                        nbr_barre=nbr_barre,
                        n_of=n_of,
                        realise=realise,
                        obj=obj)
                else:
                    prod_physique_p_r = request.POST[
                        'prod_physique_p_r-{}'.format(i)]

                    rapport = RapportJournalierConcerner(
                        ref=ref,
                        prod_physique_p_r=prod_physique_p_r,
                        prod_physique=prod_physique,
                        prod_conforme=prod_conforme,
                        prod_non_conforme=prod_non_conforme,
                        realise=realise,
                        n_of=n_of,
                        typeR=type_du_rap,
                        obj=obj)

                rapport.save()

        except Exception as e:
            print(e)


def get_data(typeR, date_created):

    data = ProductionPlan.objects.filter(Q(date_created=date_created),
                                         typeP=typeR.lower())

    return data


def saveRapport(request, typeR):
    date_created = time.strftime("%Y-%m-%d", time.localtime())

    if request.method == "POST":
        datalength = request.POST['datalength']

        rapportEALR(request, typeR, get_data(typeR, date_created), datalength)

        return redirect('rapportAujourdui')
