'''' Updated Rock, Paper, Scissors Program
where you play against the computer for 5 rounds:
added Lizard & Spock to choices & allow abbreviations for choice input.
    Rules:
    scissors beats: paper & lizard
    paper beats: rock & spock
    rock beats: lizard & scissors
    lizard beats: Spock & paper
    spock beats: scissors & rock
'''

import random
import os
from time import sleep

VALID_CHOICES = {
    'rock' : {'rock', 'r'},
    'paper' : {'paper', 'p'},
    'scissors' : {'scissors', 'sc'},
    'lizard' : {'lizard', 'l'},
    'spock' : {'spock', 'sp'}
    }

def clear_screen(seconds):
    sleep(seconds)
    os.system('clear')

def prompt(message):
    print(f"==> {message}")

def display_error(message):
    print(f"    !!!! ERROR: Invalid input. {message} !!!!")

def display_game_rules():
    print('--------------------------------------------------')
    print(' Welcome to Rock, Paper, Scissors, Lizard, Spock!\n')
    print('                 * RULES *')
    print('''You have 5 rounds to try to beat your oponent.
Choose between 5 objects:
    * SCISSORS beats paper & lizard
    * PAPER beats rock & Spock
    * ROCK beats lizard & scissors
    * LIZARD beats Spock & paper
    * SPOCK beats scissors & rock''')
    print('--------------------------------------------------')
    prompt('Enter any key to start')
    input()

def display_welcome(game_round):
    print(f'------------- ROUND {game_round} of 5 ---------------')
    print('ROCK * PAPER * SCISSORS * LIZARD * SPOCK')
    print('---------------- GO! ---------------------')

def choice_invalid(user_choice):
    choice_is_invalid = True
    for choices in VALID_CHOICES.values():
        if user_choice in choices:
            choice_is_invalid = False
    return choice_is_invalid

def get_choice():
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input().lower()

    while choice_invalid(choice) is True:
        display_error(f'''Enter {" OR ".join(VALID_CHOICES)}.
        Abbreviations also accepted: r, p, sc, l, sp''')
        choice = input().lower()
    return choice

# Update users choice to matching choice from keys in VALID_CHOICES:
    # i.e 'r' --> rock
def update_choice(user_choice):
    for key, section in VALID_CHOICES.items():
        if user_choice in section:
            update_choice_full_name = key
    return update_choice_full_name

def display_winner(user, computer, game_round):
    winning_combinations = {
        'rock' : ['scissors', 'lizard'],
        'paper' : ['rock', 'spock'],
        'scissors' : ['paper', 'lizard'],
        'lizard' : ['spock', 'paper'],
        'spock' : ['scissors', 'rock']
        }

    if computer in winning_combinations.get(user, []):
        display_results(f'ROUND {game_round}: YOU WIN!')
        return "user_wins"
    if user in winning_combinations.get(computer, []):
        display_results(f'ROUND {game_round}: COMPUTER WINS!')
        return "computer_wins"

    display_results(f"ROUND {game_round}: TIE!")
    return "tie"

def display_results(message):
    print(f'    ** {message} **')

def update_counters(score,
                    user_win_count,
                    computer_win_count,
                    tie_count):
    if score == 'user_wins':
        user_win_count += 1
    elif score == 'computer_wins':
        computer_win_count += 1
    else:
        tie_count += 1

def display_final_winner(user_wins, computer_wins, ties):
    print("-------------- GAME OVER -----------------")
    if user_wins > computer_wins:
        print('               YOU WIN! :D')
    elif user_wins < computer_wins:
        print('             COMPUTER WINS!')
    else:
        print('           THERES BEEN A TIE! :O')
    print('\n              your results')
    print(f'                 win: {user_wins}')
    print(f'                loss: {computer_wins}')
    print(f'                 tie: {ties}')
    print('------------------------------------------')

def prompt_play_again():
    print('\n==> Play again? (y/n)')
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break
        display_error("Enter Y for yes OR N for no.")
        answer = input().lower()

    if answer[0] == 'n':
        return display_bye()

    clear_screen(0.5)
    return rock_paper_scissors_l_sp()

def display_bye():
    prompt('''Thanks for playing Rock, Paper, Scissors, Lizard, Spock!
    See you later!''')
    clear_screen(3)

# ROCK PAPER SCISSOR LIZARD SPOCK PROGRAM - main entry point
def rock_paper_scissors_l_sp():
    display_game_rules()
    clear_screen(.5)

    game_round_count = 0
    computer_win_count = 0
    user_win_count = 0
    tie_count = 0

    while game_round_count < 5:
        game_round_count += 1
        display_welcome(game_round_count)

        # GET PLAYER CHOICES:
        user_choice = get_choice()
        user_fullname_choice = update_choice(user_choice)
        computer_choice = random.choice(list(VALID_CHOICES.keys()))

        # ROUND RESULTS
        display_results(f'''You chose {user_fullname_choice}. **
    ** Computer chose {computer_choice}.''')

        # UPDATE COUNTERS
        score = display_winner(
            user_fullname_choice,
            computer_choice,
            game_round_count
            )
        if score == 'user_wins':
            user_win_count += 1
        elif score == 'computer_wins':
            computer_win_count += 1
        else:
            tie_count += 1
        clear_screen(3)

    # FINAL RESULTS
    display_final_winner(user_win_count, computer_win_count, tie_count)
    sleep(2)
    prompt_play_again()

# RUN PROGRAM
rock_paper_scissors_l_sp()