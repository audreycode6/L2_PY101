'''' Update Rock, Paper, Scissors Program where you play against the computer:
add Lizard & Spock to choices:
    Rules:
    scissors beats: paper & lizard
    paper beats: rock & spock
    rock beats: lizard & scissors
    lizard beats: Spock & paper
    spock beats: scissors & rock
'''

import random

VALID_CHOICES = {
    'rock' : {'rock', 'r'},
    'paper' : {'paper', 'p'},
    'scissors' : {'scissors', 'sc'},
    'lizard' : {'lizard', 'l'},
    'spock' : {'spock', 'sp'}
    }

def choice_invalid(user_choice):
    choice_is_invalid = True
    for choices in VALID_CHOICES.values():
        if user_choice in choices:
            choice_is_invalid = False

    return choice_is_invalid

def update_choice(user_choice):
    for key, section in VALID_CHOICES.items():
        if user_choice in section:
            update_choice_full_name = key

    return update_choice_full_name

def prompt(message):
    print(f"==> {message}")

def display_error(message):
    print(f"    !!!! ERROR: Invalid input. {message} !!!!")

def display_welcome():
    print('\n----------------------------------------')
    print('ROCK * PAPER * SCISSORS * LIZARD * SPOCK')
    print('----------------GO!---------------------')

def display_winner(user, computer):
    winning_combinations = {
        'rock' : ['scissors', 'lizard'],
        'paper' : ['rock', 'spock'],
        'scissors' : ['paper', 'lizard'],
        'lizard' : ['spock', 'paper'],
        'spock' : ['scissors', 'rock']
        }
    if computer in winning_combinations.get(user, []):
        display_results('YOU WIN! :D')
    elif user in winning_combinations.get(computer, []):
        display_results('COMPUTER WINS!')
    else:
        display_results("IT'S A TIE!")

def display_results(message):
    print(f'    {message}')

def display_bye():
    prompt('Thanks for playing, see you later!')
    print('----------------------------------------')

while True: # ROCK PAPER SCISSOR LIZARD SPOCK PROGRAM
    display_welcome()

    # ASK USER FOR THEIR CHOICE: R P SC L SP
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input().lower()

    while choice_invalid(choice) is not False:
        display_error(f'Enter {" OR ".join(VALID_CHOICES)}')
        choice = input().lower()

    # UPDATE USERS CHOICE TO MATCHING CHOICE FROM KEYS IN VALID_CHOICES:
        # i.e 'r' --> rock
    USER_FULLNAME_CHOICE = update_choice(choice)

    COMPUTER_CHOICE = random.choice(list(VALID_CHOICES.keys()))

    # DISPLAY CHOICES: USER VS COMPUTER
    prompt(f'''You chose {USER_FULLNAME_CHOICE} ...
    computer chose {COMPUTER_CHOICE} ...''')

    display_winner(USER_FULLNAME_CHOICE, COMPUTER_CHOICE)

    # CHECK IF USER WANTS TO PLAY AGAIN
    print('\n==> Play again? (y/n)')
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break
        display_error("Enter Y for yes OR N for no.")
        answer = input().lower()

    if answer[0] == 'n':
        display_bye()
        break