from django.db import models


class Location(models.Model):
    name_point = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def get_map_link(self):
        # self.longitude = Location.longitude
        # self.latitude = Location.latitude
        if not (self.latitude and self.longitude):
            return None
        return f"https://yandex.ru/maps/?ll={self.longitude},{self.latitude}&z=12&l=map"
