from django.db import models

# Create your models here.
class Hero(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True,)
    title = models.CharField(unique=True, max_length=150, blank=True,)
    gender = models.CharField(max_length=50, blank=True,)
    height = models.CharField(max_length=50,blank=True,)
    mass = models.CharField(max_length=50,blank=True,)
    birth_year = models.CharField(max_length=20, blank=True,)
    
    
    def __str__(self):
        return self.title
    