commands=["create","read","update","delete"]
usercommand=input("type in your command:")

if usercommand not in commands:
    print("please type in a valid command")
else:
    print("I'll be happy to ",usercommand," for you")

