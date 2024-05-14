'''' Rock, Paper, Scissors Program where you play against the computer:
takes in user input (R,P,S) and get computer randomly generated (R,P,S)
and annouce winner (user or computer) or if tie; 
continue game until user wants to stop '''

import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f"==> {message}")

def display_error(message):
    print(f"    !!!! ERROR: {message} !!!!")

# welcome message:
def display_welcome():
    print('\n-----------------------')
    print('ROCK * PAPER * SCISSORS')
    print('---------SHOOT---------\n')

display_welcome()

# ask user for their choice: rock, paper, scissors
prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
choice = input().lower()

while choice not in VALID_CHOICES:
    display_error(f'Invalid input. Expecting {" OR ".join(VALID_CHOICES)}')
    choice = input().lower()

computer_choice = random.choice(VALID_CHOICES)

# Display choices: user VS computer
prompt(f'You chose {choice}, computer chose {computer_choice}')

# Winning conditions:
if ((choice == 'rock' and computer_choice == 'scissors') or
    (choice == 'paper' and computer_choice == 'rock')or
    (choice == 'scissors' and computer_choice == 'paper')):
    prompt('YOU WIN! :D') # MAYBE PRETTY PRINT function for results
elif ((choice == 'rock' and computer_choice == 'paper') or
      (choice == 'paper' and computer_choice == 'scissors')or
      (choice == 'scissors' and computer_choice == 'rock')):
    prompt('COMPUTER WINS!')
else:
    prompt("IT'S A TIE!")

