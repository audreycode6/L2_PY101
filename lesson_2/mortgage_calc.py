''' build a mortgage calculator that takes
in loan amount, APR, and loan duration and returns the
monthly payment assuming that interest is compounded monthly.'''

def prompt(message):
    print(f"==> {message}")

def invalid_loan_amount(loan_amount_input):
    try:
        float(loan_amount_input)
    except ValueError:
        return True
    return False

def invalid_apr(annual_percentage_rate_input):
    try:
        float(annual_percentage_rate_input)
    except ValueError:
        return True
    return False

def invalid_loan_duration(loan_duration):
    try:
        int(loan_duration)
    except ValueError:
        return True
    return False

# TODO: fix 33, 38, 40 too long
messages = {
    "welcome" : "Welcome to Loan Calculator!",
    "loan_amount" : "What is your loan amount?",
    "invalid_loan_amount" : "ERROR: Invalid input, enter numbers only. EX: $1234 -> 1234",
    "APR" : "What is your Annual Percentage Rate (APR)?",
    "invalid_apr" : "ERROR: Invalid input, enter numbers only. EX: 4% -> 4",
    "loan_duration" : "Now I'll need your loan duration: years and months.",
    "years" : "Enter year(s)!",
    "invalid_year" : "ERROR: Invalid input, enter numbers only. EX: 6 years -> 6",
    "months" : "Enter month(s)!",
    "invalid_months" : "ERROR: Invalid input, enter numbers only. EX: 6 months -> 6"
}

def loan_calc():
    prompt(messages["welcome"])
    print()

    # LOAN AMOUNT INPUT:
    prompt(messages["loan_amount"])
    loan_amount_input = input()
    while invalid_loan_amount(loan_amount_input):
        prompt(messages["invalid_loan_amount"])
        loan_amount_input = input()
    loan_amount = float(loan_amount_input)

    # MONTHLY APR:
    prompt(messages["APR"])
    annual_percentage_rate_input = input()
    while invalid_apr(annual_percentage_rate_input):
        prompt(messages["invalid_apr"])
        annual_percentage_rate_input = input()
    # CONVERT APR TO DECIMAL FORMAT
    annual_percentage_rate = float(annual_percentage_rate_input) * .01
    # APR -> MONTHLY INTEREST RATE
    monthly_interest_rate = annual_percentage_rate / 12

    # LOAN DURATION
    prompt(messages["loan_duration"])
    # YEAR(S)
    prompt(messages["years"])
    year_duration = input()
    while invalid_loan_duration(year_duration):
        prompt(messages["invalid_year"])
        year_duration = input()
    year_month_conversion = int(year_duration) * 12
    # MONTH(S)
    prompt(messages["months"])
    month_duration = input()
    while invalid_loan_duration(month_duration):
        prompt(messages["invalid_months"])
        month_duration = input()
    month_duration = int(month_duration)

    loan_duration_months = year_month_conversion + month_duration

    # MONTHLY PAYMENT :
    monthly_payment = loan_amount * (monthly_interest_rate /
    (1 - (1 + monthly_interest_rate) ** (-loan_duration_months)))
    return f'==> Your monthly payment is: ${monthly_payment:.2f}'

print(loan_calc())




    