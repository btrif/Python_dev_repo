#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
            Twenty-two Foolish Primes           -           Problem 239

A set of disks numbered 1 through 100 are placed in a line in random order.

What is the probability that we have a partial derangement such that exactly 22 prime number discs
are found away from their natural positions?
(Any number of non-prime disks may also be found in or out of their natural positions.)

Give your answer rounded to 12 places behind the decimal point in the form 0.abcdefghijkl.

'''
# from __future__ import division
import time, zzz, gmpy2
from operator import mul
from functools import reduce


# @ 2017-03-23, 20:00      -       ANALYSIS OF THE PROBLEM, Undestanding !!!
# 1. There are 25 primes in 100 from which we need de-arranged only 22.
# 2. It doesn't matter the non-primes number if they are arranged / de-arranged
# Instead it matters that the 3 leftovers primes must be arranged !!! This is very important !!!
# 3. The probability that we have a prime ARRANGED . Example for a list [1,2,3] we have that P(k=1) in place = 1/3
# Probability that we have P(k=2) numbers in place is = 1/3 * 1/2 =1/6
#



print('\n------------------------ TESTS------------------------------')
t1  = time.time()


# def P(n, m, k) :
#     ''':Description:
#     Probability that, in a lineup of n integers,     the first m are in order, the next k are not
#
#     :param n: int, total numbers , our case n =100
#     :param m: the numbers which are correctly arranged, there are 3 primes at correct position => m=3
#     :param k:  int , the number of de-arranged prime numbers. Our case k = 22
#     :return: total probability that we have a DE-ARRANGEMENT of k elements from a total of n elements
#     '''
#     num = [ n-m-i for i in range(1, k+1) ]
#     den = [ n-m for i in range(1, k+1) ]
#     num = reduce(mul, num)
#     den = reduce(mul, den)
#     den *= n**m
#     print('num = ',num, '       den=',den,'\n')
#     res = num/den
#     return  res          # Rounded to 12 decimal places !
#
#
# n, m, k = 100, 3, 22
# perm = reduce(mul, [ (m+k-i)/ (i+1) for i in range(m)  ] )
# print(perm, [(25-i)  for i in range(m)]  )
# res = perm * P(n, m, k)
# res = "{:.12f}".format(float(res) )
# print(' Total Probability that EXACTLY '+str(k)+
# ' primes from the first '+str(n)+' numbers are DE-ARRANGED   :\n ', res  )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

# IDEAS  :
# https://en.wikipedia.org/w/index.php?title=Derangement&action=edit&section=2
# http://oeis.org/wiki/Number_of_derangements
# http://math.stackexchange.com/questions/17320/derivation-of-the-partial-derangement-rencontres-numbers-formula

# Example
#
# You have 6 balls in 6 different colors, and for every ball you have a box of the same color.
# How many derangements do you have, if no ball is in a box of the same color?
# !6 = 6!\cdot\left(1-\frac{1}{1!}+\frac{1}{2!}-\frac{1}{3!}+\frac{1}{4!}-\frac{1}{5!}+\frac{1}{6!}\right) = 265
#
# ========   Partial Derangement   ===========
# A permutation of n distinct, ordered items in which none of the items is in its original ordered position is known as a derangement.
# If some, but not necessarily all, of the items are not in their original ordered positions,
# the configuration can be referred to as a partial derangement (Evans et al. 2002, p. 385).
#
# Among the n! possible permutations of n distinct items,
# examine the number R(n,k) of these permutations in which exactly k items are in their original ordered positions. Then
#
# R(n,n)	=	1
# R(n,n-1)	=	0
# R(n,k)	=	comb(n ; k) !(n-k)

def R(n,k):
    ''' Determine the number R(n,k) of these permutations in which exactly
    k items are in their original ordered positions
    :param n:
    :param k:
    :return:                                                                        '''
    from gmpy2 import comb, fac
    return comb(n, k)* fac(n-k)

def Dearrangements( n ):
    '''A000166 Subfactorial or rencontres numbers, or derangements:
    number of permutations of n elements with no fixed points.
            {1, 0, 1, 2, 9, 44, 265, 1854, 14833, 133496, 1334961, 14684570, 176214841, 2290792932, ...}
    :param n: int
    :return: int                                                                    '''
    from math import factorial, e
    return int(factorial(n)/e + 0.5)

# In our case there are 3 ordered primes from 100

D = [  Dearrangements( 22 +i )*gmpy2.comb(75, i) for i in range(1, 75+1)]
print(D)
D = sum(D)
res =  D* gmpy2.comb(25,3)  / gmpy2.fac(100)

print('\nAnswer : \t',  "{:.12f}".format(float(res) ) )

### FAILED
### 0.000000060392          #  100*99*98
# 0.000000058593            # 100**3
#   0.000134762752





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

