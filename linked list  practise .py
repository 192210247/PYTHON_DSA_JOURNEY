class node:
    def __init__(self,name):
        self.name = name
        self.pointer = None

class LinkedList :
    def __init__(self):
        self.head = None

    def add(self,data):
        newnode = node(data)
        if self.head == None:
            self.head = newnode
        else:
            cur = self.head
            while cur.pointer is not None:
                cur = cur.pointer
            cur.pointer = newnode

    def remove(self,data):
            if self.head is  not None:
                if (self.head.name == data):
                    self.head = self.head.pointer

                else:
                    cur = self.head
                    while (cur.pointer is not None and cur.pointer.name!=data):
                        cur = cur.pointer
                    cur.pointer = cur.pointer.pointer
    def print_list(self):
        cur = self.head
        if self.head is None:
            print("The list is empty")
        while cur is not None:
            print(cur.name , end=" -> ")
            cur =  cur.pointer
        print("none")

obj1 = LinkedList()
obj1.add(2)
obj1.add(3)
obj1.add(4)
obj1.add(5)
obj1.add(6)
obj1.print_list()
obj1.remove(3)
obj1.print_list()