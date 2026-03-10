class si:
	def __init__(self,p,t,r):
		self.p=p
		self.r=r
		self.t=t
	def show(self):
		print("principal=",self.p)
		print("rate=",self.r)
		print("time=",self.t)
	def sical(self):
		return self.p*self.r*self.t/100
i1=si(1000,10,2)
i1.show()
print("simple intrest=",i1.sical())