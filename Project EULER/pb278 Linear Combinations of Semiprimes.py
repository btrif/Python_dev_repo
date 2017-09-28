#  Created by Bogdan Trif on 08-09-2017 , 11:55 PM.

# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Linear Combinations of Semiprimes       -       Problem 278

Given the values of integers 1 < a1 < a2 <... < an, consider the linear combination
q1a1 + q2a2 + ... + qnan = b, using only integer values qk ≥ 0.

Note that for a given set of ak, it may be that not all values of b are possible.
For instance, if a1 = 5 and a2 = 7, there are no q1 ≥ 0 and q2 ≥ 0 such that b could be
1, 2, 3, 4, 6, 8, 9, 11, 13, 16, 18 or 23.
In fact, 23 is the largest impossible value of b for a1 = 5 and a2 = 7.
We therefore call f(5, 7) = 23.
Similarly, it can be shown that f(6, 10, 15)=29 and f(14, 22, 77) = 195.

Find ∑ f(p*q,p*r,q*r), where p, q and r are prime numbers and p < q < r < 5000.
'''


import numpy as np

def test1(a1, a2) :
    S = []
    for q1 in range(0, 11):
        for q2 in range(0,11) :
            print("q1 = ", q1, "  ; q2 = ", q2 ,"           res  = ", a1*q1+a2*q2)
            S.append( a1*q1 + a2*q2 )

    S.sort()
    print('\n',S)

# test1(a1 = 5, a2 = 7)

def test2(a1, a2, a3) :
    S = []
    for q1 in range(0, 11):
        for q2 in range(0,11) :
            for q3 in range(0,11) :
                print("q1 = ", q1, "  ;  q2 = ", q2 , " ;  q3 = ", q3 ,"           res  = ", a1*q1+a2*q2+a3*q3 )
                S.append( a1*q1+a2*q2+a3*q3 )

    S.sort()
    S = set(S)
    print('\n',S)

# test2( a1 = 6, a2 = 10, a3 = 15)
test2( a1 = 14, a2 = 22, a3 = 77)


1. Generate the 3 combinations of primes like 2,3,5 ; 5,7,11 ...etc...for
2.  form the pq, pr, qr numbers
3. for each investigate only the numbers bigger then largest number which are primes and which are not