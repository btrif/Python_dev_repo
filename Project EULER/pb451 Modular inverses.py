#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                    Modular inverses        -   Problem 451

Consider the number 15.
There are eight positive numbers less than 15 which are coprime to 15: 1, 2, 4, 7, 8, 11, 13, 14.
The modular inverses of these numbers modulo 15 are: 1, 8, 4, 13, 2, 11, 7, 14
because
1*1 =1 mod 15=1
2*8 = 16 mod 15=1
4*4 = 16 mod 15=1
7*13 = 91 mod 15=1
11*11 = 121 mod 15=1
14*14 = 196 mod 15=1

Let I(n) be the largest positive number m smaller than n-1 such that the modular inverse of m modulo n equals m itself.
So I(15)=11.
Also I(100)=51 and I(7)=1.

Find ∑I(n) for 3 ≤ n ≤ 2*10**7

'''
import time
from math import gcd

import itertools


def egcd(a, b):
    '''     Extended Euclidian Algorithm    '''
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    '''Modular multiplicative inverse function   '''
    g, x, y = egcd(a, m)
    if g != 1:
        # raise Exception('modular inverse does not exist')
        return -1
    else:
        return x % m

class PrimeTable():    #  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
    def __init__(self, bound):
        self.bound = bound
        self.primes = []
        self._sieve()

    def _sieve(self):
        visited = [False] * (self.bound + 1)
        visited[0] = visited[1] = True
        for i in range(2, self.bound + 1):
            if not visited[i]:
                self.primes.append(i)
            for j in range(i + i, self.bound + 1, i):
                visited[j] = True
        print('Prime count:', len(self.primes))

class Factorization():

    ''' Based on a prebuilt prime sieve, and we must pay attention that the prime up range is not
    to low, so that we don't miss a prime when we first factor . As default the value is set to 10.000
      So we need uprange /2         '''
    def __init__(self):
        self.prime_table = PrimeTable(10**4)

    def get_divisors(self, n):
        d = n
        f = {}
        for p in self.prime_table.primes:
            if d == 1 or p > d:
                break
            e = 0
            while d % p == 0:
                d = d // p
                e += 1
            if e > 0:
                f[p] = e
        if d > 1:
            f[d] = 1
            #raise Exception('prime factor should be small', d)
        unpacking = [[p**e for e in range(f[p] + 1)] for p in f]
        return sorted([self._product(divisor) for divisor in itertools.product(*unpacking)])

    def _product(self, list):
        result = 1
        for number in list:
            result *= number
        return result


F  = Factorization()
print( F.get_divisors(360) )


print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def brute_force_understanding( up_lim) :
    S=0
    for n in range(3, up_lim +1) :
        for i in range(n-2 , 0, -1 ) :      # Decreasing sequence
            if gcd(n , i) == 1 :
                m_inv =  modinv(i, n)
                # print(str(i)+'.    ' ,  m_inv )
                if m_inv == i :
                    print(str(n)+'.        LMI :      ', m_inv ,'*', i ,' ( mod', n,') = 1          I( '+str(n)+' )= ', i  )
                    S += m_inv
                    break
    return print('\n Total sum = ', S)

brute_force_understanding(1000)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

### 2017-02-21, 22:00
# IDEA : We need to find a square which (mod n) == 1. Example
#             27**2 (mod 52) ==1
#             51**2 (mod 100) ==1
#             503**2 (mod 753) ==1
#               1*1 (mod 751) == 1 ==> 751 does not have a != 1 modulo inverse
# There are numbers which have more mods : Like :
#                 281**2 ---> has (mod 470) and (mod 329) == 1
# 912.         LMI :  799  corresponding to :  799
# 950.         LMI :  799  corresponding to :  799

# Must build some kind of SIEVE, CHINESE REMAINDER THEOREM

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

# up_lim = 1000
# sieve = [1] * ( up_lim+1 )
# sieve[0:4] = [0]*3
# print(sieve[:30])
# for n in range(3, up_lim+1) :
#     nn1 = n*n-1
#     L = F.get_divisors( nn1 )
#     print(str(n)+'.    ',  L)






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
