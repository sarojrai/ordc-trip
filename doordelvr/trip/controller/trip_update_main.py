import os
import json
import datetime
import time
from django.views.decorators.csrf import csrf_exempt

from ..models import Trip
from location.models import Pincode, Address, Area
from transport.models import VehicleCategory
from shipment.models import Shipment

def get_address_obj(address_info):
    """
    Returns the address
    object created

    checking if address exists
    """
    pincode_isexists = Pincode.objects.filter(is_active=True, pincode=address_info["pincode"])
    if pincode_isexists:
        address_info["pincode"]=pincode_isexists[0]
        address_obj = Address.objects.create(**address_info)
        return address_obj
    else:
        return None

def check_address_exists(reqdata):
    """
    Check if address already
    exists in database

    Return id if true
    """
    pickup_address = None
    drop_address = None

    if "meta_info" in reqdata:
        if "pickup_address_already_exist" in reqdata["meta_info"]:
            if reqdata["meta_info"]["pickup_address_already_exist"].lower() == "true":
                pickup_address_id = reqdata["meta_info"]["pickup_address_id"]
                pickup_address = Address.objects.get(id=int(pickup_address_id))
                
        if "drop_address_already_exist" in reqdata["meta_info"]:
            if reqdata["meta_info"]["drop_address_already_exist"].lower() == "true":
                drop_address_id = reqdata["meta_info"]["drop_address_id"]
                drop_address = Address.objects.get(id=int(drop_address_id))
    
    return pickup_address, drop_address


def trip_update(reqdata):
    """
    parse the request
    packet & create trip
    """
    error_message=""
    trip_response = {"status":"SUCCESS", "message":"trip created successfully!", "trip_status":"CREATED"}

    ## preparing pickup & drop address
    pickup_address, drop_address = check_address_exists(reqdata)
    if pickup_address is None: pickup_address = get_address_obj(reqdata["trip_pickup_address"])
    if drop_address is None: drop_address = get_address_obj(reqdata["trip_drop_address"])

    pincode_service_check = False
    if pickup_address is None:
        pincode_service_check = True
        error_message = "pickup pincode not in service - "+str(reqdata["trip_pickup_address"]["pincode"]+",")
    if drop_address is None:
        pincode_service_check = True
        error_message = "drop pincode not in service - "+str(reqdata["trip_drop_address"]["pincode"]+" ")

    if pincode_service_check:
        trip_response["status"] = "FAILED"
        trip_response["message"] = error_message
        trip_response["trip_status"] = "NOT-CREATED"
        trip_response["error_code"] = "E01"

        return trip_response

    ## vehicle category
    vehicleCategory = VehicleCategory.objects.get_or_create(vehicle_type=reqdata["vehicle_category"])

    ## creating trip
    trip_ref_num = str(time.time()).replace(".","")
    trip_obj = Trip.objects.create(trip_ref_number=trip_ref_num, \
                trip_pickup_address=pickup_address, trip_drop_address=drop_address,\
                trip_created_by=reqdata["trip_created_by"]["user_id"], number_of_items=reqdata["number_of_items"], \
                vehicle_category=vehicleCategory[0], total_weight=reqdata["total_weight"], \
                total_delivery_value=reqdata["total_delivery_value"])
    
    ## adding shipments in created trip
    shipment_objs = []
    for ship in reqdata["shipment"]:
        sh = Shipment.objects.create(**ship)
        shipment_objs.append(sh)
    trip_obj.shipment.set(shipment_objs)

    ## response preparation
    trip_response["trip_id"] = trip_obj.id
    trip_response["trip_ref_number"] = trip_ref_num
    trip_response["pickup_address_id"] = pickup_address.id
    trip_response["drop_address_id"] = drop_address.id

    return trip_response

