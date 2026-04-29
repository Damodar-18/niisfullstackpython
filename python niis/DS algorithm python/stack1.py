MAX = 5
queue = [0] * MAX = -1

def push(item):
    global top
    if top == MAX - 1:
        print("Stack Overflow")
    else:
        top += 1
        stack[top] = item
        print(f"Pushed {item}")

def pop():
    global top
    if top == -1:
        print("Stack Underflow")
    else:
        item = stack[top]
        top -= 1
        print(f"Popped {item}")

def peek():
    if top == -1:
        print("Stack is empty")
    else:
        print(f"Top element is {stack[top]}")

def display():
    if top == -1:
        print("Stack is empty")
    else:
        print("Stack elements:", stack[:top+1])

# Example usage
push(10)
push(20)
push(30)
display()
peek()
pop()
display()