import math,sys
def compute_square_root(strNum):
        #Validate that the data is proper for floating point numbers.
        #To be a valid floating point number, each character of the string
        #needs to be a digit and there can only be one decimal point
        hasDecimal=False
        sError=""
        for c in strNum:
                if c=='.':
                        if hasDecimal==False:
                                hasDecimal=True
                        else:
                                sError="Invalid number, too many decimal points!"
                elif not c.isdigit():
                        sError="Invalid number - bad character!"


        if sError !="":
                print("Error converting:" + sError)
                return -1.0
	
	#Validate that the data is within the valid bounds
        fVal=float(strNum)
        if fVal <= 0 or fVal > 1000:
                print("Error: value out of range 0-1000")
                return -1.0
	
	#compute the square root of the input
        fSquare=math.sqrt(fVal)
	
	#return the valid value to the calling code
        return fSquare
print("test")


