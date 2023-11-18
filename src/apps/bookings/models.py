from django.db import models
from ..musicians.models import Musician
from ..locations.models import Location
from .const import BookingStatus


class Booking(models.Model):
    # музыкант (связь с моделью Musician)
    musician = models.ForeignKey(Musician, on_delete=models.PROTECT)
    # локация (связь с моделью Location)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    # дата-время начала
    date_time_start = models.DateTimeField(
        null=True, blank=True, help_text='дата-время начала')
    # статус (статус бронирования)

    status = models.IntegerField(
        choices=BookingStatus.choices, default=BookingStatus.SUBMITTED)
