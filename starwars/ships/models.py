from django.db import models


# Create your models here.
class Starship(models.Model):
    id = models.IntegerField(
        primary_key=True,
        auto_created=True,
    )
    name = models.CharField(
        max_length=150,
        blank=True,
    )
    model = models.CharField(
        max_length=150,
        blank=True,
    )
    manufacturer = models.CharField(
        max_length=150,
        blank=True,
    )
    cost_in_credits = models.CharField(
        max_length=150,
        blank=True,
    )
    length = models.CharField(
        max_length=150,
        blank=True,
    )
    starship_class = models.CharField(
        max_length=150,
        blank=True,
    )

    def __str__(self):
        return self.name
    