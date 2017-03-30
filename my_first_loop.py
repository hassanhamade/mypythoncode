signal_variable=False
#signal_variable est une variable de type booléenne.
total=0
while not signal_variable:
# que signifie l'instruction 'while not signal_variable' ? Analysons en découpant par morceaux.
# Oublions la valeur donnée au départ du script à 'signal_variable'.
# Comme 'signal_variable' est un booléen, alors 'not signal_variable' signifie que 'signal_variable=False'. C'est en quelque sorte la négation de 'signal_variable'. Faire le test dans IDLE.
# Définir une variable du nom de bool et lui donner la valeur de True. Tapper bool => ca retourne la valeur True. Tapper not bool, ça retourne la valeur False. Donc si bool=True, 'not bool'=False.
# Résultat: 'while not signal_variable' signifie "tant que signal_variable=False.
# Donc en donnant la valeur de départ de False à la variable signal_variable, on permet bien à la boucle de démarrer.
    inputvar=input("Enter a value or 'exit' to exit the program ")
    if inputvar=='exit':
        signal_variable=True
    else:
        total=total+int(inputvar)
print("Your entered a total of:")
print(total)
