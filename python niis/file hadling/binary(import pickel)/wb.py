#write a list using binary format
import pickle
num=[10,20,30,40,50]
f=open("bapun.dat","wb")
pickle.dump(num,f)
f.close()