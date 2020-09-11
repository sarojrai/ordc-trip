## Python module and packages
import json
import datetime
import time
from collections import defaultdict
import re

## Django module and packages
from rest_framework import viewsets
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action

## Project module and packages
from common.restapiviewwrapper import (
    Response, status, AuthenticatedAPIView, AllowAnyAPIView
)
from common.response import \
    ResponseEntity, ExceptionResponseEntity, ValidationErrorResponseEntity
from common.common_methods import convert_to_dict

from trip.bll.trip import TripManager

from common.logger import CustomLogger
logger = CustomLogger.get_logger(__name__)

class Constant:
    IS_ERROR = True
    FAILED_STATUS = "FAILED"
    DEFUALT_MSG = "Something Went Wrong"
    POST = "POST"
    GET = "GET"


class SampleView(viewsets.ViewSet, AllowAnyAPIView):
    
    def __init__(self, **kwargs):
        super(SampleView, self).__init__(**kwargs)
        self.success_resp = ResponseEntity()
        self.exception_error_resp = ExceptionResponseEntity()
        self.validation_error_resp = ValidationErrorResponseEntity()
        self.errors = self.validation_error_resp.errors
   
    #@class_based_api_request_response_log
    @action(
    detail = True,
    methods = [Constant.POST],
    #permission_classes = [IsAuthenticated],
    #authentication_classes = [JWTAuthentication]
    )
    def post(self, request, *args, **kwargs):
        try:
            ##Call Business Logic
            is_success, trip_details = TripManager().get_trip(trip_id=1)
            if is_success:
                msg = "Business Logic called Successfully"
                data = trip_details
            else:
                msg = "Business Logic called Failed"
                data = {}
            self.success_resp.message = msg
            self.success_resp.data = data
            return Response(status = status.HTTP_200_OK, data = convert_to_dict(self.success_resp))
        except Exception as e:
            logger.exception("Some internal server error occurred")
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR,
                data = convert_to_dict(self.exception_error_resp))


class TripView(viewsets.ViewSet, AllowAnyAPIView):

    def __init__(self, **kwargs):
        super(TripView, self).__init__(**kwargs)
        self.success_resp = ResponseEntity()
        self.exception_error_resp = ExceptionResponseEntity()
        self.validation_error_resp = ValidationErrorResponseEntity()
        self.errors = self.validation_error_resp.errors

    #@class_based_api_request_response_log
    @action( 
    detail = True,
    methods = [Constant.GET],
    #permission_classes = [IsAuthenticated],
    #authentication_classes = [JWTAuthentication]
    )
    def get_trip(self, request, *args, **kwargs):
        pass
    

    @action(
    detail = True,
    methods = [Constant.POST],
    #permission_classes = [IsAuthenticated],
    #authentication_classes = [JWTAuthentication]
    )
    def create_trip(self, request, *args, **kwargs):
        try:
            # Call Business Logic
            req_data = json.loads(request.body)
            print("reqdata: ", req_data)

            ## input validation here [pincode, mobile, etc]
            #FormFieldValidation.is_valid_pincode(re.sub('[^0-9]', '', req_data["trip_pickup_address"]["pincode"]))

            ## creating trip object
            trip_id, trip_ref_number, pickup_address_id, drop_address_id = \
                    TripManager().create_trip(req_data)
            
            #################################################
            ### Third Party Service Integration comes here
            ### Push Notification, Delivery people search etc
            #################################################
            
            ## response preparation
            trip_response = {}
            trip_response["trip_id"] = trip_id
            trip_response["trip_ref_number"] = trip_ref_number
            trip_response["pickup_address_id"] = pickup_address_id
            trip_response["drop_address_id"] = drop_address_id
            trip_response["trip_status"] = "CREATED"

            msg = "Trip Created Successfully"
            data = trip_response

            self.success_resp.message = msg
            self.success_resp.data = data
            return Response(status = status.HTTP_200_OK, data = convert_to_dict(self.success_resp))
        except Exception as e:
            logger.exception("Some internal server error occurred")
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR,
                data = convert_to_dict(self.exception_error_resp))
   
    @action( 
    detail = True,
    methods = [Constant.POST],
    #permission_classes = [IsAuthenticated],
    #authentication_classes = [JWTAuthentication]
    )
    def broadcast_trip(self, request, *args, **kwargs):
        try:
            # Call Business Logic
            req_data = json.loads(request.body)
            print("reqdata: ", req_data)

            data = {}
            trip = TripManager().get_trip(req_data["trip_id"])
            #trip.status = 7
            #trip.save()

            action_type = req_data["action_type"]
            if action_type == "broadcast":
                data = json.loads(trip.trip_json_request)
                data["trip_id"] = req_data["trip_id"]

            msg = "Trip Broadcasted Successfully !"
            self.success_resp.message = msg
            self.success_resp.data = data
            return Response(status = status.HTTP_200_OK, data = convert_to_dict(self.success_resp))
        except Exception as e:
            logger.exception("Some internal server error occurred")
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR,
                data = convert_to_dict(self.exception_error_resp))

    @action(
    detail = True,
    methods = [Constant.POST],
    #permission_classes = [IsAuthenticated],
    #authentication_classes = [JWTAuthentication]
    )
    def update_trip_acceptance_info(self, request, *args, **kwargs):
        try:
            req_data = json.loads(request.body)
            msg = "Trip Updated Successfully"
            data = {}
           
            # updating information
            TripManager().update_trip_acceptance(req_data)

            self.success_resp.message = msg
            self.success_resp.data = data
            return Response(status = status.HTTP_200_OK, data = convert_to_dict(self.success_resp))
        except Exception as e:
            logger.exception("Some internal server error occurred")
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR,
                data = convert_to_dict(self.exception_error_resp))


    @action(
    detail = True,
    methods = [Constant.POST],
    #permission_classes = [IsAuthenticated],
    #authentication_classes = [JWTAuthentication]
    )
    def update_trip_inprogress_info(self, request, *args, **kwargs):
        try:
            req_data = json.loads(request.body)
            print(req_data)
            msg = "Trip Updated Successfully"
            data = {}

            self.success_resp.message = msg
            self.success_resp.data = data
            return Response(status = status.HTTP_200_OK, data = convert_to_dict(self.success_resp))
        except Exception as e:
            logger.exception("Some internal server error occurred")
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR,
                data = convert_to_dict(self.exception_error_resp))

