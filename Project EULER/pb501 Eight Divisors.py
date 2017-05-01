#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @         Completed on Thu, 23 Mar 2017, 16:27
#The  Euler Project  https://projecteuler.net
'''
                    Eight Divisors          -       Problem 501

The eight divisors of 24 are 1, 2, 3, 4, 6, 8, 12 and 24.
The ten numbers not exceeding 100 having exactly eight divisors are 24, 30, 40, 42, 54, 56, 66, 70, 78 and 88.
Let f(n) be the count of numbers not exceeding n with exactly eight divisors.
You are given f(100) = 10, f(1000) = 180 and f(10**6) = 224427.

Find f(10**12).

'''
import time, zzz, gmpy2 , pyprimes
import os, subprocess
from math import sqrt, floor, ceil
import numpy as np


def  calculate_divisors(nr):
    '''**©** Made by Bogdan Trif @ 2016-12-08, 16:30.
        :Description: Functions which computes the number of divisors of a number.
                It uses the Numbers of Divisors Theorem :which says : if N=a**x*b**y*c**z => divisors_nr=(x+1)(y+1)(z+1)
            Example: N = 216 = 2**3 * 3**3 => divisors_nr = (3+1)(3+1) = 16
    :param nr: int, nr
    :return: int, divisors_number                   '''
    import functools, operator
    from pyprimes import factorise
    def factors(nr):
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        return [i for i in factorise(nr)]
    N = factors(nr)
    return  functools.reduce( operator.mul , [ (i[1]+1) for i in N ])

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

def count_primes_up_to(n):
    args = str(n)
    res = subprocess.getoutput(['d:\\Google Drive\\Computing & PROGRAMMING\\Project Euler\\prime count\\primecount.exe', args ])
    # subprocess.call(['d:\\Google Drive\\Computing & PROGRAMMING\\Project Euler\\prime count\\primecount.exe', str(n) ])
    return int(res)

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


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
    return  [2] + [ i for i in cand if i and i > lower ]

# os.startfile("d:/Google Drive/Computing & PROGRAMMING/Project Euler/prime count/")
# subprocess.call(['C:\\windows\\system32\\cmd.exe', '/C', 'dir'])
subprocess.call(['d:\\Google Drive\\Computing & PROGRAMMING\\Project Euler\\prime count\\primecount.exe', '1e6' ])

# @2017-03-22, 0:30
# This must be easy enough but to reach the limit 10**12 you must use combinations of elements such
# that the resulting reversed totient ( divisors numbers)  = 8. Examples:
#
# CASE 1 :  24 = [2, 2, 2, 3] = (3+1 )* (1+1) = 8
# CASE 2 : we also could have : (1+1) * (1+1) * (1+1) = 8 like : 30 = [2 ,3 ,5 ]
# or the third case could be that  :
# CASE 3 :  (7+1) = 128 = [2, 2, 2, 2, 2, 2, 2 ]
# ...and that's pretty ALL ! THIS PROBLEM IS QUITE EAsy ! Let's confirm this only after we start it !!! :) :)
# OBS : We need a HUUUUGE SIEVE ! Shit!  this is not as easy as I expected !
# No way we can use a SIEVE ! This is insane ! I would need 128- 256 Gb of RAM
# # The second case is the most difficult I must estimate how many prime numbers are up to 10**12 //(2*3)
# I must use a function which calculates how many primes are up to a certain number !
# For the first case the situation is similar !
# Only the third case p**7 is the easy one !!! as I need only to count how many numbers n**7 are up to 10**12
#
#
# http://www.ams.org/journals/mcom/1996-65-213/S0025-5718-96-00674-6/S0025-5718-96-00674-6.pdf
# https://github.com/kimwalisch/primecount
# http://math.stackexchange.com/questions/889712/the-fastest-way-to-count-prime-number-that-smaller-or-equal-n
# https://programmingpraxis.com/2011/07/22/counting-primes-using-legendres-formula/
# https://primes.utm.edu/howmany.html
# http://www.primefan.ru/stuff/primes/table.html
# http://www.ams.org/journals/mcom/1963-17-082/S0025-5718-1963-0158508-8/S0025-5718-1963-0158508-8.pdf
# http://mathworld.wolfram.com/PrimeCountingFunction.html


