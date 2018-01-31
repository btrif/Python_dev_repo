#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                            Squarefree Numbers  -   Problem 193

A positive integer n is called squarefree, if no square of a prime divides n,
thus 1, 2, 3, 5, 6, 7, 10, 11 are squarefree,

but not 4, 8, 9, 12.

How many squarefree numbers are there below 2**50 ?

'''
import time
import math
import itertools

def prime_generator(lower, upper):      ### o(^_^)o  FASTEST  o(^_^)o  ###  HIghly Efficient !!!
    """  Sieve of Eratosthenes              !!!!!!!!! THE FASTEST SIEVE. It won the battle with sieve
    Create a candidate list within which non-primes will be marked as None.         """
    cand = [i for i in range(3, upper + 1, 2)]
    end = int(upper ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (upper // cand[i]) - (upper // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [2]+[ i for i in cand if i and i > lower ]

print('\n--------------------------TESTS------------------------------')


sq_100 = [1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30, 31, 33, 34, 35, 37, 38, 39, 41, 42, 43, 46, 47, 51, 53, 55, 57, 58, 59, 61, 62, 65, 66, 67, 69, 70, 71, 73, 74, 77, 78, 79, 82, 83, 85, 86, 87, 89, 91, 93, 94, 95, 97]
print('sq_100 : ',len(sq_100),'\n')


print(len(str(2**50)),'   ', 2**50)
print(math.sqrt(2**50))
print(2**25 )

print('----------------------')

# print( prime_generator(2,100))


print('\n -------------  MY VERIFICATION CONCEPT ---------------------')



print('\n================  My FIRST SOLUTION, Can be improved  ===============\n')
t1  = time.time()

def square_free_numbers(up_nr) :        # Works Up_to   2**50
    b, S = up_nr-1, 0
    primes = prime_generator(2, int(up_nr**(1/2)) )
    for i in range(len(primes)):
        S += b//(primes[i]*primes[i])
        # print('- just i :  ', b//(primes[i]*primes[i] ), '   ', primes[i], '    ',b/(primes[i]*primes[i]) , S  )
        for j in range(i+1, len(primes)):
            a2 = (primes[i]*primes[j])**2
            if a2 > b : break
            S -= b//a2
            # print( S, '    ',primes[i], primes[j],'  ',primes[i]**2 * primes[j]**2    ,'     ' ,b/(primes[i]*primes[j] )**2,   b//(primes[i]*primes[j])**2  )
            for k in range(j+1, len(primes)):
                a3 = (primes[i]*primes[j]*primes[k])**2
                if a3 > b : break
                S += b//a3
                for l in range(k+1, len(primes)):
                    a4 = (primes[i]*primes[j]*primes[k]*primes[l])**2
                    if  a4 > b : break
                    S -= b//a4
                    for m in range(l+1, len(primes)):
                        a5 = (primes[i]*primes[j]*primes[k]*primes[l]*primes[m])**2
                        if  a5 > b : break
                        S += b//a5
                        for n in range(m+1, len(primes)):
                            a6 = (primes[i]*primes[j]*primes[k]*primes[l]*primes[m]*primes[n])**2
                            if a6 > b : break
                            S -= b//a6
                            for o in range(n+1, len(primes)):
                                a7 = (primes[i]*primes[j]*primes[k]*primes[l]*primes[m]*primes[n]*primes[o])**2
                                if  a7 > b : break
                                S += b//a7
                                for p in range(o+1, len(primes)):
                                    a8 = (primes[i]*primes[j]*primes[k]*primes[l]*primes[m]*primes[n]*primes[o]*primes[p])**2
                                    if  a8 > b : break
                                    S -= b//a8
                                    # for q in range(p+1, len(primes)):
                                    #     a9 = primes[i]*primes[j]*primes[k]*primes[l]*primes[m]*primes[n]*primes[o]*primes[p]*primes[p]*primes[q])**2
                                    #     if a9 > b : break
                                    #     S += b//a9

                # print(S, primes[i], primes[j] , primes[k] , b/(primes[i]*primes[j]*primes[k])**2, b//(primes[i]*primes[j]*primes[k])**2  )
            #             print(S, primes[i], primes[j] ,primes[l], primes[k] ,primes[m], b/(primes[i]*primes[j]* primes[l]* primes[k] *primes[m] )**2 )
            # print( primes[i], primes[j] , end='    ')
    return print('\nRESULT :\t', b-S)

# square_free_numbers(10**3)
# square_free_numbers(2**30)
# square_free_numbers(2**50)             #  RESULT :	 684465067343069


# I need to condense all those 8 loops


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')            # Completed in : 98426.629782 ms


print('\n================  My SECOND SOLUTION, INCLUSION EXCLUSION,  Not Working ===============\n')
t1  = time.time()
import functools, operator

def square_free_combinations(up_nr) :
    b, S = up_nr-1, 0
    P = prime_generator(2, int(up_nr**(1/2)) )
    for i in range(2, 4):
        for c in itertools.combinations( P , i):
            G = (functools.reduce( operator.mul, c ))**2
            # print(c , G)
            if G < b :
                if i % 2 == 0  :
                    S +=  b//G
                if i % 2 == 1  :
                    S -= b//G
            # if  G > b : break
    return print('\nRESULT :\t', b-S)


square_free_combinations( 2**8 )



t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')            # Completed in : 98426.629782 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
##########  2016-12-19 --GENERAL IDEAS #############
# Sequence is this : https://oeis.org/A005117/b005117.txt
# Method 1 to solve : Use Mobius Function
# Method II : Use inclusion/ exclusion (As I did myself)


print('\n--------------------------SOLUTION 0, 20 sec ,  Moebius sieve  --------------------------')
t1  = time.time()


# ===  Sat, 28 Jan 2017, 09:19, mbh038, England
#
# 7.7 s in Python. I use the identity:
#
# Q(n) = ∑ {k=1, n} μ(k) ⌊n / k^2⌋  =  ∑ { k=1, ⌊n√⌋ } μ(k)  ⌊n/k^2⌋
#
#
# In the code I use a sieve to generate the Moebius numbers and vectorise where possible to avoid loops.
# 90% of the time is taken up in the Moebius sieve, in the part where I do use a loop.
# I can't see how to avoid this. As it is, though, the sieve is about three times faster than my implementation ' \
# in Python of Marcus Andrews' Moebius sieve, listed as Algorithm 9 in his fantastic overview to problem 351.


import numpy as np
import time

#find Q, the number of square-free numbers less than n
def p193(n):

    moebs = moebiusSieve(int(n**.5)+1)
    ks = np.arange( 1, len(moebs)+1)
    floors = n//( ks*ks )
    Q = np.sum( moebs*floors )
    print( Q )

def moebiusSieve(limit):
    """returns array of moebius numbers 1<=n<=limit"""
    P=primeSieve(limit+1) # or any sieve
    L = np.ones(limit+1).astype(int)
    for p in P:
        L[ ::p ] *= -1
        L[ ::p**2 ] = 0
    print('L= ', L[1:])
    return L[1:]

def primeSieve(n):
    """returns array of primes 2<=p<=n"""
    sieve=np.ones( n+1, dtype=bool )
    for i in range( 2, int((n+1)**0.5+1)):
        if sieve[i] :
            sieve[ 2*i::i ] = False
    return np.nonzero(sieve)[0][2:]

p193(2**8)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 1, MOBIUS , > 10 mins  --------------------------')
t1  = time.time()

# ===== Tue, 18 Oct 2016, 15:26, aolea, Spain

from math import sqrt, floor
import sympy

def aolea( lim ) :
    sum193 = 0
    for d in range(1, int( sqrt(lim) ) ):
        # print(d, sum193)
        sum193 = sum193 + sympy.ntheory.mobius(d) * floor( lim /(d**2))
    return print(sum193)

aolea( 2**8 )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

import math
import sys

class CountingProblem():
    def __init__(self):
        self.n = 2**50
        self.bound = 2**25
        self.sieve_visited = None
        self.mobius_functions = None

        self._init_mobius_functions()

    def _init_mobius_functions(self):
        self.mobius_functions = [1] * (self.bound + 1)
        self.mobius_functions[1] = 1
        self.sieve_visited = [False] * (self.bound + 1)
        self.sieve_visited[0] = self.sieve_visited[0] = True
        for i in range(2, self.bound + 1):
            if not self.sieve_visited[i]:
                self.mobius_functions[i] *= -1
                for j in range(i+i, self.bound + 1, i):
                    self.sieve_visited[j] = True
                    self.mobius_functions[j] *= -1
                for j in range(i*i, self.bound + 1, i*i):
                    self.mobius_functions[j] = 0
        print('First ten Mobius function:', self.mobius_functions[1:11])

    def get_count(self):
        count = 0
        for d in range(1, self.bound + 1):
            count += self.mobius_functions[d] * (self.n // (d**2))
        return count

def main():
    problem = CountingProblem()
    print(problem.get_count())

# main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  90 secs --------------------------')
t1  = time.time()

# === Fri, 28 Aug 2015, 16:42, Jenny, France
# I sieved Moebius for n <= 2**25. Then I used the formula ∑{k=1, sqrt(n-1) }  μ(d)*⌊ n−1/d**2 ⌋
# temps d execution 87.90116979154118 sec
def Jenny():
    def mobius_sieve(lim):
        sqrt = math.floor(math.sqrt(lim))
        mu = [1] * (lim + 1)
        for i in range(2, sqrt+1):
            if mu[i] == 1:
                for j in range(i, lim+1, i):
                    mu[j] *= -i
                for j in range(i*i, lim+1, i*i):
                    mu[j] = 0
        for i in range(2, lim+1):
            if mu[i] == i:
                mu[i] = 1
            elif mu[i] == -i:
                mu[i] = -1
            elif mu[i] < 0:
                mu[i] = 1
            elif mu[i] > 0:
                mu[i] = -1
        return mu


    mob = mobius_sieve(2**25)
    res = 0
    for k in range(1, 2**25):
        res += mob[k]*(2**50//k**2)
    return print(res)

# Jenny()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  Moebius Function --------------------------')
t1  = time.time()

# ==== Tue, 28 Apr 2015, 15:58, Haroun, Algeria
# Took 27 seconds on python, creating a list of Moebius function values took most of the time.

from math import *;

def Haroun():
    #this is a fast prime sieve.
    def sieve(n):
        sieve = [True] * n
        for i in range(3,int(n**0.5)+1,2):
            if sieve[i]:
                sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
        return [2] + [i for i in range(3,n,2) if sieve[i]]
    #return a list of moebius function values upto to n
    def moebius_list(n):
        l=[1]*(n+1);
        P=sieve(int(sqrt(n)));
        for p in P :
            for i in range(p,n+1,p):
                l[i]*=-p;
        for p in P :
            for i in range(p*p,n+1,p*p):
                l[i]=0;
        for i in range(2,n+1):
            if abs(l[i])!= i : l[i]*=-1;
        for i in range(2,n+1):
            if l[i]>0 : l[i]=1;
            if l[i]<0 : l[i]=-1;
        return l;
    #return the number of squarefree integers <n.
    def counting_sqaurefree_numbers(n):
        r=int(sqrt(n));
        s=moebius_list(r);
        return sum(s[i]*(n//(i*i)) for i in range(1,r+1))

    sol= counting_sqaurefree_numbers(2**50);

    return print ("the answer is : ", sol  )

# Haroun()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5, Moebius Function  --------------------------')
t1  = time.time()

# ===  Tue, 30 Dec 2014, 12:01, SafassThin, France
# Well, I thought my solution would be very bad, but it seems to be in the average
# I used the Moebius function, that I implemented directly from:
# http://oai.cwi.nl/oai/asset/2136/2136A.pdf (page 7)
# Runs in about a minute
# After reading some posts I saw that I could simplify it (not sure why though)...

def euler_193(limit = pow(2,50)):

    def sign(n):
        if n>0: return 1
        if n<0: return -1
        return 0

    def moebius(limit): # http://oai.cwi.nl/oai/asset/2136/2136A.pdf (page 7)
        from eulerlib import primes
        m = [1]*limit
        for p in primes(limit):
            for n in range(p, limit, p): m[n] *= -1  # was: *= -p
            for n in range(p*p, limit, p*p): m[n] = 0
        #for n in range(limit): # this part can be removed apparently
            #if abs(m[n]) != n: m[n] *= -1
            #m[n] = sign(m[n])
        return m

    sqrt = int(pow(limit, 0.5))
    m = moebius(sqrt)
    return sum(((limit-1)//(n*n))*m[n] for n in range(1,sqrt))

# euler_193()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6, INCLUSION/ EXCLUSION,  91 seconds --------------------------')
t1  = time.time()

# ===== Sat, 15 Feb 2014, 19:19, Ido Nahshon, Israel
# I used sieve to find all primes bellow 2^25, then used the inclusion-exclusion to find
# the number of integers bellow 2^50 that divide a square.
# The problem can be solved with the mobius function as others wrote, maybe I'll code that later.
# Runs in 30 seconds in python

'''
"Squarefree Numbers"
Project Euler Problem 193

