class node:
    def __init__(self,data):
        self.data = data
        self.children = []
class tree:
    def __init__(self):
        self.root = None
    
    def add_node(self, data, parentnode = None):
        newnode = node(data)

        if not self.root:
            self.root = newnode
            return 
        
        parent =  self.findnode(self,parentnode,self.root)

        if parent:
            parent.children.append(newnode)
        else:
            print("The parentnode  is not found ")

        
    def findnode(self,data,node):
        if node.data == data:
            return node
        
        for  child in children :
            node_found = self.findnode(self,data,child)
            if  node_found :
                return node_found
            return None

