import stringfunc2
s=input("please input a string to reversed: ")
if len(s)>stringfunc2.maximumlength:
    print("The string is too long!")
else:
    sr=stringfunc2.func1(s)
    #sr=func1(s)
    print("Reversed string is={}".format(sr))
    
