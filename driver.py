from configuration import get_redis_connection
import redis_inserter
import json_reader

def main():
    inserter = redis_inserter.RedisInserter()
    json_data_reader = json_reader.JsonReader()

if __name__ == '__main__':
    main()