class student:
	def __init__(self,n,r,m):
		self.__name=n
		self.__roll=r
		self.__mark=m
	def show(self):
		print("my name=",self.__name)
		print("my rollno=",self.__roll)
		print("my mark=",self.__mark)
	def update(self,n,r,m):
		self.__name=n
		self.__roll=r
		self.__mark=m
	def set__name(self,name):
		self.__name=name
	def set__roll(self,roll):
		self.__roll=roll
	def set__mark(self,mark):
		self.__mark=mark
	def get__name(self):
		return self.__name
	def get__roll(self):
		return self.__roll
	def get__mark(self):
		return self.__mark
s=student("muna",1,90.50)
s.show()
s.update("muna das",2,90.50)
s.show()
print("my nane=",s.get__name())

		
