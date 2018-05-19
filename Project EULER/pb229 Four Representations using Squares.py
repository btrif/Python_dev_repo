#  Created by Bogdan Trif on 15-10-2017 , 10:20 PM.
# © o(^_^)o  Solved by Bogdan Trif  @   Completed on Tue, 17 Oct 2017, 09:05
#The  Euler Project  https://projecteuler.net
'''
                        Four Representations using Squares          -           Problem 229

Consider the number 3600. It is very special, because

3600 = 482 +     362

3600 = 202 + 2×402

3600 = 302 + 3×302

3600 = 452 + 7×152

Similarly, we find that 88201 =
992 + 2802 =
2872 + 2×542 =
2832 + 3×522 =
1972 + 7×842.

In 1747, Euler proved which numbers are representable as a sum of two squares.
We are interested in the numbers n which admit representations of all of the following four types:

n = a_1^2 +   b_1^2

n = a_2^2 + 2 b_2^2

n = a_3^2 + 3 b_3^2

n = a_7^2 + 7 b_7^2,

where the a_k and b_k are positive integers.

There are 75373 such numbers that do not exceed 10^7.
How many such numbers are there that do not exceed 2×10^9?

'''
import time, zzz
from math import sqrt
import numpy as np
import sys

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
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

print('\n--------------------------TESTS------------------------------')
t1  = time.time()




t2  = time.time()
print('\n# Completed in :', round((t2-t1) , 2), 's\n\n')


# === GENERAL IDEA ====
# It can be done with :
# https://en.wikipedia.org/wiki/Legendre_symbol

# ==== Sun, 25 Jan 2009, 21:38, zeycus, Spain
# Very nice and hard to me. My solution is similar to tolstopuz's and Balakrishnan's.
# Analogously to Lagrange's proof in
# Wikipedia,
# I found that the primes that can be written as x^2 + k*y^2 are those for which the Jacobi symbol (p-k over p) = 1.
# Combining conditions for k=1,2,3,7, I found that p should have residue 1, 25 or 121 modulo 168.
# Then, the numbers n that can be written as x_k^2 + k * y_k^2 for k = 1,2,3,7
# are those whose prime factors of odd exponent have all residue 1, 25 or 121 modulo 168.
#
# So, I built all those numbers using Miller-Rabin (about 20 min in my slow PC, in Python),
# then computed all the products below 2*10^9, and for each one,
#     I divided to find how many squares I could use with that number.
#     For example, with 193 there are sqrt(2*10^9 / 193) = 3219.
#
# Using that I was getting about 77000 solutions below 10000000, instead of the 75373.
# After a while I found the reason: in the problem, the values for x and y must be positive.
# This means that some squares should not be
# counted, but others like 60^2 = 3600 must.
# I found that for the equation x^2 + k*y^2 = z^2 we can use
# generator x = k*c^2-d^2, y = 2*c*d and z = k*c^2 + d^2, where gcd(c,d) = 1 and x > 0.
# Those are not all primitive, but anyway it allowed me to calculate exactly which squares must be counted as solutions,
# and find the answer.


# ===Fri, 26 Feb 2010, 12:34, siva k d, USA
# Same as zeycus. After using a lot of memory and 38 minutes of time to solve,
# I posted it in the public forum and hk responded that it can be done in about 10 seconds.
# So, that's when I started more research and ended up here and till then I was using mod 24 and then realized
# I can use mod 168 and so I did 3 modulo sieves (for 1, 25 and 121).
#
# My final solution runs in 38 seconds. I thought that the solutions where n is a square are easy and won't take much time.
# But, actually these square n solutions cost me 32 seconds and the others using the modulo 168 only 6 seconds.
# For the squares, after using p^2+[7,3,2,1]q^2 values,
# I found lcm of those and that's where the computation got expensive.

