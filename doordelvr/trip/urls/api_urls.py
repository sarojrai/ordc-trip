from django.urls import include, path
from django.conf.urls import url
from trip.views import api_views as api
from trip.views import web_views as we

urlpatterns = [
        url(r'^sample/', api.SampleView.as_view({"post":"post"}), name="sample_view"),
        url(r'^create_trip/', api.TripView.as_view({"post":"create_trip"}), name="create_trip"),
        url(r'^broadcast_trip/', api.TripView.as_view({"post":"broadcast_trip"}), name="broadcast_trip"),

        #""" As per last discussion - 30Sept2020 11:28 PM """
        ## BroadCast
        ## Trip Request For Request To Deliver  # trip_id, requestor_info={user_id:1, vehicle=""} action_type=request_to_deliver 
        ## Trip Creator -- Grant/Allow Trip # trip_id, requestor_info={user_id:1, vehicle=""} ## True/False
        #-----Clean Queue of all the broadcasted users. trip_id, action=clean_queue
        ## Cancel Trip # trip_id, action=cancel_trip, 
        #-----Clean Queue if Creator Only
        #-----Resume Broadcast Trip if Cancelled by Delivery Boy
        
        ##
        #url(r'^update_trip/trip_accepted_info/', api.TripView.as_view({"post":"update_trip_acceptance_info"}), name="update_trip_acceptance_info"),
        #url(r'^update_trip/trip_completed_info/', api.TripView.as_view({"post":"update_trip"}), name="update_trip"),
        #url(r'^update_trip/trip_inprogress_info/', api.TripView.as_view({"post":"update_trip"}), name="update_trip"),
        #url(r'^update_trip/trip_fare_info/', api.TripView.as_view({"post":"update_trip"}), name="update_trip"),
        #url(r'^update_trip/trip_payment_info/', api.TripView.as_view({"post":"update_trip"}), name="update_trip"),

]



