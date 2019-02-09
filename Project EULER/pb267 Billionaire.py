#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @         Completed on Sun, 6 Jan 2019, 18:52
#The  Euler Project  https://projecteuler.net
'''
                                        Billionaire     -       Problem 267

You are given a unique investment opportunity.

Starting with £1 of capital, you can choose a fixed proportion, f,
of your capital to bet on a fair coin toss repeatedly for 1000 tosses.

Your return is double your bet for heads and you lose your bet for tails.

For example, if f = 1/4, for the first toss you bet £0.25, and if heads comes up you win £0.5
and so then have £1.5. You then bet £0.375 and if the second toss is tails, you have £1.125.

Choosing f to maximize your chances of having at least £1,000,000,000 after 1,000 flips,
what is the chance that you become a billionaire?

All computations are assumed to be exact (no rounding),
but give your answer rounded to 12 digits behind the decimal point in the form 0.abcdefghijkl.
'''
print(__doc__)

import time
import random
from math import log, floor, ceil
from gmpy2 import comb, fac

f = 1/4     # proportion of your capital to bet on a fair coin toss repeatedly for 1000 tosses.
capital = 1       #   Starting with £1 of capital


def bet( f, money ) :
    chance = random.randint(0,1)
    if chance == 1 :         money += 2*money*f
    else  :         money -= money*f
    print('chance : ', chance, '    money = ', money)
    return money, chance

bet( 1/4, 2.25 )



'''
money = 1
f = 0.25
money = 1
for turn in range(0, 1000) :

    money, chance = bet( f, money )
    print(str(turn+1) +'.        chance = ', chance, '        money =' , money ,)
'''

''' @2019-01-06 -   General IDEA
We know that there are 1000 throws, so we would expect that the number of possible value of money
to be = 2*1000, but here one interesting happens : (visual representation with f = 0.25 )
1 =  gain (Head) , 0 = loss (Tail)

                                                       --> 3.375 (0,0,0)
                     --> 2.25 (1,1)  -
        --> 1.5 -                                   --> 1.6875 (1,1,0) or (1,0,1)
1--                --> 1.125 (1,0) or (0,1) --
        --> 0.75 -                                  --> 0.84375 (0,0,1) or (0,1,0)
                    --> 0.5625 (0,0) -
                                                         --> 0.421875 (0,0,0)
                    
# 1.125  chance :  1     money =  1.6875        , chance :  0     money =  0.84375
# 0.5625    chance :  0     money =  0.421875,  chance :  1     money =  0.84375

So we observe that instead of 2**1000 different results we will obtain a limited number of results :
results = 1000+1 = 1001 . This FACT si CRITICAL to solve the problem !
Now we must establish a formula !

'''





print('\n--------------------------TESTS------------------------------')
t1  = time.time()


L = lambda f : (9 * log(10) - 1000 * log(1 - f) ) / ( log(1 + 2 * f) - log(1-f) )





def gradient_descend(f, alpha, fold ):
    '''
    f = 0.95     # Starting value for f
    alpha = 1e-5        # Learning rate
    fold = 1        #   will represent the previous value of the function with which will compare

    dL/df = [ L(f+h) - L(h)  ] / h              # where h - step size, h = 1e-6 here,
     represents the derivative of the function L(f)

    :param f : the initial value of the function at the starting point, the hypothsis
    :param alpha : sometimes called learning rate
    :param fold : previous value of the function f, in the beginning can have any reasonable value
                            This is used to compare the advancement
    :return:
    '''

    while abs( f  - fold ) >= 1e-6 :
        fdev = ( L(f + 1e-6) - L(f) ) / 1e-6        # dL/df = ( L(f +  h) - L(f) ) /  h
        # print('before    f = ', f, '      fold =', fold ,'      fdev = ', fdev  )

        fold = f
        f -= alpha * fdev

        print('after    f = ', f, '      fold =', fold ,'      fdev = ', fdev  )

    print('\nf = ', f )
    return f

f_min = gradient_descend( f = 0.95, alpha = 1e-5, fold = 1 )

# Now we must evaluate L(f) with f = f_min the minimization of the f function, the value for which we found
# f_min = 0.14690527630564243
nr_of_heads = L(f_min)
#               (9 * log(10) - 1000 * log(1 - f) ) / ( log(1 + 2 * f) - log(1-f) ) = L(f)

print('nr_of_heads = ',  nr_of_heads  )
# But the nr_of_heads must be an integer, OBVIOUSLY, the upper value, not an exact value
nr_of_heads = ceil(nr_of_heads)

print('nr_of_heads = ',  nr_of_heads  )
'''

# And now we can find the probability  that we get  nr_of_heads = 432 .
This is done using combinations. How many combinations of 432 heads and (1000-432) = 568 tails
BUT we must go UP because we just found a minimum number of head, but there could be more
than that like, 433, 434, 435 ,.... , 1000 heads

Example For a 5 total sum of head and tails :  2 heads (1's ) and 3 tails (0's)  we would have :
00011, 00101, 01001, 10001, 00110, 01010, 10010, 01100, 10100, 11000    =   10 permutations
the formula is :       P(n1+n2) /  ( P(n1) * P(n2) )  


QUESTION : 
What is the probability to hit EXACTLY 432 heads from 1000 coin tosses  ? 
'''



flips = 1000
total_perm = 0
for heads in range( nr_of_heads, flips+1) :
    perm =  fac(flips ) / ( fac(heads)*fac(flips-heads ) )
    total_perm += perm
    # print('heads = ', heads ,'      perm= ', perm , '       total_perm = ' ,  total_perm )

print('\ntotal_perm = ', total_perm)

# What is the probability to hit EXACTLY 432 heads from 1000 coin tosses  ?
Probability =  total_perm / (2**flips)
print('\nProbab of 432 H in 1000 flips   = ',    format(Probability, '.12f') ,'               P =   ', Probability   )

###### ANSWER :     Probab of 432 H in 1000 flips   =  0.999992836187                        Completed in : 86.004734 ms

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
