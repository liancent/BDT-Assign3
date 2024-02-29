import json
from configuration import get_redis_connection
from redis.commands.json.path import Path

def average_mileage():
    r = get_redis_connection()

    with open('car_output.json', 'r', encoding='utf-8') as car_data:
        data = json.load(car_data)
        counter = 0
        for entry in data['data']:
            r_json_data = {
                'make': entry['make_model_trim']['make_model']['make']['name'],
                'msrp': entry['make_model_trim']['msrp'],
                'year': entry['make_model_trim']['year'],
                'city mpg': entry['epa_city_mpg'],
                'hwy mpg': entry['epa_highway_mpg'],
                'combined mpg': entry['combined_mpg']
            }

            r.json().set('car_data:' + str(counter), '$', r_json_data)

            counter += 1

def retrieve_data():
    r = get_redis_connection()

    data = r.json().get("car_data:1")
    print(data)

average_mileage()
retrieve_data()