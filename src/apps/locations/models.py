from django.db import models


class Location(models.Model):
    name_point = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def get_map_link(self):
        # self.longitude = Location.longitude
        # self.latitude = Location.latitude
        if not self.latitude or not self.longitude:
            return None
        return f"https://yandex.ru/maps/?pt={self.longitude},{self.latitude}&z=19&l=map"
