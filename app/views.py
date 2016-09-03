from django.shortcuts import render
from django import forms
from geoposition.forms import GeopositionField

from app.models import PointOfInterest, PeopleWeKnow

# Create your views here.

def home_view(request):
    return render(request,'home.html')



def poi_list(request):
    pois = PointOfInterest.objects.all()
    return render(request, 'poi_list.html', {'pois': pois})

def pwk_list(request):
    pwks = PeopleWeKnow.objects.all()
    return render(request, 'whoweknow.html', {'pwks': pwks})
