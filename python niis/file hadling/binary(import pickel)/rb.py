import pickle
f=open("bapun.dat", "rb")
l=pickle.load(f)
print(l)
f.close()