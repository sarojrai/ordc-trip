from django.db import models


TRIP_STATUS = (
        (0, "CANCELED"),
        (1, "CREATED"),
        (2, "STARTED"),
        (3, "COMPLETED"),
        (4, "INPROGRESS"),
        (5, "ACCEPTED"),
        (6, "REJECTED"),
        (7, "BROADCASTED")
        )

PAYMENT_TYPE = (
        (0, "CASH"),
        (1, "PREPAID")
    )

class Trip(models.Model):
    trip_ref_number             = models.CharField(max_length=128, db_index=True)
    trip_pickup_address         = models.ForeignKey('location.Address', models.SET_NULL, blank=True, null=True, related_name='trip_pickup_address')
    trip_drop_address	        = models.ForeignKey('location.Address', models.SET_NULL, blank=True, null=True, related_name='trip_drop_address')
    trip_via                    = models.ManyToManyField("location.Area", default=True)
    trip_created_by             = models.IntegerField(db_index=True, null=False)
    trip_delivered_by           = models.IntegerField(db_index=True, null=True)
    trip_created_at             = models.DateTimeField(auto_now_add=True, db_index=True)
    trip_updated_at             = models.DateTimeField(auto_now=True, db_index=True)
    trip_accepted_at            = models.DateTimeField(null=True, blank=True, db_index=True)
    trip_started_at	        = models.DateTimeField(null=True, blank=True, db_index=True)
    trip_ended_at	        = models.DateTimeField(null=True, blank=True, db_index=True)
    trip_json_request           = models.TextField(null=True, blank=True)
    start_km                    = models.FloatField(default=0)
    end_km                      = models.FloatField(default=0)
    shipment                    = models.ManyToManyField("shipment.Shipment")
    shipment_handover_to        = models.CharField(max_length=128)
    number_of_items	        = models.IntegerField(default=0)
    vehicle_category            = models.ForeignKey('transport.VehicleCategory', models.SET_NULL, blank=True, null=True)
    status	                = models.IntegerField(choices=TRIP_STATUS, default=1)
    total_weight                = models.FloatField(default=0)
    total_delivery_value        = models.FloatField(default=0)
    trip_charge	                = models.FloatField(default=0)
    trip_discount	        = models.FloatField(default=0)
    gst_type    	        = models.CharField(max_length=50, default="OTHER") ## manufacture, other, service
    gst_percentage	        = models.FloatField(default=0)
    cgst	                = models.FloatField(default=0)
    sgst	                = models.FloatField(default=0)
    igst	                = models.FloatField(default=0)
    gst_charge	                = models.FloatField(default=0)
    flat_surchage	        = models.FloatField(default=0)
    surchage_percentage	        = models.FloatField(default=0)
    percentage_surchage	        = models.FloatField(default=0)
    gross_total_charge	        = models.FloatField(default=0)
    notification_status	        = models.BooleanField(default=False)
    #os_platform_deails

    def distance_travelled(self):
        dis = self.end_km-self.start_km
        return dis
    
    def update_gross_total_charge(self):
        ## TODO 
        return 


