class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left = left
        self.right= right
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add_node(self,data):
        if self.root is None:
            self.root = BSTNode(data)
            return 
        else:
            self.recursive_add(data,self.root)

    def recursive_add(self,data,node):
        if node.data < data :
            if node is None:
                node = BSTNode(data)
                return
            else:
                self.recursive_add(data,node.left)

        if node.data > data:
            if node is None:
                node = BSTNode(data)
                return
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
        



