#  Created by Bogdan Trif on 04-11-2017 , 11:59 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
Pivotal Square Sums             -           Problem 261

Let us call a positive integer k a square-pivot, if there is a pair of integers m > 0 and n ≥ k,
such that the sum of the (m+1) consecutive squares up to k equals
the sum of the m consecutive squares from (n+1) on:

(k-m)^2 + ... + k^2  = (n+1)^2 + ... + (n+m)^2.

Some small square-pivots are :

4:          3^2 + 4^2 = 5^2
21:         20^2 + 21^2 = 29^2
24:         21^2 + 22^2 + 23^2 + 24^2 = 25^2 + 26^2 + 27^2
110:       108^2 + 109^2 + 110^2 = 133^2 + 134^2

Find the sum of all distinct square-pivots ≤ 10^10.


'''
import time, zzz

# https://brilliant.org/wiki/sum-of-n-n2-or-n3/
# OBSERVATION : nr of right terms are = nr of left terms - 1              !!!!!
#
# BINARY SEARCH ! for the RHS terms
#


# Sum{k=1, n} ( k**2) = n*(n+1)*(2*n+1) / 6     So it starts with 1
Sum_squared_basic = lambda n :  n*(n+1)*(2*n+1) // 6

print('Sum_squared_basic = ', Sum_squared_basic( 4 ))

def Sum_squared(k, n) :
    ''':Description: returns Sum{k, n} (k^2)
        :Example: Sum{4, 7} (k^2) = Sum{1, 7} (k^2) - Sum{1, 3} (k^2)
    :param k:  int, the starting k number
    :param n: int, ending number
    :return: int, Sum{k, n} (k^2)           '''
    Sum_squared_basic = lambda n :  n*(n+1)*(2*n+1) // 6
    S1 = Sum_squared_basic(k-1)
    S2 = Sum_squared_basic(n)
    return S2 -  S1

print('Sum_squared = ' , Sum_squared(4,7) )
print('Verification : ' , sum(  [i*i for i in range(1,7+1)]) - sum( [i*i for i in range(1,3+1) ])    )


print('\n--------------------------TESTS------------------------------')
t1  = time.time()


print('Data problem verif : ', Sum_squared(21, 21+3) , Sum_squared(25, 25+2)   )



t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()





# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')




