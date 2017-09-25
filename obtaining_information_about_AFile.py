import os
from os import listdir
from os.path import isfile,join


f=input("Enter a file to parse: ")
drive,path=os.path.splitdrive(f)
path,filename=os.path.split(path)


print("Drive: {}".format(drive))
print("Path: {}".format(path))
print("Filename: {}".format(filename))

sz=os.stat(f)
print("Size of the file: {}".format(sz.st_size))

    
