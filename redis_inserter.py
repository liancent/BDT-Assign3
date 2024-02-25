from configuration import get_redis_connection
from redis.commands.json.path import Path
import json

class RedisInserter():
    def __init__(self) -> None:
        pass

    def insert_new_data(self):#, json_data):
        """
        This method reads the contents of a JSON file and inserts it into the Redis Database
        """
        r = get_redis_connection()

        # with open(json_data, "r", encoding="utf-8") as file:
        #     data = json.load(file)            
        #     r.json().set('car_data:1', Path.root_path(), data)

        data = {
            "car":"Mazda",
            "msrp":29500,
            "year":2022
        }

        r.json().set('car_data:3', '$', data)

def main():
    inserter = RedisInserter()
    # inserter.insert_new_data('car_output.json')
    inserter.insert_new_data()

if __name__ == '__main__':
    main()