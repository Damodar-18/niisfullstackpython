print("start")
L=[10,20,40,50]
try:
	print(L[5])
except IndexError as e:
	print(e)
print("end")