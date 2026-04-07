f=open("data.text","r")
l=f.readlines()
for i in l:
	print(i,end="")
f.close()