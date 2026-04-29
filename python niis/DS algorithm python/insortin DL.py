# Linked List Create and Display using OOP Concept
class Node:
    def __init__(self, ele):   # ✅ fixed
        self.prev = None
        self.data = ele
        self.next = None


class DLinkedList:
    def __init__(self):   # ✅ fixed
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
                cur.prev = ptr   # ✅ link backward

            ptr = cur

            print("Do you continue? (yes/no)")
            ch_input = input().lower()
            ch = True if ch_input == "yes" else False

    def displayf(self):
        if self.head is None:
            print("No element")
            return

        print("Elements in forward:")
        ptr = self.head

        while ptr is not None:
            print(ptr.data, end=" <-> ")
            ptr = ptr.next
        print("None")

    def displayb(self):
        if self.head is None:
            print("No element")
            return

        print("Elements in backward:")

        ptr = self.head

        # move to last node
        while ptr.next is not None:
            ptr = ptr.next

        # traverse backward
        while ptr is not None:
            print(ptr.data, end=" <-> ")
            ptr = ptr.prev
        print("None")
    def insertbeg(self,data):
        cur=Node(data)
        print(data,"insert begning")
        cur.next=self.head
        self.head.prev=cur
        self.head=cur


# Run program
obj = DLinkedList()
obj.create()
obj.displayf()
obj.displayb()