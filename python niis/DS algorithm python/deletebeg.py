class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        ch = True
        c = 0
        ptr = None

        while ch:
            c += 1
            print("Enter node", c, "data:")
            ele = int(input())

            cur = Node(ele)

            if self.head is None:
                self.head = cur
            else:
                ptr.next = cur

            ptr = cur

            print("Do you want to continue? (yes/no)")
            ch_input = input().lower()
            ch = True if ch_input == "yes" else False

    def display(self):
        print("Elements are:")
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end=" -> ")
            ptr = ptr.next
        print("None")

    def insertbeg(self, data):
        cur = Node(data)
        cur.next = self.head
        self.head = cur
        print("Data inserted at beginning")

    # ✅ Delete from beginning
    def deletebeg(self):
        if self.head==None:
            print("no element")
            return
        print("delete element=",self.head.data)
        self.head= self.head.next
        self.head.prev=None
# Run program
obj = DLinkedList()
obj.create()
obj.displayf()
obj.deletebeg()
obj.displayf()
obj.displayb()