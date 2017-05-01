#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Cardano Triplets            -           Problem 251

A triplet of positive integers (a,b,c) is called a Cardano Triplet if it satisfies the condition:

                (a + b* c **(1/2) )**(1/3) + (a - b* c **(1/2) )**(1/3) = 1

For example, (2,1,5) is a Cardano Triplet.

There exist 149 Cardano Triplets for which a+b+c ≤ 1000.

Find how many Cardano Triplets exist such that a+b+c ≤ 110,000,000.


'''
import time, zzz
import gmpy2
from math import floor

# http://math.stackexchange.com/questions/1885095/parametrization-of-cardano-triplet

#  (a + b* c **(1/2) )**(1/3) + (a - b* c **(1/2) )**(1/3) = 1
#
# can be written as :   ( http://www.wolframalpha.com/input/?i=((a%2Bbsqrt(c))%5E(1%2F3))+%2B+((a-bsqrt(c))%5E(1%2F3))+%3D+1 )
#
# 8*a**3 + 15*a**2 + 6*a - 27*b**2*c = 1
#
# That is really faster to compute for higher numbers than the previous form, but it goes up really
# fast and I need BigInteger (Java) that slows down again the code.
# I found on google that this formula can be parametrized with
# a = 3*k + 2
# and
# b**2* c= (k+1)**2 * (8*k+5)
# http://stackoverflow.com/questions/36727886/how-do-i-write-this-equation-in-python
# https://www.math.ucdavis.edu/~kkreith/tutorials/sample.lesson/cardano.html
# http://www.wolframalpha.com/input/?i=((a%2Bbsqrt(c))%5E(1%2F3))+%2B+((a-bsqrt(c))%5E(1%2F3))+%3D+1
# https://proofwiki.org/wiki/Cardano%27s_Formula
# https://en.wikipedia.org/wiki/Cubic_function#Cardano.27s_method

def is_cardano_triplet(a, b, c):
    return (a + 1)**2 * (8*a - 1) - 27*b**2*c == 0

print('is_cardano_triplet: \t' , is_cardano_triplet(2, 1, 5) )
print('is_cardano_triplet: \t' , is_cardano_triplet(5, 4, 13) )

is_square = lambda x :  int( x**(1/2) )**2 == x

def get_divisors(n):      ### ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST     MUST BE IMPROVED !! It is a sqrt(n) Algorithm
    from math import sqrt
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def brute_force( lim) :
    for a in range(1, lim ) :
        for b in range(1, a) :
            for c in range(b, lim) :
                if is_cardano_triplet(a,b,c) :
                    print(a, b, c ,'            ', is_cardano_triplet(a,b,c) ,'        bbc=', b**2*c)

# brute_force(100)
print('------------------------')



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

def first_solution( up) :
    S, cnt = 0, 0
    for k in range(10**5, up //5 ) :
        a = 3*k + 2
        bbc = (k+1)**2 * (8*k+5)
        D = get_divisors(bbc)
        # print(bbc,'       ',D)
        for b in D :
            c = bbc //(b*b)
            if is_cardano_triplet(a, b, c) :
                if a+b+c <= up :
                    cnt+=1
                    # if cnt%10**5 == 0 :
                    print(str(cnt)+'.            k= ', k, '       a, b, c = ', a, b, c,'          s= ', a+b+c,'        bbc= ',bbc )

    return print('\nAnswer : \t', cnt)

@ 2017-04-22 - For now this is FAR TOO SLOW
first_solution(11*10**7)
# first_solution(10**3)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
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
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

