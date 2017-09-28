#!/usr/bin/python
# Solved by Bogdan Trif    ( ͡° ͜ʖ ͡°)     @    Completed on Wed, 18 Jan 2017, 21:22
#The  Euler Project  https://projecteuler.net
'''
            Diophantine reciprocals II          -           Problem 110

In the following equation x, y, and n are positive integers.
                    1 / x  +  1 / y  =  1 / n

It can be verified that when n = 1260 there are 113 distinct solutions and this is the least value of n
for which the total number of distinct solutions exceeds one hundred.

What is the least value of n for which the number of distinct solutions exceeds four million (4*10**6)   ?

NOTE: This problem is a much more difficult version of Problem 108 and as it is well beyond the limitations
of a brute force approach it requires a clever implementation.


'''
import time
import functools, operator
import functools, operator
from pyprimes import factorise
import gmpy2

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def  calculate_divisors(nr):
    '''**©** Made by Bogdan Trif @ 2016-12-08, 16:30.
        :Description: Functions which computes the number of divisors of a number.
                It uses the Numbers of Divisors Theorem :which says : if N=a**x*b**y*c**z => divisors_nr=(x+1)(y+1)(z+1)
            Example: N = 216 = 2**3 * 3**3 => divisors_nr = (3+1)(3+1) = 16
    :param nr: int, nr
    :return: int, divisors_number    '''

    def factors(nr):
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        return [i for i in factorise(nr)]
    N = factors(nr)
    return  functools.reduce( operator.mul , [ (i[1]+1) for i in N ])


def Diophantine_Reciprocals(n):
    ''':Description: Function to get the Reciprocals of the Diophantine Equation **1/x  +  1/y  =  1/n**
    :param n:   n from Diophantine Eqn
    :return: int, the number of reciprocals    '''
    count = 0
    nsquared = n**2
    for i in range(1, n+1):
        if nsquared % i == 0:
            count += 1
    return count


print('\n--------------------------TESTS------------------------------')
t1  = time.time()


# L = [2, 19, 3,  5, 7, 11, 13 , 5 ,2, 17 ]
# n = functools.reduce(operator.mul, L )
n = 510510*2
print('Number to test : ', n)

print('\n Test for get_factors() Function :', get_factors(n))

print(' Diophantine_Reciprocals Function :\t' , Diophantine_Reciprocals(n) )
print(' calculate_divisors Function :\t' , calculate_divisors(n) )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n=============  My FIRST SOLUTION, Using aolea s algorithm, 2 min  ===============\n')
t1  = time.time()



import pyprimes
import sympy

def aolea_sol(n=10**3) :

    listResult = [2]
    divisors = 3
    solutions = 2
    flag = False
    i1 = 2
    while flag == False:
        listResult.append(pyprimes.nth_prime(i1))
        num = 1
        for i in listResult:
            num = num*i
        divisors = len(list(sympy.divisors(num**2)))
        solutions =(divisors-1)/2 + 1
        k1, k2, k3, k4 = 0 ,0, 0, 0
        if solutions > n:
            while   k1+1<= len(listResult) and listResult[-1] > listResult[k1]*listResult[k1+1] and int(round(solutions*25/27))>=n :
                    listResult.pop()
                    listResult.append(pyprimes.nth_prime(k3+1))
                    listResult.append(pyprimes.nth_prime(k3+2))
                    k3 = k3 + 2
                    k1 = k1 + 4
                    num = 1
                    for i in listResult:
                        num = num * i
                    divisors = len(list(sympy.divisors(num ** 2)))
                    solutions = (divisors - 1) / 2 + 1
                    listResult=sorted(listResult)
            while   k2+1<= len(listResult) and listResult[-1] > listResult[k2]*listResult[k2+1] and int(round(solutions*49/75))>= n :
                    listResult.pop()
                    listResult.append(pyprimes.nth_prime(k4+1))
                    listResult.append(pyprimes.nth_prime(k4+2))
                    k4 = k4 + 2
                    k2= k2 + 4
                    num = 1
                    for i in listResult:
                        num = num * i
                    divisors = len(list(sympy.divisors(num ** 2)))
                    solutions = (divisors - 1) / 2 + 1
                    listResult = sorted(listResult)
            print(n, 'Number : ',num, '       Solutions :',solutions, '    Divisors:',divisors,       '             List', listResult)
            flag = True
        i1 = i1 + 1

