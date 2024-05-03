
# 2. a function that takes a list of strings, and returns a string that is all those strings 
# concatenated together

# START
# GET list of strings
list = ['hi', 'bye', 'haha', 'fuck']

def add_strings(list):
    # SET length: len(list) + 1
    length = len(list) + 1
    # SET new_string: empty string
    new_string = ''
    # WHILE length --> new_string += string
    for string in list:
        new_string += string
    return new_string
# PRINT new_string
print(add_strings(list))
# END
