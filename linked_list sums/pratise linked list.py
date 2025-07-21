class node:
    def __init__(self,name):
        self.name = name
        self.pointer = None

class linked_list:
    def __init__(self):
        self.head = None
    def add_element(self,data):
        newnode = node(data)

        if not self.head:
            self.head = newnode
            return
        cur = self.head
        while cur.pointer is not None:
            cur = cur.pointer
        cur.pointer = newnode
        return 
    
    def remove_element(self,data):
        if self.head == data:
            self.head = None
        else :
            cur = self.head
            while cur is not None and cur.pointer.name !=data:
                cur = cur.pointer
            cur.pointer = cur.pointer.pointer
    def print_element(self):
        cur = self.head
        while cur is not None:
            print(cur.name, end =" -> ")
            cur = cur.pointer
        print("None")
lis = linked_list()
lis.add_element(1)
lis.add_element(2)
lis.add_element(3)
lis.add_element(4)
lis.print_element()

lis.remove_element(2)
lis.print_element()
