# Parent class
class Parent:
    def parent_info(self):
        print("This is the Parent class")

# Student class inherits Parent
class Student(Parent):
    def student_info(self, name, roll):
        self.name = name
        self.roll = roll
        print("Student Name:", self.name)
        print("Roll Number:", self.roll)

# EngStudent class inherits Student
class EngStudent(Student):
    def eng_info(self, branch):
        self.branch = branch
        print("Engineering Branch:", self.branch)

# Creating object
s = EngStudent()

# Calling methods
s.parent_info()
s.student_info("Rahul", 101)
s.eng_info("Computer Science")