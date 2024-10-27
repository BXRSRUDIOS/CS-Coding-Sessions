class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
            if self.right is None:
               self.right = Node(data)
            else:
               self.right.insert(data)
         else:
            self.data = data

   def printTree(self):
      if self.left:
         self.left.printTree()
      print( self.data),
      if self.right:
         self.right.printTree()

   def preOrderTraversal(self, root):
    res = []
    if root:
        res.append(root.data)
        res = res + self.preOrderTraversal(root.left)
        res = res + self.preOrderTraversal(root.right)
    return res
   
   def postOrderTraversal(self, root):
    res = []
    if root:
        res = res + self.postOrderTraversal(root.left)
        res = res + self.postOrderTraversal(root.right)
        res.append(root.data)
    return res
   
   def inOrderTraversal(self, root):
    res = []
    if root:
        res = res + self.inOrderTraversal(root.left)
        res.append(root.data)
        res = res + self.inOrderTraversal(root.right)
    return res
   

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.printTree()
print(root.preOrderTraversal(root))
print(root.postOrderTraversal(root))
print(root.inOrderTraversal(root))