from django.shortcuts import render
from django.http import HttpResponseBadRequest
import urllib.request
import json
from .models import Film


def load_data():
    url = "https://swapi.dev/api/films"
    with urllib.request.urlopen(url) as r:
        if r.status == 200:
            data = json.loads(r.read().decode("utf-8"))
            films = data.get("results")
            for item in films:
                el = Film(
                    id=item.get("episode_id"),
                    title=item.get("title"),
                    body=item.get("opening_crawl"),
                )
                el.save()


# Create your views here.
def index(request):
    if Film.objects.count() == 0:
        load_data()
    if Film.objects.count() == 0:
        return HttpResponseBadRequest("Films not available right now...")
    films = Film.objects.all()
    context = {"list": [x for x in films], "path": "films"}
    return render(request, "index.html", context)
    
def detail(request, id):
    film = Film.objects.filter(id=id)\
    .values('title', 'body')[0]
    if film:
        context = {"item": film, "path": "films"}
        return render(request, "index.html", context)
    return HttpResponseBadRequest("Films not available right now...")

