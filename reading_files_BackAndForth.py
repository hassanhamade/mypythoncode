import datetime
import os
import random

#create a text file and write out a bunch of lines.
f=open("MyTextFile2.txt","w")
for i in range(0,1000):
    f.write("This is line {}".format(i))
f.close()
print("Wrote the file to {}".format(os.getcwd()))

#Now, re-open the file for read access.
f=open("MyTextFile2.txt","r")

#Now, let's jump around the various lines
for i in range(0,5):
    position=random.randrange(0,1000)
    f.seek(position)
    s=f.read(30)
    print("At position {} read characters[{}]".format(f.tell(),s))

    
            
    
