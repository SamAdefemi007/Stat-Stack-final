from email import message
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Player, Country, Club
from django.core.paginator import Paginator
from django.core.exceptions import *
from django.contrib import messages
from django.urls import reverse
