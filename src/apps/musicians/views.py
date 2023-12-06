from django.http.request import HttpRequest
from django.shortcuts import render

from apps.musicians.models import Musician


def index(request: HttpRequest):
    genre = request.GET.get("genre")

    if genre:
        musicians = Musician.objects.filter(genre=genre)
    else:
        musicians = Musician.objects.all()

    return render(request, "musicians/index.html", context={"musicians": musicians})


def create(request: HttpRequest):
    if not request.method:
        raise ValueError("Method not allowed")

    if request.method.lower() == "get":
        return render(request, "musicians/create.html")
    elif request.method.lower() == "post":
        data = request.POST
        musician = Musician.objects.create(
            name=data["name"],
            genre=data["genre"],
            description=data["description"],
        )
        return render(request, "musicians/create.html", context={"musician": musician})

    raise ValueError("Method not allowed")
