import cryptocompare
from datetime import datetime
from time import sleep
from os import system
from pprint import pprint
from json_tools import *


def clear_screen():
    
    _ = system('clear')


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
    
    while True:

        date_and_time = get_datetime()
        ada_supply = get_crypto_supply('ADA')

        # Add the date_and_time and supply to the master dictionary
        master_pairs[date_and_time] = ada_supply

        clear_screen()
        pprint(master_pairs)

        dict_to_json(master_pairs, 'data.json')

        # Check again in 20 minutes
        sleep(20 * 60)


if __name__ == '__main__':

    try:

        main_loop()

    except KeyboardInterrupt:

        print('\nClosing...')

    # In case of any error, log it on the screen and retry in a minute
    except Exception as error:
        
        error_message = f"""ERROR: {error}
Retrying in one minute..."""

        print(error_message)

        sleep(60)
        main_loop()
