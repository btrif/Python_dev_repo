'''
It simulates a credit bank account. Suppose you have a credit. You pay each month a monthlyPaymentRate
and each month an annualInterestRate is calculated for the remaining money resulting in a remaining balance
each month.
'''

balance  = 5000    # Balance
monthlyPaymentRate = 2/100           # Monthly payment rate,  %
annualInterestRate  = 18/100          # Annual Interest Rate, %


#def bank_account(balance , annualInterestRate  , monthlyPaymentRate ):
for i in range(1,13):
    balance  = balance  - (monthlyPaymentRate * balance)
    balance  = balance  + (balance  * annualInterestRate /12)

    print(round(balance , 2),'  ;     ', round(-monthlyPaymentRate*balance ,2) , ' ;     ', round((balance  * annualInterestRate /12),2))
print ('\nRemaining balance after a year : ',round(balance, 2))

#print(bank_account(484, 0.2, 0.04))