# APIs Detail
## 1. Create pincode for location
* Endpoint : https://{{HOST}}/api/locations/create-pincode/
* Method: POST
* Request:
    * [Sample response](/doordelvr/location/tests/sample_input/pincode_create.json)
* Field Request
    * pincode : Required
    * city : Required
    * state : Required
    * gst_state_code : Required
    
* Response:
    * [Sample response](/doordelvr/location/tests/sample_output/pincode_create.json)
    

## 2. Update pincode status
* Endpoint : https://{{HOST}}/api/locations/update-pincode-status
* Method: POST
* Request:
    * [Sample response](/doordelvr/location/tests/sample_input/pincode_activate.json)
    * [Sample response](/doordelvr/location/tests/sample_input/pincode_deactivate.json)
* Field Request
    * pincode : Required
    * action_type : Required
    
* Response:
    * [Sample response](/doordelvr/location/tests/sample_output/pincode_activate.json)
    * [Sample response](/doordelvr/location/tests/sample_output/pincode_deactivate.json)

## 3. Fetch Pincode details
* Endpoints : https://{{HOST}}/api/locations/get-pincode-details
* Method: POST
* Request:
    * [Sample request](/doordelvr/location/tests/sample_input/pincode_get_details.json)
* Field Request
    * pincode : Required
    
* Response:
    * [Sample response](/doordelvr/location/tests/sample_output/pincode_get_details.json)
    
## 1. Create pincode for location
* Endpoint : https://{{HOST}}/api/locations/create-pincode/
* Method: POST
* Request:
    * [Sample response](/doordelvr/location/tests/sample_input/pincode_create.json)
* Field Request
    * pincode : Required
    * city : Required
    * state : Required
    * gst_state_code : Required
    
* Response:
    * [Sample response](/doordelvr/location/tests/sample_output/pincode_create.json)
    

## 2. Update pincode status
* Endpoint : https://{{HOST}}/api/locations/update-pincode-status
* Method: POST
* Request:
    * [Sample response](/doordelvr/location/tests/sample_input/pincode_activate.json)
    * [Sample response](/doordelvr/location/tests/sample_input/pincode_deactivate.json)
* Field Request
    * pincode : Required
    * action_type : Required
    
* Response:
    * [Sample response](/doordelvr/location/tests/sample_output/pincode_activate.json)
    * [Sample response](/doordelvr/location/tests/sample_output/pincode_deactivate.json)

## 3. Fetch Pincode details
* Endpoints : https://{{HOST}}/api/locations/get-pincode-details
* Method: POST
* Request:
    * [Sample request](/doordelvr/location/tests/sample_input/pincode_get_details.json)
* Field Request
    * pincode : Required
    
* Response:
    * [Sample response](/doordelvr/location/tests/sample_output/pincode_get_details.json)
  

## 4. Create area for location
* Endpoint : https://{{HOST}}/api/locations/create-area/
* Method: POST
* Request:
    * [Sample response](/doordelvr/location/tests/sample_input/area_create.json)
* Field Request
    * code : Required
    * name : Required
    * picode_id : Required (refer form pincode)
    * latitude : Required
    * longitude : Required
    
}
* Response:
    * [Sample response](/doordelvr/location/tests/sample_output/area_create.json)
    

## 5. Update area status
* Endpoint : https://{{HOST}}/api/locations/update-area-status
* Method: POST
* Request:
    * [Sample response](/doordelvr/location/tests/sample_input/area_activate.json)
    * [Sample response](/doordelvr/location/tests/sample_input/area_deactivate.json)
* Field Request
    * code : Required
    * action_type : Required
    
* Response:
    * [Sample response](/doordelvr/location/tests/sample_output/area_activate.json)
    * [Sample response](/doordelvr/location/tests/sample_output/area_deactivate.json)

## 6. Fetch area details
* Endpoints : https://{{HOST}}/api/locations/get-area-details
* Method: POST
* Request:
    * [Sample request](/doordelvr/location/tests/sample_input/area_get_details.json)
* Field Request
    * code : Required
    
* Response:
    * [Sample response](/doordelvr/location/tests/sample_output/area_get_details.json)

