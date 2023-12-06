from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from apps.musicians.models import Musician


def index(request):
    # get_object_or_404(Musician, pk=1)
    Musician or None
    musicians = Musician.objects.all()
    # library Jinja2 for templates
    return render(request, "musicians/index.html", context={"musicians": musicians})
