from queue import Queue
 
queue = Queue()
class Node:
   def __init__(self, val):
 
       self.leftChild = None
       self.rightChild = None
       self.data = val
 
 
# Insert Node
   def insert(self, data):
       if data is None:
           return
       if self.leftChild is None:
           self.leftChild = Node(data)
           #print(self.data, '-- Left -->', data)
           data = None
       elif self.rightChild is None:     
           self.rightChild = Node(data)
           #print(self.data, '-- Right -->', data)
           data = None
       else:
           queue.put(self.leftChild)
           queue.put(self.rightChild)
 
       while queue.empty() is False:
           queue.get().insert(data)
 
# Print tree
   def printTree(self):
       ret = []
       ret.append(self.data)
       if self.leftChild is not None:
           queue.put(self.leftChild)
       if self.rightChild is not None:
           queue.put(self.rightChild)
 
       #print (len(stack))
       while queue.empty() is False:
           ret = ret + queue.get().printTree() 
       return ret
 
 
# postorder traversal
# leftChild -> rightChild -> parent
   def postorderTraversal(self, root):
       ret = []
       if root:
           ret = ret + self.postorderTraversal(root.leftChild)
           ret = ret + self.postorderTraversal(root.rightChild)
           ret.append(root.data)
       return ret
 
root = Node(27)
root.insert(14)
root.insert(5)
root.insert(10)
root.insert(6)
root.insert(31)
root.insert(9)
print("\n\nData is tree is = ", root.printTree())
 
print("\n\nresult of postorder traversal is = ", root.postorderTraversal(root))