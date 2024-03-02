from configuration import get_redis_connection
import redis_inserter
import json_reader
import api_getter

def main():
    api_requestor = api_getter.RetrieveApi()
    inserter = redis_inserter.RedisInserter()
    json_data_reader = json_reader.JsonReader()

    data = api_requestor.get_data_from_api()
    inserter.insert_new_data('car_data', data)

if __name__ == '__main__':
    main()