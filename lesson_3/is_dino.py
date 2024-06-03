'''Determine whether the name Dino appears in the strings below
-- check each string separately:'''

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

def is_dino(string):
    print('Dino' in string)

is_dino(str1)
is_dino(str2)

'''How can we add the family pet, "Dino", to the following list?'''
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append("Dino")

'''How can we add multiple items to our list
(e.g., 'Dino' and 'Hoppy')? Replace the call 
to append with another method invocation.
'''
print(flintstones + ["Dino", "Hoppy"])
# OR
# flintstones.extend("Dino", "Hoppy")
