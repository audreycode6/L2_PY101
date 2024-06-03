'''Determine whether the following dictionary of
people and their age contains an entry for 'Spot':'''
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

# dict.get()_ method
print(ages.get('Spot', 'No Spot :('))

#OR use 'in' 
print('Spot' in ages)