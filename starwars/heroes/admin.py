from django.contrib import admin

# Register your models here.
from .models import Hero


class HeroAdmin(admin.ModelAdmin):
    pass


admin.site.register(Hero, HeroAdmin)