import Constants
import requests

url = 'https://beta3.api.climatiq.io/estimate'
region = 'US'
parameters = {
    "distance": 100,
    "distance_unit": "mi"
}


def passenger():
    activity_id = "passenger_vehicle-vehicle_type_car-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na"

    json_body = {
        "emission_factor": {
            "activity_id": activity_id,
            "region": region,
        },

        "parameters": parameters
    }

    authorization_headers = {"Authorization": f"Bearer: {Constants.Climate_IQ_Key}"}

    response = requests.post(url, json=json_body, headers=authorization_headers).json()

    # You can now do anything you want with the response
    print(response['co2e'], response['co2e_unit'])

passenger()