# -*- coding: utf-8 -*-
__author__ = "Anil Kumar  Gupta"
__copyright__ = "Copyright (©) 2017. ORDC. All rights reserved."
__credits__ = ["ORDC"]

# Python module and packages
import json

# Django module and packages
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework import viewsets

# Project module and packages
from common.restapiviewwrapper import (
    Response, status, AllowAnyAPIView
)
from common.response import \
    ResponseEntity, ExceptionResponseEntity, ValidationErrorResponseEntity
from common.common_methods import convert_to_dict
from location.bll.location_bll import LocationManager
from common.logger import CustomLogger
LOGGER = CustomLogger.get_logger(__name__)

class Constant:
    """ defining constant"""
    IS_ERROR = True
    FAILED_STATUS = "FAILED"
    DEFUALT_MSG = "Something Went Wrong"
    POST = "POST"
    GET = "GET"


class LocationView(viewsets.ViewSet, AllowAnyAPIView):
    """ Location related operation """
    def __init__(self, **kwargs):
        super(LocationView, self).__init__(**kwargs)
        self.success_resp = ResponseEntity()
        self.exception_error_resp = ExceptionResponseEntity()
        self.validation_error_resp = ValidationErrorResponseEntity()
        self.errors = self.validation_error_resp.errors

    @action(
        detail=True,
        methods=[Constant.POST]
    )
    @csrf_exempt
    def create_area(self, request):
        """
        create Area and return result with status code
        """
        requested_data = json.loads(request.body)
        try:
            is_success, message, area_details = LocationManager().create_area(requested_data)
            if is_success:
                msg = message
                data = area_details
            else:
                msg = message
                data = {}
            self.success_resp.message = msg
            self.success_resp.data = data
            self.success_resp.is_error = not is_success  ## Toggle the success msg 
            return Response(
                status=status.HTTP_200_OK,
                data=convert_to_dict(
                    self.success_resp))
        except Exception as e:
            LOGGER.exception("Some internal server error occurred")
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data=convert_to_dict(self.exception_error_resp))

    @action(
        detail=True,
        methods=[Constant.POST]
    )
    @csrf_exempt
    def update_area_status(self, request):
        """
        update status of area as active or deactive
        """
        requested_data = json.loads(request.body)
        try:
            is_success, message, area_details = LocationManager().update_area_status(requested_data)
            if is_success:
                msg = message
                data = area_details
            else:
                msg = message
                data = {}
            self.success_resp.message = msg
            self.success_resp.data = data
            return Response(
                status=status.HTTP_200_OK,
                data=convert_to_dict(
                    self.success_resp))
        except Exception as e:
            LOGGER.exception("Some internal server error occurred")
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data=convert_to_dict(self.exception_error_resp))

    @action(
        detail=True,
        methods=[Constant.GET]
    )
    @csrf_exempt
    def get_area_details(self, request):
        """
        Get area details
        """
        requested_data = json.loads(request.body)
        try:
            is_success, message, area_details = LocationManager().get_area_details(requested_data)
            if is_success:
                msg = message
                data = area_details
            else:
                msg = message
                data = {}
            self.success_resp.message = msg
            self.success_resp.data = data
            return Response(
                status=status.HTTP_200_OK,
                data=convert_to_dict(
                    self.success_resp))
        except Exception as e:
            LOGGER.exception("Some internal server error occurred")
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data=convert_to_dict(self.exception_error_resp))

    @action(
        detail=True,
        methods=[Constant.POST]
    )
    @csrf_exempt
    def create_pincode(self, request):
        """
        create pincode and return result with status code
        """
        requested_data = json.loads(request.body)
        try:
            is_success, message, pincode_details = LocationManager().create_pincode(requested_data)
            if is_success:
                msg = message
                data = pincode_details
            else:
                msg = message
                data = {}
            self.success_resp.message = msg
            self.success_resp.data = data
            return Response(
                status=status.HTTP_200_OK,
                data=convert_to_dict(
                    self.success_resp))
        except Exception as e:
            LOGGER.exception("Some internal server error occurred")
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data=convert_to_dict(self.exception_error_resp))

    @action(
        detail=True,
        methods=[Constant.POST]
    )
    @csrf_exempt
    def update_pincode_status(self, request):
        """
        update status of pincode as active or deactive
        """

        requested_data = json.loads(request.body)
        try:
            is_success, message, pincode_details = LocationManager(
            ).update_pincode_status(requested_data)
            if is_success:
                msg = message
                data = pincode_details
            else:
                msg = message
                data = {}
            self.success_resp.message = msg
            self.success_resp.data = data
            return Response(
                status=status.HTTP_200_OK,
                data=convert_to_dict(
                    self.success_resp))
        except Exception as e:
            LOGGER.exception("Some internal server error occurred")
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data=convert_to_dict(self.exception_error_resp))

    @action(
        detail=True,
        methods=[Constant.GET]
    )
    @csrf_exempt
    def get_pincode_details(self, request):
        """
        Get pincode details
        """
        requested_data = json.loads(request.body)
        try:
            is_success, message, pincode_details = LocationManager(
            ).get_pincode_details(requested_data)
            if is_success:
                msg = message
                data = pincode_details
            else:
                msg = message
                data = {}
            self.success_resp.message = msg
            self.success_resp.data = data
            return Response(
                status=status.HTTP_200_OK,
                data=convert_to_dict(
                    self.success_resp))
        except Exception as e:
            LOGGER.exception("Some internal server error occurred")
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data=convert_to_dict(self.exception_error_resp))
