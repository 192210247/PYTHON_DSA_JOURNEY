class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.pointer = self.head
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.pointer is not None:
            cur = cur.pointer
        cur.pointer = new_node

    # Insert at a given position (0-based index)
    def insert_at_position(self, position, data):
        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        cur = self.head
        count = 0

        # Traverse to node before the desired position
        while cur is not None and count < position - 1:
            cur = cur.pointer
            count += 1

        if cur is None:
            print("Position out of bounds")
            return

        new_node.pointer = cur.pointer
        cur.pointer = new_node

    # Print the linked list
    def print_list(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.pointer
        print("None")


# Testing the LinkedList
ll = LinkedList()

# Insert at end
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

# Insert at beginning
ll.insert_at_beginning(5)

# Insert in middle (position = 2)
ll.insert_at_position(2, 15)

# Insert in middle (position = 4)
ll.insert_at_position(4, 25)

# Print final list
ll.print_list()
