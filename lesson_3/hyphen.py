'''Let's do some "ASCII Art": a stone-age form of nerd
artwork from back in the days before computers had 
video screens. For this practice problem, write a
program that outputs The Flintstones Rock!
10 times, with each line prefixed by one more
hyphen than the line above it. The output should start out like this:
-The Flintstones Rock!
--The Flintstones Rock!
---The Flintstones Rock!
    ...
'''

def add_10_hyphens(string):
    count = 1
    for _ in range(10):
        hyphen_count = "-" * count
        print(hyphen_count + string)
        count += 1
    
add_10_hyphens("The Flintstones Rock!")

# OR cleaner: use for loop index
def add_10_hyphen(string):
    for num in range(1,11):
        hyphen_count = "-" * num
        print(hyphen_count + string)
 
add_10_hyphen("The Flintstones Rock!")