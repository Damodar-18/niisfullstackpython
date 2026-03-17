print("Start")
L=[20,40,50]
try:
    print(L[2]//0)
except IndexError:
    print("Index out of range")
except ZeroDivisionError:
    print("Cannot divide by zero")

except:
    print("handal all exception")

print("End")