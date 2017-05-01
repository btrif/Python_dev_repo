#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @         Completed on Tue, 28 Mar 2017, 13:09
#The  Euler Project  https://projecteuler.net
'''
                Prime Subset Sums       -       Problem 249

Let S = {2, 3, 5, ..., 4999} be the set of prime numbers less than 5000.

Find the number of subsets of S, the sum of whose elements is a prime number.
Enter the rightmost 16 digits as your answer.


'''
import time, zzz
from gmpy2 import is_prime

def prime_sieve_generator(lower, upper):      #FIFTH FASTEST
    """  Sieve of Eratosthenes
    Create a candidate list within which non-primes will be marked as None.         """
    cand = [i for i in range(3, upper + 1, 2)]
    end = int(upper ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (upper // cand[i]) - (upper // (2 * cand[i])) - 1 )

    # Filter out non-primes and return the list.
    return [2] + [ i for i in cand if i and i > lower ]







print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# primes = prime_sieve_generator(1, 1000)
# t = [1] + [0] * sum(primes)
#
# sp = 0
# for p in primes:
#     sp += p
#     for j in range(sp, p-1, -1):
#         t[j] = (t[j] + t[j-p])
#
# print ("Project Euler 249 Solution =", (sum(t[p] for p in range(sp) if is_prime(p)) % 10**16))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


####### === GENERAL IDEA
# http://stackoverflow.com/questions/18305843/find-all-subsets-that-sum-to-a-particular-value

print('\n============ My FIRST SOLUTION,  DYNAMIC PROGRAMMING,  2 min ===============\n')
t1  = time.time()



def my_first_solution(up) :
    P = prime_sieve_generator(1,up)
    print(len(P) ,P[:100])
    T = [1] + [ 0 for i in range(sum(P)) ]

    for p in P :
        sp = sum( P[:P.index(p)+1] )
        print(p,'       ' ,sp )
        for i in range( sp,  p-1 , -1) :
            T[i] = T[i] + T[i-p]

    print(T[:100])
    S =   sum( [ T[i] for i in range(len(T))  if is_prime(i) ] )
    return print('\nAnswer : \t' , S%10**16 , '\n', S )

# my_first_solution(5000)             #   Answer : 	 9275262564250418



t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60, 6), 'min\n\n')          #   Completed in : 2.349051 min


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  SLOW , Coin Change PRoblem --------------------------')
t1  = time.time()

# ==== Mon, 2 Sep 2013, 11:17, ChopinPlover, Taiwan
# Coin change problem

SIEVE_RANGE = 1550000
PROBLEM_MOD = 10**16

sieve = [False] * SIEVE_RANGE
primes = []
coins = []

def init_primes():
    sieve[0], sieve[1] = True, True
    for i in range(2, SIEVE_RANGE):
        if sieve[i] is False:
            primes.append(i)
            for j in range(i+i, SIEVE_RANGE, i):
                sieve[j] = True

def init_coins(coin_range):
    for i in range(len(primes)):
        if primes[i] > coin_range:
            break
        coins.append(primes[i])

def get_coin_change_ways():
    ways = [0] * SIEVE_RANGE
    ways[0] = 1
    for c in coins:
        for j in range(SIEVE_RANGE-1, -1, -1):
            if j+c < SIEVE_RANGE:
                ways[j+c] = (ways[j+c] + ways[j]) % PROBLEM_MOD

    total_ways = 0
    for i in range(len(ways)):
        if sieve[i] is False:
            total_ways += ways[i]
    total_ways %= PROBLEM_MOD
    print(total_ways)

def main():
    init_primes()
    init_coins(5000)
    get_coin_change_ways()

# main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 2, Not entirely correct  --------------------------')
t1  = time.time()

def solution2() :
    import numpy

    limit = 5000
    primes = prime_sieve_generator(1, limit)
    maxsum = int(sum(primes))
    maxsofar = 1
    histo = numpy.zeros((maxsum + 1,), dtype=numpy.uint64)
    histo[0] = 1
    for pidx, p in enumerate(primes):
        maxsofar += p
        histo[maxsofar-1:p-1:-1] += histo[maxsofar-p-1::-1]
        if pidx % 10 == 9: histo %= (10**16)
    return print(sum(int(v) for v in histo[prime_sieve_generator(2, maxsum) ]) % 10**16)

# solution2()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 3,  3 min --------------------------')
t1  = time.time()

# ==== Sat, 20 Jun 2009, 00:12, quilan, USA
# Same general idea as #250. I don't pay too much thought to the whole minute rule vs. 2-3 minute rule in python.
# # It's infinitely more enjoyable to program in than anything else I use, so I don't mind if it's a bit slow.
# Python, 110.4s:

from gmpy2 import is_prime


def manual():
    v1016 = 10**16;

    mx=3; c=[0]*(sum(primes)+1); c[2]=1;
    for p in primes[1:]:
        nc = c[:]; nc[p]+=1;
        for x in range(mx): nc[x+p]+=c[x];
        for x in range(mx+p):
            while(nc[x]>=v1016): nc[x]-=v1016;
        c=nc; mx+=p;

    total=0;
    for x in range(len(nc)):
        if(is_prime(x)): total+=nc[x];
    return total % v1016;

#==============================================

def main3():
    primes = prime_sieve_generator(1, 5000);
    total=manual();
    return print( "Total = %d"%total)

# main3()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 4, 2 min  --------------------------')
t1  = time.time()

# ==== Sat, 13 Jun 2009, 08:05, sigh, Australia
# My short but fairly slow python code (I haven't included the prime handling functions here):

from collections import defaultdict
from gmpy2 import is_prime


def p249(limit = 5000):
    ss = defaultdict(int)
    ss[0] = 1 # empty set

    for p in prime_sieve_generator(1, 5000) :
        for s in sorted(ss.keys(), reverse=True):
            ss[s+p] += ss[s]

    return print(sum(ss[s] for s in ss if is_prime(s)))

p249(5000)

t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6 ), 's\n\n')


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

