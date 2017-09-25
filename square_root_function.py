


import math,sys

def compute_square_root():
    "Inputs a string from the user and returns the square root or -1 for error"

    #input data from user
    strNum=input("Enter a number to take square root of: ")

    #validate if the data is valid for floating-point numbers.
    #To be a valid floating-point number, each character of the string
    #needs to be a digit, and there can only be one decimal point
    hasDecimal=False
    sError=""
    for c in strNum:
        if not c.isdigit():
            if c!=".":
                sError="Invalid number - bad character!"
            else:
                if hasDecimal==False:
                    hasDecimal=True
                else:
                    sError="Invalid number, too many decimal points!"
    if sError!="":
        print("Error converting: "+sError)
        sys.exit()
    
    #validate that the data is within proper bounds
    fVal=float(strNum)
    if fVal <=0 or fVal > 1000:
        print("Error: value out of range 0-1000")
        sys.exit()
    
    #compute the square root of the input
    fSquare=math.sqrt(fVal)

    #return the valid value to the calling code
    return fSquare
