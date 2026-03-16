class p:
	def f1(self):
		print("f1 method")
class c(p):
	def f2(self):
		print("f2 method")
ob=c()
ob.f1()
ob.f2()
obj=p()
#obj.f2()