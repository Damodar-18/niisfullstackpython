for i in range(1,5,1):
	for j in range(5-i,5,1):
		print(chr(64+j),end="\t")
	print()

for i in range(68,64,-1):      #new one
	for j in range(i,69,1):
		print(chr(j),end="\t")  
	print()