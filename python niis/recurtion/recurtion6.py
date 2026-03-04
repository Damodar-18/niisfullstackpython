def show(i):
	print("A",i)
	if i<=3:
		show(i+1)
	print("B",i)
def main():
	print("C")
	show(1)
	print("D")
main()