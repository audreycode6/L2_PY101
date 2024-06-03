'''Print a new version of the sentence given by
advice that ends just before the word house.
Don't worry about spaces or punctuation: remove 
everything starting from the beginning of house 
to the end of the sentence.'''

advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

house_index = advice.find('house')
print(house_index) # 39
print(advice[:39]) # slice start to before house
# OR
print(advice.split("house")[0])

'''Print the following string with the word important replaced by urgent:
'''
advice1 = "Few things in life are as important as house training your pet dinosaur."
print(advice1.replace('important', 'urgent'))