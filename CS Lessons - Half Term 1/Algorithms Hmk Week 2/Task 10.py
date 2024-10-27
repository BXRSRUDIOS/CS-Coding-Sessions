'''
Task 10
Write an algorithm which is going to ask the user to enter a string as a password. 
The algorithm should output the number of upper and lower case characters, as well as number characters and other characters used. 
The password must have at least 1 uppercase, 1 lowercase, 1 number character and 1 other character to be a valid password entered.
'''

password = input("Enter a message")
upper, lower, special, numeric = 0, 0, 0, 0
special_characters = "!@#$%^&*()-+?_=,<>/"
for i in range(len(password)):
    if password[i].isupper():
        upper+=1
    elif password[i].islower():
        lower+=1
    elif password[i].isnumeric():
        numeric+=1
    elif password[i] in special_characters:
        special+=1

if upper >= 1 and lower >= 1 and numeric >= 1 and special >= 1:    
    print(f"Number of Upper Case Characters: {upper}. Number of Lower Case Characters: {lower}.")
    print(f"Number of Number Characters: {numeric}. Number of Special Characters: {special}.")
    print("VALID PASSWORD")
else:
    print(f"Number of Upper Case Characters: {upper}. Number of Lower Case Characters: {lower}.")
    print(f"Number of Number Characters: {numeric}. Number of Special Characters: {special}.")
    print("NOT VALID PASSWORD")