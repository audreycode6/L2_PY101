
# 2. a function that takes a list of strings, and returns a string that is all those strings 
# concatenated together

# START
def add_strings(list):

    # SET new_string: empty string
    new_string = ''
    # WHILE length --> new_string += string
    for string in list:
        new_string += string
    return new_string
# PRINT new_string
# END

# GET list of strings
list = ['hi', 'bye', 'haha', 'fuck']
print(add_strings(list))

