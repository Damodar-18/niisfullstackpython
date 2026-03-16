class Person:
	def _init_(self,name,age):
		self.name=name       #property
		self.age=age
	def show_person(self):
		print("Name=",self.name)
		print("Age=",self.age)
class Student(Person):
	def _init_(self,name,age,roll):
		super()._init_(name,age)
		self.roll=roll
	def show_student(self):
		print("Roll=",self.roll)
class Enggstudent(Student):
	def _init_(self,name,age,roll,branch):
		super()._init_(name,age,roll)
		self.branch=branch
	def show_engg(self):
		print("Branch=",self.branch)
e=Enggstudent("Satya",22,56,"MCA")
e.show_person()
e.show_student()
e.show_engg()