def myFunction(input_value):
    input_value=input_value*2
    ret_val=0
    if input_value<100:
        ret_val=1
    return input_value,ret_val

inp=20
transformed_input,oup=myFunction(inp)
print(inp,transformed_input,oup)

