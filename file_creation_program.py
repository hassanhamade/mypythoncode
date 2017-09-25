import os
os.chdir("/Users/hhamade/Code/Python")
f=open("InTheAir2.txt","w")
f.write("This is a test")
f.close()
print("This is where my file is: {}".format(os.getcwd()))

