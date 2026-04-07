import pickle
class student:
	def __init__(self,roll,name,mark):
		self.roll=roll
		self.name=name
		self.mark=mark
	def show(self):
		print(self.roll,self.name,self.mark)
		f=open("student.dat","wb")
		s1=student(101,"amit",89)
		s2=student(102,"manas",85)
		s3=student(103,"milan",90)
		pickle.dump(s1,f)
		pickle.dump(s2,f)
		pickle.dump(s3,f)
		f.close()

