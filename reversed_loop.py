mySTR=input("Enter a string ")
i=len(mySTR) - 1
myReverseString=""
while i>=0:
    myReverseString+=mySTR[i]
    i-=1
print("Reversed, the string is ", myReverseString);
