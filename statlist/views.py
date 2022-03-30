from email import message
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Player, Country, Club
from django.core.paginator import Paginator
from django.core.exceptions import *
from django.contrib import messages
from django.urls import reverse


def country(request):
    try:
        countryObj = Country.objects.all().values_list(
            "countryName", flat=True).distinct()
    except ObjectDoesNotExist:
        print("the country object does not exist or could not be fetched from the database")
    playerobj = {}
    countryname = None
    countryflag = None
    if request.method == "POST":
        countryname = request.POST["countrySet"]
        try:
            countryflag = Country.objects.all().filter(
                countryName=countryname).first().countryFlag
        except MultipleObjectsReturned:
            print(
                "The query returned more than one object, possible duplication of countryname or wrong queryset")
        else:
            playerobj = Player.objects.all().filter(
                playerCountry__countryName=countryname).order_by("-skills__rating")
    return render(request, 'statlist/country.html', {'countries': countryObj, 'players': playerobj, 'countryname': countryname, 'countryflag': countryflag})

