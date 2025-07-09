class node:
    def __init__(self,name):
        self.name = name
        self.children = []

class TreeStructure:
    def __init__(self):
        self.root = None
    
    def Add_element(self, data, parentnode=None):
        newnode = node(data)

        if self.root is None:
            self.root = newnode
            return

        parent = self.finding_parent(self.root , parentnode)

        if parent:
            parent.children.append(newnode)
        else:
            print("The parent node is not found and the data is not added")
    
    def finding_parent(self,cur,parentnode):
        if cur.name  == parentnode:
            return cur
        for child in cur.children:
            nodefound = self.finding_parent(child,parentnode)
            if nodefound :
                return nodefound
        return None

        
    def remove(self,data):
        if not self.root:
            print("The tree is empty")
            return 
        if self.root.name == data:
            self.root = None

        parent = self.findParentNode(data,self.root)
        
        if parent:
            for child in parent.children:
                if child.name ==  data:
                    parent.children.remove(child)
                    return 

    #finding parentnode is important because the children is stored as a list.. for traversing to the nextnode ,parentnode needed
    # in add function we directing giving parent value as argument now only by using data we are finding parentnode..

    def findParentNode(self, data, node):
        for child in node.children:
            if child.name== data:
                return node
            nodefound = self.findParentNode(data,child)
            if nodefound:
                return nodefound
        return None


    def print_tree(self, node=None, level =0):
        if node is None:
            node = self.root
        print(" " *level* 4 + str(node.name))
        for child in node.children:
            self.print_tree(child,level + 1)

tree = TreeStructure()         
tree.Add_element(5)
tree.Add_element(7, 5)
tree.Add_element(8, 5)
tree.Add_element(9, 7)
tree.Add_element(11,7)
tree.Add_element(10, 8)
tree.Add_element(12,7)

tree.remove(8)
tree.remove(12)

tree.print_tree()
