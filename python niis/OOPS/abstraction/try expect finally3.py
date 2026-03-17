print("Start")

try:
    num = int(input("Enter a number: "))
    print("Square:", num * num)

except ValueError:
    print("Please enter a valid number")

finally:
    print("Execution completed")

print("End")