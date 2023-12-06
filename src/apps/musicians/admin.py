from django.contrib import admin

from apps.musicians.models import Musician


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    ...
