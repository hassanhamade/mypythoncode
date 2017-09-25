
#this variable is program-level in scope
gA=10

#variables defined in the function are local to the function
#functions can use program-level variables

def myfunc1():
    lA=5
    print("local value of a in myfunct1={}".format(lA))
    print("program level value of a={}".format(gA))

def myfunc2():
    lA=10
    print("local value of a in myfunct2={}".format(lA))
    print("program level value of a={}".format(gA))

def myfunc3():
    gA=20
    print("In myfunc3, gA={}".format(gA))

#This line is OK
print("Program level variables are OK here: {}".format(gA))

#And they don't change in local functions
myfunc1()

#but program level variables can be changed anywhere.
#or can they not?
myfunc3()
print("Program level variable is: {}...has it changed ?".format(gA))
