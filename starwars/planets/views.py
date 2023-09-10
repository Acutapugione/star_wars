from django.shortcuts import render
from django.http import HttpResponseBadRequest
import urllib.request
import json
from .models import Planet


def load_data():
    items = []
    next_url = "https://swapi.dev/api/planets"
    while next_url:
        with urllib.request.urlopen(next_url) as r:
            if r.status == 200:
                data = json.loads(r.read().decode("utf-8"))
                items += data.get("results")
                next_url = data.get("next")
                
                print('loading ...')
              
    # name, climate, gravity,population, terrain
    for item in items:
        el = Planet(
            name=item.get("name"),
            climate=item.get("climate"),
            gravity=item.get("gravity"),
            population=item.get("population"),
            terrain=item.get("terrain"),
        )
        el.save()


# Create your views here.
def index(request):
    if Planet.objects.count() == 0:
        load_data()
    if Planet.objects.count() == 0:
        return HttpResponseBadRequest("Planets not available right now...")
    items = Planet.objects.all()[:25]
    context = {"list": [x for x in items], "path": "planets"}
    return render(request, "index.html", context)
    
def detail(request, id):
    # name, climate, gravity,population, terrain
    item = Planet.objects.filter(id=id)\
    .values('name', 'climate', 'gravity', 'population', 'terrain' )[0]
    if item:
        context = {"item": item, "path": "planets"}
        return render(request, "index.html", context)
    return HttpResponseBadRequest("Planets not available right now...")

