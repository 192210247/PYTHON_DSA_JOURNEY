class Node:
    def __init__(self, name):
        self.name = name
        self.pointer = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            cur = self.head
            while cur.pointer is not None:
                cur = cur.pointer
            cur.pointer = newnode

    def search(self, data):
        cur = self.head
        while cur is not None:
            if cur.name == data:
                return True
            cur = cur.pointer
        return False

link = LinkedList()
link.add(2)
link.add(3)
link.add(4)
link.add(5)

print(link.search(4))   
print(link.search(10))  
