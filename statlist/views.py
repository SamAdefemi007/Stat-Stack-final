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


def compare(request):
        try:
            playerObj = Player.objects.all().values_list(
            "playerName", flat=True).distinct()
        except ObjectDoesNotExist:
            print("the club object does not exist or could not be fetched from the database")
        
        player1object = None
        player2object = None

        player1 = request.GET.get("player1")
        player2 = request.GET.get("player2")

        if player1 != None:
            if player1 == player2:
                messages.add_message(request, messages.INFO, f"Warning: We are unable to compare the same player \"{player1}\",  Please Select different players and try again!")
        else:
            player1object = Player.objects.get(playerName=player1)
            player2object = Player.objects.get(playerName=player2)
        return render(request, 'statlist/compare.html', {'players': playerObj, 'player1': player1object, 'player2': player2object})