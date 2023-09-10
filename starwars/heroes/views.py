from django.shortcuts import render

from django.http import HttpResponseBadRequest
import urllib.request
import json
from .models import Hero


def load_data():
    heroes = []
    next_url = "https://swapi.dev/api/people"
    while next_url:
        with urllib.request.urlopen(next_url) as r:
            if r.status == 200:
                data = json.loads(r.read().decode("utf-8"))
                heroes += data.get("results")
                next_url = data.get("next")
                
                print('loading ...')
              
    for item in heroes:
        el = Hero(
            title=item.get("name"),
            gender=item.get("gender"),
            height=item.get("height"),
            mass=item.get("mass"),
            birth_year=item.get("birth_year"),
        )
        el.save()


def index(request):
    if Hero.objects.count() == 0:
        load_data()
    if Hero.objects.count() == 0:
        return HttpResponseBadRequest("Heroes not available right now...")
    heroes = Hero.objects.all()[:25]
    context = {"list": [x for x in heroes], "path": "heroes"}
    return render(request, "index.html", context)
    
    # title,gender,height,mass,birth_year  
def detail(request, id):
    hero = Hero.objects.filter(id=id)\
    .values('title', 'gender', 'height', 'mass', 'birth_year' )[0]
    if hero:
        context = {"item": hero, "path": "heroes"}
        return render(request, "index.html", context)
    return HttpResponseBadRequest("Heroes not available right now...")
