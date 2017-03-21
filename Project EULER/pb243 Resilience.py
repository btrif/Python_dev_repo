#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Fri, 27 Jan 2017, 20:20
#The  Euler Project  https://projecteuler.net
'''
                                                        Resilience      -   Problem 243
A positive fraction whose numerator is less than its denominator is called a proper fraction.
For any denominator, d, there will be d−1 proper fractions;
for example, with d = 12:
1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d),
to be the ratio of its proper fractions that are resilient; for example, R(12) = 4/11 .

In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .

Find the smallest denominator d, having a resilience R(d) < 15499/94744 .

'''
import time
from math import gcd
import gmpy2
import numpy as np
import sympy



def primesieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!

    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]


def sieve(n):       # SECOND FASTEST
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def R(d):
    o = 0
    for i in range(1, d, 2):
        if gcd (i,d) ==1:
            o+=1
    return (o, d-1 )

print('\nResilience R(d) : \t', R(12))

# for i in range(10**4, 10**6 , 4):
#     if  R(i)[0]/R(i)[1] < target :
#         print(i, '     ', R(i))
#     if i% 10**4 == 0 : print(i)
print(gmpy2.mpq(6 ,9 ))

print('\n--------------------------TESTS------------------------------\n')
t1  = time.time()

lim = 20
primes = sieve(10**1)
print(len(primes), primes[:100])


# id = np.nonzero(primes == 5)
# id = primes.index(5)
# print('Numpy find index of a item : ' ,id, primes[:id])

N=[0]+[1]*(lim-1)

for p in primes :
    k = 1
    i  = 2*p
    while i < lim :
        id = primes.index(p)
        if p>2 :
            for p2 in primes[:id] :
                if i % p2 != 0 :

                    N[i]+=k
        else : N[i]+=k
        i+=p
        k+=1

print('N[12] = ',N[12])

print('\n',N)






def get_resilient_denom(nr):
    I=[]
    for i in range(nr):
        if gcd(i, nr) ==1 :
            I.append(i)
    # print('\n', nr,   ' : ',len(I), I)
    return len(I)

print('\nget_resilient_denom  : ' ,get_resilient_denom(690) )
print('sympy.totient : \t', sympy.totient(690))


# for i in range(2,100) :
#     print(i, get_resilient_denom(i), sympy.totient(i) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()


def first_solution() :
    target = 15499/94744
    print('target : ',target, '\n')
    n = 2*3*5*7*11*13*17*19

    tot = sympy.totient(n)
    min_res = 1
    print('starting fraction : ', tot/(n-1),'\n')

    while True :
        tot = sympy.totient(n)
        if tot/(n-1) < min_res :
            print(str(n)+'.         current: ', tot/(n-1) , '             target =  ', target)
            min_res = tot/(n-1)
        if tot/(n-1) < target :
            return print('\n Solution :   '+str(n)+'       with totient = '+str(tot) ,'        and resilience =  ', tot/(n-1))

        n += 2*3*5*7*11*13*17*19

first_solution()    #


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()


# About 0.3 ms in Python.
# I use the same ideas as many here, noting that R(d)=ϕ(n)/n−1≈ϕ(n)/n for large n,
# and so is a function only of the prime factors of n, independent of the exponents of those factors.
# The denominator will be minimised if n is a primorial.
# Thus we look for the smallest primorial number for which ϕ(n)n<15499/94744
# and then multiply that successively by 2 until ϕ(n)/n−1<15499/94744,
# knowing that in doing so we will not change the value of ϕ(n)/n.


import time
import numpy as np

def p243():

    primes=primesieve(100)
    Rtrial=1
    i=0
    while et(Rtrial)/Rtrial>15499/94744:
        Rtrial*=primes[i]
        i+=1
    while et(Rtrial)/(Rtrial-1)>15499/94744:
        Rtrial*=2
    print(Rtrial)


def primesieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

#Euler totient is number of integers m 1 <= m <=n that are coprime with n
def et(n):
    """returns Euler totient (phi) of n """
    phi=n
    pfs=set(prime_factors(n))
    for pf in pfs:
        phi*=(1-1/pf)
    return int(phi)

def prime_factors(n):
    """returns the prime factors of n"""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


p243()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
