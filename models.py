from django.db import models

# Create your models here.
class Vehicle(models.Model):
    model = models.CharField(max_length=60)
    full_name = models.CharField(max_length=200)
    plate_number = models.CharField(max_length=10)


class Position(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    lan = models.FloatField()
    lon = models.FloatField()