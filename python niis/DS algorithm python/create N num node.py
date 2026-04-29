class Node:
	def __init__(self,ele):
		self.data=ele
		self.next=None
head= None
curr=None
ptr=None
c=0
ch=True
while ch:
	c=c+1
	print("Enter node",c,"data")
	ele=int(input())
	cur=Node(ele)
	if head== None:
		head=cur
	else:
		ptr.next=cur
	ptr=cur
	print("do you continue? press True/False")
	ch=input()
	if ch=="True":
		CH=True
	else:
		ch=False
print("elements are:")
ptr=head
while ptr!=None:
	print(ptr.data)
	ptr=ptr.next