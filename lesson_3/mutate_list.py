'''Given a list of numbers [1, 2, 3, 4, 5],
mutate the list by removing the number at index 2,
so that the list becomes [1, 2, 4, 5].'''

num = [1, 2, 3, 4, 5]
num.pop(2) # remove index provided in arg

#OR
# del num[2]

print(num) # [1, 2, 4, 5]


'''How would you verify whether the data structures
assigned to the variables numbers and table are of type list?'''

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
print(type(numbers)) # <class 'list'>
print(type(table)) # <class 'dict'>
 # OR PREFERREed solution: isinstance
print(isinstance(numbers, list))
print(isinstance(table, list))