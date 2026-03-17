print("Start")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a + b
except:
    print("Invalid input")
else:
    print("Sum =", result)

print("End")