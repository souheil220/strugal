from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .sql import connexion_ad2000, connexion_email
import re

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect("planing/")
    else:
        return redirect("login")


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        pass_django = 'Azerty@22'
        if not re.match(r"^[A-Za-z0-9\.\+-]+@[A-Za-z0-9\.-]+\.[a-zA-Z]*$",
                        username):
            email_util = 'GROUPE-HASNAOUI\\' + username
            connexion = connexion_ad2000(email_util, password)
        else:
            connexion = connexion_email(username, password)
        if connexion == 'deco':
            messages.error(request, 'Accès non autorisé')
            return render(request, 'pages/login.html', {'msg': ''})
        else:
            print(connexion['ad_2000'])
            user = authenticate(request,
                                username=connexion['ad_2000'],
                                password=pass_django)

            if user is not None:
                login(request, user)
                return redirect("planing/")

            else:
                utilisateur = User.objects.create_user(username, None,
                                                       'Azerty@22')
                utilisateur.save()
                user = authenticate(request,
                                    username=connexion['ad_2000'],
                                    password=pass_django)
                login(request, user)
                return redirect("planing/")
                # messages.error(request, 'username or password is invalid')
    return render(request, 'pages/login.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        if '@' in username:
            try:
                user = User.objects.get(email=username)
            except:
                messages.error(request, 'Utilisateur innexistant')
                return render(request, 'pages/login.html')

        else:
            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, 'Utilisateur innexistant')
                return render(request, 'pages/login.html')

            # connexionAd(request, username, password)
        pass_django = 'Azerty@22'
        if not re.match(r"^[A-Za-z0-9\.\+-]+@[A-Za-z0-9\.-]+\.[a-zA-Z]*$",
                        username):
            email_util = 'GROUPE-HASNAOUI\\' + username
            connexion = connexion_ad2000(email_util, password)
        else:
            connexion = connexion_email(username, password)

        print("connexion ", connexion)
        if connexion == 'deco':
            messages.error(request, 'Something went wrong')
        else:

            user = authenticate(request,
                                username=connexion['ad_2000'],
                                password=pass_django)

            if user is not None:
                login(request, user)
                return redirect("index")

            else:
                messages.error(request, 'Accès non autorisé')

    return render(request, 'pages/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')
