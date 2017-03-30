import datetime
import os
f=open("MyTestFile.txt","w")
f.write("La date d'aujourd'hui est: {}".format(datetime.datetime.now()))
f.close()
print("You will find the file at: {}".format(os.getcwd()))



