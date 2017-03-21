#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                Semidivisible numbers           -       Problem 234

For an integer n ≥ 4, we define the lower prime square root of n, denoted by lps(n),
as the largest prime ≤ √n and the upper prime square root of n, ups(n), as the smallest prime ≥ √n.

So, for example, lps(4) = 2 = ups(4), lps(1000) = 31, ups(1000) = 37.
Let us call an integer n ≥ 4 semidivisible, if one of lps(n) and ups(n) divides n, but not both.

The sum of the semidivisible numbers not exceeding 15 is 30, the numbers are 8, 10 and 12.
15 is not semidivisible because it is a multiple of both lps(15) = 3 and ups(15) = 5.
As a further example, the sum of the 92 semidivisible numbers up to 1000 is 34825.

What is the sum of all semidivisible numbers not exceeding 999966663333 ?


'''
import time, gmpy2, zzz, math
import sympy


def numpy_prime_sieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    import numpy as np
    """return array of primes 2<=p<=n"""
    sieve=np.ones( n+1, dtype=bool )
    for i in range( 2, int((n+1)**0.5+1) ) :
        if sieve[i] :
            sieve[2*i :: i] = False
    return np.nonzero(sieve)[0][2:]


print(sympy.prevprime(4))








print('\n--------------------------TESTS------------------------------')
t1  = time.time()

UP_NR = 999966663333
print('Square root of UP_NR : \t', math.sqrt(UP_NR),'\n'  )     # 1 milion is affordable :) !

So we need a sieve up to 10**6, EASY PROBLEM !!!!


def brute_force_testing(lim) :
    S, cnt = 0, 0
    for n in range(7, lim+1):
        if gmpy2.is_square(n) : continue
        sqd = math.floor((n**(1/2)))
        squ = math.ceil((n**(1/2)))
        # print(sq)
        lps = sympy.prevprime(squ)
        ups = gmpy2.next_prime(sqd)
        if (n%lps !=0 and n%ups == 0) or (n%lps ==0 and n%ups != 0)  :
            cnt += 1
            print(str(cnt)+'.     n=', n , '    lps=',lps, '      ups=',ups  )
            S+=n

    return print('\nAnswer : \t', S)

brute_force_testing(1000)


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
