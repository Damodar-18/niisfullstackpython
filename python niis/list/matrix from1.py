l = [[10,20,30],[40,50,60],[70,80,90]]

for i in range(0, len(l), 1):
    for j in range(0, len(l[i]), 1):
        print(l[i][j], end="\t")
    print()