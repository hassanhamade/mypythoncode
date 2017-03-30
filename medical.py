income=int(input("What is your income?"))
medicalCosts=int(input("What is the expected medical cost?"))
deduction=0

if income>100000:
    if medicalCosts>income/10:
        deduction=medicalCosts
    else:
        deduction=1000
else:
    if medicalCosts>income/50:
        deduction=medicalCosts
    else:
        deduction=500

print("Based on your income, your deduction will be:", deduction)


        
        
