'''
Task 9
Write an algorithm which is going to take a string value, the algorithm should output the amount of lower- and upper-case characters 
contained within the string value.
'''

strMessage = input("Enter a message")
upper, lower = 0, 0
for i in range(len(strMessage)):
    if strMessage[i].isupper():
        upper+=1
    elif strMessage[i].islower():
        lower+=1

print(f"Number of Upper Case Characters: {upper}. Number of Lower Case Characters: {lower}.")