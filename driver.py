from configuration import get_redis_connection
import redis_inserter
import api_getter
import create_graphs

def main():
    api_requestor = api_getter.RetrieveApi()
    inserter = redis_inserter.RedisInserter()
    data_visualizer = create_graphs.DataVisualization()

    data = api_requestor.get_data_from_api()
    inserter.insert_new_data('car_data', data)
    data_visualizer.create_msrp_vs_combined_mpg_graph()


if __name__ == '__main__':
    main()