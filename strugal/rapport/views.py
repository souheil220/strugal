from django.shortcuts import render, redirect
from planing.models import ProductionPlanE
import time
from .models import RapportJournalier
from django.db.models import Q

# Create your views here.


def rapport(request):
    data = ProductionPlanE.objects.filter(
        Q(date_created=time.strftime("%Y-%m-%d",
                                     time.localtime()))).values_list('ref',
                                                                     flat=True)

    return render(request, "rapport/index.html", {
        'data': data,
        'list': len(data)
    })


def rapportJ(request, date):

    data = RapportJournalier.objects.filter(Q(date_created=date))
    for i in range(len(data)):
        data[i].prod_physique_pou = round(
            ((data[i].prod_physique * 100 / data[i].ref.qte)), 2)
        data[i].prod_conforme_pou = round(
            ((data[i].prod_conforme * 100 / data[i].ref.qte)), 2)
        data[i].prod_non_conforme_pou = round(
            ((data[i].prod_non_conforme * 100 / data[i].ref.qte)), 2)
        data[i].deche_geometrique_pou = round(
            ((data[i].deche_geometrique * 100 / data[i].ref.qte)), 2)

    context = {'data': data, date: "date"}
    print(date)
    return render(request, "rapport/rapport.html", context)


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

        rapport = RapportJournalier(
            ref=ref,
            prod_physique=prod_physique,
            prod_conforme=prod_conforme,
            prod_non_conforme=prod_non_conforme,
            deche_geometrique=deche_geometrique,
            nbr_barre=nbr_barre,
            n_of=n_of,
        )

        rapport.save()


def saveRapport(request):
    date_created = time.strftime("%Y-%m-%d", time.localtime())
    data = ProductionPlanE.objects.filter(Q(date_created=date_created))
    print(len(data))
    if request.method == "POST":
        datalength = request.POST['datalength']
        if int(datalength) == len(data):
            saveThings(request)
        else:
            print(datalength)
            ref = request.POST.get('ref-{}'.format(datalength))
            print('reffffffffffffffffffffffff')
            print('ref-{}'.format(datalength))
            prod_physique = request.POST['prod_physique-{}'.format(datalength)]

            planing = ProductionPlanE((int(data[len(data) - 1].id) + 1), ref,
                                      prod_physique, date_created)
            planing.save()

            saveThings(request)

        return redirect('rapport')
