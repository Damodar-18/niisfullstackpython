l = []
print("enter how many lists to store")
s = int(input())

for i in range(0, s, 1):
    print("enter the list data")
    x = eval(input())
    l.append(x)

print("elements are")
for i in range(0, len(l), 1):
    for j in range(0, len(l[i]), 1):
        print(l[i][j], end="\t")
    print()
  