def show(i):
	print(i)
	if i<10:
		show(i+1)
def main():	
	show(1)
main()