print('First case : \t', calculate_divisors(24))
print('Second case : \t', calculate_divisors(30))
print('Third case : \t', calculate_divisors(128))

###################

from bisect import bisect       #### Works up to 10**6
from functools import lru_cache
from pyprimes import primes_below

prime = list(primes_below(10000))

@lru_cache(maxsize=None)
def phi(x, a):
    if a == 1:
        return (x+1)//2
    else:
        return phi(x, a-1) - phi(x//prime[a - 1], a - 1)

def pi(n):      # Is only approximative
    ''' return number of primes <= n

    # >>> pi(10)
    # 4
    # >>> pi(1000)
    # 168
    # >>> pi(1000000)
    78498
    '''
    if n < prime[-1]:
        return bisect(prime, n)
    else:
        a = pi(int(sqrt(n)))
        return phi(n, a) + a - 1

####################


print('\n------------------------ TESTS, understanding the concept ------------------------------')
t1  = time.time()

n=10**12
print('Test for Primes bellow : ', n, '  are ', count_primes_up_to(n), '\n')

def brute_force_testing_1(up) :
    gnt =0
    SET = set()
    for n in range(up) :
        f = get_factors(n)
        d = calculate_divisors(n)
        if d ==8 :
            gnt += 1
            if len(set(f))  in [ 2 ]  :
                SET.add(n)
            # print('n= ', n , '      div = ', d,'       factors=', f, len(set(f)))
    # return print('\nAnswer :\t', gnt)
    print('THERE ARE : ',len(SET))
    return SET

print('brute_force_testing_1 : \n' , brute_force_testing_1(10**3) )


def selective_brute_force( p1, p2, lim ) :
    # Obs : p1 < p2
    cnt =0
    test_prime_sieve = prime_sieve_numpy(lim)
    rng = np.where( test_prime_sieve == p2)[0]
    # print(rng, type(rng))
    i = rng +1
    while p1*p2*test_prime_sieve[i] < lim :
        cnt +=1
        i+=1
    return cnt

# print(' selective_brute_force : \t' ,selective_brute_force(2, 3, 10**6 ) )


def case_2_selective_brute_force(p1, lim):
    cnt =0
    sieve = prime_sieve_numpy(lim)
    p = p1**3
    i = 0
    while p*sieve[i] < lim :
        if sieve[i] != p1 :
            cnt +=1
            i+=1
        else : i+=1
    return cnt

print(' case_2_selective_brute_force : \t' ,case_2_selective_brute_force(2,  10**3 ) )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,  VERY VERY SLOW, 12 hours ===============\n')
t1  = time.time()

### The fact that it is so SLOW is due to the fact that the function count_primes_up_to uses a subprocess
# to call an exe made on C to count the primes up to a number

##### 10**12
P1 = prime_sieve_numpy(10**4+10)
print(P1[-6::])
P = prime_sieve_numpy( int(10**6//sqrt(2)) + 20 )
print(9973 *10007* 10009 ,  9973 *10007* 10009 >10**12, 10007* 10009 *10037 >10**12  )
print(P[-6::])
print(2* 707099 * 707111, 2* 707099 * 707111 >10**12,  2* 707111 * 707117 > 10**12 )

print('\n--------------------')
##### 10**6
P3 = prime_sieve_numpy( int(10**3//sqrt(2)) + 20 )
print(89 * 97 *101, 89 * 97 *101 >10**6  ,  97 * 101 *103 >10**6 )
print(P3[-20::])
print(2* 691 *701, 2* 701* 709 > 10**6,  2*  709 * 719 > 10**6 )

#############
print('\n------------------')

def first_solution(LIM) :
    counter = 0
    i=0
    while P[i] < LIM**(1/3) :
        j=i+1
        while P[i] * P[j] * P[j+1] < LIM :
            up =  LIM // (P[i] * P[j])
            k = count_primes_up_to( up ) - j-1
            # selective_bf = selective_brute_force(P[i] , P[j] , LIM )
            # if k != selective_bf :
            # print('i, j = ',  P[i], P[j]  ,  '  up =   ', up  , '   k= ', k , '    sel BF = ',  selective_bf , '    reCheck=', pyprimes.prime_count(up)-j-1 )
            print('i, j = ',  P[i], P[j]  ,  '  up =   ', up  , '   k= ', k )
            counter +=k
            j+=1
        i+=1

    print()
    o=0
    while P[o]**3 * P[0] < LIM :
        p1 = P[o]**3
        up = LIM // p1
        if up <= P[o] : k = count_primes_up_to( up )
        if up >P[o] : k = count_primes_up_to( up ) - 1

        # selective_bf2 = case_2_selective_brute_force( P[o] , LIM )
        # print('o  = ',  P[o] ,'      p1 = ', p1 , '  up =   ', up   ,'      k= ', k, '      sel BF2 = ',  selective_bf2  )
        print('o  = ',  P[o] ,'      p1 = ', p1 , '  up =   ', up   ,'      k= ', k  )
        counter +=k
        # for a in prime_sieve_generator(1, up ) :
        #     if P[o] != a and p1 *a < LIM :
        #         BOG.add( p1 * a )
                # print(p1, a)
        o+=1

    primes = prime_sieve_generator(1, 100 )
    power_7 = len([ i**7 for i in primes if  i**7 < LIM ])
    print('\npower_7 = ', power_7)
    counter+=power_7

    return print('\nAnswer : \t', counter)          #       Answer:     197912312715


#########       !!!!!!!!!!!!       Please DON'T RUN IT AGAIN IN THIS LIFE !!!!! Just make another better if you wish
# first_solution( 10**12)                     ###  Answer : 	 197912312715

# fs = first_solution( 10**6)
#
# print(len(fs) ,fs )
# fbt = brute_force_testing_1(10**6)
# print('DIFF : \n' ,fbt - fs )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60 ,6), 'mins\n\n')

#### ===== GENERAL IDEA :
# Count the primes up to a given limit. Difficult formula which is called :  prime counting function, Lehmer Formula :
# http://mathworld.wolfram.com/LehmersFormula.html
# Reference problem 10      !!!!!!!!!!!!!!!

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  2 min --------------------------')
t1  = time.time()

# ===== Sat, 31 Jan 2015, 15:28, Min_25, Japan
# Let π(n) be the number of primes less than or equal to nn.
#
# Then,
# f(n) = π(n**(1/7) + ∑ { p≤ n**(1/3)}   (π(N/ p**3) ) − π(N**(1/4) + ∑ { p < n**(1/3)  ∑ { p<q< √(N/p) (π(N/pq)−π(q)),
#
# where p and q are prime numbers.
# I used a similar method as Lucy_Hedgehog's one (see his post in Problem 10) to tabulate the needed values of π(n):
#
#                     { π(N/n)| 1≤n≤N }.
# About 12.3s with pypy.


from math import sqrt

def prob501():
  def isqrt(n):
    if n <= 0:
      return 0

    x = int(sqrt(n) * (1 + 1e-12))
    while True:
      y = (x + n // x) >> 1
      if y >= x:
        return x
      x = y

  def icbrt(n):
    if n <= 0:
      return 0

    x = int(n ** (1. / 3.) * (1 + 1e-12))
    while True:
      y = (2 * x + n // (x * x)) // 3
      if y >= x:
        return x
      x = y

  def prime_sieve(N):
    if N < 2:
      return []

    size = (N + 1) // 2
    is_prime = [1] * size
    is_prime[0] = 0
    v = int(N ** 0.5) // 2 + 1
    for p in range(1, v):
      if not is_prime[p]:
        continue
      for k in range(2 * p * (p + 1), size, 2 * p + 1):
        is_prime[k] = 0

    primes = [2]
    primes.extend([2 * p + 1 for p in range(1, size) if is_prime[p]])
    return primes

  def tabulate_pis(N):
    if N <= 1:
      raise ValueError(N)
    v = int(N ** 0.5)
    smalls = [i - 1 for i in range(v + 1)]
    larges = [0 if i == 0 else N // i - 1 for i in range(v + 1)]

    for p in range(2, v + 1):
      if smalls[p - 1] == smalls[p]:
        continue

      p_cnt = smalls[p - 1]
      q = p * p
      end = min(v, N // q)
      for i in range(1, end + 1):
        d = i * p
        if d <= v:
          larges[i] -= larges[d] - p_cnt
        else:
          larges[i] -= smalls[N // d] - p_cnt
      for i in range(v, q - 1, -1):
        smalls[i] -= smalls[i // p] - p_cnt
    return smalls, larges

  N = 10 ** 12
  smalls, larges = tabulate_pis(N)

  ans = 0

  # p * q * r
  primes = prime_sieve(isqrt(N))
  for pi in range(smalls[icbrt(N)]):
    p = primes[pi]
    if p ** 3 >= N:
      break
    M = N // p
    for pj in range(pi + 1, smalls[isqrt(M)]):
      q = primes[pj]
      r = M // q
      ans += (smalls[r] if r < len(smalls) else larges[p * q]) - smalls[q]

  # p^3 * q
  for p in primes[:smalls[icbrt(N)]]:
    r = N // p ** 3
    if r <= 1:
      break
    ans += smalls[r] if r < len(smalls) else larges[p ** 3]

  # p^4
  ans -= smalls[isqrt(isqrt(N))]

  # p^7
  sth_root = int(pow(N, 1. / 7))
  while sth_root ** 7 <= N:
    sth_root += 1
  while sth_root ** 7 > N:
    sth_root -= 1
  ans += smalls[sth_root]
  print(ans)

# prob501()

t2  = time.time()
print('\nCompleted in :', round((t2-t1) , 6), 's\n\n')


print('\n--------------------------SOLUTION 2,   needs adjusting --------------------------')
t1  = time.time()

def p501():
    N = 10**12
    M = 10**8
    plist = list(head_lt(primes(), M+1))

    def phi(m, b, bm=0):
        ctr = Counter()
        ctr[m] = 1
        for b in reversed(range(b)):
            ctr_ = Counter()
            for m, c in ctr.items():
                if c:
                    ctr_[m] += c
                    if m >= plist[b]:
                        ctr_[m//plist[b]] -= c
            ctr = ctr_
        return sum(m*c for m, c in ctr.items())

    def p2(m, n):
        r2 = isqrt(m)
        z = pi(r2)
        return sum(pi(m//plist[k]) - k for k in range(n, z))

    def pi(m):
        if m <= M:
            return bisect(plist, m)
        else:
            r3 = icbrt(m)
            y = r3 if r3**3 == m else r3+1
            n = pi(y)
            return phi(m, n) + n - 1 - p2(m, n)

    t = 0

    # Numbers of the form p^7
    i = int(N**(1/7))
    while i**7 > 10^7:
        i -= 1
    while (i+1)**7 <= 10^7:
        i += 1
    t += pi(i)

    # Numbers of the form p^3 * q
    for i in range(len(plist)):
        p = plist[i]
        p3 = p**3
        if p3 >= N:
            break
        r = N//p3
        t += pi(r) - (1 if r>=p else 0)

    # Numbers of the form p*q*r
    for i in range(len(plist)):
        p = plist[i]
        if p**3 > N:
            break
        for j in range(i+1, len(plist)):
            q = plist[j]
            if p*q*plist[j+1] > N:
                break
            t += pi(N//(p*q)) - (j+1)

    return t


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 3, Nice idea but not working  --------------------------')
t1  = time.time()

from collections import defaultdict

def primesLessThan(x):
    """ Number of primes less than m using Lehmer Formula.
        Good for x<10^12 or so.
        Ensure that initPrimeCount() is run first."""
    x = int(x+0.000000001)
    if x<=10**6: return pi106[x]
    try:
        return pLTStorage[x]
    except:
        a = primesLessThan(pow(x,1/4))
        b = primesLessThan(pow(x,1/2))
        c = primesLessThan(pow(x,1/3))
        res = meisselFunct(x,a) + ((b+a-2)*(b-a+1))//2
        for i in range(a,b):
            res -= primesLessThan(x/Q[i])
            if i < c:
                bi = primesLessThan(pow(x/Q[i],1/2))
                for j in range(i,bi):
                    res += j - primesLessThan(x/Q[i]/Q[j])
        pLTStorage[x] = res
        return res



meisStorage = defaultdict()
def meisselFunct(m,n):
    """The number of numbers <= m that are coprime to the first n prime numbers.
Ensure that initPrimeCount() is run first."""
    m = int(m)
    if m<=10000: return meis104[n][m]
    if n==0: return m
    try:
        return meisStorage[m][n]
    except:
        meisStorage[m][n] = meisselFunct(m,n-1) - meisselFunct(m/Q[n-1],n-1)
        return meisStorage[m][n]




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

