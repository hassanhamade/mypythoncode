import array
a=input("Entrez une array de chiffres ")
s=int(input("Entrez une somme à trouver "))
A=[]
for n in a:
    A.append(int(n))
B=array.array('i',A)
R=False
low=0
high=len(B)-1
while low < high:
    if (B[low]+B[high])==s:
        print("SUCCESS")
        break
        
