print("start")
try:
    print(10//0)
except ZeroDivisionError as e:
    print("caught",e)
print("end")