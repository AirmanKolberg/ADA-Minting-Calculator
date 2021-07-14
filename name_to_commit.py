from system_functions import clear_screen, bash_command
from json_tools import *
from data_updater import countdown

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
    add_another = input('Add another?  (Leave blank if no, type anything if yes)\n')

    # If so, recursively go through the process again
    if add_another:
        add_key_value_pair()


if __name__ == '__main__':

    add_key_value_pair()    
