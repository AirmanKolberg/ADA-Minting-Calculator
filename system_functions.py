from os import system


def bash_command(user_in):
    
    _ = system(user_in)



def clear_screen():

    bash_command('clear')


if __name__ == '__main__':
    pass
