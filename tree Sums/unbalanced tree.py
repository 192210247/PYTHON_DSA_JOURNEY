class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self, data):
        newnode = Node(data)
        if self.root is None:
            self.root = newnode
        else:
            self.recursive_add(self.root, newnode)

    def recursive_add(self, current, newnode):
        if current.left is None:
            current.left = newnode
        elif current.right is None:
            current.right = newnode
        else:
            self.recursive_add(current.left, newnode)

    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        if node is not None:
            print(" " * 4 * level + str(node.data))
            self.display(node.left, level + 1)
            self.display(node.right, level + 1)

tree = Tree()
tree.add(5)
tree.add(6)
tree.add(7)
tree.add(8)
tree.add(9)
tree.add(0)
tree.add(1)
tree.add(2)

tree.display()
