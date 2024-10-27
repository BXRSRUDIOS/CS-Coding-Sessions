# Circular Queue Programming

arrayDaLads = ['Maahn', 'Chanul', 'Bilal', 'Sulayman', 'Rohan', 'Yu', 'Haisu', 'Joe', 'Jane', 'Sarah', 'Max', 'Muhammad', 'Imogen']
headPointer = 0
tailPointer = len(arrayDaLads)


# Create a function to check the queue size
def checkQueueSize(queue):
    return len(queue)

# Check queue is empty function
def checkQueueEmpty(queue, hP, tP):
    return tP==hP

#print(checkQueueSize(arrayDaLads))
#print(checkQueueEmpty(arrayDaLads, headPointer, tailPointer))

# Add Items to the Queue
def addItemQueue(queue, item, tP):
    queue.insert(tP, item)
    tP+=1
    return queue

# Remove Items from the Queue
def removeItemQueue(queue, hP, tP):
    if checkQueueEmpty(queue, hP, tP):
        return False
    else:
        queue.pop(hP)
        hP+=1
        return queue
    
#print(addItemQueue(arrayDaLads, "bxrr23", tailPointer))
#print(removeItemQueue(arrayDaLads, headPointer, tailPointer))
#print(removeItemQueue(arrayDaLads, headPointer, tailPointer))
#print(removeItemQueue(arrayDaLads, headPointer, tailPointer))

# Create this as a class
class Queue:
    def __init__(self, queue, headPointer, tailPointer):
        self.queue = queue
        self.headPointer = headPointer
        self.tailPointer = tailPointer

    def checkQueueSize(self):
        return len(self.queue)

    def checkQueueEmpty(self):
        return self.headPointer == self.tailPointer
    
    def addItemToQueue(self, item):
        self.queue.append(item)
        return self.queue
    
    def removeItemFromQueue(self):
        if self.checkQueueEmpty():
            return False
        else:
            self.queue.pop(self.headPointer)
            return self.queue
    
    def printQueue(self):
        print(self.queue)

queue = Queue(arrayDaLads, headPointer, tailPointer)

print(queue.checkQueueSize())
print(queue.checkQueueEmpty())
print(queue.addItemToQueue("bxrr23"))

'''
for i in range(queue.checkQueueSize()):
    queue.removeItemFromQueue()
    queue.printQueue()
'''
for j in range(queue.checkQueueSize()):
    queue.addItemToQueue("Chanul")
    queue.printQueue()