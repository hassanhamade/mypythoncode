import array
myArray = array.array('i', [1,2,3,4,5,6,7,8,9,10])
#pos=0
found=False
while not found:
    pos=0
    inputVar=input("Which value do you want me to search for ?: ")
    for i in myArray:
        if i == int(inputVar):
            print("Found the value",inputVar,"at position:", pos)
            found=True
            break
        pos+=1
    else:
        print("Didn't find value of", inputVar)
        print("Try again")
    

    
        
