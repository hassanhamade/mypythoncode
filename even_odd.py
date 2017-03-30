Valid_Entry=True
while Valid_Entry==True:
    inputVar=input("Enter a number: ")
    if int(inputVar) == 0:
        print("0 is not a valid entry since it is neither odd or even.")
        print("Please enter a new value.")
        continue
    else:
        if int(inputVar)%2== 0:
            print(inputVar," is an EVEN number.")
        else:
            print(inputVar," is an ODD number.")
        Valid_Entry=False
        break

        


