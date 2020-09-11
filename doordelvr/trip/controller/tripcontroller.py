import os
import json
import datetime

from django.http import Http404
from http import HTTPStatus
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from ..models import Trip

from .trip_create_main import trip_create 

@csrf_exempt
def get_trip(request):
    """
    Get Trip By
    TripId
    """
    tripid = request.GET.get('tripid', None)
    httpstatus = 200
    data = {"status_code":httpstatus, "message":"trip found !", "tripid":tripid}
    try:
        trip = Trip.objects.get(id=tripid)
        data["trip_info"] = {}
    except Trip.DoesNotExist:
        httpstatus = 404
        data["status_code"] = 404
        data["message"] = "Trip Does Not Exist"

    return HttpResponse(json.dumps(data), status=httpstatus, content_type='application/json')


@csrf_exempt
def create_trip(request):
    """
    Create Trip With
    Requisite Request

    Parse Request & Validate
    The Request So that It 
    doesn't throw any exception/error
    while execution
    """
    httpstatus = 201
    data = {"status_code":httpstatus}

    if request.method == "POST":
        # validating inputs
        reqdata=json.loads(request.body)
        data["response"]=trip_create(reqdata)
        if data["response"]["status"] == "FAILED":
            httpstatus = 204
            data["status_code"] = httpstatus
    else:
        httpstatus = 405
        data["status_code"] = 405
        data["message"] = "method not allowed!"

    return HttpResponse(json.dumps(data), status=httpstatus, content_type='application/json') 

@csrf_exempt
def update_trip(request):
    """
    Update Trip With
    Requisite Details

    Parse Request & Validate
    The Request So that It 
    doesn't throw any exception/error
    while execution
    """
    httpstatus=200
    data={"status":200, "message":"Update Trip In Progress"}
    return HttpResponse(json.dumps(data), status=httpstatus, content_type='application/json')


