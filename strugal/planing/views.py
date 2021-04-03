from django.shortcuts import render,redirect
from.models import ProductionPlan

def planing(request):
    return render(request,"planing/index.html")
    # return render(request,"planing/ess.html")