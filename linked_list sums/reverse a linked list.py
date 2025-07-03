class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
        else:
            cur = self.head
            while cur.pointer:
                cur = cur.pointer
            cur.pointer = newnode

    def reverse(self):
        prev = None
        current = self.head
        while current:
            temp = current.pointer
            current.pointer = prev
            prev = current
            current = temp
        self.head = prev

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.pointer
        print("None")

# Example usage:
ll = LinkedList()
for val in ['A', 'B', 'C', 'D']:
    ll.add(val)

print("Original:")
ll.print_list()

ll.reverse()

print("Reversed:")
ll.print_list()
