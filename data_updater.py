from time import sleep
from system_functions import bash_command, clear_screen

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


if __name__ == '__main__':

    clear_screen()

    while True:

        # Wait six hours to push an update
        countdown(60 * 60 * 6)

        git_commands = ['git add data.json',
                        'git commit -am "💽  Freebee Starting Data"',
                        './push']

        # Execute all of the git_commands as Shell commands
        for command in git_commands:
            
            bash_command(command)