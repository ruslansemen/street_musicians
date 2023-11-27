# Generated by Django 4.2.7 on 2023-11-27 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("musicians", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Repertoire",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("song_title_auth", models.CharField(max_length=100)),
                ("duration", models.DurationField(blank=True, null=True)),
                (
                    "musician_auth",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="repertoires",
                        to="musicians.musician",
                    ),
                ),
            ],
        ),
    ]
