'''Given a number and a list, determine whether the number
is included in the list. '''

numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]
number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

def in_list(number, list):
    print(number in list)

in_list(number1, numbers)
in_list(number2, numbers)