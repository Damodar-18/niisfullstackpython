f=1
def fact(n):
	global f
	if n>0:
		f=f*n
		n=n-1
		fact(n)
		return f
print(fact(5))