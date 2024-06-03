'''Write two distinct ways of reversing the list
without mutating the original list.'''

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

#reversed() built in function
new_list = list(reversed(numbers))
print(new_list)

# OR retrieves numbers index backwards : slicing
print(numbers[::-1])
# _________________________________________________

# OR (pretty much above) in list append numbers backwards to new list
reverse_list = []
for number in numbers[::-1]:
    reverse_list.append(number)
print(reverse_list)

# OR use range to get sequence of numbers and using -1  step to go backwards
reverse_numbers = list(range(5, 0, -1))
print(reverse_numbers)

print(numbers) # check numbers is unchanged

