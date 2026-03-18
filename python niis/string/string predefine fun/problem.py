print("Enter the number")
s=input()
c,alp,up,lw,vw,cd,dg,sp,sy,wd=0,0,0,0,0,0,0,0,0,0
for i in s:
	c=c+1
	if i.isalpha():
		alp=alp+1
		if i.isupper():
			up=up+1
		else:
			lw=lw+1
		if i in "aeiouAEIOU":
			vw=vw+1
		else:
			cd=cd+1
	elif i.isdigit():
		dg=dg+1
	elif i.isspace():
		sp=sp+1
	else:
		sy=sy+1
wd=wd+1
print("no of char=",c)
print("no of alp=",alp)
print("no of upper=",up)
print("no of lower=",lw)
print("no of vw=",vw)
print("no of consonsnt=",cd)
print("no of digit=",dg)
print("no of space=",sp)
print("no of sp symble=",sy)
print("no of word=",wd)

