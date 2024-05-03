
# 3. a function that takes a list of integers, and returns a new list with every other element from 
# the original list, starting with the first element. For instance: every_other([1,4,7,2,5]) 
# # => [1,7,5]

# START
# GET list_ints: list of ints 
list = [1, 2, 3, 4]
def every_other_element(list):
# SET: new_list : []
    new_list = []
# WHILE: for list_element in range(::2) -->new_list.append(list_element)
    for element in range(1, len(list) + 1, 2):
        new_list.append(element)
# PRINT new_list
    return new_list
# END
print(every_other_element(list))

