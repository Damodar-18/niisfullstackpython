no=125
e=0
o=0
while no!=0:
	r=no%10
	if r%2==0:
		e=e+r
	else:
		o=o+r
	no=no//10
print("sum of  odd digit=",o)
print("sum of  even digit=",e)