from os import listdir
from os.path import isfile,join
import os

filename=input("Enter a file to parse: ")
drive,path=os.path.splitdrive(filename)
path,filename=os.path.split(path)

print("Drive: {}".format(drive))
print("Path: {}".format(path))
print("Filename: {}".format(filename))
