'''height if the tree'''

class Node:
    def __init__ (self,data):
        self.data = data
        self.left = None
        self.right = None
        
def identical(a,b):
    if a is None and b is None:
        return True
        
    elif a is not None and b is not None:
        return ((a.data)==(b.data)) and identical(a.left,b.left) and identical(a.right,b.right)
        
    else:
        return False
        
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)

root2 = Node(4)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)

if __name__ == "__main__":
  if identical(root1, root2):
      print("Both trees are identical")
  else:
      print("Trees are not identical")    