# === Fri, 4 May 2012, 05:15, ving, USA
#
# I am about 40 months late -- my program has just came back with the answer... :)
# Seriously, my solution is similar to tolstopuz's on Page 1 who "found a smart solution."
#
# Suppose n = r^2*s, where s is square free, s > 1.
# n = a^2 + b^2 iff s has only prime factors of the form 4k+1.
# n = a^2 + 2b^2 iff s has only prime factors of the form 8k+1 or 8k+3.
# n = a^2 + 3b^2 iff s has only prime factors of the form 6k+1.
# n = a^2 + 7b^2 iff s has only prime factors of the form 7k+1 or 7k+2 or 7k+4.
# To satisfy the first three conditions, s must have only prime factors of the form 24k+1.
# Among these primes, the smallest ones of the form 7k+1, 7k+2 and 7k+4 are p1 = 337, p2 = 457,
# and p4 = 193, respectively.  All others fall into the progressions p1+168k, p2+168k, and p4+168k (168=24*7).
# We can quickly find all primes in an arithmetic progression using a sieve:
#
#
# The list of acceptable primes is not too long, and they are pretty big,
# so we can generate quickly all the possible values for the square free part of n under 2*10^9
# by taking one of them or the product of two or three:
#
#
# There are additional solutions when n = r^2 (s = 1).  In that case, r is under sqrt(2*10^9) -- not too big;
# we can get its prime factors.  r^2 is a solution iff r has at least one "4k+1" prime factor;
# an "8k+1" or "8k+3" prime factor; a 2 or a "6k+1" prime factor;
# and is divisible by 4 or has a "7k+1" or "7k+2" or "7k+4" prime factor:

print('\n================  My FIRST SOLUTION,  5 hours ===============\n')
t1  = time.time()


def my_first_solution(lim) :

    sieve = np.ones(lim, dtype=int)

    for a in range(1, int(sqrt(lim))*2  ) :
        sys.stdout.write('\r' + str(a) +'              '+  str(round((time.time() - t1),2)) +'  sec'   )   # Font Segoe UI Semibold
        b = 1
        while (a*a+b*b) < lim  :
            n1 = a*a + b*b

            n2 = a*a + 2 *b*b
            n3 = a*a + 3 *b*b
            n7 = a*a + 7 *b*b

            if sieve[n1] % 5 != 0 : sieve[n1] *= 5

            if n2 < lim :
                if sieve[n2] % 2 != 0 : sieve[n2] *= 2
            if n3 < lim :
                if sieve[n3] % 3 != 0 : sieve[n3] *= 3
            if n7 < lim :
                if sieve[n7] % 7 != 0 : sieve[n7] *= 7

            # if n1==3600 or n2==3600 or n3==3600 or n7==3600 :
            #     print('3600 =   ' ,a, b , '    k = ', (3600-(a*a))//(b*b) )

            b+=1

    cnt2 = np.sum(sieve == 210 )    # This counts all the elements which have 210 value
    print( np.where( sieve == 210 ) )
    return print('\nResult = ',  cnt2 )

# my_first_solution(2*10**9+1)                Result =  11325263          # Completed in : 17041.36 s



t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,     IMPRESSIVE , 38 sec    --------------------------')
t1  = time.time()

# ==== Sat, 24 Jan 2009, 17:28, tolstopuz, Russia
# It seems that I have found a smart way. 41 sec on E8400. It should be less than 5 secs in C++.

# I'll try to explain.
#
# If x is a square, we can factor it and then test as in demonc post.
#
# If x is not a square, its squarefree part must consist of primes congruent to 1, 25 or 121 (mod 168),
# because p = 1, 3 (mod 8), p = 1 (mod 6) and p = 1, 9, 11 (mod 14).
#
# To generate all such prime factors I create three sieves and for each prime p not exceeding sqrt(n)
# calculate the pattern that p is "printing" on the sieves and then repeat this pattern.
#
# Next I must find all squarefree combinations of these primes.
# There are two categories: having zero factors > sqrt(n) and having one factor > sqrt(n).
# But first category is small and can be computed by a small sieve up to sqrt(n) and brute force combining.
# And any number from second category is simply a number from first category multiplied once by a prime > sqrt(n).
#
# And last, for each combination q I count all its square multiples: [sqrt(n / q)].


import math

nmax = 2 * 10 ** 9

ns = int(math.sqrt(nmax))

primes = (ns + 1) * [True]

primes[0:2] = [False,False]

s = [1]

for x in range(2, len(primes)):
    if primes[x]:
        for y in range(2 * x, len(primes), x):
            primes[y] = False
        if x % 168 in (1, 25, 121):
            for j in range(len(s)):
                if x * s[j] > nmax:
                    break
                s.append(x * s[j])
        s.sort()

p = [x for x in range(len(primes)) if primes[x]]

def factor(x):
    factors = {}
    for q in p:
        if q * q > x:
            break
        i = 0
        while x % q == 0:
            x //= q
            i += 1
        if i:
            factors[q] = i
    if x > 1:
        factors[x] = 1
    return factors

