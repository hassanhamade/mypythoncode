f=open("MyTestFile.txt","r")
s=f.read(256)
print("I read in {}".format(s))
f.close()
