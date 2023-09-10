from django.db import models


# Create your models here.
class Planet(models.Model):
    id = models.IntegerField(
        auto_created=True,
        primary_key=True,
    )
    name = models.CharField(
        max_length=150,
        blank=True,
        unique=True,
    )
    climate = models.CharField(
        max_length=150,
        blank=True,
    )
    gravity = models.CharField(
        max_length=50,
        blank=True,
    )
    population = models.CharField(
        max_length=150,
        blank=True,
    )
    terrain = models.CharField(
        max_length=150,
        blank=True,
    )

    # name, climate, gravity,population, terrain
    def __str__(self):
        return self.name
    