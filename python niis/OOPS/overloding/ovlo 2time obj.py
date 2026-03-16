class mytime:
	def __init__(self,h,m,s):
		self.h=h
		self.m=m
		self.s=s
	def __add__(self,t2):
		t3=mytime(0,0,0)
		t3.s=self.s+t2.s
		t3.s=t3.s%60
		t3.h=self.h+t2.h+t3.m//60
		t3.m=t3.m%60
		return t3
	def show(self):
		print(self.h,":",self.m,":",self.s)
t1=mytime(5,40,35)
t2=mytime(4,45,40)
t3=t1+t2
t1.show()
t2.show()
t3.show()