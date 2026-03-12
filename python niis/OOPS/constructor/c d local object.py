class demo:
	def __init__(self):
		print("constructor")
	def __del__(self):
		print("destructor")
def show():
	print("A")
	di=demo()
	print("B")
print("main start")
show()
print("main end")