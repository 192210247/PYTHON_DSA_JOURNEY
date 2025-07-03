class node:
    def __init__(self,name):
        self.name = name
        self.pointer = None
class linked_list:
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
    def printed(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            cur = self.head
            while cur is not None:
                print(cur.name ,end=" -> ")
                cur = cur.pointer
            print("None")
linedlist = linked_list()
linedlist.add(2)
linedlist.add(3)
linedlist.add(4)
linedlist.add(5)
linedlist.add(6)
linedlist.printed()