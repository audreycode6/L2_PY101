''' build a mortgage calculator that takes
in loan amount, APR, and loan duration and returns the
monthly payment assuming that interest is compounded monthly.'''

import json
with open('mortgage_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"==> {message}")

def invalid_input(input_value):
    try:
        float(input_value)
        if float(input_value) <= 0:
            return True
    except ValueError:
        return True
    return False

def invalid_loan_duration(loan_duration):
    try:
        int(loan_duration)
        if int(loan_duration) < 0:
            return True
    except ValueError:
        return True
    return False

def zero_or_less_duration(year_month_conversion, month_duration):
    duration = year_month_conversion + month_duration
    if duration <= 0:
        return True
    return False

def loan_calc():
    prompt(MESSAGES["welcome"])
    print()

    # LOAN AMOUNT INPUT:
    prompt(MESSAGES["loan_amount"])
    loan_amount_input = input()
    while invalid_input(loan_amount_input):
        prompt(MESSAGES["invalid_loan_amount"])
        loan_amount_input = input()
    loan_amount = float(loan_amount_input)

    # MONTHLY APR:
    prompt(MESSAGES["APR"])
    annual_percentage_rate_input = input()
    while invalid_input(annual_percentage_rate_input):
        prompt(MESSAGES["invalid_apr"])
        annual_percentage_rate_input = input()
    # CONVERT APR TO DECIMAL FORMAT
    annual_percentage_rate = float(annual_percentage_rate_input) * .01
    # APR -> MONTHLY INTEREST RATE
    monthly_interest_rate = annual_percentage_rate / 12

    # LOAN DURATION:
    prompt(MESSAGES["loan_duration"])
    # YEAR(S)
    prompt(MESSAGES["years"])
    year_duration = input()
    while invalid_loan_duration(year_duration):
        prompt(MESSAGES["invalid_year"])
        year_duration = input()
    year_month_conversion = int(year_duration) * 12
    # MONTH(S)
    prompt(MESSAGES["months"])
    month_duration = input()
    while invalid_loan_duration(month_duration):
        prompt(MESSAGES["invalid_months"])
        month_duration = input()
    month_duration = int(month_duration)
    # CHECK LOAN DURATION IS GREATER THAN 0: N START OVER, Y KEEP GOING
    while zero_or_less_duration(year_month_conversion, month_duration):
        prompt(MESSAGES["invalid_loan_duration"])
        print("-------PLEASE TRY AGAIN!-------")
        print(loan_calc())

    loan_duration_months = year_month_conversion + month_duration

    # MONTHLY PAYMENT:
    monthly_payment = loan_amount * (monthly_interest_rate /
    (1 - (1 + monthly_interest_rate) ** (-loan_duration_months)))
    prompt(f'Your monthly payment is: ${monthly_payment:.2f}')
    # ASK USER IF THEY WANT TO CALC AGAIN:
    print()
    calc_again()

def calc_again():
    prompt(MESSAGES["another_calculation"])
    another_calc = input()
    if another_calc.lower() == 'y':
        return loan_calc()

    return prompt(MESSAGES["bye"])

loan_calc()  