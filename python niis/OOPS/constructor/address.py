class student:
	def __init__(self,n,r,m):
		self.name=n
		self.rollno=r
		self.mark=m
def show(self):
		print(id(self))
		print("my name=",self.name)
		print("my roll=",self.rollno)
		print("my mark=",self.mark)
s=student("muna",1,80.60)
print(id(s))
show(s)
