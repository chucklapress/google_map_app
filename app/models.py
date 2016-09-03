from django.db import models
from geoposition.fields import GeopositionField


# Create your models here.


class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()
    def __str__(self):
        return self.name

class PeopleWeKnow(models.Model):
    name = models.CharField(max_length=40)
    position = GeopositionField()
    def __str__(self):
        return self.name
