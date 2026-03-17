print("start")
L=[20,30,50]
try:
	res=L[2]//2
except:
	print("handle all exception")
else:
	print("else block ",res)
print("end")