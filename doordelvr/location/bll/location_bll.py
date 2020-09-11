from location.models import Area, Pincode
from django.db.models import Q

class LocationManager:
    def get_trip(self, location_id):
        is_success = True
        location_detail = {"location_id": location_id}
        return is_success, location_detail

    def create_area(self,requested_data):
        """ validate and insert area into table """
        if Area.objects.filter(code=requested_data["code"].strip()).count():
            is_success = False
            message = 'Area Code "{0}" is already in use.'.format(requested_data["code"])
            area_detail = {"code":requested_data["code"]}
            return is_success, message, area_detail
        else:
            try:
                area = Area()
                area.code = requested_data["code"]
                area.name = requested_data["name"]
                area.pincode_id = requested_data["pincode_id"]
                area.latitude = requested_data["latitude"]
                area.longitude = requested_data["longitude"]
                area.is_serviceable = True
                area.save()
                is_success = True
                message = "Area has been created successfully"
                area_detail = requested_data
            except Exception as e:
                is_success = False
                message = "Area creation has been failed"
                area_detail = {"code":requested_data["code"]}
            return is_success, message, area_detail

    def update_area_status(self,requested_data):
        """ update area status as active or deactive"""
        if Area.objects.filter(code=requested_data["code"].strip()).count():
            if requested_data["action_type"]=="activate":
                is_active = 1
                message = 'You have successfully changed status as active'
            elif requested_data["action_type"]=="deactivate":
                is_active = 0
                message = 'You have successfully changed status as deactive'
            else:
                is_active = 'unknown'
            if  is_active != 'unknown':
                try:
                    Area.objects.filter(code=requested_data["code"]).update(is_active=is_active)
                    is_success = True
                    area_detail = {}
                except Exception as e:
                    is_success = False
                    message = str(e)
                    area_detail = {"code":requested_data["code"]}
            return is_success, message, area_detail
        else:
            is_success = False
            message = "No record found for given area code"
            area_detail = {"code":requested_data["code"]}
            return is_success, message, area_detail
 
    def get_area_details(self,requested_data):
        """ fetching area details"""
        q = Q()
        if requested_data.get("code"):
            q = q & Q(code=requested_data.get("code"))
        areas = Area.objects.filter(q)
        message =  'You Fetched Area Details Successfully'
        is_success = True
        area_detail = []
        for a in areas:
            pincode = ""
            if a.pincode:
                pincode = a.pincode.pincode
            data = {"code":a.code,
                "name":a.name,
                "is_serviceable":a.is_serviceable,
                "pincode":pincode,
                "latitude":a.latitude,
                "longitude":a.longitude,
                "is_active":a.is_active,
                "created_at":a.created_at,
                "updated_at":a.updated_at
                }

            area_detail.append(data)
        if area_detail:
            return is_success, message, area_detail
        else:
            is_success = False
            message = "No record found for given area code"
            area_detail = {"code":requested_data["code"]}
            return is_success, message, area_detail

    def create_pincode(self,requested_data):
        """ validate and insert pincode """
        if Pincode.objects.filter(pincode=requested_data["pincode"].strip()).count():
            is_success = False
            message = 'Pincode Code "{0}" is already in use.'.format(requested_data["pincode"])
            pincode_detail = {"pincode":requested_data["pincode"]}
            return is_success, message, pincode_detail
        else:
            try:
                pincode = Pincode()
                pincode.pincode = requested_data["pincode"]
                pincode.city = requested_data["city"]
                pincode.state = requested_data["state"]
                pincode.gst_state_code = requested_data["gst_state_code"]
                pincode.save()
                is_success = True
                message = "Pincode has been created successfully"
                pincode_detail = requested_data
            except Exception as e:
                is_success = False
                message = "Pincode creation has been failed"
                pincode_detail = {"pincode":requested_data["pincode"]}
            return is_success, message, pincode_detail

    def update_pincode_status(self,requested_data):
        """ update pincode status """
        if Pincode.objects.filter(pincode=requested_data["pincode"].strip()).count():
            if requested_data["action_type"]=="activate":
                is_active = 1
                message = 'You have successfully changed status as active'
            elif requested_data["action_type"]=="deactivate":
                is_active = 0
                message = 'You have successfully changed status as deactive'
            else:
                is_active = 'unknown'
            if  is_active != 'unknown':
                try:
                    Pincode.objects.filter(pincode=requested_data["pincode"]).update(is_active=is_active)
                    is_success = True
                    pincode_detail = {}
                except Exception as e:
                    is_success = False
                    message = str(e)
                    pincode_detail = {"pincode":requested_data["pincode"]}
            return is_success, message, pincode_detail
        else:
            is_success = False
            message = "No record found for given pincode code"
            pincode_detail = {"pincode":requested_data["pincode"]}
            return is_success, message, pincode_detail
 
    def get_pincode_details(self,requested_data):
        """ fetch pincode details """
        q = Q()
        if requested_data.get("pincode"):
            q = q & Q(pincode=requested_data.get("pincode"))
        pincodes = Pincode.objects.filter(q)
        message =  'You Fetched Pincode Details Successfully'
        is_success = True
        pincode_detail = []
        for p in pincodes:
            data = {"pincode":p.pincode, 
            "city":p.city,
            "state":p.state,
            "gst_state_code":p.gst_state_code,
            "is_active":p.is_active,
            "created_at":p.created_at,
            "updated_at":p.updated_at}
            pincode_detail.append(data)
        
        if pincode_detail:
            return is_success, message, pincode_detail
        else:
            is_success = False
            message = "No record found for given pincode code"
            pincode_detail = {"pincode":requested_data.get("pincode")}
            return is_success, message, pincode_detail
