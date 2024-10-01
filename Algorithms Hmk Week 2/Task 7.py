'''
Task 7
Write a function as an algorithm which is going to capitalise each second letter of a string message entered.  
The function must input each character and iterate through a loop. 
'''

strMessage = input("Enter a message")
newMessage = "" 
for i in range(len(strMessage)):
    if i % 2 == 1:
        newMessage += (strMessage[i].capitalize())
    else:
        newMessage += (strMessage[i])

print(newMessage)
