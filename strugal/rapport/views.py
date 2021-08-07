from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from planing.models import *
from django.contrib.auth.models import User
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
        typeP=TypePlaning.objects.get(typeP=typeR.lower()))
    test = []
    try:
        for plan in data:
            haja = []
            rapport = reportM.objects.filter(ref=plan).values()
            haja.append(rapport)
            haja.append(plan)
            test.append(haja)

        i = 0

        for t in test:
            if i < len(test):

                if typeR == 'Extrusion':

                    test[i].deche_geometrique = t[0]['deche_geometrique']
                    # print(data[i].deche_geometrique)
                    test[i].nbr_barre = t[0]['nbr_barre']
                else:
                    test[i].prod_physique_p_r = t[0]['prod_physique_p_r']

            i += 1
        return test
    except:
        return test


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
        context = {'data': data, 'list': test, "typeR": typeR}
        return render(request, 'rapport/rediget_rapport.html', context)


@login_required(login_url='login')
def rapportAujourdui(request):
    aujourdhui = date.today().strftime("%Y-%m-%d")
    typeR = TypeRapport.objects.get(value='Anodisation')
    data = RapportJournalierALR.objects.filter(date_created=aujourdhui,
                                               typeR=typeR)

    if (len(data) > 0):
        data = list(data)
        result_calc_data = calc_data(list(data), typeR, RapportJournalierALR)
        prod_phy_pour = round(
            result_calc_data['totalProd'] * 100 / data[0].obj.value, 2)
        context = {
            "data": data,
            "totalPPPR": result_calc_data['totalProd'],
            "totalPC": result_calc_data['totalPC'],
            "totalPNC": result_calc_data["totalPNC"],
            "prod_phy_pour": prod_phy_pour
        }
    else:
        context = {
            "data": "",
            "totalPC": "",
            "totalPCP": "",
            "totalPNC": "",
            "totalPNCP": ""
        }
    return render(request, 'rapport/rapportAujourdui.html', context)


def rapportJ(request, typeR, dateC):
    if request.is_ajax and request.method == 'GET':
        try:
            if typeR == 'Extrusion':
                data = RapportJournalierE.objects.filter(date_created=dateC)
                totalDG = RapportJournalierE.objects.filter(
                    date_created=dateC).aggregate(Sum('deche_geometrique'))
                totalNBR = RapportJournalierE.objects.filter(
                    date_created=dateC).aggregate(Sum('nbr_barre'))
                result_calc_data = calc_data(list(data), typeR,
                                             RapportJournalierE)
                result_calc_data['totalDG'] = totalDG['deche_geometrique__sum']
                result_calc_data['totalNBR'] = totalNBR["nbr_barre__sum"]

            else:
                typeRap = TypeRapport.objects.get(value=typeR)
                data = RapportJournalierALR.objects.filter(date_created=dateC,
                                                           typeR=typeRap)
                result_calc_data = calc_data(list(data), typeR,
                                             RapportJournalierALR)
                prod_phy_pour = round(
                    result_calc_data['totalProd'] * 100 / data[0].obj.value, 2)
                result_calc_data['prod_phy_pour'] = prod_phy_pour

            result = result_calc_data
            print("result ", result)
            final_data = data_returned(data, typeR)
            context = {
                "final_data": final_data,
                "result": result,
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
    if typeR == "Extrusion":
        obj = Objectif.objects.get(id=1)
    elif typeR == 'LaquageBlanc':
        type_du_rap = TypeRapport.objects.get(value='Laquage Blanc')
        obj = Objectif.objects.get(id=2)
    elif typeR == 'LaquageCouleur':
        type_du_rap = TypeRapport.objects.get(value='Laquage Couleur')
        obj = Objectif.objects.get(id=3)
    elif typeR == 'Anodisation':
        type_du_rap = TypeRapport.objects.get(value='Anodisation')
        print(type(type_du_rap))
        obj = Objectif.objects.get(id=4)
    else:
        type_du_rap = TypeRapport.objects.get(value='RPT')
        obj = Objectif.objects.get(id=5)

    print(typeR)
    if typeR == 'Extrusion':
        RapportJournalierConcerner = RapportJournalierE
    else:
        RapportJournalierConcerner = RapportJournalierALR

    for i in range(1, int(datalength) + 1):
        ref = data[i - 1]
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
            print(id)
            rapportExistant = RapportJournalierConcerner.objects.select_related(
            ).filter(ref=ref)

            print('existe  ?: ', len(rapportExistant) > 0)

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

    data = ProductionPlan.objects.filter(
        Q(date_created=date_created),
        typeP=TypePlaning.objects.get(typeP=typeR.lower()))

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


def savePlaning(request, typeR, longeur, datalength, date_created):
    print("longeur ", longeur)
    print("datalength ", datalength)
    for i in range(longeur + 1, datalength):
        print("i ", i)
        print("ref ", request.POST.get('ref-{}'.format(i)))
        ref = request.POST.get('ref-{}'.format(i))

        prod_physique = request.POST.get('prod_physique-{}'.format(i))
        planing = ProductionPlan(
            ref=ref,
            qte=prod_physique,
            date_created=date_created,
            typeP=TypePlaning.objects.get(typeP=typeR.lower()),
            planned=False)
        planing.save()


def calc_data(data, typeR, rapport):
    final_data = {}
    aujourdhui = date.today().strftime("%Y-%m-%d")
    if typeR == "Extrusion":
        field = "prod_physique"
    else:
        print(rapport)
        field = "prod_physique_p_r"
        data[0].prod_physique_pour = 100
    totalPC = rapport.objects.filter(date_created=aujourdhui).aggregate(
        Sum('prod_conforme'))
    totalPNC = rapport.objects.filter(date_created=aujourdhui).aggregate(
        Sum('prod_non_conforme'))
    totalProd = rapport.objects.filter(date_created=aujourdhui).aggregate(
        Sum(field))
    field = field + "__sum"
    final_data["totalPC"] = totalPC['prod_conforme__sum']
    final_data["totalPNC"] = totalPNC['prod_non_conforme__sum']
    final_data["totalProd"] = totalProd[field]
    print(final_data)
    return final_data


def data_returned(data, typeR):
    final_data = {}

    i = 0
    for j in data:
        final_data[i] = {}
        final_data[i]['ref'] = j.ref.ref
        final_data[i]['obj'] = j.obj.value
        if typeR == "Extrusion":
            final_data[i]["prod_physique"] = j.prod_physique
            final_data[i]['deche_geometrique'] = j.deche_geometrique
            final_data[i]['nbr_barre'] = j.nbr_barre
        else:
            final_data[i]["prod_physique_p_r"] = j.prod_physique_p_r

        final_data[i]['prod_conforme'] = j.prod_conforme
        final_data[i]['prod_non_conforme'] = j.prod_non_conforme
        final_data[i]['n_of'] = j.n_of
        i += 1

    print(final_data)
    return final_data


def update_obj(request):
    if request.method == "POST":
        updated_obj = request.POST['obj']
        type_of_p = request.POST['typeP']
        obj = Objectif.objects.get(id=int(type_of_p))
        obj.value = float(updated_obj)
        obj.save()

    type_Planing = TypePlaning.objects.all()
    context = {"type_Planing": type_Planing}
    return render(request, 'rapport/update_objectif.html', context)


def donner_permission(request):
    if request.method == "POST":
        ad2000 = request.POST['ad2000'].lower()
        email = request.POST['email']
        utilisateur = User.objects.create_user(username=ad2000,
                                               email=email,
                                               password='Azerty@22')
        utilisateur.save()

    return render(
        request,
        'rapport/donner_permission.html',
    )
