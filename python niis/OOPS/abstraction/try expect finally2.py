print("Start")

try:
    L = [10, 20, 30]
    print("Value:", L[5])

except IndexError as r:
    print("Index out of range",r)

finally:
    print("This block always runs")

print("End") 