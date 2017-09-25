#defining the function
def myFunction(input_value):
    input_value=input_value*2
    ret_val=0
    if input_value<100:
        ret_val=1
    return input_value,ret_val

#the below is the calling program.
#it includes the variable initialization phase (inp=20)
inp=20
inp,oup=myFunction(inp)
print(inp,oup)

