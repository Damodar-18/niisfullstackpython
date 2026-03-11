#input for keyboard
class obj():
	def __init__(self):
		self.x=int(input())
		self.y=int(input())
print("enter obj1 2 variable")
r=obj()
print("enter obj2 2 variable")
d=obj()
print("display 1st object value")
print(r.x,r.y)
print("display  2nd obj value")
print(d.x,d.y)