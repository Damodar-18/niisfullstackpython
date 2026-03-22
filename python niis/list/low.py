l = [
    [4, 3, 2],
    [6, 5, 1],
    [9, 8, 7]
]
for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        if i <= j:
            print(l[i][j], end="\t")
        else:
            print( end="\t")
    print()