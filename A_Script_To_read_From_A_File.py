import os
import datetime
#Reading a free form text file
#Now let's read back in
f=open("MyTextFile3", "r")
s=f.read() #this figure determines how many characters should be read at max from the file
f.close()
print("In the file called 'MytextTiles3', I read the following string: {}".format(s))



