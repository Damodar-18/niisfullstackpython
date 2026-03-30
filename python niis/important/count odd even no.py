no=125
e=0
o=0
while no!=0:
	r=no%10
	if r%2==0:
		e=e+1
	else:
		o=o+1
	no=no//10
print("no of  odd digit=",o)
print("no of  even digit=",e)