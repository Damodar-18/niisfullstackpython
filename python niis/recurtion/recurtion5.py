def show(i):
	print("A")
	if i<=3:
		show(i+1)
	print("B")
def main():
	print("C")
	show(1)
	print("D")
main()