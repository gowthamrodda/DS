
# A simple tree structure with four children
class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

root = Node(1)

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)