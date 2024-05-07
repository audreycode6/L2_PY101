'''calculator program that will:
    Ask the user for two numbers.
    Ask the user for operation to perform: add, subtract, multiply or divide.
    Perform the calculation and display the results'''

def prompt(message):
    print(f"==> {message}")

def invalid_input(str_num):
    try:
        int(str_num)
    except ValueError:
        return True
    return False

prompt('Welcome to Calculator!')

# NUM1
prompt('Enter a number!')
num1 = input()
while invalid_input(num1):
    prompt("Error: That isn't a valid number, expecting an integer!")
    num1 = input()
num1 = int(num1) # ugly conversion to int, but following tut they did
# -- def know i can make better

# NUM2
prompt('Enter another number!')
num2 = input()
while invalid_input(num2):
    prompt("Error: That isn't a valid number, expecting an integer!")
    num2 = input()
num2 = int(num2)

# OPERATION
prompt('What operation would you like to perform?:\n'
        '==> 1) Addition 2) Subtraction 3) Multiplication 4) Division')
operation = input()
while operation not in ['1', '2', '3', '4']:
    prompt('You must choose 1, 2, 3, or 4.')
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
    print(output)
else:
    print(f"The result is {output}!")