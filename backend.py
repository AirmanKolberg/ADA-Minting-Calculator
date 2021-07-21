import cryptocompare
from datetime import datetime
from system_functions import clear_screen, bash_command, countdown
from pprint import pprint
from json_tools import *
from commit_and_push_all import add_and_commit_file

"""
Run this script like as a server, just running
in the background simply collecting data and
constantly displaying to you the results in the
Terminal emulator window.  I've also set this
application to share the updated results with
you guys in the GitHub community.
"""


def get_datetime():

    return datetime.now().strftime('%m/%d/%y @ %H:%M:%S')


def get_crypto_supply(coin):

    total_supply = cryptocompare.get_price(coin=coin,
                                           currency='USD',
                                           full=True)['RAW'][coin]['USD']['SUPPLY']

    return total_supply


def main_loop():

    # Retrieve the master_pairs variable
    master_pairs = json_to_dict('data.json')

    date_and_time = get_datetime()
    ada_supply = get_crypto_supply('ADA')

    # Add the date_and_time and supply to the master dictionary
    master_pairs[date_and_time] = ada_supply

    clear_screen()

    pprint(master_pairs)

    # Save new data to .json file
    bash_command('rm data.json')
    dict_to_json(master_pairs, 'data.json')

    # Share results with GitHub community every hour
    add_and_commit_file(['data.json'])

        


if __name__ == '__main__':

    try:

        while True:
            main_loop()

            # Check again in 20 minutes
            countdown(20 * 60)

    except KeyboardInterrupt:

        print('\nClosing...')

    # In case of any error, log it, print it, and retry in a minute
    except Exception as error:
        
        # Gather error details
        error_time = datetime.now()
        error_message = f'ERROR: {error}'

        # Retrieve the errors log
        error_dict = json_to_dict('errors.json')

        # Add the new error to the log
        error_dict[error_time] = error_message
        bash_command('rm errors.json')
        dict_to_json(error_dict, 'errors.json')

        print(f'{error_message}\nRetrying in one minute...')

        countdown(60)
        main_loop()
