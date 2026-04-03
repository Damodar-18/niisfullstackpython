r=int(input("enter row"))
for i in range(r,0,-1):
	for j in range(r-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print("*",end="")
	for j in range(i-1,0,-1):
		print("*",end="")
	print()
for i in range(2,5,1):
	for j in range(r-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print("*",end="")
	for j in range(i-1,0,-1):
		print("*",end="")
	print()