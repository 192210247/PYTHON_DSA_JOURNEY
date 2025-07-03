class node:
    def __init__(self,name):
        self.name =  name
        self.pointer = None
class linkedlist:
    def __init__(self):
        self.head = None

    def add(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
        else:
            cur = self.head
            while cur.pointer is not None:
               cur =  cur.pointer
            cur.pointer = newnode
    def middle_element(self):
        slow = self.head
        fast = self.head
        while fast and fast.pointer:
            slow = slow.pointer
            fast = fast.pointer.pointer
        if slow:
            return slow.name
        else:
            return None

lists = linkedlist()
lists.add("A")
lists.add("b")
lists.add("c")
lists.add("d")
lists.add("e")
lists.add("f")
print("The middle element in the linked list is  ",lists.middle_element())
