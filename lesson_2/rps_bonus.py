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

def display_welcome(round):
    print(f'\n------------- ROUND {round} of 5 ---------------')
    print('ROCK * PAPER * SCISSORS * LIZARD * SPOCK')
    print('---------------- GO! ---------------------')

def display_winner(user, computer, game_round):
    winning_combinations = {
        'rock' : ['scissors', 'lizard'],
        'paper' : ['rock', 'spock'],
        'scissors' : ['paper', 'lizard'],
        'lizard' : ['spock', 'paper'],
        'spock' : ['scissors', 'rock']
        }

    if computer in winning_combinations.get(user, []):
        display_results(f'ROUND {game_round}: You win!')
        return "user_wins"
    elif user in winning_combinations.get(computer, []):
        display_results(f'ROUND {game_round}: Computer wins!')
        return "computer_wins"
    else:
        display_results(f"ROUND {game_round}: Tie!")
        return "tie"

def display_results(message):
    print(f'    {message}')

def display_round_5_winner(user_wins, computer_wins, ties):
    print("\n-------------- GAME OVER -----------------")
    if user_wins > computer_wins:
        print('               YOU WIN! :D')
    elif user_wins < computer_wins:
        print('             COMPUTER WINS!')
    else: 
        print('           THERES BEEN A TIE! :O')
    print(f'                 wins: {user_wins}')
    print(f'               losses: {computer_wins}')
    print(f'                  tie: {ties}')
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
    return rock_paper_scissors_l_sp()

def display_bye():
    prompt('Thanks for playing, see you later!')
    print('-----------------------------------------')

def rock_paper_scissors_l_sp(): # ROCK PAPER SCISSOR LIZARD SPOCK PROGRAM
    game_round_counter = 0
    computer_wins_counter = 0
    user_wins_counter = 0
    ties_counter = 0
    while game_round_counter < 5:
        game_round_counter += 1
        display_welcome(game_round_counter)

        # ASK USER FOR THEIR CHOICE: R P SC L SP
        prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
        choice = input().lower()

        while choice_invalid(choice) is not False:
            display_error(f'Enter {" OR ".join(VALID_CHOICES)}')
            choice = input().lower()

        # UPDATE USERS CHOICE TO MATCHING CHOICE FROM KEYS IN VALID_CHOICES:
            # i.e 'r' --> rock
        user_fullname_choice = update_choice(choice)

        computer_choice = random.choice(list(VALID_CHOICES.keys()))

        # DISPLAY CHOICES: USER VS COMPUTER
        prompt(f"You chose {user_fullname_choice}. Computer chose {computer_choice}.")

        score = display_winner(
            user_fullname_choice, 
            computer_choice,
            game_round_counter
            )
        # print(score)
        if score == 'user_wins':
            user_wins_counter += 1
        elif score == 'computer_wins':
            computer_wins_counter += 1
        else:
            ties_counter += 1

    # FINAL RESULTS
    display_round_5_winner(user_wins_counter, computer_wins_counter, ties_counter)

    prompt_play_again()

rock_paper_scissors_l_sp()