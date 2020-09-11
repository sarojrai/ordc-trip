from .models import Pincode, Address, Area
from rest_framework import serializers


class PincodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pincode
        fields = '__all__' #["pincode", "city", "state", "gst_state_code", "is_active"]

class AreaSerializer(serializers.ModelSerializer):
    pincode  = PincodeSerializer()
    class Meta:
        model = Area
        fields = ["code", "name", "is_serviceable"]

