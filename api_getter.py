import requests
from configuration import load_config
from json_reader import JsonReader

class RetrieveApi():
    json_parser = JsonReader()
    config = load_config()

    def car_mileage_api_getter(self):
        url = "https://car-api2.p.rapidapi.com/api/mileages"

        querystring = {"direction":"asc","verbose":"yes","sort":"id", "page": "3"}

        headers = {
            "X-RapidAPI-Key": self.config["rapid-api-key"]["x-rapid-api-key"],
            "X-RapidAPI-Host": "car-api2.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        self.json_parser.export_json_data(response, 'car_output3.json')
        