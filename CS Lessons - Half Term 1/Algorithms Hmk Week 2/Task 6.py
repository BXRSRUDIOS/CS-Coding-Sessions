'''
Task 6
Congratulations you have a baby brother arrived yesterday and in a fit of madness your parents have decided to name him using 
the last 3 letters of your first name, 3 letters selected at random and then the last 3 characters of your surname, 
they also want to stick at the end 3 random numbers between 0 and 9 for good measure.

Write an algorithm as a function to return the new name.
This will involve using string slicing, the function must have parameters passed in.
Adapt your algorithm to produce 3 random names
'''

import random

# Initialise names to store 3 random names & letters to store all the random letters
names = []
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Create 3 baby names
for i in range(0,3):
    fName = input(f"Enter first name {i+1}")
    sName = input(f"Enter surname {i+1}")

    babyName = fName[-3:]
    for j in range(0,3):
        babyName += letters[random.randint(0, len(letters)-1)]
    babyName = babyName + sName[-3:] + str(random.randint(100,999))
    
    names.append(babyName)
print(names)