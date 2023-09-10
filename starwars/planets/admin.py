from django.contrib import admin

# Register your models here.
from .models import Planet


class PlanetAdmin(admin.ModelAdmin):
    pass


admin.site.register(Planet, PlanetAdmin)