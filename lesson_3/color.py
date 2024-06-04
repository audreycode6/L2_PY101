'''The following function unnecessarily uses two 
return statements to return boolean values. 
Can you rewrite this function so it only has one
return statement and does not explicitly use either
True or False? Try to come up with two different solutions.'''

# def is_color_valid(color):
#     if color == "blue" or color == "green":
#         return True
#     else:
#         return False

# OPTION 1: using == to check if color is == to blue or green
# def is_color_valid(color):
#     return color == "blue" or color == "green"

#OPTION 2: OR list of valid colors and check that arg is in list
def is_color_valid(color):
    valid_color = ['blue', 'green']
    return color in valid_color
#cleaner: return color in ['blue', 'green']




print(is_color_valid('red'))
print(is_color_valid('blue'))

