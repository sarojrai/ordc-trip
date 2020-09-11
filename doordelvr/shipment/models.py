from django.db import models

class Shipment(models.Model):
    description                 = models.CharField(max_length=512)
    dimension                   = models.CharField(max_length=128)
    weight                      = models.FloatField(default=0)
    value                       = models.FloatField(default=0)
    quantity                    = models.IntegerField(default=0)
    category                    = models.CharField(max_length=128) # controlled from front-end
    image_top                   = models.ImageField(upload_to="images/")
    image_bottom                = models.ImageField(upload_to="images/")
    image_left                  = models.ImageField(upload_to="images/")
    image_right                 = models.ImageField(upload_to="images/")
    additional_note             = models.CharField(max_length=128)
    added_on                    = models.DateTimeField(auto_now_add=True)