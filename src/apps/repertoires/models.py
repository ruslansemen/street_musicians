from django.db import models
from ..musicians.models import Musician


class Repertoire(models.Model):
    song_title_auth = models.CharField(max_length=100)
    # уточнить правильность выбора типа данных:
    duration = models.DurationField(null=True, blank=True)
    musician_auth = models.ForeignKey(Musician, on_delete=models.CASCADE)
