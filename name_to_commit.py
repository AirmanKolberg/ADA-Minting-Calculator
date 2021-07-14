from system_functions import clear_screen, bash_command, verify_yes_or_no, countdown
from json_tools import *
from time import sleep

"""
This file is to be used to add a new
key:value pair to the masterCommit.json
file.  This will be useful to connect
file names with file descriptions.
"""


def get_new_info():

    new_file_name = input('What is the new file name?\n')
    new_description = input('Write the description: ')

    return new_file_name, new_description


def confirmation_timer(new_file_name, new_description):

    clear_screen()

    print(f"""Please confirm, you have 5 seconds to Ctrl + C (just to keep you awake)\n
File Name:  {new_file_name}
Comment:  {new_description}""")
    
    try:

        countdown(5)

    except KeyboardInterrupt:

        # Try again
        new_file_name, new_description = get_new_info()
        confirmation_timer(new_file_name, new_description)


def add_key_value_pair():

    commit_dict = json_to_dict('masterCommit.json')

    new_file_name, new_description = get_new_info()

    confirmation_timer(new_file_name, new_description)

    # Add the confirmed file:description pair to the commit_dict
    commit_dict[new_file_name] = new_description

    # Remove and replace .json file
    bash_command('rm masterCommit.json')
    dict_to_json(commit_dict, 'masterCommit.json')

    # Ask to add another
    add_another = verify_yes_or_no(input('Add another?\n').lower())

    # If so, recursively go through the process again
    if add_another:
        
        add_key_value_pair()


def check_for_existing_key():

    commit_dict = json_to_dict('masterCommit.json')

    key_to_find = input("What is the name of the file for which you'd like to search?\n")

    if key_to_find in commit_dict:

        print(f'{key_to_find} exists, the description is:\n{commit_dict[key_to_find]}')

    else:

        add_key = verify_yes_or_no(input(f'{key_to_find} does not exist.  Would you like to add it?\n').lower())

        if add_key:

            add_key_value_pair()


def main_menu():

    menu_options = """
add     -     add a new key:value pair
check   -     check if key (file name) already exists
"""

    option = input(f"Please select an option below:\n{menu_options}").lower()

    if option == 'add':

        add_key_value_pair()

    elif option == 'check':

        check_for_existing_key()

    else:

        print('You cannot type, ergo you cannot use this app, goodbye.')
        sleep(2.5)
        clear_screen()


if __name__ == '__main__':

    main_menu()    
