def show(i):
	if i<11:
		show(i+1)
		print(i)
def main():	
	show(1)
main()