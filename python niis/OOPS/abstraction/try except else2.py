print("Start")

try:
    a = int(input("Enter a number: "))
    result = a * 5
except ValueError:
    print("Invalid input")
else:
    print("Result =", result)

print("End")