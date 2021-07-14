from system_functions import bash_command
from time import sleep
from json_tools import json_to_dict


def get_file_names_to_update():

     # Get a list of all modified files
    bash_command('git status | grep modified >> updated.txt')

    # Import that list
    modified = open('updated.txt', 'r')
    line = modified.read()
    modified.close()

    # Delete the list to avoid overlap
    bash_command('rm updated.txt')

    # Make each line its own variable in an array
    files = line.split('\n')

    # Define an empty master list for the file names
    file_names = list()

    # Iteratively add each name to the list
    while files:

        file = files.pop()
        file_name = file.replace('	modified:   ', '')

        if file_name != '':
            file_names.append(file_name)
    
    # Returns a list of modified file names
    return file_names


def add_and_commit_file(file_names):

    # Import the file_name:description data
    commit_data = json_to_dict('masterCommit.json')

    # Whilst there are still files left in the files list
    while file_names:

        this_file = file_names.pop()

        if this_file in commit_data:

            bash_command(f'git add {this_file}')
            sleep(2)

            file_description = commit_data[this_file]

            bash_command(f'git commit -m "{file_description}"')
            sleep(2)

            bash_command('git push https://github.com/AirmanKolberg/ADA-Minting-Calculator.git')
            sleep(4)


        else:

            print(f'Update key:value pair for {this_file} with name_to_commit.py')


if __name__ == '__main__':

    files_to_update = get_file_names_to_update()

    if files_to_update:

        add_and_commit_file(files_to_update)
