'''calculator program that will:
    Ask the user for two numbers.
    Ask the user for operation to perform: add, subtract, multiply or divide.
    Perform the calculation and display the results
    Ask user if they wanto continue calculating: 
        Y = start over, N =end program
    
    '''
# ORGANIZE CALC MESSAGES IN DICT
messages = {
'another_calc' : 'Would you like to do another calculation?'
                ' Enter Y to continue OR any other key to stop.',
'bye' : 'See you later!',
'welcome' : 'Welcome to Calculator!',
'num1' : 'Enter a number!',
'num2' : 'Enter another number!',
'num_error' : "Error: That isn't a valid number, expecting an integer!",
'operation': 'What operation would you like to perform?:\n'
            '   1) Addition 2) Subtraction 3) Multiplication 4) Division',
'operation_error' : 'You must choose 1, 2, 3, or 4.'
}

def prompt(message):
    print(f"==> {message}")

def invalid_input(str_num):
    try:
        int(str_num)
    except ValueError:
        return True
    return False

def calc_again():
    prompt(messages.get('another_calc'))
    answer = input()
    if answer.lower() == 'y':
        return calculator()
    return prompt(messages.get('bye'))

def calculator():
    prompt(messages.get('welcome'))

    # NUM1
    prompt(messages.get('num1'))
    num1 = input()
    while invalid_input(num1):
        prompt(messages.get('num_error'))
        num1 = input()
    num1 = int(num1)

    # NUM2
    prompt(messages.get('num2'))
    num2 = input()
    while invalid_input(num2):
        prompt(messages.get('num_error'))
        num2 = input()
    num2 = int(num2)

    # OPERATION
    prompt(messages.get('operation'))
    operation = input()
    while operation not in ['1', '2', '3', '4']:
        prompt(messages.get('operation_error'))
        operation = input()

    match operation:
        case '1': # addition
            output = num1 + num2
        case '2': # subtraction
            output = num1 - num2
        case '3': # multiplication
            output = num1 * num2
        case '4': # division
            if num2 == 0:
                output = 'Error: Cannot divide by zero!'
            else:
                output = num1 / num2

    # PRINT RESULTS
    if isinstance(output, str):
        prompt(output)
    else:
        prompt(f"The result is {output}!")
        # ASK USER IF THEY WANT TO CALC AGAIN
        calc_again()

calculator()