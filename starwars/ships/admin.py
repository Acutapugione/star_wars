from django.contrib import admin

# Register your models here.
from .models import Starship


class StarshipAdmin(admin.ModelAdmin):
    pass


admin.site.register(Starship, StarshipAdmin)