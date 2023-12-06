from django.http import HttpResponse

from apps.musicians.models import Musician


def index(request):
    musicians = Musician.objects.all()
    return HttpResponse(musicians)
