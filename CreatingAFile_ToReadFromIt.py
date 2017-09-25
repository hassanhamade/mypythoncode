import os
import datetime
#A free form text example
#First, create a new file and write out the date and time to it.
f=open("MyTextFile3", "w")
f.write("Todays Date is: {}".format(datetime.datetime.now()))
f.close()
print("This file was created in: {}".format(os.getcwd()))


