'''How can you determine whether a given string
ends with an exclamation mark (!)?
Write some code that prints True or False depending
on whether the string ends with an exclamation mark. '''

def is_exclamation(string):
    if '!' in string:
        print(True)
    else:
        print(False)

str1 = "Come over here!"  # True 
str2 = "What's up, Doc?"  # False

is_exclamation(str1)
is_exclamation(str2)
# OR
print(str1.endswith('!'))
print(str2.endswith('!'))
# OR
print(str1[-1] == '!')
print(str2[-1] == '!')