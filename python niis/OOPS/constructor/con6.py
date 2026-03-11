#input user parameter constructor
class obj():
	def __init__(self,x,y):
		self.x=x
		self.y=y
print("enter two value")
r=obj(int(input()),int(input()))
print("display obj value")
print(r.x,r.y)