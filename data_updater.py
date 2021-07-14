from time import sleep
from system_functions import bash_command, clear_screen
from commit_and_push_all import add_and_commit_file

"""
This application can be used to automate the process
of updating the data.json file to GitHub when new
information is obtain in an effort to stay up-to-date
with the data I'm sharing.
"""


def countdown(seconds):
    
    # Count down until 0 so that the last second is counted
    while seconds > -1:

        mins, secs = divmod(seconds, 60)

        # Setup grammar conditions for min/mins
        if mins != 1:
            min_display = 'mins'
        else:
            min_display = 'min'

        # Setup grammar conditions for sec/secs
        if secs != 1:
            sec_display = 'secs'
        else:
            sec_display = 'sec'

        # `timer` example: "Updating in 121mins 1sec..."
        timer = f'Updating in {mins}{min_display} {secs}{sec_display}...'


        print(timer, end="\r")
        sleep(1)
        seconds -= 1
    clear_screen()


def startup_question():

    response = input("Update now?  ('y' or 'yes', 'n' or 'no'):\n").lower()
    return response


def verify_update_at_startup(user_response):

    if user_response == 'y' or user_response == 'yes':
        return True

    elif user_response == 'n' or user_response == 'no':
        return False
    
    else:
        response = startup_question()
        verify_update_at_startup(response) 


if __name__ == '__main__':

    clear_screen()

    # Verify if user wishes to update the data before the 6 hour timer
    response = startup_question()

    update_at_startup = verify_update_at_startup(response)

    if update_at_startup:

        add_and_commit_file(['data.json'])
        clear_screen()

    while True:

        # Wait two hours to push an update
        countdown(60 * 60 * 2)

        add_and_commit_file(['data.json'])
        clear_screen()
