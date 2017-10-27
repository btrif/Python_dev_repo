#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Fri, 13 Oct 2017, 00:04
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

import numpy
def prime_sieve_numpy(n):                       ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    """ Input n>=6, Returns a array of primes, 2 <= p < n
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188 """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[ ((3*numpy.nonzero(sieve)[0][1:]+1)|1) ]



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


def brute_force_Sp(p):
    '''(prime-k) factorial (mod p)
    :return:  For example, if p=7,
            (7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! = 720+120+24+6+2 = 872.
            and 872 % 7 = 4    '''
    S=0
    p = int(p)
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
    p = int(p)
    r1 = p-1
    r2 = 1
    r3 = (p-1)//2
    r4 = modinv((p-2)*(p-3), p )
    r5 = modinv((p-2)*(p-3)*(p-4), p )

    return  (r1+r2+r3+r4+r5)%(p)


# fac 6 = 720    ;     mod 7 = 6
# fac 5 = 120    ;     mod 7 = 1
# fac 4 = 24    ;     mod 7 = 3
# fac 3 = 6    ;     mod 7 = 6
# fac 2 = 2    ;     mod 7 = 2
# Sp : 	 4

#### @ 2017-02-27 - Got that for the prime p first  p-1 (mod p ) is p-1, 2-nd p-2 is always 1
# and 3-rd p-3 is always p-1/2 (p-1 is always even). I need to find the rest of two p-4 and p-5
# I can do the DIRECT OPERATION STARTing from p-5 but I can't find the inverse operation
# https://kshandilya.wordpress.com/2014/05/02/hacking-project-euler-problem-381/
# Wilson Theorem


# print('gmpy2 fac : \t',gmpy2.fac(7) ,'\n')

lim = 10**2

primes = prime_sieve_numpy(lim)[2:]
print(len(primes), primes[:50])

S = 0
for p in primes :
    x = brute_force_Sp(p)
    print('p= ', p, '      BF  Sp = \t', x  , '           Calc :   ', Sp(p) ,'\n')
    S += x

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

print('\n=============  My FIRST SOLUTION,  WILSON  THEOREM ===============\n')
t1  = time.time()



def prime_k_factorials( lim ) :
    primes = prime_sieve_numpy( lim )
    print(primes[:100])
    S = 0
    for p in primes :
        k  = Sp(p )
        # print(str(p)+'.       prime_k =    ', k   )
        S += k

    return print('\nResult : \t', S )

# prime_k_factorials(10**8)         #   139602943319822


t2  = time.time()
print('\nCompleted in :', round((t2-t1), 4 ), 's\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# === Fri, 12 May 2017, 15:48, MY FRIEND, mbh038, England
# In my first analysis, for each prime pp I expressed the sum over (p−k)! as the product of a single factorial (p−5)!
# and a polynomial in pp, and then used Wilson's theorem to calculate the factorial.
# This works, but takes 56s in Python and involves terms up to p4.
# I couldn't get it to work in C++.
# dawghaus's method (above) is much neater. We can use Wilson's theorem to factor out (p−1)!
# from each sum of factorials in S(p)S(p) and show  (remarkably!) that
# S(p)=(−3/8) (mod p)
#
# With this, I get the answer in 18 s in Python and about 5.4s in C++.

import time
import numpy as np

def p381(limit):
    t=time.clock()
    primes=primeSieve(limit)
    ssum=0
    for p in primes[2:]:
        ssum+=(-3*inverse(8,p))%p
    print (ssum)
    print(time.clock()-t)

#returns multiplicative inverse of a mod n. a and n must be-co-prime
def inverse(a, n):
    t1,t2=0,1
    r1,r2=n,a
    while r2!=0:
        q = r1 // r2
        t1, t2 = t2, t1 - q * t2
        r1, r2 = r2, r1 - q * r2
    if t1 < 0:
        t1 +=n
    return t1

#returns array of primes 2<=p<=n
def primeSieve(n):
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

#Uses Wilson's theorem to return n! mod n with only m-n-1 multiplications and one inverse
#not used in the end
def fnmWilson(n,m):
    prod=-1
    for i in range(n+1,m):
        prod=(prod*i)%m
    return inverse(prod,m)


p381(10**8)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
