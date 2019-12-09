
            
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tracker
import random
from .forms import Form


def showmap(request):
    sightings = list(Tracker.objects.all())
    if len(sightings) > 100:
        sightings = random.sample(sightings,100)
    context = {'sightings':sightings}
    return render(request,'sightings/map.html',context)

def sightings(request):
    sightings = Tracker.objects.order_by('unique_squirrel_id')
    context = {'sightings':sightings}
    return render(request, 'sightings/sightings.html', context)

def stats(request):
    count_sightings = Tracker.objects.all().count()
    adults = Tracker.objects.filter(age='Adult').count()
    cinnamons = Tracker.objects.filter(primary_fur_color = 'Cinnamon').count()
    plane_location = Tracker.objects.filter(location = 'Ground Plane').count()
    running_mode = Tracker.objects.filter(running = 'TRUE').count()
    context = {
            'count_sightings':count_sightings,
            'adults':adults,
            'cinnamons':cinnamons,
            'plane_location':plane_location,
            'running_mode':running_mode,
            }
    return render(request, 'sightings/stats.html',context)

def update(request,unique_squirrel_id):
    squirrel_id = get_object_or_404(Tracker, pk = unique_squirrell_id)
    form = Form(request.POST or None, instance=squirrel_id)
    context = {'form':form}
    if form.is_valid():
        Squirrel = form.save(commit=False)
        Squirrel.save()
        return redirect('/sightings/')
    else:
        context={'form':form}
        return render(request,'sightings/update.html',context)
def add(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
        else:
            form = Form()
            context = {'form':form}
            return render(request,'sightings/add.html',context))