cc = sum(int(math.sqrt(nmax // x)) for x in s[1:])

pp = {d:[True for i in range(nmax // 168 + 1)] for d in (1, 25, 121)}

for x in p:
    for k in range(0, x * 168, x):
        q, r = divmod(k, 168)
        if r in pp:
            pq = pp[r]
            for y in range(0, len(pq) - q, x):
                pq[y+q] = False

sq = [int(math.sqrt(x)) for x in range(ns + 1)]

for y, pq in pp.items():
    z = y
    for x in range(len(pq)):
        if pq[x] and ns < z <= nmax:
            for j in s:
                k = sq[nmax // (z * j)]
                if not k:
                    break
                cc += k
        z += 168

for x in range(1, ns + 1):
    f = factor(x)
    if any(x for x in f if x % 4 == 1) and \
       any(x for x in f if x == 3 or x % 8 in (1, 3)) and \
       any(x for x in f if x == 2 or x % 6 == 1) and \
       any(x for x in f if x == 2 and f[2] >= 2 or x % 14 in (1, 9, 11)):
        cc += 1

print(cc)




t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Sun, 25 Jan 2009, 21:38, zeycus, Spain
# Very nice and hard to me. My solution is similar to tolstopuz's and Balakrishnan's.
# Analogously to Lagrange's proof in
# Wikipedia,
# I found that the primes that can be written as x^2 + k*y^2 are those for which the Jacobi symbol (p-k over p) = 1.
# Combining conditions for k=1,2,3,7, I found that p should have residue 1, 25 or 121 modulo 168.
# Then, the numbers n that can be written as x_k^2 + k * y_k^2 for k = 1,2,3,7
# are those whose prime factors of odd exponent have all residue 1, 25 or 121 modulo 168.
#
# So, I built all those numbers using Miller-Rabin (about 20 min in my slow PC, in Python),
# then computed all the products below 2*10^9, and for each one,
#     I divided to find how many squares I could use with that number.
#     For example, with 193 there are sqrt(2*10^9 / 193) = 3219.
#
# Using that I was getting about 77000 solutions below 10000000, instead of the 75373.
# After a while I found the reason: in the problem, the values for x and y must be positive.
# This means that some squares should not be
# counted, but others like 60^2 = 3600 must.
# I found that for the equation x^2 + k*y^2 = z^2 we can use
# generator x = k*c^2-d^2, y = 2*c*d and z = k*c^2 + d^2, where gcd(c,d) = 1 and x > 0.
# Those are not all primitive, but anyway it allowed me to calculate exactly which squares must be counted as solutions,
# and find the answer.


from __future__ import division
from math import gcd, sqrt
from gmpy2 import is_prime


def sqrtFloor(n):
    x = sqrt(n)
    x = 1 + int(round(x))
    while x**2 > n:
        x -= 1
    return x

def nbCases(n, b):
    return sqrtFloor(b/n)

def prods(xs, bound, cum=1, ind=-1):
    yield cum
    for nextInd in range(ind+1, len(xs)):
        nextCum = cum * xs[nextInd]
        if nextCum <= bound:
            for sol in prods(xs, bound, cum*xs[nextInd], nextInd):
                yield sol
        else:
            break

def validSquares(maxS, k):
    valid = set([])
    c = 1
    while k*c**2 <= maxS * 10:
        d = 1
        while True:
            if gcd(c,d) == 1:
                num = k * c**2 - d**2
                den = k * c**2 + d**2
                if num:
                    gc = gcd(num, den)
                    num //= gc
                    den //= gc
                    if den <= maxS:
                        aux = den
                        while aux < maxS:
                            valid.add(aux)
                            aux += den
            d += 1
            if d**2 >= k*c**2:
                break
        c += 1
    return valid

def countValidSquares(maxS):
    v1 = validSquares(maxS, 1)
    v2 = validSquares(maxS, 2)
    v3 = validSquares(maxS, 3)
    v7= validSquares(maxS, 7)
    found = v1 & v2 & v3 & v7
    return len(found)


# *********************** MAIN *************************
bound = 2000000000
basicPrimes = []
counter = 0
n = 1
while n <= bound:
    if is_prime(n):
        basicPrimes.append(n)
        counter += 1
        if counter % 1000 == 0:
            print (counter, n)
    n += 168
n = 25
while n <= bound:
    if is_prime(n):
        basicPrimes.append(n)
        counter += 1
        if counter % 1000 == 0:
            print (counter, n)
    n += 168
n = 121
while n <= bound:
    if is_prime(n):
        basicPrimes.append(n)
        counter += 1
        if counter % 1000 == 0:
            print (counter, n)
    n += 168
basicPrimes.sort()

numbers = []
counter = 0
for s in prods(basicPrimes, bound):
    if s > 1:
        nb = nbCases(s, bound)
        for i in range(1, nb+1):
            numbers.append(s * i**2)
        counter += nb
counter += countValidSquares(sqrt(bound))
print ('Solution:', counter)



t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')



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




