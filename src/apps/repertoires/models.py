from django.db import models

from ..musicians.models import Musician


class Repertoire(models.Model):
    song_title_auth = models.CharField(max_length=100)
    # уточнить правильность выбора типа данных:
    duration = models.DurationField(null=True, blank=True)
    # one to many
    musician_auth = models.ForeignKey(
        Musician, on_delete=models.CASCADE, related_name="repertoires"
    )
    # one to one
    # models.OneToOneField(related_name="repertoire")
