import requests
from configuration import load_config
from json_reader import JsonReader
import redis_inserter
import json

class RetrieveApi():
    """
    This class makes the request to a REST API
    """

    # Class Variables
    json_parser = JsonReader()
    r_inserter = redis_inserter.RedisInserter
    config = load_config()

    def __init__(self) -> None:
        """
        Class Constructor
        """

        pass

    def get_data_from_api(self):
        """
        This method makes a call to a REST API gets the response

        Returns:
            REST API response in the form of a JSON

        """
        url = "https://car-api2.p.rapidapi.com/api/mileages"

        querystring = {"direction":"asc","verbose":"yes","sort":"id", "page": "1"}

        headers = {
            "X-RapidAPI-Key": self.config["rapid-api-key"]["x-rapid-api-key"],
            "X-RapidAPI-Host": "car-api2.p.rapidapi.com",
            "content-type": "application/json"
        }

        response = requests.get(url, headers=headers, params=querystring)
    
        return response.json()
    