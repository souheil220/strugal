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


def checkRepport(productP, reportM, typeR):
    data = productP.objects.filter(
        Q(date_created=time.strftime("%Y-%m-%d", time.localtime())))

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
        data = checkRepport(ProductionPlanE, RapportJournalierE, typeR)
        if data is not None:
            test = len(data)
        context = {'data': data, 'list': test, "typeR": typeR}
        return render(request, 'rapport/rediget_rapportE.html', context)
    else:
        if typeR == 'Anodisation':
            data = checkRepport(ProductionPlanA, RapportJournalierA, typeR)

        elif typeR == 'LaquageBlanc':
            data = checkRepport(ProductionPlanLB, RapportJournalierLB, typeR)

        elif typeR == 'LaquageCouleur':
            data = checkRepport(ProductionPlanLC, RapportJournalierLC, typeR)

        else:
            data = checkRepport(ProductionPlanRPT, RapportJournalierRPT, typeR)

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
    data = RapportJournalierA.objects.filter(date_created=aujourdhui)
    if (len(data) > 0):
        data[0].prod_physique = RapportJournalierA.objects.filter(
            date_created=aujourdhui).aggregate(Sum('prod_physique_p_r'))
        totalPC, totalPCP, totalPNC, totalPNCP = 0, 0, 0, 0
        for i in range(len(data)):
            data[0].prod_physique_pou = round(
                ((data[0].prod_physique['prod_physique_p_r__sum'] * 100 /
                  data[0].obj)), 2)
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
            if typeR == 'Anodisation':
                rapport = RapportJournalierA
                data = RapportJournalierA.objects.filter(date_created=dateC)
            elif typeR == 'Extrusion':
                data = RapportJournalierE.objects.filter(date_created=dateC)
            elif typeR == 'Language Blanc':
                rapport = RapportJournalierLB
                data = RapportJournalierLB.objects.filter(date_created=dateC)
            elif typeR == 'Language Couleur':
                rapport = RapportJournalierLC
                data = RapportJournalierLC.objects.filter(date_created=dateC)
            else:
                rapport = RapportJournalierRPT
                data = RapportJournalierRPT.objects.filter(date_created=dateC)

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
                             data[i].obj), 2)

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
                    print(j.ref.ref)
                    final_data[i]['ref'] = j.ref.ref
                    final_data[i]['obj'] = j.obj
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
                    totalPP['prod_physique__sum'] * 100 / data[0].obj, 2)
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
                }
            else:
                data[0].prod_physique = rapport.objects.filter(
                    date_created=dateC).aggregate(Sum('prod_physique_p_r'))
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
                            ((data[0].prod_physique * 100 / data[0].obj)), 2)
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
                    print(j.ref.ref)
                    final_data[i]['ref'] = j.ref.ref
                    final_data[i]['obj'] = j.obj
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


def savePlaning(request, typeR, longeur, datalength, date_created):
    for i in range(longeur, datalength):
        ref = request.POST.get('ref-{}'.format(i))
        if typeR == 'Extrusion':
            prod_physique = request.POST.get('prod_physique-{}'.format(i))
            planing = ProductionPlanE(ref=ref,
                                      qte=prod_physique,
                                      date_created=date_created)
        else:
            prod_physique = request.POST.get('prod_physique_p_r-{}'.format(i))
            if typeR == 'Anodisation':
                planing = ProductionPlanA(ref=ref,
                                          qte=prod_physique,
                                          date_created=date_created)
            elif typeR == 'LaquageBlanc':
                planing = ProductionPlanLB(ref=ref,
                                           qte=prod_physique,
                                           date_created=date_created)
            elif typeR == 'LaquageCouleur':
                planing = ProductionPlanLC(ref=ref,
                                           qte=prod_physique,
                                           date_created=date_created)
            else:
                planing = ProductionPlanRPT(ref=ref,
                                            qte=prod_physique,
                                            date_created=date_created)

        planing.save()


def sauvegarder(rapportExistant, deche_geometrique, nbr_barre, obj,
                prod_physique, prod_conforme, prod_non_conforme, n_of, realise,
                prod_physique_p_r):

    if deche_geometrique != None and nbr_barre != None:
        rapportExistant.deche_geometrique = deche_geometrique
        rapportExistant.nbr_barre = nbr_barre
    else:
        rapportExistant.prod_physique_p_r = prod_physique_p_r
    rapportExistant.obj = obj
    rapportExistant.prod_physique = prod_physique
    rapportExistant.prod_conforme = prod_conforme
    rapportExistant.prod_non_conforme = prod_non_conforme
    rapportExistant.n_of = n_of
    rapportExistant.realise = realise
    rapportExistant.save()


