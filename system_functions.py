from os import system
from time import sleep


def bash_command(user_in):
    
    _ = system(user_in)



def clear_screen():

    bash_command('clear')


def verify_yes_or_no(response):

    if response == 'yes' or response == 'y':

        return True

    elif response == 'no' or response == 'n':
        
        return False

    else:
        return verify_yes_or_no(input(f"{response} is neither 'yes' nor 'no', please try again: ").lower())


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

        # Wait a second
        sleep(1)

        # Take a second away from the total
        seconds -= 1

    clear_screen()


if __name__ == '__main__':
    pass
