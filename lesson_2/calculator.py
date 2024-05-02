# calculator program that will:
    # Ask the user for two numbers.
    # Ask the user for operation to perform: add, subtract, multiply or divide.
    # Perform the calculation and display the results

print('Welcome to Calculator!')

# no error for input/ will crash if input is wrong --> would add error if was function
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))

operation = input('What operation would you like to perform?\n'
                  '1) Addition 2) Subtraction 3) Multiplication 4) Division: ')

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
    case _: # wrong input for operation
        output = ('Error: Did not input operation you want as a number! ' 
                  '(i.e: 1, 2, 3, or 4)')
        
# printing error vs results        
if type(output) != int:
    print(output)
else:
    print(f"The result is {output}")