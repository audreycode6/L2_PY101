'''Alan wrote the following function, which was
intended to return all of the factors of number:
Alyssa noticed that this code would fail when the
input is a negative number, and asked Alan to
change the loop. How can he make this work?
Note that we're not looking to find the factors
for negative numbers, but we want to handle it
gracefully instead of going into an infinite loop.
'''
# Bonus Question: What is the purpose of number % divisor == 0 in that code?
    # if number / by divisor == 0 then that means that divisor is a factor
    # factors are numbers that are multiples of a number, 
    # meaning the (divisor)factor multipled by another number will = number
    # if the number divided by the divisor != 0 that means that divisor 
    # doesnt evenly mulitiply to make that number, 
    # and if factor or not we minus 1 from the divisor the list
    # and continue to search for factors

def factors(number):
    if number == 0:
        return None
    if number < 0:
        return 'Error: expecting postive number, please try again.'
        # number = abs(number) would need to return result postive and negative
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors(0))
print(factors(7))
print(factors(-20))
print(factors(-3))