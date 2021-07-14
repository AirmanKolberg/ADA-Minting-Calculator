from system_functions import bash_command
from time import sleep


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


def add_and_commit_file(file_name):

    bash_commands = ['git status',
                     f'git add {file_name}',
                     f'git commit -am "{}"']
    
    for each_command in bash_commands:

        bash_command(each_command)
        sleep(2)


if __name__ == '__main__':

    files_to_update = get_file_names_to_update()

    if files_to_update:

        add_and_commit_file()
