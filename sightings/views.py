from django.shortcuts import render
from .models import Tracker
# Create your views here.



def showmap(request):
    sightings = Tracker.objects.all()
    context = {'sightings':sightings}
    
    return render(request,'sightings/map.html',context)
