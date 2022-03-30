from email import message
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Player, Country, Club
from django.core.paginator import Paginator
from django.core.exceptions import *
from django.contrib import messages
from django.urls import reverse


def club(request):
    try:
        clubObj = Club.objects.all().values_list(
            "clubName", flat=True).distinct()
    except ObjectDoesNotExist:
        print("the club object does not exist or could not be fetched from the database")
    playerobj = {}
    clubname = None
    clublogo = None
    if request.method == "POST":
        clubname = request.POST.get("clubSet")
        try:
            clublogo = Club.objects.all().filter(
                clubName=clubname).first().clubLogo
        except MultipleObjectsReturned:
            print(
                "The query returned more than one object, possible duplication of countryname or wrong queryset")
        else:
            playerobj = Player.objects.all().filter(
                playerClub__clubName=clubname).order_by("-skills__rating")

    return render(request, 'statlist/club.html', {'clubs': sorted(clubObj), 'players': playerobj, 'clubname': clubname, 'clublogo': clublogo})


    def profile(request):
    try:
        playerobj = Player.objects.all().order_by("-skills__rating")
    except ObjectDoesNotExist:
        print("the player object does not exist or could not be fetched from the database")
    else:
        paginator = Paginator(playerobj, 15)
        page_num = request.GET.get("page")
        page_obj = paginator.get_page(page_num)
    return render(request, 'statlist/profile.html', {'players': page_obj})
