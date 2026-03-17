print("Start")

L = [10, 20, 30, 40]

try:
    print(L[5])   # Index 5 does not exist
except IndexError as e:
    print("Error:", e)
