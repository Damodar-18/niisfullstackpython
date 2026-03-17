print("Start")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    L = [10, 20, 30]

    print("Division:", a / b)
    print("List value:", L[5])

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter numbers only")

except IndexError:
    print("List index out of range")

except:
    print("Some other error occurred")

print("End")