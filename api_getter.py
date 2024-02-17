import requests
from configuration import load_config
from json_reader import JsonReader

class RetrieveApi():
    json_parser = JsonReader()
    config = load_config()

    def movie_api_getter(self):
        url = "https://movies-tv-shows-database.p.rapidapi.com/"

        querystring = {"year":"2020","page":"1"}

        headers = {
            "Type": "get-popular-movies",
            "X-RapidAPI-Key": self.config["rapid-api-key"]["x-rapid-api-key"],
            "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        self.json_parser.export_json_data(response, 'movie_output.json')

    def car_api_getter(self):
        url = "https://car-api2.p.rapidapi.com/api/mileages"

        querystring = {"direction":"asc","verbose":"yes","sort":"id"}

        headers = {
            "X-RapidAPI-Key": self.config["rapid-api-key"]["x-rapid-api-key"],
            "X-RapidAPI-Host": "car-api2.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        self.json_parser.export_json_data(response, 'car_output.json')


def main():
    retrieve_api = RetrieveApi()
    #retrieve_api.car_api_getter()
    retrieve_api.movie_api_getter()

if __name__ == '__main__':    
    main()