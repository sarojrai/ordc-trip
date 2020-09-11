from .models import Trip
from rest_framework import serializers


class TripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Trip
        fields = ["trip_ref_number", "trip_pickup_address", "trip_drop_address", "trip_via", "trip_created_by", "trip_delivered_by", "trip_created_at", "trip_updated_at", "trip_started_at", "trip_ended_at", "start_km", "end_km", "shipment", "shipment_handover_to", "number_of_items", "vehicle_category", "status", "total_weight", "total_delivery_value", "trip_charge", "trip_discount", "gst_charge", "gst_percentage","surchage", "gross_total_charge"]




