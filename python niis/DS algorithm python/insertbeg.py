class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def create(self):
        ch = True
        ptr = None
        while ch:
            ele = int(input("Enter data: "))
            cur = Node(ele)
            if self.head is None:
                self.head = cur
            else:
                ptr.next = cur
            ptr = cur
            ch_input = input("Continue? (yes/no): ").lower()
            ch = True if ch_input == "yes" else False
    def display(self):
        ptr = self.head
        print("List:")
        while ptr:
            print(ptr.data, end=" -> ")
            ptr = ptr.next
        print("None")
    def insertbeg(self, data):
        cur = Node(data)
        cur.next = self.head
        self.head = cur
        print("Inserted at beginning")
# Run program
obj = LinkedList()
obj.create()
obj.display()
obj.insertbeg(5)
obj.display()