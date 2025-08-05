class BSTNode:
    def __init__(self,data):
        self.data =  data
        self.left = None
        self.right = None

class binarySearchTree:
    def __init__(self):
        self.root = None
    
    def add(self,data):
        if self.root is None:
            self.root = BSTNode(data)
    
    def recursive_add(self,data,node):
        if data < node.data:
            if node.left is not None:
                node.left = BSTNode(data)
            else:
                self.recursive_add(data,node.left)

        if data>node.data:
            if node.right is not None:
                node.right = BSTNode(data)
            else:
                self.recursive_add(data,self.right)

BST = binarySearchTree()
BST.add(45)
BST.add(4)
BST.add(78)
BST.add(34)
BST.add(87)
BST.add(23)
BST.add(1)
BST.add(67)
