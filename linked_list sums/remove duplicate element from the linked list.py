class node:
    def __init__(self, name):
        self.name = name
        self.pointer = None

class linkedlist:
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

    def remove_duplicates(self):
        if self.head is None or self.head.pointer is None:
            return  # Nothing to do for empty or single-node list

        cur = self.head
        seen = set()
        seen.add(cur.name)

        while cur.pointer is not None:
            if cur.pointer.name in seen:
                # Skip the duplicate node
                cur.pointer = cur.pointer.pointer
            else:
                seen.add(cur.pointer.name)
                cur = cur.pointer

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.name, end=" -> ")
            cur = cur.pointer
        print("None")

# Create and populate the list
lists = linkedlist()
lists.add("A")
lists.add("b")
lists.add("b")
lists.add("d")
lists.add("A")
lists.add("f")

# Remove duplicates and print result
lists.remove_duplicates()
print("After removing duplicates from the linked list:")
lists.print_list()
