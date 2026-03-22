l=[[1,2,3],[4,5,6]]
t=[]
for i in range(0,len(l[0])):
	r=[]
	for j in range(0,len(l)):
		r.append(l[j][i])
	t.append(r)
print("transpose",t)
