l=[]
print("enter 2D list data")
l=eval(input())
print("elements are")
for i in range(0,len(l),1):
	for j in range(0,len(l[i]),1):
		print(l[i][j],end="\t")
	print()