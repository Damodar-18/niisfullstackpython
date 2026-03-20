l=[10,20,3,7,30,50,9,40,60]
l1=[]
for i in range(0,len(l),1):
	if l[i]%2==0:
		l1.append(l[i])
print(l1)