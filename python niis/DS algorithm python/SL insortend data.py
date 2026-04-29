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

    # ✅ Correct insert at beginning
    def insertbeg(self, data):
        cur = Node(data)
        cur.next = self.head   # link new node to first node
        self.head = cur        # update head
        print("Data inserted at beginning")


# Run program
obj = LinkedList()
obj.create()
obj.display()

obj.insertbeg(5)
obj.display()