from configuration import get_redis_connection
import json

class RedisInserter():
    def __init__(self) -> None:
        pass

    def insert_new_data(json_data):
        """
        This method reads the contents of a JSON file and inserts it into the Redis Database
        """
        with open(json_data, "r", encoding="utf-8") as file:
            data = json.load(file)