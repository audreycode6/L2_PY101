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

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

def prompt(message):
    print(f"==> {message}")

def display_error(message):
    print(f"    !!!! ERROR: Invalid input. {message} !!!!")

def display_welcome():
    print('\n----------------------------------------')
    print('ROCK * PAPER * SCISSORS * LIZARD * SPOCK')
    print('----------------GO!---------------------')


def display_winner(user, computer):
    if ((user == 'rock' and computer == 'scissors' or computer == 'lizard') or
        (user == 'paper' and computer == 'rock' or computer =='spock') or
        (user == 'scissors' and computer == 'paper' or computer == 'lizard') or
        (user == 'lizard' and computer == 'paper' or computer == 'spock') or
        (user == 'spock' and computer == 'scissors' or computer == 'rock')
        ):
        display_results('YOU WIN! :D')
    elif ((user == 'rock' or user == 'spock' and computer == 'paper') or
        (user == 'paper' or user == 'lizard' and computer == 'scissors') or
        (user == 'scissors' or user == 'lizard' and computer == 'rock') or
        (user == 'paper' or user == 'spock' and computer == 'lizard') or
        (user == 'scissors' or user == 'rock' and computer == 'spock')):
        display_results('COMPUTER WINS!')
    else:
        display_results("IT'S A TIE!")

def display_results(message):
    print(f'    ... {message}')

def display_bye():
    prompt('Thanks for playing, see you later!')
    print('----------------------------------------')

while True: # ROCK PAPER SCISSOR LIZARD SPOCK PROGRAM
    display_welcome()

    # ASK USER FOR THEIR CHOICE: R P SC L SP
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input().lower()

    while choice not in VALID_CHOICES:
        display_error(f'Enter {" OR ".join(VALID_CHOICES)}')
        choice = input().lower()

    computer_choice = random.choice(VALID_CHOICES)

    # DISPLAY CHOICES: USER VS COMPUTER
    prompt(f'You chose {choice} ... computer chose {computer_choice}')

    display_winner(choice, computer_choice)

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