import os
from os import listdir
mypath=input("Enter a directory to list: ")
for f in listdir(mypath):
    print("File: {}".format(f))
    
    
