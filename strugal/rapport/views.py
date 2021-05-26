from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from planing.models import ProductionPlanE
import time
from .models import *
from django.db.models import Q
from datetime import date
import json

# Create your views here.


def rapport(request):
    data = ProductionPlanE.objects.filter(
        Q(date_created=time.strftime("%Y-%m-%d",
                                     time.localtime()))).values_list('ref',
                                                                     flat=True)

    return render(request, "rapport/rapport_aujourdui.html", {
        'data': data,
        'list': len(data)
    })


def index(request):
    aujourdhui = date.today().strftime("%Y-%m-%d")
    data = RapportJournalierE.objects.filter(Q(date_created=aujourdhui))
    context = {"data": data}
    return render(request, 'rapport/index.html', context)


def rapportJ(request, typeR, dateC):
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
                        ((data[i].prod_physique * 100 / data[i].ref.qte)), 2)
                    data[i].prod_conforme_pou = round(
                        ((data[i].prod_conforme * 100 / data[i].ref.qte)), 2)
                    data[i].prod_non_conforme_pou = round(
                        ((data[i].prod_non_conforme * 100 / data[i].ref.qte)),
                        2)
                    data[i].deche_geometrique_pou = round(
                        ((data[i].deche_geometrique * 100 / data[i].ref.qte)),
                        2)
                print('prod_non_conforme_pou ', data[0].prod_non_conforme_pou)
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
                for i in range(len(data)):
                    data[i].prod_conforme_pou = round(
                        ((data[i].prod_conforme * 100 / data[i].ref.qte)), 2)
                    data[i].prod_non_conforme_pou = round(
                        ((data[i].prod_non_conforme * 100 / data[i].ref.qte)),
                        2)
                final_data = {}
                i = 0
                for j in data:
                    final_data[i] = {}
                    print(j.ref.ref)
                    final_data[i]['ref'] = j.ref.ref
                    final_data[i]['obj'] = "7"
                    final_data[i]['prod_physique'] = "1615" 
                    final_data[i]['prod_physique_pour'] = "108%" 
                    final_data[i]['prod_physique_par_ref'] = j.prod_physique
                    final_data[i]['prod_physique_pou'] = j.prod_physique_pou
                    final_data[i]['prod_conforme'] = j.prod_conforme
                    final_data[i]['prod_non_conforme'] = j.prod_non_conforme
                    final_data[i][
                        'prod_non_conforme_pou'] = j.prod_non_conforme_pou
                    final_data[i]['nbr_barre'] = j.nbr_barre
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


def saveThings(request):
    date_created = time.strftime("%Y-%m-%d", time.localtime())
    data = ProductionPlanE.objects.filter(Q(date_created=date_created))
    datalength = request.POST['datalength']
    for i in range(1, int(datalength) + 1):
        ref = data[i - 1]
        prod_physique = request.POST['prod_physique-{}'.format(i)]
        prod_conforme = request.POST['prod_conforme-{}'.format(i)]
        prod_non_conforme = request.POST['prod_non_conforme-{}'.format(i)]
        deche_geometrique = request.POST['deche_geometrique-{}'.format(i)]
        nbr_barre = request.POST['nbr_barr-{}'.format(i)]
        n_of = request.POST['n_of-{}'.format(i)]
        realise = request.POST.get('realise-{}'.format(i), 'False')
        if realise == 'on':
            realise = 'True'

        rapport = RapportJournalierE(ref=ref,
                                     prod_physique=prod_physique,
                                     prod_conforme=prod_conforme,
                                     prod_non_conforme=prod_non_conforme,
                                     deche_geometrique=deche_geometrique,
                                     nbr_barre=nbr_barre,
                                     n_of=n_of,
                                     realise=realise)

        rapport.save()


def saveRapport(request):
    date_created = time.strftime("%Y-%m-%d", time.localtime())
    data = ProductionPlanE.objects.filter(Q(date_created=date_created))
    if request.method == "POST":
        datalength = request.POST['datalength']
        if int(datalength) == len(data):
            saveThings(request)
        else:
            if len(data) == 0:
                longeur = 1
                print("longueur if ", longeur)
            else:
                longeur = len(data)
                print("longueur else ", longeur)
            print(datalength)
            for i in range(longeur, int(datalength) + 1):
                print("rani fel for ", i)
                print('ref-{}'.format(i))
                ref = request.POST.get('ref-{}'.format(i))
                print("ref ", ref)
                prod_physique = request.POST.get('prod_physique-{}'.format(i))
                print("prod_physique ", prod_physique)
                planing = ProductionPlanE(ref=ref,
                                          qte=prod_physique,
                                          date_created=date_created)

                planing.save()

            saveThings(request)

        return redirect('rapport')
