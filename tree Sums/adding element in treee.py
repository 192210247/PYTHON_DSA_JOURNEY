class TreeNode:
    def __init__(self,name):
        self.name = name
        self.children = []

class Tree:
    def __init__(self):
        self.root = None

    def add_element(self,data,parentnode=None):
        newnode = TreeNode(data)

        if not self.root:
            self.root = newnode
            return 

        parent = self.finding_parent(self.root,parentnode)

        if parent:
            parent.children.append(newnode)
        else:
            print("The parent not found and the data is not added")
    
    def finding_parent(self,cur,parentnode):
        if cur.name == parentnode:
            return cur
        for child in cur.children :
            nodefound = self.finding_parent(child,parentnode)
            if nodefound :
                return nodefound
        return None

    def print_tree(self,node=None , level = 0 ):
        if node is None:
            node = self.root
        print(" "*level*4 +str(node.name))
        for child in node.children:
            self.print_tree(child,level+1)
tree = Tree()
tree.add_element(5)
tree.add_element(7, 5)
tree.add_element(8, 5)
tree.add_element(9, 7)
tree.add_element(11,7)
tree.add_element(10, 8)
tree.add_element(12,7)

tree.print_tree()