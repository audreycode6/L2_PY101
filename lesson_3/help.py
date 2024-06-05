'''Ben was tasked to write a simple Python function
to determine whether an input string is an IP
address using 4 dot-separated numbers, e.g., 10.4.5.11.
Alyssa supplied Ben with a function named is_an_ip_number.
It determines whether a string is a numeric string between
0 and 255 as required for IP numbers and asked Ben to use it.
Here's the code that Ben wrote:
Alyssa reviewed Ben's code and said, 
"It's a good start, but you missed a few things.
You're not returning a false condition, and you're
not handling the case when the input string has more
or less than 4 components, e.g., 4.5.5 or 1.2.3.4.5:
both those values should be invalid."
Help Ben fix his code.
'''
def is_an_ip_number(string):
    '''Alyssa's code'''
    try:
        num = int(string)
        if num in range(0,256):
            return True
        else:
            return False
    except ValueError:
        return False
    

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False
    for string in dot_separated_words:
        if not is_an_ip_number(string):
            return False
    return True

print(is_dot_separated_ip_address("10.4.5.11")) # T
print(is_dot_separated_ip_address("1.2.3.4.5")) # F
print(is_dot_separated_ip_address("4.5.5")) # F
print(is_dot_separated_ip_address("4.544.5.")) # F
print(is_dot_separated_ip_address("4.54.5.")) # F
print(is_dot_separated_ip_address("4.54.5.255")) # T
