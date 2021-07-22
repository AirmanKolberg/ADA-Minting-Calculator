import matplotlib.pyplot as plt
import numpy as np
from json_tools import json_to_dict
import datetime
from math import floor

"""
Run this script to graph all of the
data found within the data.json file.
"""


def get_difference_between_datetimes(latter_time, former_time):

    delta = latter_time - former_time
    minutes_difference = floor(delta.seconds / 60)

    return minutes_difference


def determine_x_values(x_data):

    # Declare list of x values to return
    x_values = [0]

    while x_data:

        # Identify the first x value as 0
        origin = x_data.pop(0)

        # Add the next value to the list
        try:
            next_val = get_difference_between_datetimes(x_data[0], origin)
            x_values.append(x_values[-1] + next_val)

        except IndexError:
            break

    return x_values


def clean_data(x_data):

    x_cleaned = list()

    for i in x_data:
        
        x_val = datetime.datetime.strptime(i, '%m/%d/%y @ %H:%M:%S')
        x_cleaned.append(x_val)

    return x_cleaned


def plot_data(x, y):

    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':

    # Retrieve ADA data
    ada_data = json_to_dict('data.json')

    # Import all y variables to a list
    y = [ada_data[i] for i in ada_data]

    # Import data components to determine x values
    x = [i for i in ada_data]
    x = clean_data(x)
    x = determine_x_values(x)
    
    plot_data(x, y)
