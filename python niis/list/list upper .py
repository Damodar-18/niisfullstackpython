l=[[3,4,2],[6,5,1],[9,8,7]]
for i in range(0,len(l),1):
	for j in range(0,len(l[i]),1):
		if i<=j:
			print(l[i][j],end="\t")
		else:
			print(end="\t")
	print()