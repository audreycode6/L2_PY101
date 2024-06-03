'''Starting with the string:
Show two different ways to create a new string
with "Four score and " prepended to the front of the string.
'''
famous_words = "seven years ago..."
start =  "Four score and "

interpolate_string = f'{start}{famous_words}' # string interpolation with f string
concatenate_stirng = start+famous_words # string concatenation

print(interpolate_string)
print(concatenate_stirng)