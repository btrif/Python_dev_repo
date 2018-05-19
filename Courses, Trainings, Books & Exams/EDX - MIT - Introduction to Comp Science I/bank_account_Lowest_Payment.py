'''
It simulates a credit bank account. Suppose you have a credit. You pay each month a FIXED monthlyPaymentRate
and each month an annualInterestRate is calculated for the remaining money resulting in a remaining balance
each month.
This  function calculates the lowest Payment one needs to do such that the balance is ~0 at the end of the period.
'''

balance = 5000
annualInterestRate = 0.18
#monthlyIntRate = annualInterestRate/12.0

getpayment = True
ranonce = False
MoMin = balance/12
MoMax = (balance*(1+annualInterestRate/12)**12)/12.0
MoPayment = (MoMin+MoMax)/2
NewBal=0

#Create a function to run 12 months of payments, and then create a loop to re-run the function if the Ending Balance is not close enough to 0.
def CCPayment(balance, annualInterestRate, MoPay):

    global NewBal
    Month = 1               #Month begins at 1

    while Month <= 12:
            balance = (balance - MoPay)
            balance = balance + (annualInterestRate * balance/12)
            Month += 1
    NewBal=balance          #sets the var NewBal to be used globally
    if (balance < .02) and (balance > -0.02) : #cannot evaluate to '0' as you are evaluating a float and it will 'inf loop'. Must evaluate it to a number 'close enough'
        return MoPayment
    else:
        return False

while getpayment == True:
    if CCPayment(balance, annualInterestRate, MoPayment):
        getpayment = False
        print ("Lowest Payment: ", round(CCPayment(balance, annualInterestRate, MoPayment),2))
    else:
        if NewBal < 0.01:           #paid too much! Lower the max payment and rerun function
            if ranonce == True:             #Bool check to avoid resetting the Min/Max values before running it once
                MoMax=MoPayment             #sets the Max payment to the current monthly payment
                MoPayment=(MoMin+MoMax)/2           #sets the Monthly payment to average the Min/Max payments
            ranonce = True
            CCPayment(balance, annualInterestRate, MoPayment)

        elif NewBal > 0.01:                                 #didn't pay enough! Raise min payment and rerun function
            if ranonce == True:                             #Bool check to avoid resetting the Min/Max values before running it once
                    MoMin=MoPayment                     #sets the Min payment to the current monthly payment
                    MoPayment=(MoMin+MoMax)/2           #sets the Monthly payment to average the Min/Max payments
            ranonce = True
            CCPayment(balance, annualInterestRate, MoPayment)
