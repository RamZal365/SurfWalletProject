from django.contrib.auth.models import User
from django.db import models


class SurfBoard(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    # Measured in feet (ft)
    length = models.FloatField()

    # Measured in inches (in)
    width = models.FloatField()
    thickness = models.FloatField()

    # Measured in liters (L)
    volume = models.FloatField()


class WetSuit(models.Model):
    brand = models.CharField(max_length=100)

    # Measured in feet (ft)
    height = models.FloatField()

    # Measured in kilograms (kg)
    weight = models.FloatField()

    # Measured in inches (in)
    chest = models.FloatField()
    waist = models.FloatField()

    # Measured in millimeters (mm)
    chest_thickness = models.FloatField()
    extremities_thickness = models.FloatField()


class Spot(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    long_description = models.TextField()

    # Info of the location of the spot
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