# aolea_sol(n = 4*10**6)

# Answer : 4.000.000 Number :  9350130049860600
# Solutions : 4018613.0     Divisors: 8037225              List [2, 2, 2, 3, 3, 3, 5, 5, 7, 7, 11, 13, 17, 19, 23, 29, 31, 37]

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')             #  Completed in : 115694.617271 ms

############## GENERAL IDEAS #################
# ==== Mon, 13 Jan 2014, 18:23, PhilLeTaxi, France
# I solved this problem without programming.
#
# I have used the formula that gives the number of solutions :
# 4000000=((2a_1+1)(2a_2+1)...(2a_k+1)+1)/2
# This is equivalent to :
# 7999999=(2a1+1)(2a2+1)...(2ak+1)
#
# It's easy to see that : 7999999=7×199×57437999999=7×199×5743
#
# Then I have searched the nearest product of odd numbers and I have found :
# 8037225=3**8×5**2×7**2
#
# Knowing this, the smallest number for 4000000 solutions is :
# 23×33×52×72×11×13×17×19×23×29×31×37
#
# Many thanks for all the hints and explanations on the forum.


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  INCREDIBLY FAST --------------------------')
t1  = time.time()

# ==== Fri, 2 Dec 2016, 10:58, ninhnn, Vietnam
# Brute-force solution with early cut-off. Tricky!
# Super fast, 10 miliseconds

import math
import functools
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
          73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151 ]

def solve(Dmin):
    Dmin = 2*Dmin - 1
    K = int(math.log(Dmin,3)) + 1
    WORST = functools.reduce(lambda x,y: x*y, primes[:K])
    print (K, 3**K, 3**(K-1), Dmin, WORST, math.log(WORST,10), math.log(WORST,2))
    TrickyCase = int(math.log(WORST,2) / math.log(Dmin) ) * 2 - 2
    global best
    best = WORST
    def find(k, exponents, num, nDivisors):
        if nDivisors >= Dmin:
            global best
            best = min(best, num)
            print (exponents)
            return
        if k<K:
            maxExpo= TrickyCase if k==0 else int(math.log(best/num, primes[k]))
            maxExpo= min(maxExpo, exponents[-1] if len(exponents)>0 else maxExpo)
            for e in range(maxExpo,-1,-1):
                newnum = num*primes[k]**e
                newDivCnt = nDivisors*(2*e+1)
                divRemain = 1 + Dmin / newDivCnt
                extra = 0 if divRemain<3 else int(math.log(divRemain, 3))
                if newnum * primes[k+1]**extra < best:
                    find(k+1, exponents + [e], newnum, newDivCnt)
    find(0, [], 1, 1)
    print ("\nANS =", best)

solve(4*10**6)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  INSTANT SOLUTION ,4 ms --------------------------')
t1  = time.time()

# ==== Tue, 9 Aug 2016, 06:47, GoBrewers14, USA
# My solution in python.

from pyprimes import factorise
import functools
def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

LIMIT = 8000000
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

tmp = []

# this could be better but w/e
for x in range(1, 10):
    for y in range(1, 10):
        for z in range(1, 10):
            tmp.append((3**x)*(5**y)*(7**z))

smallest = min([u for u in tmp if u > LIMIT])
exponents = [(p-1)/2 for p in get_factors(smallest)][::-1]

ans = functools.reduce(lambda x,y: x*y, [x**y for x,y in zip(primes, exponents)])
print (ans)                                     # 9350130049860600

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  150 ms --------------------------')
t1  = time.time()


