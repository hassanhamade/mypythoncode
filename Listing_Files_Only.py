import os
from os import listdir
from os.path import isfile,join
mypath=input("Enter a directory to list: ")
for f in listdir(mypath):
#os.path.join recompose le chemin d'accès complet (mypath) avec le nom du fichier listé (f)
#et met ça ds la variable filename sur laquelle sera exécutée la fonction isfile()
    filename=os.path.join(mypath,f)
    if isfile(filename):
        print("File: {}".format(f))
    
    
