class Queue:
    # First in First Out Structure - Enter from back of array (len(array)) and exit from front of array (0)
    def __init__(self, data=[]):
        self.data = data
    
    def insert(self, data):
        self.data.append(data)
    
    def remove(self):
        self.data.pop(0)

    def printQueue(self):
        print(self.data)

print("\nQueues")
queue = Queue([3,5,6,7,9])

print("Original Queue")
queue.printQueue()

print("\nAdding Items")
queue.insert(4)
queue.printQueue()

print("\nRemoving Items")
queue.remove()
queue.printQueue()

