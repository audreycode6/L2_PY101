
# 4. a function that determines the index of the 3rd occurrence of a given character in a string. 
# For instance, if the given character is 'x' and the string is 'axbxcdxex', the function should 
# return 6 (the index of the 3rd 'x'). If the given character does not occur at least 3 times, 
# return None.

# START
# GET string, char
string = input('Enter a word or phrase: ')
char = input('Enter a character from your word/phrase: ')
def find_3rd_char(string, char):
# IF/ELIF/ ElSE: 
#     if count(char) < 3 return None
    if string.count(char) < 3: 
        return None
#     else:
    else:
#     SET counter:0
#     SET index:0
        counter = 0
        index = 0
#     WHILE: len(string)+1, if element == char --> counter += 1 and index = element
        for element in string:
            index += 1
            if element == char:
                counter += 1
#     if counter == 3 return index
                if counter == 3:
                    return index - 1
# END
print(find_3rd_char(string, char))
