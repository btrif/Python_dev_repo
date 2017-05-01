#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
        (prime-k) factorial         -       Problem 381

For a prime p let S(p) = (∑(p-k)!) mod(p) for 1 ≤ k ≤ 5.

For example, if p=7,
(7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! = 720+120+24+6+2 = 872.
As 872 mod(7) = 4, S(7) = 4.

It can be verified that ∑S(p) = 480 for 5 ≤ p < 100.

Find ∑S(p) for 5 ≤ p < 10**8.
'''

import time
from math import factorial
from gmpy2 import is_prime, mpq, fac


def prime_generator(lower, upper):      #THIRD FASTEST
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.         """
    cand = [i for i in range(3, upper + 1, 2)]
    end = int(upper ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (upper // cand[i]) - (upper // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [ i for i in cand if i and i > lower ]


def brute_force_Sp(p):
    '''(prime-k) factorial (mod p)
    :return:  For example, if p=7,
            (7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! = 720+120+24+6+2 = 872.
            and 872 % 7 = 4    '''
    S=0
    for k in range(1, 6):
        S+= ( fac(p-k))%p
        print('fac', p-k, '=', fac(p-k) , '   ;     mod', p ,'=' ,  ( fac(p-k))%p   )
    return S%p
    # return  sum([ (gmpy2.fac(p-k))%p for k in range(1,6) ])%p


def Sp(p):
    '''(prime-k) factorial (mod p)
    :return:  For example, if p=7,
            (7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! = 720+120+24+6+2 = 872.
            and 872 % 7 = 4    '''
    # a = p-1
    # print(a)
    # for i in range(2, 6) :
    #     a+=p
    #     a-= (p-i ) % 7
    #     print(a, p-i, (p-i ) % 7)
    # return a%p
    return  ( -1  - mpq(1, p-1 )  - mpq(1, (p-1)*(p-2) ) - mpq(1, (p-1)*(p-2)*(p-3) )  - mpq(1, (p-1)*(p-2)*(p-3)*(p-4) )            )


# fac 6 = 720    ;     mod 7 = 6
# fac 5 = 120    ;     mod 7 = 1
# fac 4 = 24    ;     mod 7 = 3
# fac 3 = 6    ;     mod 7 = 6
# fac 2 = 2    ;     mod 7 = 2
# Sp : 	 4

#### @ 2017-02-27 - Got that for the prime p first  p-1 (mod p ) is p-1, 2-nd p-2 is always 1
# and 3-rd p-3 is always p-1/2 (p-1 is always even). I need to find the rest of two p-4 and p-5
# I can do the DIRECT OPERATION STARTing from p-5 but I can't find the inverse operation
https://kshandilya.wordpress.com/2014/05/02/hacking-project-euler-problem-381/
Wilson Theorem


# print('gmpy2 fac : \t',gmpy2.fac(7) ,'\n')

lim = 10**2
primes = prime_generator(4, lim )
print(len(primes), primes[:50])

S = 0
for p in primes :
    x = brute_force_Sp(p)
    print('p= ', p, '        Sp = \t', x  , '          ', Sp(p) ,'\n')
    S+= x

print('\nAnswer : ', S)

# print('Sp : \t', Sp(19))




print('\n--------------------------TESTS------------------------------')
t1  = time.time()





# cnt = 0
# SUM = 0
# for p in primes :
#     cnt+=1
#     if cnt % (2*10**5) == 0 :
#         print(str(cnt)+'.    ', p, Sp(p)  )
#     SUM += Sp(p)
#
# print('\nAnswer : \t', SUM)



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
