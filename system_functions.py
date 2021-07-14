from os import system


def bash_command(user_in):
    
    _ = system(user_in)



def clear_screen():

    bash_command('clear')


def verify_yes_or_no(response):
    if response == 'yes':
        return True
    elif response == 'no':
        return False
    else:
        return verify_yes_or_no(input(f"{response} is neither 'yes' nor 'no', please try again: ").lower())


if __name__ == '__main__':
    pass
