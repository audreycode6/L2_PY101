
# 3. a function that takes a list of integers, and returns a new list with every other element from 
# the original list, starting with the first element. For instance: every_other([1,4,7,2,5]) 
# # => [1,7,5]

# START

def every_other_element(list):
# SET: new_list : []
    new_list = []
    index = 0
# WHILE: for list_element in range(::2) -->new_list.append(list_element)
    for element in list:
        if index % 2 == 0:
            new_list.append(element)
            index += 1
        else:
            index += 1
            continue
        
# PRINT new_list
    return new_list
# END

# GET list_ints: list of ints 
# list = [0, 1, 2, 3, 4] # =>[0,2,4]
list = [1,4,7,2,5]  # => [1,7,5]
print(every_other_element(list))

