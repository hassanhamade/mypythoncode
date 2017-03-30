commands=["Create”, "Read”, "Update”, "Delete”]
while True:
    inputVar=input("Enter a valid command: ")
    if inputVar in commands:
        print("You have entered a valid command")
        break
    else:
        print("You didn't enter a valid command")

