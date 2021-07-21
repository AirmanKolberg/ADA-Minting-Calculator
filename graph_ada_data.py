import matplotlib.pyplot as plt
import numpy as np
from json_tools import json_to_dict

"""
Run this script to graph all of the
data found within the data.json file.
"""


if __name__ == '__main__':

    # Retrieve ADA data
    ada_data = json_to_dict('data.json')

    # Declare lists for all x coordinates
    x = list()

    # Import all y variables to a list
    y = [ada_data[i] for i in ada_data]

    # Import all x variables
    
