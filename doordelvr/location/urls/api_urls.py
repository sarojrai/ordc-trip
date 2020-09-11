from django.urls import include, path
from django.conf.urls import url
from location.views import api_views as api

urlpatterns = [
        path('create-area/', api.LocationView.as_view({"post":"create_area"}), name="create_area"),
        path('update-area-status/', api.LocationView.as_view({"post":"update_area_status"}), name="update_area_status"),
        path('areas/', api.LocationView.as_view({"get":"get_area_details"}), name="get_area_details"),
        path('create-pincode/', api.LocationView.as_view({"post":"create_pincode"}), name="create_pincode"),
        path('update-pincode-status/', api.LocationView.as_view({"post":"update_pincode_status"}), name="update_pincode_status"),
        path('pincodes/', api.LocationView.as_view({"get":"get_pincode_details"}), name="get_pincode_details"),
]



