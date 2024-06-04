'''Write two different ways to remove all of
the elements from the following list:'''

numbers = [1, 2, 3, 4]

#clear method: removes all elems from sequence
numbers.clear()

# OR while loop using remove to remove 1st index
# while numbers:
#     numbers.remove(numbers[0])

#OR using pop()
# while numbers:
#     numbers.pop()

# OR reassign to empty list (?)
# numbers = [] 

print(numbers)
