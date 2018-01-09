import array
a=input("Entrez une array de chiffres ")
s=int(input("Entrez une somme à trouver "))
A=[]
for n in a:
    A.append(int(n))
B=array.array('i',A)
R=False
for i in range (0,len(B)):
    for j in range (i+1,len(B)):
        print(B[i]+B[j])
        if B[i]+B[j]==s:
            print("SUCCESS")
            R=True
            break #break qui fait sortir de la boucle j (boucle intérieure) dès qu'on a trouvé le nombre recherché. On revient au corps du code, donc dans la boucle i.
            print("Test du break: si ceci imprimé, alors le break de sortie de la boucle j n'a pas marché")
    if R:
        break #break qui fait sortir de la boucle i (boucle extérieure). On sort donc du programme.car on a trouvé le nombre.

#on peut aussi faire une variante qui ne fait pas sortir du programme. On continue à calculer pour voir combien de fois on trouve le nombre recherché. On laisse finir les boucles et on incrémente un
#compteur à chaque fois qu'on tombe sur le chiffre recherché.
                  
    
            

        

