import datetime
import time
#declaration de ma date de naissance
mybirthday=datetime.date(2009,3,6)
#creation de la variable year que l'on va incrémenter à partir de mon année de naissance.
#On fait cela car la fonction native pour incrémenter des dates, timedelta, n'accepte pas des incréments en années.
year=2009
#on créé une liste days dans laquelle on va venir stocker chaque jour d'anniversaire
days=[]
#on créé une liste fixe contenant les jours de la semaine sur laquelle on va faire itérer n
week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
#début de la boucle. On fait l'exercice sur mes 45 premières années.
startime=time.time()
for i in range(0,8):
    if i<40:
        x=mybirthday.strftime("%c")
        print("In {}, my birthday day was a {}".format(x[-4:],mybirthday.strftime("%A")))
    else:
        print("In {}, my birthday day will be a {}".format(x[-4:],mybirthday.strftime("%A")))
    day=mybirthday.strftime("%A")
    days.append(day)
    year+=1
    mybirthday=datetime.date(year,9,7)
for n in week:
    print("I had {} {}s as birthdays in my life".format(days.count(n), n))
endtime=time.time()
print("Time to run this program was: {}".format(endtime-startime))

    
    


    
    

                          

