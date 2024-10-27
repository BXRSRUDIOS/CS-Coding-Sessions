# You don't need OOP to implement Stacks & Queues but I used it here

class Stack:
    # Last In First Out Structure - Enter from bottom of Array (len(array)) and Exit from Start of Array (len=0)
    def __init__(self, data=[]):
        self.data = data
    
    def insert(self, data):
        self.data.append(data)
    
    def remove(self):
        self.data.pop(0)

    def printStack(self):
        print(self.data)

print('Stacks')
stack = Stack([3,5,6,7,9])

print("Original Stack")
stack.printStack()

print("\nAdding Items")
stack.insert(4)
stack.printStack()

print("\nRemoving Items")
stack.remove()
stack.printStack()

class Queue:
    # First in First Out Structure - Enter from 
    def __init__(self, data=[]):
        self.data = data
    
    def insert(self, data):
        self.data.append(data)
    
    def removeLeft(self):
        self.data.pop(0)
    
    def removeRight(self):
        self.data.pop(len(self.data)-1)

    def printQueue(self):
        print(self.data)

print("\nQueues")
queue = Queue([3,5,6,7,9])

print("Original Queue")
queue.printQueue()

print("\nAdding Items")
queue.insert(4)
queue.printQueue()

print("\nRemoving Items from Left Queue")
queue.removeLeft()
queue.printQueue()

print("\nRemoving Items from Right of Queue")
queue.removeRight()
queue.printQueue()