How many Squarefree numbers are there below 2^50 ?
'''

import time

def prime_sieve(n):
	l = [True] * (n+1)
	for i in range (2, int(n**0.5) + 1):
		if l[i] == True:
			for j in range(2, int(n / i) + 1):
				l[i*j] = False
	return l

def xprimes(n):
	sieve_list = prime_sieve(n)
	for i in range(2,n):
		if sieve_list[i] == True:
			yield i

def rec(prime_list, max_val, n = 0, x = 1, min_index = 0):
	result = 0
	for i in range(min_index, len(prime_list)):
		p = prime_list[i]
		y = p * p * x
		if y > max_val: break
		result += ((-1) ** n) * (max_val / y)
		result += rec(prime_list, max_val, n + 1, y, i + 1)

	return result

def main():
	start_time = time.time()
	print ('Generating a list of primes bellow 2^25...    ',)
	prime_list = list(xprimes(2 ** 25))
	print ('Done.')
	print ('Making an inclusion-exclusion iteration through all prime combinations...    ',)
	result = rec(prime_list, 2 ** 50)
	print ('Done.')
	print ('There are %d non-squarefree integers bellow 2**50' % result)
	print ('Result = %d' % (2**50 - result))
	print ('Calculated in %d seconds.' % (time.time() - start_time))


# main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 7,  Inclusion/ Exclusion, SLOW, 2 min  --------------------------')
t1  = time.time()

# ===== Sun, 20 Jan 2013, 21:00, Thierry Machicoane, Switzerland

import gmpy2

def Machicoane():
    def init(n):
        p = 2
        s = [p * p]
        while s[-1] <= n:
            p = int(gmpy2.next_prime(p))
            s.append(p * p)
        return s

    def f(Qi , i):
        global N,P
        if Qi <= N:
            S = 0
            j = i
            Q = Qi * P[j]

            while Q <= N:
                S += (N / Q) - f(Q, j+1)
                j += 1
                Q = Qi * P[j]
            return S

        else: return 0

    N = 2**50
    P = init(N)
    return print (N - f(1,0))

# Machicoane()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8, INCLUSION / Exclusion  ,MUCH TOO SLOW --------------------------')
t1  = time.time()

# ===== Wed, 8 May 2013, 19:35, tom.wheldon, England
# Another inclusion-exclusion solution using recursion.
# Straightforward to code and runs in 43 seconds in Python without extensions, which I'm quite content with.

from sympy import primerange
from bisect import bisect_right

def very_slow():
    N = 2**50 - 1
    primes = primerange(1, int(N**0.5))
    squares = [p*p for p in primes]

    def rec(ind, prod):
        prod *= squares[ind]
        q = N//prod
        tot = q
        for i in range(ind+1, bisect_right(squares,q)):
            tot -= rec(i, prod)
        return tot

    sqs = 0
    for i in range(len(squares)):
        sqs += rec(i, 1)

    ans = N - sqs
    return print(ans)

# very_slow()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 9,  1 min  --------------------------')
t1  = time.time()

# =====Mon, 3 Jun 2013, 09:52, bobrovsky.serj , Russia
# No recursion. 18sec (plus 5 for sieve).


def euler193(limit):
    primes = prime_generator(1, limit)
    l = [(i, p) for i, p in enumerate(primes)]

    tot = limit2 = limit ** 2 - 1
    sig = 1
    while l:
        sig *= -1
        l1 = []
        for i, q in l:
            tot += limit2 // (q * q) * sig
            for j in range(i + 1, len(primes)):
                pq = primes[j] * q
                if pq > limit:
                    break
                l1.append((j, pq))
        l = l1

    return tot

# print(euler193(2 ** 25))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