# ===== Tue, 13 Sep 2016, 14:41, mbh038, England
# About 6 ms, and 12 ms for nn=4 billion. Same code as for p108. No prior knowledge of prime factors is assumed.
#
# I recast the given formula into the form
# y=n**2*k+n
#  where k=x−n. It follows that kk must be a divisor of n2.
# If the prime factors of n**2 are p_1**2a p_2**2b p_3**2c...p1 p2 p3... where p1,p2,p3, are the primes and a≥b≥c...,
# then there will be (2a+1)(2b+1)(2c+1).. divisors.
# If this number is dd, then the number of distinct solutions for (x,y),
# given that we do not distinguish them from solutions for (y,x), is (d+1)/2.
# The problem then is to find the smallest value of n=p1**a *p2**b * p3**c... such that d>2m−1,
# where m is the minimum number of solutions that the equation is required to have, 4,000,000 in this case.
#
# We are looking for a highly divisible number, which will likely have several prime factors,
# each with a low exponent. In my code, I don't assume this, but do choose a maximum possible value
# for the exponent of p1, then find the minimum value of nn for each of the possible values of
# p1**a *p2**b * p3**c..., starting with only two prime factors,
# such that our criterion d>2m−1 is met, then increment the maximum exponent and repeat,
# then repeat this up to the maximum number of prime factors that n**2 can possibly have.
# So, for example, if I were testing with three prime factors, and allowed the exponent a to have the value 3,
# then I would be testing for a,b,ca,b,c values (1,1,1),(2,1,1),(2,2,1),(2,2,2),(3,1,1),(3,2,1),(3,3,1),(3,2,2),(3,3,2) and (3,3,3).
# The trick to not missing the lowest possible value of nn was to to test in ascending order of values of p1**a *p2**b * p3**c..
#
# I had trouble on large numbers with the np.prod() function for finding products of elements of a list.
# On replacing it with my own not very Pythonic code I got more speed and
# it still worked for large n. n=4 trillion takes 26 ms!


import itertools as it
import numpy as np
from operator import itemgetter

