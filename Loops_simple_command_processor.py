commands=["Exit", "Load", "Create", "Delete"]
signal=False
while not signal:
    user_command=input("Enter a valid command")
    if user_command in commands:
        signal=True
        print("signal set to True. You have entered a valid command")
    else:
        print("you didn’t enter a valid command")

    
