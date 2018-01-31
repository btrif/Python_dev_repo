#  Created by Bogdan Trif on 20-11-2017 , 10:30 PM.

# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                Fractional Sequences            -           Problem 343

For any positive integer k, a finite sequence ai of fractions xi/yi is defined by:
a_1 = 1/k and
a_i = (xi-1+1)/(yi-1-1) reduced to lowest terms for i>1.

When ai reaches some integer n, the sequence stops. (That is, when yi=1.)

Define f(k) = n.

For example, for k = 20:

1/20 → 2/19 → 3/18 = 1/6 → 2/5 → 3/4 → 4/3 → 5/2 → 6/1 = 6

So f(20) = 6.

Also            f(1) = 1, f(2) = 2, f(3) = 1 and
                Σf(k3) = 118937 for 1 ≤ k ≤ 100.

Find Σf(k3) for 1 ≤ k ≤ 2×10^6.


'''
import time, zzz
# from functools import lru_cache
# from gmpy2 import mpq
# from math import gcd

# import sys
# sys.setrecursionlimit(10**4)

def gcd(a, b):      # GCD
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

# @lru_cache(maxsize=None)
def f_rec(k):

    a1= [1, k ]
    xi, yi = 1, k

    def sequence( xi, yi ) :
        if gcd(xi, yi ) != 1 :
            g = gcd(xi, yi )
            xi, yi = xi//g, yi//g

        if  (xi/yi) %1 ==0 :
            return xi//yi

        return sequence( xi+1 , yi-1  )

    return sequence(xi, yi)


def f(k):

    xi, yi = 1, k

    while ( xi / yi ) %1 != 0 :
        if gcd(xi, yi ) != 1 :
            g = gcd(xi, yi )
            xi, yi = xi//g, yi//g

        if  (xi/yi) %1 ==0 :
            return xi//yi

        xi = xi+1
        yi = yi-1


    return xi// yi







print('f_rec test  =  ',  f_rec(34) )
print('f_rec test  =  ',  f_rec(173**3) )

print('f test  =  ',  f(34) )
print('f test  =  ',  f(173**3) )





print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def brute_force_concept(lim ) :
    W = 0
    for k in range(1, lim+1) :
    # for k in range(850000, lim+1) :
        fs = f(k**3)
        print(str(k) + '.       k^3 = ', k**3,  '       fs =    ' , fs  )
        W += fs

    print('\nAnswer : ', W )
    return W

brute_force_concept(10**2)

# IDEAS @2017-11-20
x^3+ 1 = (x+1) (x^2-x+1 )                   factorize smaller numbers

https://en.wikipedia.org/wiki/Fermat%27s_factorization_method



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

