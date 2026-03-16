class mycomplex:
	def __init__(self,r,i):
		self.r=r
		self.i=i
	def __add__(self,c2):
		c3=mycomplex(0,0)
		c3.r=self.r+c2.r
		c3.i=self.i+c2.i
		return c3
	def show(self):
		print(self.r,"+",self.i,"i")
c1=mycomplex(2,4)
c2=mycomplex(3,5)
c3=c1+c2
c1.show()
c2.show()
c3.show()