from configuration import get_redis_connection
import matplotlib.pyplot as plt
import numpy as np

class DataVisualization():
    """
    This class is used for creating graphs of the data that was collected
    """

    # Class Variables
    redis = get_redis_connection()

    def __init__(self) -> None:
        """
        Class Constructor
        """
        pass

    def create_msrp_vs_combined_mpg_graph(self):
        """
        Create a matplotlib graph with X = msrp and Y = combined mpg

        Params:
            None

        Returns: 
            Image of scatterplot graph
        """
        msrp = []
        combined_mpg = []

        iter = 0
        redis_data = self.redis.json().get("car_data:" + str(iter))
        
        while redis_data:
            msrp.append(redis_data["msrp"])
            combined_mpg.append(redis_data["combined_mpg"])
            iter += 1
            redis_data = self.redis.json().get("car_data:" + str(iter))

        plt.xlabel("MSRP")
        plt.ylabel("Combined MPG")
        plt.title("Comparison between MSRP and Combined MPG")
        plt.scatter(msrp, combined_mpg)
        plt.show()