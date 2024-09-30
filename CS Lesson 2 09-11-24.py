'''
Task 1
Write an algorithm as a function which takes in a string as input. The string needs to be valudated as a password, it must be 8 characters
in length before being passed into the function.

For the password to be:
Weak - All Lowercase Characters
Medium - Weak + 2 Upper Characters
Strong = Medium + 2 Digits
Extra Strong = Medium + 2 Other Characters

Write a Procedure to write password and strength to a file.
'''

def passwordStrength(password):
    strength = ""
    upper, lower, digits, special = 0, 0, 0, 0
    special_characters = "!@#$%^&*()-+?_=,<>/"
    if password.length() >= 8:
        for i in range(len(password)):
            if password[i].islower():
                lower+=1
            elif password[i].isupper():
                upper+=1
            elif password[i].isnumeric():
                digits+=1
            elif password[i] in special_characters:
                special+=1
    else:
        return "Password not long enough"
    
    if special >= 2 and digits >= 2 and upper >= 2:
        strength = (password, upper, lower, digits, special, "Extra Strong")
    elif digits >= 2 and upper >= 2:
        strength = (password, upper, lower, digits, special, "Strong")
    elif upper >= 2:
        strength = (password, upper, lower, digits, special, "Medium")
    else:
        strength = (password, upper, lower, digits, special, "Weak")
    
    with open("strengths.txt", "a") as file:
        file.write(str(strength))
        file.write("\n")
        file.close()
    return strength 

password = input("Enter a password")
print(passwordStrength("DaGoodLookingJuan178@@"))