while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    divisor = 2
    isPrime = True
    while divisor < number:
        if number % divisor == 0:
            isPrime = False
            break
        divisor += 1
    if isPrime == False:
        print(number, "IS NOT a Prime number")
    else:
        print(number, "IS a Prime number") 

print("0 is not a valid input. This program is written so as to exit when you enter 0.")
