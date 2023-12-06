from django.db import models


# class Genre(models.Choices):
#     ROCK = "Rock"


class Musician(models.Model):
    name = models.CharField(max_length=80)
    genre = models.CharField(max_length=200)
    description = models.TextField(default="")
    date_of_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | {self.genre} | {self.description} | {self.date_of_registration}"

    # many to one
    # repertoire_set: "models.RelatedManager[Repertoire]"
