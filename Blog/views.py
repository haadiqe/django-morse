from django.shortcuts import render
from django.http import HttpResponse
import datetime 

# Create your views here.

def date_time(request):
    now = datetime.datetime.now()
    return HttpResponse (now)
