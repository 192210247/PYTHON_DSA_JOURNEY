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
        else:
            self.recursive_add(data,self.root)
    
    def recursive_add(self,data,node):
        if data < node.data:
            if node.left is  None:
                node.left = BSTNode(data)
            else:
                self.recursive_add(data,node.left)

        if data>node.data:
            if node.right is  None:
                node.right = BSTNode(data)
            else:
                self.recursive_add(data,node.right)
    
    def display(self):
        result =[]
        self.inorderTraversal(self.root,result)
        print(result)

    def inorderTraversal(self,node,result):
        if node is None:
            return None
        else:
            self.inorderTraversal(node.left,result)
            result.append(node.data)
            self.inorderTraversal(node.right,result)


BST = binarySearchTree()
BST.add(45)
BST.add(4)
BST.add(78)
BST.add(34)
BST.add(87)
BST.add(23)
BST.add(1)
BST.add(67)
BST.display()
