from configuration import get_redis_connection
from redis.commands.json.path import Path
import json

class RedisInserter():
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

        self.redis.json().set(key, '.', json.dumps(data))
