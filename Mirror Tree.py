class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def mirror(node):
    if node is None:
        return None

    # Swap the left and right subtrees
    node.left, node.right = node.right, node.left
    
    # Recursively mirror the left and right subtrees
    mirror(node.left)
    mirror(node.right)
    return node

def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data, end=" ")
    in_order_traversal(node.right)

# Creating the tree with the expected structure
#       1
#      / \
#     2   3
#    / \
#   4   5
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

print("Original tree (in-order traversal):")
in_order_traversal(root1)
print()

mirror(root1)

print("Mirrored tree (in-order traversal):")
in_order_traversal(root1)
print()
