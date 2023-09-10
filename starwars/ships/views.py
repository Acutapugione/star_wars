from django.shortcuts import render
from django.http import HttpResponseBadRequest
import urllib.request
import json
from .models import Starship


def load_data():
    items = []
    next_url = "https://swapi.dev/api/starships"
    while next_url:
        with urllib.request.urlopen(next_url) as r:
            if r.status == 200:
                data = json.loads(r.read().decode("utf-8"))
                items += data.get("results")
                next_url = data.get("next")

                print("loading ...")

    # name, climate, gravity,population, terrain
    for item in items:
        el = Starship(
            name=item.get("name"),
            model=item.get("model"),
            manufacturer=item.get("manufacturer"),
            cost_in_credits=item.get("cost_in_credits"),
            length=item.get("length"),
            starship_class=item.get("starship_class"),
        )
        el.save()


# Create your views here.
def index(request):
    if Starship.objects.count() == 0:
        load_data()
    if Starship.objects.count() == 0:
        return HttpResponseBadRequest("Starships not available right now...")
    items = Starship.objects.all()[:25]
    context = {"list": [x for x in items], "path": "ships"}
    return render(request, "index.html", context)


def detail(request, id):
    # name, climate, gravity,population, terrain
    item = Starship.objects.filter(id=id).values(
        "name",
        "model",
        "manufacturer",
        "cost_in_credits",
        "length",
        "starship_class",
    )[0]
    if item:
        context = {"item": item, "path": "ships"}
        return render(request, "index.html", context)
    return HttpResponseBadRequest("Starships not available right now...")
