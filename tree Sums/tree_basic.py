class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

class TreeStructure:
    def __init__(self):
        self.root = None

    def addnode(self, data, parentnode=None):
        node = TreeNode(data)


        if not self.root:
            self.root = node
            return

        parent = self.findparent(self.root, parentnode)

        if parent:
            parent.children.append(node)
        else:
            print(f"Parent '{parentnode}' not found. Node '{data}' not added.")

    def findparent(self, cur, parentnode):
        if cur.name == parentnode:
            return cur

        for child in cur.children:
            nodefound = self.findparent(child, parentnode)
            if nodefound:
                return nodefound
        return None

    def printtree(self, node=None, level=0):
        if node is None:
            node = self.root
        print(' ' * level * 4 + str(node.name))
        for child in node.children:
            self.printtree(child, level + 1)

tree = TreeStructure()
tree.addnode(5)
tree.addnode(7, 5)
tree.addnode(8, 5)
tree.addnode(9, 7)
tree.addnode(11,7)
tree.addnode(10, 8)
tree.addnode(12,7)

tree.printtree()
