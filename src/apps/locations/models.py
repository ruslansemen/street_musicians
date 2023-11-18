from django.db import models

# Create your models here.


class Location(models.Model):
    name_point = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def get_map_link(self):
        self.longitude
