'''Write a one-liner to count the number of
lower-case t characters in each of the 
following strings:'''
statement1 = "The Flintstones Rock!" # 3
statement2 = "Easy come, easy go." # 0

print(statement1.count('t'))

# OR IF not checking lower
#.lower() == ensure string same case and .count('t') == count instances of 't'
print(statement1.lower().count('t'))
print(statement2.lower().count('t'))