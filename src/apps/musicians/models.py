from django.db import models

# Create your models here.


class Musician(models.Model):
    name = models.CharField(max_length=80)
    genre = models.CharField(max_length=200)
    description = models.TextField(default='')
    date_of_registration = models.DateTimeField(
        auto_now_add=True)
