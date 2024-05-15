'''' Rock, Paper, Scissors Program where you play against the computer:
takes in user input (R,P,S) and get computer randomly generated (R,P,S)
and annouce winner (user or computer) or if tie; 
continue game until user wants to stop '''

import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f"==> {message}")

def display_error(message):
    print(f"    !!!! ERROR: Invalid input. {message} !!!!")

def display_welcome():
    print('\n----------------------------------------')
    print('   ROCK     *   PAPER   *    SCISSORS   ')
    print('---------------SHOOT--------------------')

def display_winner(user, computer):
    if ((user == 'rock' and computer == 'scissors') or
        (user == 'paper' and computer == 'rock') or
        (user == 'scissors' and computer == 'paper')):
        display_results('YOU WIN! :D')
    elif ((user == 'rock' and computer == 'paper') or
        (user == 'paper' and computer == 'scissors') or
        (user == 'scissors' and computer == 'rock')):
        display_results('COMPUTER WINS!')
    else:
        display_results("IT'S A TIE!")

def display_results(message):
    print(f'    ... {message}')

def display_bye():
    prompt('Thanks for playing, see you later!')
    print('----------------------------------------')

while True: # ROCK PAPER SCISSOR PROGRAM
    display_welcome()

    # ASK USER FOR THEIR CHOICE: ROCK, PAPER, OR SCISSORS
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