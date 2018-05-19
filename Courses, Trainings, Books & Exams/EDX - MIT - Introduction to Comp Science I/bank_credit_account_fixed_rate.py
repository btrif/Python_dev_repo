'''
It simulates a credit bank account. Suppose you have a credit. You pay each month a FIXED monthlyPaymentRate
and each month an annualInterestRate is calculated for the remaining money resulting in a remaining balance
each month.
It is approximative. Works only with +/-10 increments as was requested by the problem.
'''
balance  = 4619         #    Balance
annualInterestRate  =  0.04             #18/100          # Annual Interest Rate, %
fixedRate = 400            # Monthly payment rate,  %
epsilon = 50
end_balance = 200
numGuesses= 0

#def bank_account(balance , annualInterestRate  , monthlyPaymentRate ):

def comp_balance(balance, fixedRate, annualInterestRate ):
    for i in range(1,13):
        balance  = balance  +  (balance  * annualInterestRate) /12 - fixedRate
        #print(round(balance , 2),'  ;     ', round(-fixedRate,2) )
    print ('\nRemaining balance after a year : ',round(balance, 2))
    global end_balance
    end_balance = round(balance,2)
    return end_balance

while abs(end_balance) > epsilon :
    if end_balance > 0 :
        fixedRate = fixedRate + 10
    else :
        fixedRate = fixedRate - 10
    #fixedRate = (high + low)/2
    numGuesses+=1
    #print(str(numGuesses)+'.     The Fixed Rate must be :  ',fixedRate)
    comp_balance( balance, fixedRate, annualInterestRate )
print('\nLowest Payment: ',round(fixedRate,2))


#print(comp_balance(5000, 200, 18/100))
