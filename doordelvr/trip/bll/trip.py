# pytho module here
import time
import os
import json
import datetime

# django module here


# db models here
from ..models import Trip, TRIP_STATUS
from location.models import Pincode, Address, Area
from transport.models import VehicleCategory
from shipment.models import Shipment
from common.validate import FormFieldValidation

# variables initialization
trip_status_mapping = {}
for k, v in dict(TRIP_STATUS).items():
    trip_status_mapping.update({v: k})


# code

class TripManager:
    def __init__(self):
        #self.trip_status_mapping = trip_status_mapping
        pass

    def get_trip(self, trip_id):
        """
        
        checking trip record
        in database
        :param trip_id:
        :return trip_object:
        """
        try:
            trip = Trip.objects.get(id=trip_id)
            return trip
        except:
            return None
    
    def trip_action(self, action_type, trip_id):
        """
        trip_id : status change basis action_type

        """
        trip_info = {}
        trip_info["trip_details"] = self.get_trip(trip_id)
        trip_info["users"] = self.get_trip_users(pickup_area_id, drop_area_id, product_category_id, **kwargs)
        return trip_info

    def get_trip_users(self, pickup_area_id, drop_area_id, product_category_id, **kwargs):
        """
        return 
        """
        users = []
        return users

    def save_address(self, addrinfo):
        """
        save address
        :param addrinfo (dict)
        :return id
        """
        addrinfo["pincode"] = Pincode.objects.filter(pincode=addrinfo["pincode"])[0]
        addr = Address.objects.get_or_create(id=addrinfo["id"], defaults=addrinfo)
        return addr[0].id

    def save_shipments(self, shipmentinfo):
        """
        shipment(s) creation in db
        :param shipmentinfo (list of dict(s)):
        :return shipment objects:
        """
        shipments = []
        for shipment in shipmentinfo:
            ship = Shipment.objects.get_or_create(id=shipment["id"], defaults=shipment)
            shipments.append(ship[0])
        return shipments

    def save_vehicle(self, vehicle_category):
        """

        :param vehicleinfo:
        :return vehicle object:
        """
        vc = VehicleCategory.objects.get_or_create(vehicle_type=vehicle_category)
        return vc[0]

    def create_trip(self, req_data):
        """

        creating trip here
        with required attributes
        :param:
        :param:
        :return trip object:
        """
        actual_req_data = json.dumps(req_data)
        # creating dependent objects
        pickup_address_id = self.save_address(req_data["trip_pickup_address"])
        drop_address_id   = self.save_address(req_data["trip_drop_address"])
        vehicle_category  = self.save_vehicle(req_data["vehicle_category"])
        shipments         = self.save_shipments(req_data["shipments"])
        
        ## creating trip
        trip_ref_number = str(time.time()).replace(".","")

        trip_object = Trip.objects.create(
                        trip_ref_number = trip_ref_number, \
                        trip_pickup_address_id = pickup_address_id, \
                        trip_drop_address_id = drop_address_id, \
                        trip_created_by = req_data["trip_created_by"]["user_id"], \
                        number_of_items = req_data["number_of_items"], \
                        vehicle_category = vehicle_category, \
                        total_weight = req_data["total_weight"], \
                        total_delivery_value = req_data["total_delivery_value"], \
                        trip_json_request = actual_req_data
                    )

        # adding shipments to trip object
        trip_object.shipment.set(shipments)
        
        return trip_object.id, trip_ref_number, pickup_address_id, drop_address_id 

