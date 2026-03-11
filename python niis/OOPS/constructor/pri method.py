class demo:
	def __show(self):  #private method
		print("hii")
	def disp(self):
		self.__show()
ob=demo()
#ob.__show()  #error
ob.disp()
		