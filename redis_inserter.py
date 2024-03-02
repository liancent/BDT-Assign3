from configuration import get_redis_connection
from redis.commands.json.path import Path
import json

class RedisInserter():
    """
    This class is used to insert data into Redis
    """
    redis = get_redis_connection()

    def __init__(self) -> None:
        pass

    def insert_new_data(self, key, data):
        """
        This method reads the contents of a JSON file and inserts it into the Redis Database

        Params:
            key: The key that the data is to be stored under
            data: The data to be inserted into the Redis Database
        """
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

            self.redis.json().set(key + ':' + str(counter), '.', r_json_data)
            counter += 1