def dr(m):
    """
    returns minimum value of n for which the diophantine equation 1/x + 1/y = 1/n
    has more than m solutions
    """
    primes=[]
    prime=erat2a()
    while 1:
        primes.append(next(prime))
        if listprod(primes)>m**2:
            break
    powers=[]
    minsol=np.inf

    for i in range (len(primes)):
        for pmax in range(1,4):
            powers=pfpowers(primes[:i],pmax)
            for a in powers:
                if listprod([2*a[x]+1 for x in range(i)])>2*m-1:
                        csol=myprod(primes[:i],a)
                        if csol<minsol:
                            minsol=csol
                            amin=a
                            break

    print('Diophantine reciprocal equation: 1/x + 1/y = 1/n')
    print('Least value of n for which the number of solutions exceeds limit =', minsol)
    print('Prime factors:',primes[:len(amin)])
    print('Prime factor exponents:',amin)
    print ('Number of solutions:',(divisibility(amin)+1)//2)

def pfpowers(pfs,maxpow):
    """
    returns list of possible exponents a,b,c,d... where maxpow =a>=b>=c...of a list of prime factors
    2,3,5,7...in order such that 2^a*3^b*4^c...is an ascending sequence.
    """
    ps=[]
    for a in it.combinations_with_replacement([x for x in range(maxpow,0,-1)],len(pfs)):
        ps.append(list(a))
    ranks=[]
    ps=ps[::-1]
    ranks=sorted([(i,myprod(ps[i],pfs)) for i in range(len(ps))],key=itemgetter(1))
    rps=[]
    for i in range(len(ps)):
        rps.append(ps[ranks[i][0]])
    return rps

def divisibility(powers):
    d=1
    for x in powers:
        d*=(2*x+1)
    return d

#Not very Pythonic, but faster and/or more readable than any of several Pythonic one-liners
# I have tried (reduce, np.cumprod etc)
def myprod(primes,exponents):
    p=1
    pfs=[x**y for (x,y) in zip(primes,exponents)]
    for i in range(len(primes)):
        p*=pfs[i]
    return p

#avoids overflow problems of np.prod for large numbers, and is faster than
# reduce(mul,list,1), in Python 3, anyway.
def listprod(numbers):
    p=1
    for i in range(len(numbers)):
        p*=numbers[i]
    return p

from itertools import islice,count
def erat2a():
    """primes generator"""
    D = {}
    yield 2
    for q in islice(count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = 2 * q # use here 2 * q
            yield q
        else:
            x = p + q
            while x in D:
                x += p
            D[x] = p

dr(4*10**6)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, SUPER FAST  --------------------------')
t1  = time.time()

# ===== Wed, 7 Jan 2015, 07:28, wakkadojo, USA
# Like everyone else I identified the formula repeated on this forum to derive the number of solutions
# based on the prime factorization.
# The trick was generating the string of prime powers that construct into
# the smallest composite number with enough solutions.
#
# The way I did this was by creating all the "step" numbers to define prime exponents,
# with a maximum power of 5 (I figured we wouldn't be seeing too many repeats).
# So I generate all the strings of powers of a=∏{k,i} p_i ** r_i such that r+k = 1 and r_(i+1)≤r_k.
# Loop over r_tot=∑{i} r_i from r_tot = 5  to 20, and we save the smallest solution.

def prime ():
    yield 2
    p = 3
    while True:
        if gmpy2.is_prime (p):
            yield p
        p += 2

def num (pd): # input prime decomposition, output the number
    r = 1
    for x in pd: r *= x[0]**x[1]
    return r

def count (pd): # input prime decomposition, output num of solutions
    r = 1
    for x in pd: r *= 2*x[1] + 1
    return (r + 1)//2

def step_sequences (n, d, m): # sum of digits n, max digit d, memorization m
    key = str (n) + ',' + str (d)
    if key not in m:
        if d*(d+1)//2 > n or n < 1:
            m[key] = []
        elif d == 1:
            m[key] = [[1]*n]
        else:
            m[key] = []
            for x in range (1, d+1):
                tail = step_sequences (n-x, x, m) + step_sequences (n-x, x-1, m)
                for y in tail:
                    m[key] += [[x] + y]
    return m[key]

a, target, m = -1, 4000000, {}
for nfac in range (5, 20):
    seq = step_sequences (nfac, 3, m)
    for s in seq:
        p = prime ()
        pd = [ [next (p), x] for x in s ]
        c, n = count (pd), num (pd)
        if c > target and (n < a or a < 0):
            nsol, a = c, n
print (a)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# ==== Sun, 18 Jan 2015, 04:28, Xin, OCaml , China

import sympy as sy
from operator import mul
from functools import reduce

plist = list(sy.primerange(2,100))
p_num = len(plist)
MAX = 1e16
cutoff = 4000000
ans = MAX

def cnt_sols(pf):
    return (reduce(mul,[x*2+1 for x in pf])+1)//2

def find_ans(i,pf,n):
    global ans
    if i>=p_num: return
    pf_tmp = pf.copy()
    while True:
        pf_tmp[i] += 1
        n *= plist[i]
        if n>MAX: break
        n_sols = cnt_sols(pf_tmp)
        if n_sols>cutoff:
            if n<ans: ans = n
            break
        find_ans(i+1,pf_tmp,n)

find_ans(0,[0]*p_num,1)
print(ans)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,  VERY FAST --------------------------')
t1  = time.time()

# ==== Wed, 8 Jan 2014, 06:25, artch
# First 3 assumptions:
# * multiplication of primes from 2 to 47 is enough (the first 15);
# * number of suitable solutions for n would be number of divisors of square of n minus 1;
# * hope that none of the factors of n will have power greater than 4.
#
# Then brute over 15^4 options and check if it fit. If so, then compare with best found result.
#
# Code in python 3:

primes = [2, 3, 5, 7, 11,
			13, 17, 19, 23, 29,
			31, 37, 41, 43, 47]

des = 4 * 10 ** 6
des2 = des * 2

# something very big for beginning
res = 10 ** 100

for x1 in range(16): # pow(1)
    for x2 in range(16 - x1): # pow(2)
        for x3 in range(16 - x1 - x2): # pow(3)
            for x4 in range(16 - x1 - x2 - x3): # pow(4)
                if (3 ** x1 * 5 ** x2 * 7 ** x3 * 9 ** x4) >= des2:
                    tres = 1
                    for c in primes[0:x4]:
                        tres *= c ** 4
                    for c in primes[x4:x4 + x3]:
                        tres *= c ** 3
                    for c in primes[x4 + x3:x4 + x3 + x2]:
                        tres *= c ** 2
                    for c in primes[x4 + x3 + x2:x4 + x3 + x2 + x1]:
                        tres *= c
                    res = min(res, tres)

print('Result:', res)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n-----------SOLUTION 7,  INSTANT SOLUTION , SUPER ELEGANT SOLUTION--------------------------')
t1  = time.time()

# # ==== Wed, 15 Jan 2014, 01:34, tazunemono
# Using what I learned in 108 (d(n**2)+1) /2>4,000,000  I figured I could do this one
# by guessing the exponents of the prime factorization.  I used logarithms to guess starting values:
#
# (s_i+1)m>8,000,000 where s_i=2
# log_10(2+1)**m=log_10 (8,000,000)
# m=log_10(8,000,000)/log_10 (3)
# m=14.46820890645068 so will need ~ 15 prime terms for the top range of possible product candidates.
#
# I started with: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47 but this number was too large
# and returned too many results.
# Since I had too many prime factors, I had to remove large factors (e.g., 47)
# and replace with smaller ones (e.g., 2^2 * 3*2).
# Sure enough, after fiddling around with a dozen or so tries,
# I got an answer above 4M.
# See my final prime factorization in the code below.


def return_factors(factors_of_input_val):
    num_factors = 1
    for tuple in factors_of_input_val:
        num_factors *= (2*tuple[-1] + 1) # iterate over the tuple & grab the exponent of si
        # the math is d(n) = (s1 + 1)*(s2 + 1)* ... *(sn + 1) where d(n) returns the count of divisors
        # 2D(n^2) = (2s1 + 1)*(2s2 + 1)* ... *(2sn + 1)
    return num_factors/2 # divide by 2 to get number of unique solutions


def prime_product(factors_of_input_val):
    prime_product = 1
    for tuple in factors_of_input_val:
        prime_product *= (tuple[0]**tuple[1]) # iterate over the tuple & return prime product
    return prime_product

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
exponents = [3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]

prime_tuples = zip(primes, exponents)

print ("Answer n =", prime_product(prime_tuples), "has", return_factors(prime_tuples), "unique factors")



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8,  INSTANT --------------------------')
t1  = time.time()

# # ==== Sat, 17 May 2014, 23:06, brainiac1530, USA
# It was much easier to hack out a very specific solution rather than a very convoluted, more general, one.
# Python is pretty terrible at prime sieving, so I just made a literal list of the first few.
# To be fair, I used C++ to find the solution at first, and I had access to a well-tested prime sieve.

primes = [2,3,5,7,11,13,17,19,23,29,31,37]
def e110divs(n):
	d,ct = 1,0
	for p in primes:
		while not n % p:
			n //= p
			ct += 1
		if ct:
			ct += ct + 1
			d *= ct
			ct = 0
	return d
inc,divs,k = 1,0,0
for p in primes:
	inc *= p
for i in range(4):
	inc *= primes[i]
while divs < 4*10**6:
	k += inc
	divs = e110divs(k) + 1
	divs >>= 1

print(k,k//inc)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 9, SUPER FAST & ELEGANT  --------------------------')
t1  = time.time()

# ====Mon, 22 Dec 2008, 04:34, tolstopuz, Python , Russia
import functools, operator

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

smax = 4000000

def q(nmax, p=[]):
    pr = functools.reduce(operator.mul, (primes[i] ** p[i] for i in range(len(p))), 1)
    if (functools.reduce(operator.mul,
                         (2 * p[i] + 1 for i in range(len(p))), 1) - 1) // 2 > smax:
        return min(nmax, pr)
    for i in range(1, 1000 if len(p) == 0 else p[-1] + 1):
        if pr * primes[len(p)] ** i >= nmax:
            break
        nmax = q(nmax, p + [i])
    return nmax

nmax = 1
s = 1
for p in primes:
    if s > smax:
        break
    s *= 3
    nmax *= p

print(q(nmax))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

