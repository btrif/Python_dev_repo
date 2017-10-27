#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @         Completed on Tue, 3 Oct 2017, 22:23
#The  Euler Project  https://projecteuler.net
'''
                Semidivisible numbers           -       Problem 234

For an integer n ≥ 4, we define the lower prime square root of n, denoted by lps(n),
as the largest prime ≤ √n and the upper prime square root of n, ups(n), as the smallest prime ≥ √n.

So, for example, lps(4) = 2 = ups(4),
    lps(1000) = 31, ups(1000) = 37.

Let us call an integer n ≥ 4 semidivisible, if one of lps(n) and ups(n) divides n, but not both.

The sum of the semidivisible numbers not exceeding 15 is 30, the numbers are 8, 10 and 12.
15 is not semidivisible because it is a multiple of both lps(15) = 3 and ups(15) = 5.

As a further example, the sum of the 92 semidivisible numbers up to 1000 is 34825.

What is the sum of all semidivisible numbers not exceeding 999966663333 ?


'''
import time, gmpy2, zzz, math
import sympy
from math import sqrt
import numpy as np

def numpy_prime_sieve(n):          ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    """return array of primes 2<=p<=n"""
    sieve=np.ones( n+1, dtype=bool )
    for i in range( 2, int((n+1)**0.5+1) ) :
        if sieve[i] :
            sieve[2*i :: i] = False
    return np.nonzero(sieve)[0][2:]


print('\n--------------------------TESTS------------------------------')
t1  = time.time()

UP_NR = 999966663333
print('Square root of UP_NR : \t', math.sqrt(UP_NR),'\n'  )     # 1 milion is affordable :) !

# So we need a sieve up to 10**6, EASY PROBLEM !!!!


def brute_force_testing(lim) :
    S, cnt = 0, 0
    for n in range(7, lim+1):
        if gmpy2.is_square(n) : continue
        sqd = math.floor((n**(1/2)))
        squ = math.ceil((n**(1/2)))
        # print(sq)
        lps = sympy.prevprime(squ)
        ups = gmpy2.next_prime(sqd)
        if (n%lps !=0 and n%ups == 0) or (n%lps ==0 and n%ups != 0)  :
            cnt += 1
            print(str(cnt)+'.     n=', n , '    lps=',lps, '      ups=',ups  )
            S+=n

    return print('\nAnswer : \t', S)

brute_force_testing(1000)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,  27 sec, OK  ===============\n')
t1  = time.time()

def get_semidivisible(p1, p2 ):      # Ugly function
    '''     @Made by Bogdan Trif @ 2017-10-03, 21:50.
        Efficient but ugly function . Its design and code redundancy must be reduced.
    :Description:     computes the semidivisible numbers as described in the problem request Euler 234,
        where p1 & p2 are consecutive prime numbers
    :param p1: p1, p2 are consecutive primes, p1 is the lowest. Example : p1=31, p2-37
                                     '''
    N = []
    lps1 = lps2 = ups1 = ups2 = p1*p2
    while sqrt(lps1) > p1 :
        lps1-=p1
        if sqrt(lps1) > p1 :
            # print(lps1)
            N.append(lps1)

    while sqrt(lps2) > p1 :
        lps2-=p2
        if sqrt(lps2) > p1 :
            # print(lps2)
            N.append(lps2)

    while sqrt(ups1) < p2 :
        ups1 += p1
        if sqrt(ups1) < p2 :
            # print(ups1)
            N.append(ups1)

    while sqrt(ups2) < p2 :
        ups2 += p2
        if sqrt(ups2) < p2 :
            # print(ups2)
            N.append(ups2)


    return N

# print('\nget_semidivisible : \t' , get_semidivisible(31 , 37) )


def main_solution(up_lim) :
    SUM = 0
    H = []
    primes = numpy_prime_sieve( int(sqrt(up_lim)) )
    last_p = gmpy2.next_prime( int(sqrt(up_lim)) )
    primes = np.insert(primes,  len(primes) , last_p )
    print( len(primes), primes[:100] ,'\n')

    for i in range(len(primes)-1 ) :
        p1, p2 = primes[i] , primes[i+1]
        # print(str(i)+'.     ', p1 , p2 ,  )
        H = get_semidivisible( p1, p2 )
        if i >= len(primes)-2 :
            print('             condition met : ', p1, p2 )
            # print(H)
            O = [ j for j in H if j < up_lim ]
            H = O[:]
        # print(H)
        SUM += sum(H)

    return print('\nthe sum of all semidivisible numbers : \t', SUM)


# main_solution(1000)
# main_solution(999966663333)         #   Anser  :            1259187438574927161






t2  = time.time()
print('\nCompleted in :', round((t2-t1), 4 ), 's\n\n')      #   Completed in : 26.9435 s


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  4 sec, Must learn the improvement --------------------------')
t1  = time.time()

# === Thu, 26 May 2016, 20:34, go_to_dmc, South Korea
# Pretty easy. It takes 5 secs to get the answer though.

def primes_sieve(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return primes


p_list=primes_sieve(10**6)
import math
prob234ans=0
for i in range(len(p_list)-1):
    for j in range(p_list[i]+1,int(p_list[i+1]**2/p_list[i])+1):
        if j%p_list[i+1]!=0:
            prob234ans+=p_list[i]*j
            continue

    for k in range(math.ceil(p_list[i]**2/p_list[i+1]),p_list[i+1]):
        if k%p_list[i]!=0:
            prob234ans+=p_list[i+1]*k
            continue



print(prob234ans)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Thu, 26 May 2016, 20:34, go_to_dmc. South Korea
# Pretty easy. It takes 5 secs to get the answer though.

def primes_sieve(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return primes


p_list=primes_sieve(10**6)
import math
prob234ans=0
for i in range(len(p_list)-1):
    for j in range(p_list[i]+1,int(p_list[i+1]**2/p_list[i])+1):
        if j%p_list[i+1]!=0:
            prob234ans+=p_list[i]*j
            continue

    for k in range(math.ceil(p_list[i]**2/p_list[i+1]),p_list[i+1]):
        if k%p_list[i]!=0:
            prob234ans+=p_list[i+1]*k
            continue



print(prob234ans)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