def rapportEALR(request, typeR, data, datalength):
    if typeR == 'Extrusion':
        RapportJournalierConcerner = RapportJournalierE
    elif typeR == 'Anodisation':
        RapportJournalierConcerner = RapportJournalierA
    elif typeR == 'LaquageBlanc':
        RapportJournalierConcerner = RapportJournalierLB
    elif typeR == 'LaquageCouleur':
        RapportJournalierConcerner = RapportJournalierLC
    else:
        RapportJournalierConcerner = RapportJournalierRPT

    for i in range(1, int(datalength) + 1):
        ref = data[i - 1]
        id = request.POST.get('id-{}'.format(i))
        obj = request.POST['obj-{}'.format(i)]
        prod_physique = request.POST['prod_physique-{}'.format(i)]
        prod_conforme = request.POST['prod_conforme-{}'.format(i)]
        prod_non_conforme = request.POST['prod_non_conforme-{}'.format(i)]
        n_of = request.POST['n_of-{}'.format(i)]
        realise = request.POST.get('realise-{}'.format(i), 'False')
        if realise == 'on':
            realise = 'True'

        try:

            rapportExistant = RapportJournalierConcerner.objects.select_related(
            ).filter(ref=id)

            print('existe  ?: ', len(rapportExistant) > 0)
            if len(rapportExistant) > 0:
                if typeR == "Extrusion":
                    deche_geometrique = request.POST[
                        'deche_geometrique-{}'.format(i)]
                    nbr_barre = request.POST['nbr_barr-{}'.format(i)]
                    print(rapportExistant[0])
                    sauvegarder(
                        rapportExistant[0],
                        deche_geometrique,
                        nbr_barre,
                        obj,
                        prod_physique,
                        prod_conforme,
                        prod_non_conforme,
                        n_of,
                        realise,
                        None,
                    )
                else:
                    prod_physique_p_r = request.POST[
                        'prod_physique_p_r-{}'.format(i)]
                    sauvegarder(
                        rapportExistant[0],
                        None,
                        None,
                        obj,
                        prod_physique,
                        prod_conforme,
                        prod_non_conforme,
                        n_of,
                        realise,
                        prod_physique_p_r,
                    )

            else:

                if typeR == "Extrusion":
                    deche_geometrique = request.POST[
                        'deche_geometrique-{}'.format(i)]
                    nbr_barre = request.POST['nbr_barr-{}'.format(i)]

                    rapport = RapportJournalierConcerner(
                        ref=ref,
                        prod_physique=prod_physique,
                        obj=obj,
                        prod_conforme=prod_conforme,
                        prod_non_conforme=prod_non_conforme,
                        deche_geometrique=deche_geometrique,
                        nbr_barre=nbr_barre,
                        n_of=n_of,
                        realise=realise)
                else:
                    prod_physique_p_r = request.POST[
                        'prod_physique_p_r-{}'.format(i)]
                    rapport = RapportJournalierConcerner(
                        ref=ref,
                        obj=obj,
                        prod_physique_p_r=prod_physique_p_r,
                        prod_physique=prod_physique,
                        prod_conforme=prod_conforme,
                        prod_non_conforme=prod_non_conforme,
                        n_of=n_of)

                rapport.save()

        except Exception as e:
            print(e)


def get_data(typeR, date_created):
    if typeR == 'Extrusion':
        data = ProductionPlanE.objects.filter(Q(date_created=date_created))
    elif typeR == 'Anodisation':
        data = ProductionPlanA.objects.filter(Q(date_created=date_created))
    elif typeR == 'LaquageBlanc':
        data = ProductionPlanLB.objects.filter(Q(date_created=date_created))
    elif typeR == 'LaquageCouleur':
        data = ProductionPlanLC.objects.filter(Q(date_created=date_created))
    else:
        data = ProductionPlanRPT.objects.filter(Q(date_created=date_created))
    return data


def saveRapport(request, typeR):
    date_created = time.strftime("%Y-%m-%d", time.localtime())
    data = get_data(typeR, date_created)

    if request.method == "POST":
        datalength = request.POST['datalength']
        if int(datalength) == len(data):
            rapportEALR(request, typeR, data, datalength)

        else:
            if len(data) == 0:
                longeur = 1
            else:
                longeur = len(data)

            savePlaning(request, typeR, longeur,
                        int(datalength) + 1, date_created)

            rapportEALR(request, typeR, get_data(typeR, date_created),
                        datalength)

        return redirect('rapportAujourdui')
