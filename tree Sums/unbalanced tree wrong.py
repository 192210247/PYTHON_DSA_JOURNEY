class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def addnode(self, data):
        newnode = Node(data)
        if not self.root:
            self.root = newnode
        else:
            self.recursive_add(self.root, newnode)

    def recursive_add(self, current, newnode):
        if current.left is None:
            current.left = newnode
        elif current.right is None:
            current.right = newnode
        else:
            # Always try adding to the left subtree first (unbalanced)
            self.recursive_add(current.left, newnode)

    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        if node is not None:
            print(" " * 4 * level + str(node.name))
            self.display(node.left, level + 1)
            self.display(node.right, level + 1)

# Create tree and add nodes
Tree = BinaryTree()
Tree.addnode(5)
Tree.addnode(1)
Tree.addnode(3)
Tree.addnode(2)
Tree.addnode(7)
Tree.addnode(9)

# Display the tree
Tree.display()
