print("start")

L = [10, 20, 30, 40]

try:
    i = int(input("Enter index number: "))
    print("Element:", L[i])

except IndexError:
    print("Index out of range")

print("end")