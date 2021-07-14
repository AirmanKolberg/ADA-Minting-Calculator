from system_functions import bash_command, clear_screen
from time import sleep
from json_tools import json_to_dict


def get_file_names_to_update():

    update_types = ['modified', 'deleted']

    # Get a list of all modified and deleted files
    for update_type in update_types:
        bash_command(f'git status | grep {update_type} >> {update_type}.txt')

    # Import the modified list
    modified = open('modified.txt', 'r')
    modified_line = modified.read()
    modified.close()

    # Import the deleted list
    deleted = open('deleted.txt', 'r')
    deleted_line = deleted.read()
    deleted.close()

    # Ensure lists are deleted to avoid overlap
    bash_command('rm modified.txt && rm deleted.txt')

    # Make each modified/deleted_line its own variable in their respective arrays
    modified_files = modified_line.split('\n')
    deleted_files = deleted_line.split('\n')
    print(modified_files)
    print(deleted_files)

    # Define empty master lists for the file names
    modified_file_names = list()
    deleted_file_names = list()

    # Iteratively add each name to the modified list
    while modified_files:

        file = modified_files.pop()
        file_name = file.replace('	modified:   ', '')

        if file_name != '':
            modified_file_names.append(file_name)
    
    # Iteratively add each name to the deleted list
    while deleted_files:

        file = deleted_files.pop()
        file_name = file.replace('	deleted:    ', '')

        if file_name != '':
            deleted_file_names.append(file_name)
    
    # Returns a list of modified file names
    return modified_file_names, deleted_file_names


def add_and_commit_file(file_names):

    # Import the file_name:description data
    commit_data = json_to_dict('masterCommit.json')

    # Whilst there are still files left in the files list
    while file_names:

        this_file = file_names.pop()

        if this_file in commit_data:

            file_description = commit_data[this_file]

            bash_command(f'git add {this_file}')
            bash_command(f'git commit -m "{file_description}"')
            bash_command('git push https://github.com/AirmanKolberg/ADA-Minting-Calculator.git')

        else:

            print(f'Update key:value pair for {this_file} with name_to_commit.py')


def delete_file(file_names):

    # Whilst there are still files left in the files list
    while file_names:

        this_file = file_names.pop()

        bash_command(f'git rm {this_file}')
        bash_command('git commit -m "deleted/renamed file"')
        bash_command('git push https://github.com/AirmanKolberg/ADA-Minting-Calculator.git')


if __name__ == '__main__':

    clear_screen()

    files_to_update, files_to_delete = get_file_names_to_update()

    if files_to_update:

        add_and_commit_file(files_to_update)
    
    if files_to_delete:

        delete_file(files_to_delete)
