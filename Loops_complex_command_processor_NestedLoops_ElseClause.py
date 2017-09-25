commands=["Exit", "Load", "Create", "Delete"]
signal=False
while not signal:
    user_command=input("Enter a valid command")
    for c in commands:
        if c==user_command:
            signal=True
            print("signal set to True: exiting the inner loop. You have entered a valid command")
            break
    else:
        print("you didn’t enter a valid command")

    
