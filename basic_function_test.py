def divideByInteger(i,j):
    if (j==0):
        raise Exception("Division by zero")
    if (i==0):
        return 0
    if (i<0 or j<0):
        return -1*int(i/j)
    return int(i/j)
