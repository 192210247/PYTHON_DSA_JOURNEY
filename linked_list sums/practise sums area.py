class node:
    def __init__(self,name):
        self.name = name
        self.pointer = None

class linklist:
    def __init__(self):
        self.head = None
    
    def add_element(self,data):
        newnode = node(data)

        if not self.head :
            self.head = newnode
            return
        
        cur = self.head
        while cur.pointer is not None:
            cur = cur.pointer
        cur.pointer =  newnode
        return 
    def remove_element(self,data):
        if self.head :
            if(self.head.name ==  data):
                self.head = self.head.pointer
                return

            cur = self.head
            while cur is not None and cur.pointer.name !=data:
                cur = cur.pointer
            cur.pointer = cur.pointer.pointer
    def  printlist(self):
        cur = self.head
        if not cur:
            print("The linked list is empty")
        while cur :
            print(cur.name ,end ="->")
            cur = cur.pointer
        print("None")
lists = linklist()
'''lists.add_element(3)
lists.add_element(4)
lists.add_element(5)
lists.add_element(6)
lists.add_element(7)
lists.add_element(8)
lists.add_element(9)'''
lists.printlist()



