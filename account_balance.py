account=int(input("Enter the current balance:"))
#if the account is negative, apply a 10 dollars fee
if account<0:
    account=account-10
    print("checked first if statement")
#if the account is zero, apply a 5 dollars fee
elif account==0:
     account=account-5
     print("checked second if statement")
#if the account is up to 500, apply a 1 dollars fee
elif account>0 and account<500:
     account=account-1
     print("checked third if statement")
#if the account is greater than 500 but less than 1000, add 1%
elif account>500 and account<1000:
     account=account+account/100
     print("checked fourth if statement")
#if the account is superior than 1000, apply a 10 dollars fee
elif account>=1000:
     account=account+(account/100)*2
     print("checked fifth if statement")
else:
     print("Amount out of range")
    
print("Your final balance is:" + str(account))




