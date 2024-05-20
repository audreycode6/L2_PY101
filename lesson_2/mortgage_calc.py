''' build a mortgage calculator that takes
in loan amount, APR, and loan duration and returns the
monthly payment assuming that interest is compounded monthly.'''

import json
import os
from time import sleep

with open('mortgage_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"==> {message}")

def display_intro_outro(message):
    print(f"-------{message}-------")

def display_error(message):
    print(f"\n    !!!! {message} !!!!\n    -------TRY AGAIN!-------\n")

def clear_screen():
    sleep(1)
    os.system('clear')

def get_loan_amount():
    prompt(MESSAGES["LOAN_AMOUNT_PROMPT"])
    loan_amount_input = input()
    while invalid_loan_amount(loan_amount_input):
        display_error(MESSAGES["ERROR_LOAN_AMOUNT"])
        loan_amount_input = get_loan_amount()
    return loan_amount_input

def invalid_loan_amount(input_value):
    try:
        float(input_value)
        if float(input_value) <= 0 or input_value.lower() == 'nan':
            return True
    except ValueError:
        return True
    return False

def get_apr():
    prompt(MESSAGES["APR_PROMPT"])
    annual_percentage_rate_input = input()
    while invalid_apr(annual_percentage_rate_input):
        display_error(MESSAGES["ERROR_APR"])
        annual_percentage_rate_input = get_apr()
    return annual_percentage_rate_input

def invalid_apr(input_apr):
    try:
        float(input_apr)
        if float(input_apr) < 0 or input_apr.lower() == 'nan':
            return True
    except ValueError:
        return True
    return False

def check_apr_0_more(annual_percentage_rate):
    if annual_percentage_rate != 0:
        apr_decimal = float(annual_percentage_rate) * .01
        monthly_interest_rate = apr_decimal / 12
        return monthly_interest_rate
    return None

def get_loan_year_duration():
    prompt(MESSAGES["YEARS_PROMPT"])
    year_duration = input()
    while invalid_loan_duration(year_duration):
        display_error(MESSAGES["ERROR_YEAR"])
        prompt(MESSAGES["YEARS_PROMPT"])
        year_duration = input()
    year_month_conversion = int(year_duration) * 12
    return year_month_conversion

def get_loan_month_duration():
    prompt(MESSAGES["MONTHS_PROMPT"])
    month_duration = input()
    while invalid_loan_duration(month_duration):
        display_error(MESSAGES["ERROR_MONTHS"])
        prompt(MESSAGES["MONTHS_PROMPT"])
        month_duration = input()
    month_duration = int(month_duration)
    return month_duration

def invalid_loan_duration(loan_duration):
    try:
        int(loan_duration)
        if int(loan_duration) < 0 or loan_duration.lower() == 'nan':
            return True
    except ValueError:
        return True
    return False

def try_zero_or_less_duration(loan_duration):
    while loan_duration <= 0:
        display_error(MESSAGES["ERROR_LOAN_DURATION"])
        year_month_conversion = get_loan_year_duration()
        month_duration = get_loan_month_duration()
        loan_duration = year_month_conversion + month_duration
        try_zero_or_less_duration(loan_duration)
    return loan_duration

def calc_monthly_payment(loan_amount,
                        monthly_interest_rate,
                        loan_duration_months):
    total_monthly_payment = loan_amount * (monthly_interest_rate /
    (1 - (1 + monthly_interest_rate) ** (-loan_duration_months)))

    total_duration_interest = (
    (total_monthly_payment * loan_duration_months) - loan_amount)

    total_payment = loan_amount + total_duration_interest
    return total_monthly_payment, total_duration_interest, total_payment

def display_user_input(loan_amount, apr):
    print('---------YOUR INPUT--------')
    print(f'Loan Amount: ${loan_amount:.2f}')
    print(f'APR: {apr} %')

def display_results_with_apr(month_payment,
                            loan_duration,
                            total, interest):
    print('----------RESULTS----------')
    print(f'Payment Every Month: ${month_payment:.2f}')
    print(f'''Total Payment Amount
    ({loan_duration} months): ${total:.2f}''')
    print(f'Total Interest: ${interest:.2f}')
    print('---------------------------')

def display_results_0apr(loan_amount, loan_duration_months):
    monthly_payment =  loan_amount / loan_duration_months
    print('----------RESULTS----------')
    print(f'Payment Every Month: ${monthly_payment:.2f}')
    print(f'''Total Payment Amount
        ({loan_duration_months} months): ${loan_amount:.2f}''')
    print('---------------------------')

def calc_again():
    prompt(MESSAGES["ANOTHER_CALCULATION_PROMPT"])
    another_calc = input()
    if another_calc.lower() == 'y':
        clear_screen()
        print('\n-------NEW CALCULATION-------')
        return loan_calculator()
    return display_intro_outro('SEE YOU LATER!')

# LOAN CALC PROGRAM - main entry point
def loan_calculator():
    # LOAN AMOUNT
    loan_amount_input = get_loan_amount()
    loan_amount = float(loan_amount_input)
    clear_screen()

    # APR
    annual_percentage_rate_input = get_apr()
    annual_percentage_rate = float(annual_percentage_rate_input)
    monthly_interest_rate = check_apr_0_more(annual_percentage_rate)
    clear_screen()

    # LOAN DURATION
    prompt(MESSAGES["LOAN_DURATION_PROMPT"])
    year_month_conversion = get_loan_year_duration()
    month_duration = get_loan_month_duration()
    loan_duration_input = year_month_conversion + month_duration

    # ensure loan_duration_input is greater than 0 before continuing
    loan_duration_months = try_zero_or_less_duration(loan_duration_input)
    clear_screen()

    # RESULTS
    if monthly_interest_rate is not None:
        monthly_payment, total_interest, total_payment = calc_monthly_payment(
        loan_amount,
        monthly_interest_rate,
        loan_duration_months)

        display_user_input(loan_amount, annual_percentage_rate)

        display_results_with_apr(monthly_payment,
        loan_duration_months,
        total_payment,
        total_interest)
    else:
        display_user_input(loan_amount, annual_percentage_rate)
        display_results_0apr(loan_amount, loan_duration_months)
    calc_again()
    clear_screen()

# RUN PROGRAM
display_intro_outro(MESSAGES["DISPLAY_WELCOME"])
clear_screen()
loan_calculator()