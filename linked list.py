class node:
    def __init__(self, name):
        self.name = name
        self.pointer = None  

class Linked_list:
    def __init__(self):
        self.head = None

    def add(self, data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
        else:
            cur = self.head
            while cur.pointer is not None:
                cur = cur.pointer
            cur.pointer = newnode

    def print(self):  
        cur = self.head
        while cur is not None:
            print(cur.name, end=" -> ")
            cur = cur.pointer
        print("None")


linkedlist = Linked_list()
linkedlist.add(2)
linkedlist.add(4)
linkedlist.print()
