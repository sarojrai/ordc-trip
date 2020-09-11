from django.db import models


class VehicleCategory(models.Model):
    vehicle_type            = models.CharField(max_length=64)
    description             = models.CharField(max_length=128)

