import pickle
f=open("bapun.dat", "rb")
while True:
	try:
		l=pickle.load(f)
		print(l)
	except EOPError:
		break
f.close()