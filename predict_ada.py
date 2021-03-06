from datetime import datetime, timedelta
from math import floor
from backend import get_crypto_supply
from json_tools import *
from system_functions import clear_screen, bash_command

"""

-----This is a cheat-sheet for pushing updates!-----

Run this script each time you want to pull up
the variables in data.json, calculate the
average amount of new ADA minted per minute,
as well as give the approximate date and time
at which all 45 billion ADA will be minted,
assuming of course that they continue to be
minted at their current rate, as estimated
by this script.

"""


def get_time_between_datetimes(first_datetime, second_datetime):

    difference = second_datetime - first_datetime

    minutes = floor(difference.total_seconds() / 60)

    return minutes


def string_to_datetime_object(datetime_string):

    datetime_object_converted = datetime.strptime(datetime_string, '%m/%d/%y @ %H:%M:%S')

    return datetime_object_converted


def difference_between(a, b):
    c = a - b
    return c


if __name__ == '__main__':

    clear_screen()

    # Import data from json
    data = json_to_dict('data.json')

    # Ensure even number of data points
    if len(data) % 2 != 0:

        data.popitem()

    datetimes = list()
    supplies = list()
    differences_per_minute = list()

    # Append the new data to the datetimes and supplies arrays
    for time_date in data:

        datetime_object = string_to_datetime_object(time_date)
        datetimes.append(datetime_object)
        supplies.append(data[time_date])

    # For all indexes in the lists (of equal lengths), and calculate differences between indexes
    while datetimes:

        current_datetime = datetimes.pop()
        current_supply = supplies.pop()

        last_datetime = datetimes.pop()
        last_supply = supplies.pop()

        supply_difference = difference_between(current_supply, last_supply)
        minute_difference = get_time_between_datetimes(last_datetime, current_datetime)

        try:
            difference_per_minute = supply_difference / minute_difference

            differences_per_minute.append(difference_per_minute)
        except ZeroDivisionError:
            pass

        # Print the results
        print(f"Up {supply_difference} in {minute_difference} minutes.")
        print(f'(+{difference_per_minute} ADA per minute)\n')

    # Calculate the average amount of ADA minted each minute
    average_per_minute = sum(differences_per_minute) / len(differences_per_minute)

    # Total ADA supply is 45 billion
    total_ada = 45000000000

    # Retrieve the total number of ADA in circulation at this moment
    ada_supply = get_crypto_supply('ADA')

    # Calculate how many of the 45 billion ADA are yet to be minted
    ada_remaining = total_ada - ada_supply
    try:
        minutes_until_done = ada_remaining / average_per_minute
        hours_until_done = (minutes_until_done / 60).__round__(2)

        # Extend this average into the future and get the estimated datetime of completion
        current_time = datetime.now()
        completion_time_datetime = current_time + timedelta(hours=hours_until_done)
        completion_time = completion_time_datetime.strftime('%H%M on %m/%d/%Y')
    except ZeroDivisionError:
        pass

    # Print these results as well
    results_message = f"""Average ADA per minute created: {average_per_minute} ADA per minute.

At this rate, all ADA should be minted at around:\n{completion_time}."""

    print(results_message)

    # Log this estimation instance
    log_information = {datetime.now().strftime('%m/%d/%Y @ %H:%M:%S'): results_message}
    dict_to_json(log_information, 'estimations_log.json')
