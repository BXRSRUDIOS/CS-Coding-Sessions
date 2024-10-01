'''
Task 8
Write a function as an algorithm which is going to take in a string message and output the ASCII characters of that message. 
Adapt the algorithm so that it adds on 2 to the ASCII value and outputs that value
'''
strMessage = input("Enter a message")

for i in range(len(strMessage)):
    ascValue = ord(strMessage[i])
    ascValue2 = ascValue+2
    print(f"The ASCII Value of {strMessage[i]} is {ascValue} or {ascValue2} if you add 2 to it")