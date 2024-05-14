''' build a mortgage calculator that takes
in loan amount, APR, and loan duration and returns the
monthly payment assuming that interest is compounded monthly.'''

# TODO: break up loan_calculator to be 10-15 lines only, make more functions of the small moving parts
# TODO: make sure function names reference their side effect (ex display_intro_outro)
import json
with open('mortgage_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"==> {message}")

def intro_outro(message):
    print(f"-------{message}-------")
    print()

def error_output(message):
    print(f"\n    !!!! {message} !!!!\n\n    -------TRY AGAIN!-------")

def get_loan_amount():
    prompt(MESSAGES["loan_amount"])
    loan_amount_input = input()
    return loan_amount_input

def invalid_loan_amount(input_value):
    try:
        float(input_value)
        if float(input_value) <= 0:
            return True
    except ValueError:
        return True
    return False

def get_apr():
    prompt(MESSAGES["APR"])
    annual_percentage_rate_input = input()
    return annual_percentage_rate_input

def invalid_apr(input_apr):
    try:
        float(input_apr)
        if float(input_apr) < 0:
            return True
    except ValueError:
        return True
    return False

def get_loan_year_duration():
    prompt(MESSAGES["years"])
    year_duration = input()
    while invalid_loan_duration(year_duration):
        error_output(MESSAGES["invalid_year"])
        prompt(MESSAGES["years"])
        year_duration = input()
    year_month_conversion = int(year_duration) * 12
    return year_month_conversion

def get_loan_month_duration():
    prompt(MESSAGES["months"])
    month_duration = input()
    while invalid_loan_duration(month_duration):
        error_output(MESSAGES["invalid_months"])
        prompt(MESSAGES["months"])
        month_duration = input()
    month_duration = int(month_duration)
    return month_duration

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

def calc_again():
    prompt(MESSAGES["another_calculation"])
    another_calc = input()
    if another_calc.lower() == 'y':
        print('\n-------NEW CALCULATION-------')
        return loan_calculator()

    return intro_outro('SEE YOU LATER!')

# LOAN CALC PROGRAM - uses functions above
def loan_calculator():
    # LOAN AMOUNT INPUT:
    loan_amount_input = get_loan_amount()
    while invalid_loan_amount(loan_amount_input):
        error_output(MESSAGES["invalid_loan_amount"])
        loan_amount_input = get_loan_amount()
    loan_amount = float(loan_amount_input)

    # MONTHLY APR:
    annual_percentage_rate_input = get_apr()
    while invalid_apr(annual_percentage_rate_input):
        error_output(MESSAGES["invalid_apr"])
        annual_percentage_rate_input = get_apr()
    annual_percentage_rate = float(annual_percentage_rate_input)

    if annual_percentage_rate != 0:
        # CONVERT APR TO DECIMAL FORMAT
        apr_decimal = float(annual_percentage_rate_input) * .01
        # APR -> MONTHLY INTEREST RATE
        monthly_interest_rate = apr_decimal / 12
    else:
        annual_percentage_rate = 'No APR'

    # LOAN DURATION:
    prompt(MESSAGES["loan_duration"])
    year_month_conversion = get_loan_year_duration()
    month_duration = get_loan_month_duration()

    # CHECK TOTAL LOAN DURATION IS GREATER THAN 0:
    while zero_or_less_duration(year_month_conversion, month_duration):
        error_output(MESSAGES["invalid_loan_duration"])
        year_month_conversion = get_loan_year_duration()
        month_duration = get_loan_month_duration()

    loan_duration_months = year_month_conversion + month_duration

    # MONTHLY PAYMENT with VS without APR:
    if annual_percentage_rate != 'No APR':
        total_monthly_payment = loan_amount * (monthly_interest_rate /
        (1 - (1 + monthly_interest_rate) ** (-loan_duration_months)))
        total_duration_interest = (
        (total_monthly_payment * loan_duration_months)- loan_amount
        )
        total_payment = loan_amount + total_duration_interest

        # RESULTS
        print('\n----------RESULTS----------')
        print(f'Payment Every Month: ${total_monthly_payment:.2f}')
        print(f'''Total Payment Amount
        ({loan_duration_months} months): ${total_payment:.2f}''')
        print(f'Total Interest: ${total_duration_interest:.2f}')
        print('---------------------------')
    else:
        monthly_payment =  loan_amount / loan_duration_months
        # RESULTS
        print('\n----------RESULTS----------')
        print(f'Payment Every Month: ${monthly_payment:.2f}')
        print(f'''Total Payment Amount
         ({loan_duration_months} months): ${loan_amount:.2f}''')
        print('---------------------------')
    # ASK USER IF THEY WANT TO CALC AGAIN:
    print()
    calc_again()
intro_outro('WELCOME TO YOUR TRUSTY LOAN CALCULATOR!')
loan_calculator()