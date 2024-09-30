'''
# Basic Implementation of a Stack
# Iterate through the Stack
# Check the Length of the Stack
# Push Items on to the Stack
# Pop Items from the Stack
'''


arrayDaLads = ['Maahn', 'Chanul', 'Bilal', 'Sulayman', 'Rohan', 'Yu', 'Haisu', 'Joe', 'Jane', 'Sarah', 'Max', 'Muhammad', 'Imogen']

def iterateStack(stack):
    for stackPointer in range(len(stack)-1, -1, -1):
        print(stack[stackPointer])

def lengthOfStack(stack):
    return len(stack)

#Advance Implementation
def pushItem(stack, item):
    maxLength = 32
    stackPointer = lengthOfStack(stack)
    if lengthOfStack(stack)>=maxLength:
        return "Error - Stack Full"
    else:
        stackPointer+=1
        stack.append(item)
        return stack

def popItem(stack):
    maxLength = 32
    stackPointer = lengthOfStack(stack)
    if lengthOfStack(stack)<=0:
        return "Error - Stack Empty"
    else:
        stackPointer+=1
        stack.pop()
        return stack

iterateStack(arrayDaLads)
print(lengthOfStack(arrayDaLads))

def popAllItems(stack):
    for i in range(lengthOfStack(stack)):
        print(popItem(stack))

def pushManyItems(stack, *args):
    for i in range(len(args)):
        print(pushItem(stack, args[i]))


popAllItems(arrayDaLads)
pushManyItems(arrayDaLads, 'Maahn', 'Chanul', 'Bilal', 'Sulayman', 'Rohan', 'Yu', 'Haisu', 'Joe', 'Jane', 'Sarah', 'Max', 'Muhammad', 'Imogen')


