from django.db import models

# Create your models here.
class Film(models.Model):
    id = models.IntegerField(primary_key=True,)
    title = models.CharField(max_length=120, blank=True,)
    body = models.CharField(max_length=300, blank=True,)
    
    def __str__(self):
        return self.title