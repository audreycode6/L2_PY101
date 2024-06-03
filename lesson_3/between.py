'''Programmatically determine whether 42 lies between 10 and 100,
inclusive. Do the same for the values 100 and 101,
'''
print(10 <= 42 <= 100) # True
print(10 <= 100 <= 100) # True
print(10 <= 101 <= 100) # False

# OR use range
print(42 in range(10, 101)) # True
print(100 in range(10, 101)) # True
print(101 in range(10, 101)) # False
