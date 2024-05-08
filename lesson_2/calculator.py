'''calculator program that will:
    Ask the user for two numbers.
    Ask the user for operation to perform: add, subtract, multiply or divide.
    Perform the calculation and display the results
    Ask user if they wanto continue calculating: 
        Y = start over, N =end program
    Internationalize the calc_messages.json
    '''
import json
with open('calc_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# DEFAULT LANGUAGE FOR MESSAGES: 'es', 'fr', OR 'en'
LANGUAGE = 'es'

def messages(message, lang='en'):
    return MESSAGES[lang][message]

def prompt(key):
    message = messages(key, LANGUAGE)
    print(f"==> {message}")

def invalid_input(str_num):
    try:
        int(str_num)
    except ValueError:
        return True
    return False

def calc_again():
    prompt('another_calc')
    answer = input()
    if answer.lower() == 'y':
        return calculator()
    return prompt('bye')

def calculator():
    prompt('welcome')

    # NUM1
    prompt('num1')
    num1 = input()
    while invalid_input(num1):
        prompt('num_error')
        num1 = input()
    num1 = int(num1)

    # NUM2
    prompt('num2')
    num2 = input()
    while invalid_input(num2):
        prompt('num_error')
        num2 = input()
    num2 = int(num2)

    # OPERATION
    prompt('operation')
    operation = input()
    while operation not in ['1', '2', '3', '4']:
        prompt('operation_error')
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
                output = "Error"
            else:
                output = num1 / num2

    # PRINT RESULTS
    if isinstance(output, str):
        prompt('zero_error')
    else:
        prompt('result')
        print(f'    {output}')

        # ASK USER IF THEY WANT TO CALC AGAIN
        calc_again()

calculator()