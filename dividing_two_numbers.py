import pdb

def divide_two_numbers(a,b):
    print("x={}".format(a))
    print("y={}".format(b))
    return int(x/y)

pdb.set_trace()

x=int(input("Entrez une valeur pour x: "))
y=int(input("Entrez une valeur pour y: "))

print("x/y={}".format(divide_two_numbers(x,y)))
