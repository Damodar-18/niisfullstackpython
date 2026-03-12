class demo:
	def __init__(self,n):
		self.n=n
		print("constructor",self.n)
	def __del__(self):
		print("destructor",self.n)
d1=demo("first")
d1=demo("second")
d1=demo("third")
