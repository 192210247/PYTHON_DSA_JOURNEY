class node:
    def __init__(self,val):
        self.val = val
        self.next = None

class liss:
    def __init__(self):
        self.head  = None

    def add(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = newnode

    def detecting_cycle(self):
        slow = self.head
        fast =  self.head
        while fast and fast.next:
            slow =  slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
listed = liss()
listed.add(2)
listed.add(3)
listed.add(4)
listed.add(5)
listed.add(2)
listed.add(5)
print(listed.detecting_cycle())

node1 = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

lis = liss()
lis.head = node1
print(lis.detecting_cycle())