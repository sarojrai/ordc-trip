from django.db import models
from common.models import CommonModel

class Pincode(CommonModel):
    pincode                     = models.CharField(max_length=32, unique=True, db_index=True)
    city                        = models.CharField(max_length=64)
    state                       = models.CharField(max_length=64)
    gst_state_code              = models.CharField(max_length=64)

    def __str__(self):
        return self.pincode

class Area(CommonModel):
    code                        = models.CharField(max_length=64, unique=True, db_index=True)
    name                        = models.CharField(max_length=256) #kind of landmark
    pincode                     = models.ForeignKey(Pincode, models.SET_NULL, blank=True, null=True)
    latitude                    = models.FloatField(default=None)
    longitude                   = models.FloatField(default=None)
    is_serviceable              = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Address(CommonModel):
    address                     = models.CharField(max_length=2048)
    area                        = models.CharField(max_length=256)
    city                        = models.CharField(max_length=64)
    state                       = models.CharField(max_length=64)
    country                     = models.CharField(max_length=64)
    pincode                     = models.ForeignKey(Pincode, models.SET_NULL, blank=True, null=True)
    latitude                    = models.FloatField(default=None)
    longitude                   = models.FloatField(default=None)
    def __str__(self):
        return self.address[:20]

