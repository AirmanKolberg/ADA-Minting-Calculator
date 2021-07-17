from system_functions import bash_command, clear_screen, get_return_from_bash_command
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
        file_name = file_name.replace('\t', '')

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


# # This feature is still in-dev
# def search_for_untracked_files():

#     untracked_line = get_return_from_bash_command('git status')

#     # Make untracked_line its own variable in an arrays
#     untracked_files = untracked_line.split('\n')
    
#     # An array to be returned with the file names to be tracked
#     files_to_track = list()

#     if 'Untracked files:' in untracked_files:

#         starting_point = untracked_files.index('Untracked files:') + 2
#         tracking_files = True

#         for i in range(starting_point, len(untracked_files)):

#             current_file = untracked_files[i]

#             # The space indicates that the list is over
#             if current_file == '':
#                 tracking_files = False
            
#             current_file = current_file.replace('\t', '')
#             files_to_track.append(current_file)
        
#         # Push the updates to GitHub
#         add_and_commit_file(files_to_track)


if __name__ == '__main__':

    clear_screen()

    files_to_update, files_to_delete = get_file_names_to_update()

    if files_to_update:

        add_and_commit_file(files_to_update)
    
    if files_to_delete:

        delete_file(files_to_delete)

    search_for_untracked_files()
