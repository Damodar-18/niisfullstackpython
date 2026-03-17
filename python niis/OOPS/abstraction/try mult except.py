print("Start")

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    L = [10, 20, 30]
    print(L[4])   # This will cause IndexError
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

except IndexError:
    print("Index out of range")

print("End")