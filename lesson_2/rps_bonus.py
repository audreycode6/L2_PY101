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

NUMBER_OF_ROUNDS = 5
VALID_CHOICES = {
    'rock' : 'r',
    'paper' : 'p',
    'scissors' : 'sc',
    'lizard' : 'l',
    'spock' : 'sp'
    }
PLAY_AGAIN_INPUT_CHOICES = [
    'yes',
    'yeah',
    'y',
    'yup',
    'no',
    'n',
    'nope',
    'nah'
    ]

def clear_screen(seconds):
    sleep(seconds)
    os.system('clear')

def prompt(message):
    print(f"==> {message}")

def center_text(message, number):
    print(f"{message}".center(number))

def display_error(message):
    print(f"    !!!! ERROR: Invalid input. {message} !!!!")

def display_game_intro():
    print('--------------------------------------------------')
    print(' Welcome to Rock, Paper, Scissors, Lizard, Spock!\n')
    format_text('RULES')
    print(f'''
You have {NUMBER_OF_ROUNDS} rounds to try to beat your oponent.
Choose between 5 objects:
    * SCISSORS beats paper & lizard
    * PAPER beats rock & Spock
    * ROCK beats lizard & scissors
    * LIZARD beats Spock & paper
    * SPOCK beats scissors & rock''')
    print('--------------------------------------------------')

def clear_screen_continue(message):
    prompt(f'Press Return/Enter to {message}')
    input()
    clear_screen(.3)

def display_round_prompt(game_round):
    spacing = '-------------'
    print(f'{spacing} ROUND {game_round} of {NUMBER_OF_ROUNDS} {spacing}')
    print(' ROCK * PAPER * SCISSORS * LIZARD * SPOCK')
    print('------------------ GO! -------------------')

def choice_invalid(user_choice):
    choice_is_invalid = True
    for choices in VALID_CHOICES.items():
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
        if user_choice == section:
            update_user_choice = key
            return update_user_choice
    return user_choice


def determine_winner(user, computer):
    winning_combinations = {
        'rock' : ['scissors', 'lizard'],
        'paper' : ['rock', 'spock'],
        'scissors' : ['paper', 'lizard'],
        'lizard' : ['spock', 'paper'],
        'spock' : ['scissors', 'rock']
        }

    if computer in winning_combinations.get(user, []):
        return "user_wins"
    if user in winning_combinations.get(computer, []):
        return "computer_wins"
    return "tie"

def format_text(message):
    center_text(f'** {message} **', 43)

def display_winner(winner, game_round):
    if winner == "user_wins":
        format_text(f'ROUND {game_round}: YOU WIN!')
    elif winner == 'computer_wins':
        format_text(f'ROUND {game_round}: COMPUTER WINS!')
    else:
        format_text(f"ROUND {game_round}: TIE!")

def round_results(user_choice, computer_choice):
    format_text(f'You chose {user_choice}.')
    format_text(f'Computer chose {computer_choice}.')

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

def display_current_scores(user_win_count, computer_win_count, tie_count):
    print('\n------------- SCORE BOARD ----------------')
    center_text(f'win: {user_win_count}', 39)
    center_text(f'loss: {computer_win_count}', 39)
    center_text(f'tie: {tie_count}', 39)
    print('------------------------------------------')

def display_final_winner(user_wins, computer_wins, ties):
    print("-------------- GAME OVER -----------------")
    if user_wins > computer_wins:
        center_text('YOU WIN!!!', 40)
    elif user_wins < computer_wins:
        center_text('COMPUTER WINS!', 40)
    else:
        center_text('THERES BEEN A TIE! :O', 43)
    print()
    center_text('Your Results', 40)
    center_text(f'win: {user_wins}', 39)
    center_text(f'loss: {computer_wins}', 39)
    center_text(f'tie: {ties}', 39)
    print('------------------------------------------')

def prompt_play_again():
    print('\n==> Play again? (y/n)')
    answer = input().lower()
    while True:
        if answer in PLAY_AGAIN_INPUT_CHOICES:
            break
        display_error("Enter Y for yes OR N for no.")
        answer = input().lower()

    if answer[0] == 'n':
        return display_bye()
    clear_screen(0.5)
    return rock_paper_scissors_l_sp()

def display_bye():
    thanks = 'Thanks for playing Rock, Paper, Scissors, Lizard, Spock!'
    bye = 'See you later!'
    print()
    format_text(thanks)
    format_text(bye)

# ROCK PAPER SCISSOR LIZARD SPOCK PROGRAM - main entry point
def rock_paper_scissors_l_sp():
    display_game_intro()
    clear_screen_continue('start!')

    game_round_count = 0
    computer_win_count = 0
    user_win_count = 0
    tie_count = 0

    while game_round_count < NUMBER_OF_ROUNDS:
        game_round_count += 1
        display_round_prompt(game_round_count)

        # GET PLAYER CHOICES:
        user_choice = get_choice()
        user_fullname_choice = update_choice(user_choice)
        computer_choice = random.choice(list(VALID_CHOICES.keys()))

        round_results(user_fullname_choice, computer_choice)

        # UPDATE COUNTERS
        winner = determine_winner(
            user_fullname_choice,
            computer_choice
            )
        if winner == 'user_wins':
            user_win_count += 1
        elif winner == 'computer_wins':
            computer_win_count += 1
        else:
            tie_count += 1

        display_winner(winner, game_round_count)

        # SCORE BOARD:
        display_current_scores(user_win_count, computer_win_count, tie_count)

        if game_round_count < NUMBER_OF_ROUNDS:
            clear_screen_continue('continue.')
        else:
            clear_screen_continue('see your final results!')

    # FINAL RESULTS
    display_final_winner(user_win_count, computer_win_count, tie_count)
    sleep(1)
    prompt_play_again()

# RUN PROGRAM
rock_paper_scissors_l_sp()