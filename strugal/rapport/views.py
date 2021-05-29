from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from planing.models import *
import time
from .models import *
from django.db.models import Q
from datetime import date
import json

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


def rapportAujourdui(request):
    aujourdhui = date.today().strftime("%Y-%m-%d")
    data = RapportJournalierA.objects.filter(date_created=aujourdhui)
    for i in range(len(data)):
        data[i].prod_physique_pou = round(
            ((data[i].prod_physique * 100 / data[i].ref.qte)), 2)
        data[i].prod_conforme_pou = round(
            ((data[i].prod_conforme * 100 / data[i].ref.qte)), 2)
        data[i].prod_non_conforme_pou = round(
            ((data[i].prod_non_conforme * 100 / data[i].ref.qte)), 2)

    context = {"data": data}
    return render(request, 'rapport/rapportAujourdui.html', context)


def rapportJ(request, typeR, dateC):
    print(typeR)
    if request.is_ajax and request.method == 'GET':
        try:
            if typeR == 'Anodisation':
                data = RapportJournalierA.objects.filter(date_created=dateC)
            elif typeR == 'Extrusion':
                data = RapportJournalierE.objects.filter(date_created=dateC)
            elif typeR == 'Language Blanc':
                data = RapportJournalierLB.objects.filter(date_created=dateC)
            elif typeR == 'Language Couleur':
                data = RapportJournalierLC.objects.filter(date_created=dateC)
            else:
                data = RapportJournalierRPT.objects.filter(date_created=dateC)

            if typeR == 'Extrusion':
                for i in range(len(data)):
                    data[i].prod_physique_pou = round(
                        (((data[i].prod_physique) * 100 / data[i].ref.qte)) *
                        1000, 2)
                    data[i].prod_conforme_pou = round(
                        ((data[i].prod_conforme * 100 /
                          data[i].prod_physique)), 2)
                    data[i].prod_non_conforme_pou = round(
                        ((data[i].prod_non_conforme * 100 /
                          data[i].prod_physique)), 2)
                    data[i].deche_geometrique_pou = round(
                        ((data[i].deche_geometrique * 100 /
                          data[i].prod_physique)), 2)
                final_data = {}
                i = 0
                for j in data:
                    final_data[i] = {}
                    print(j.ref.ref)
                    final_data[i]['ref'] = j.ref.ref
                    final_data[i]['obj'] = "7"
                    final_data[i]['prod_physique'] = j.prod_physique
                    final_data[i]['prod_physique_pou'] = j.prod_physique_pou
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
                context = {"final_data": final_data}
            else:
                print('je suis fel else')
                for i in range(len(data)):
                    data[i].prod_physique_pou = round(
                        ((data[i].prod_physique * 100 / data[i].ref.qte)), 2)
                    data[i].prod_conforme_pou = round(
                        ((data[i].prod_conforme * 100 / data[i].ref.qte)), 2)
                    data[i].prod_non_conforme_pou = round(
                        ((data[i].prod_non_conforme * 100 / data[i].ref.qte)),
                        2)
                final_data = {}
                i = 0
                print(data[0].prod_physique_pou)
                for j in data:
                    final_data[i] = {}
                    print(j.ref.ref)
                    final_data[i]['ref'] = j.ref.ref
                    final_data[i]['obj'] = "7"
                    final_data[i]['prod_physique'] = j.prod_physique
                    final_data[i][
                        'prod_physique_par_ref'] = j.prod_physique_p_r
                    final_data[i]['prod_physique_pou'] = j.prod_physique_pou
                    final_data[i]['prod_conforme'] = j.prod_conforme
                    final_data[i]['prod_conforme_pou'] = j.prod_conforme_pou
                    final_data[i]['prod_non_conforme'] = j.prod_non_conforme
                    final_data[i][
                        'prod_non_conforme_pou'] = j.prod_non_conforme_pou
                    final_data[i]['n_of'] = j.n_of
                    final_data[i]['date_created'] = j.date_created
                    i += 1
                print("final_data ", final_data)
                context = {"final_data": final_data}

        except:
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


def saveRapport(request, typeR):
    date_created = time.strftime("%Y-%m-%d", time.localtime())
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

            rapportEALR(request, typeR, data, datalength)

        return redirect('rapportAujourdui')
