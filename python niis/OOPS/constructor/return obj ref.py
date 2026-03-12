class student:
	def __init__(self,n,m,r):
		self.name=n
		self.rollno=r
		self.mark=m
def show():
		s=student("muna",1,90.50)
		return s
res=show()
#print(type(res),res)
print("my name=",res.name)
print("my roll=",res.rollno)
print("my mark=",res.mark)
