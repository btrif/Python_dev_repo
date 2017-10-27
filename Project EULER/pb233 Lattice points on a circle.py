#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Tue, 24 Oct 2017, 20:38
#The  Euler Project  https://projecteuler.net
'''
            Lattice points on a circle      -       Problem 233

Let f(N) be the number of points with integer coordinates that are on a
circle passing through (0,0),   (N,0),   (0,N), and (N,N).

It can be shown that f(10000) = 36.

What is the sum of all positive integers N ≤ 10^11 such that f(N) = 420 ?


'''
import time, zzz
from math import sqrt, floor

import itertools
# import numpy
#
# def prime_sieve_numpy(n):                       ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
#     """ Input n>=6, Returns a array of primes, 2 <= p < n
#     http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188 """
#     sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
#     for i in range(1,int(n**0.5)//3+1):
#         if sieve[i]:
#             k=3*i+1|1
#             sieve[       k*k//3     ::2*k] = False
#             sieve[k*(k-2*(i&1)+4)//3::2*k] = False
#     return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]
import math


def prime_sieve(n):       # FOURTH      o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [2] + [i for i in range(3, n , 2) if sieve[i] ]


class PrimeTable():    #  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
    def __init__(self, bound):
        self.bound = bound
        self.primes = []
        self._sieve()

    def _sieve(self ):
        sieve = [True] * self.bound
        for i in range(3, int(self.bound**0.5)+1, 2):
            if sieve[i]:
                sieve[ i*i :: 2*i ] = [False] * ( (self.bound-i*i-1) // (2*i) +1 )

        self.primes =  [2] + [i for i in range(3, self.bound , 2) if sieve[i] ]
        return self.primes


class Factorization():

    ''' Based on a prebuilt prime sieve, and we must pay attention that the prime up range is not
    to low, so that we don't miss a prime when we first factor . As default the value is set to 10.000
      So we need uprange /2         '''
    def __init__(self):
        self.prime_table = PrimeTable(5*10**6)

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
print( F.get_divisors(180180) )

is_square = lambda x :  int(sqrt(x))**2 == x

def C1(lst) :
    '''  Returns the number of divisors from the list lst which are d ≡ 1 (mod4)      '''
    cnt = 0
    for i in lst :
        if i % 4 == 1 :
            cnt+=1
    return cnt


def C3(lst) :
    '''  Returns the number of divisors from the list lst which are d ≡ 3 (mod4)      '''
    cnt = 0
    for i in lst :
        if i % 4 == 3 :
            cnt+=1
    return cnt

def lattice_point_calculation( N ) :
    D = F.get_divisors(N)
    return 4*( C1(D)-C3(D) )


def compute_divisors_mod1(N):
    '''N is a list of prime factors like [5,5,5,17,17,29]
    Computes automatically the C1 which are the number of divisors =1 (mod 4) for a number
    written as factorize'''
    E = dict()
    for i in N:
        if i not in E :            E[i] = 1
        else :            E[i] +=1

    F = sorted([(k,v) for k,v in E.items()])
    print(F)
    S = 1
    for j in range(len(F)) :
#         print(F[j],'   ', (F[j][1]*2)+1  )
        S *=   (F[j][1]*2)+1

    return S


print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def lattice_points_BF( Diameter) :
    cnt = 4
    R = Diameter//2

    for x in range( 1, int((R/sqrt(2)))+1 ):
        y_sq = R*R - x*x
        # print('x = ',x, '      ', y_sq)

        if is_square(y_sq) :
            y = int(sqrt(y_sq))
            cnt+=8      # except the 4 points there are 8 symmetric points for each coordinate
            # print(' a pair from the 8 symmetric points at coordinates =      x =', x ,'     y=', y, '        radius=', R )

    # print('\nR (' + str(R),') = ' , cnt )
    return cnt



# lattice_points_BF(84246500)                   #   Total Number of points =  420
# lattice_points_BF(10**4)                            #   Total Number of points =  36
lattice_points_BF(50)

# ====== DOCUMENTATION  ==========
# https://math.stackexchange.com/questions/124165/integer-solutions-lattice-points-to-arbitrary-circles             !!!!!!!!!!!!!!!
# http://oeis.org/A004018
# http://mathworld.wolfram.com/CircleLatticePoints.html
# http://mathworld.wolfram.com/SchinzelsTheorem.html
# http://mathworld.wolfram.com/SchinzelCircle.html
# http://mathworld.wolfram.com/KulikowskisTheorem.html
# http://euler.genepeer.com/schinzels-theorem/
# https://www.cut-the-knot.org/arithmetic/algebra/Kulikowski.shtml        - FOR SPHERE INTEGRAL POINTS
# http://www.geeksforgeeks.org/circle-lattice-points/
# https://archive.lib.msu.edu/crcmath/math/math/s/s066.htm
# https://archive.lib.msu.edu/crcmath/math/math/c/c314.htm


for i in range(1,51) :
    bf = lattice_points_BF(2*i)
    lpc = lattice_point_calculation(2*i*i)

    print('R=', i ,  '    =>    lattice_point_calculation = ', lpc , '         Brute_Force = ', bf )

D1 = F.get_divisors(84246500**2)
print('\nN=', 84246500**2 ,'   => ', 'Res = ',4*( C1(D1)-C3(D1) )  )
print('C1 = ', C1(D1))
print('C3 = ', C3(D1))

D1 = F.get_divisors((5* 5* 5* 13* 17* 17* 23* 23)**2)
print('\nN=', 248431625 ,'   => ', 'Res = ',4*( C1(D1)-C3(D1) )  )
print('C1 = ', C1(D1))
print('C3 = ', C3(D1))



D1 = F.get_divisors((5)**2)
print('\nN=', 5**2 ,'   => ', 'Res = ',4*( C1(D1)-C3(D1) )  )
print('C1 = ', C1(D1))
print('C3 = ', C3(D1))

D1 = F.get_divisors((5*13)**2)
print('\nN=', 65**2 ,'   => ', 'Res = ',4*( C1(D1)-C3(D1) )  )
print('C1 = ', C1(D1))
print('C3 = ', C3(D1))

D1 = F.get_divisors((5*13*17)**2)
print('\nN=', 1105**2 ,'   => ', 'Res = ',4*( C1(D1)-C3(D1) )  )
print('C1 = ', C1(D1))
print('C3 = ', C3(D1))

D1 = F.get_divisors((5*13*17*37)**2)
print('\nN=', 40885**2 ,'   => ', 'Res = ',4*( C1(D1)-C3(D1) )  )
print('C1 = ', C1(D1))
print('C3 = ', C3(D1))


def brute_force_verification(up_lim) :
    for i in range(1, up_lim+1) :
        lpc = lattice_point_calculation(2*i*i)
        if lpc == 420 :
            print('i=', i  )

# brute_force_verification(38*10**6)

t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')

# CHECK REFERENCE VALUES :    f(84246500) = f(248431625) = 420

print('\n================  My FIRST SOLUTION, SLOW, 15 min  ===============\n')
t1  = time.time()

# ==== OBSERVATIONS :
# @2017-10-23, 10:30 - we observe that numbers of the form [ p1**3, p2**2, p3 ] squared where
# p1, p2 p3 = 1 (mod 3 )
# are solutions to our problem because they give coefficients C1(factors) = 105
# Smallest such a number is : [5,5,5,13,13,17]**2.  Then we must take all the combinations with primes different
# then the primes p1, p2, p3
# METHOD : we must form all combinations of 3 primes with (mod 4) == 1 and then see how many numbers can
# be formed with them also avoiding the multiples of other primes (mod 4) == 1
# ======!!!!!!!!! IMPORTANT CLUE !!!!!!!!!!!============
print('--------------- Numbers are of the form : ----------------------')
print(compute_divisors_mod1([5, 5, 5, 13, 13, 17]) )                        # p1**3 * p2**2 * p3**1   and permutations
print(compute_divisors_mod1([5, 5, 5, 5, 5, 5, 5, 13, 13, 13]) )        # p1**7 * p2**3     and permutations
print(compute_divisors_mod1([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 13, 13]) )        # p1**10 * p2**2    and permutations


def solution1_lattice_points_on_circle(up_lim):
    up_lim = int(up_lim)
    min_comb = 5**3 * 13**2 #* 17
    max_prime = int( (up_lim)/min_comb )
    print('max prime = ', max_prime)
    primes = prime_sieve(max_prime)
    print('length primes = ', len(primes))

    primes_mod4_1 = [ i for i in primes if i%4==1  ]
    print('length P_mod4_is_1 = ' , len(primes_mod4_1) )
    print ( primes_mod4_1[-50::]  )
    P4_1 = set(primes_mod4_1)

    Sum = 0
    for i in range(0, len(primes_mod4_1)):
        p1 = primes_mod4_1[i]
        if p1**3 > up_lim : break
        for j in range(i+1,  len(primes_mod4_1)):
            p2 = primes_mod4_1[j]
            if p1**3* p2**2 > up_lim : break
            for k in range(j+1,  len(primes_mod4_1)):
                p3 = primes_mod4_1[k]
                if p1**3* p2**2 * p3 > up_lim : break

                print(p1, p2, p3)
                perm = list(itertools.permutations([3,2,1]))
                for l in perm :
                    n = p1**l[0] * p2**l[1] * p3**l[2]
                    if n < up_lim :
                        rng = int(up_lim/n )+1
                        print(p1, p2, p3 ,'      ',l, '     ', n ,'    rng = ', rng)
                        for o in range(1, rng) :
                            for q in primes_mod4_1 :
                                if o%q == 0 : break
                                if q > o :
                                    seeked = (n*o)
                                    # print('seeked nr =  ' , seeked, '       mult = ', o )
                                    Sum += seeked
                                    break


    ccnt = 0
    F = [ (7, 3 ) , ( 10, 2 )  ]
    for a in F :
        perm2 = list( itertools.permutations(a) )
        for l2 in perm2 :
            for i2 in range(0, len(primes_mod4_1)):
                p4 = primes_mod4_1[i2]
                if p4**10 > up_lim : break

                for j2 in range(i2+1,  len(primes_mod4_1)):
                    p5 = primes_mod4_1[j2]

                    n2 = p4**(l2[0]) * p5**(l2[1])
                    if n2 > up_lim : break

                    rng2 = int(up_lim/n2)+1
                    print( p4, p5,'      ', l2 , '       ',n2 ,'      rng2 =  ', rng2, '     ' )

                    for o2 in range(1, rng2) :
                        for q2 in primes_mod4_1 :
                            if o2%q2 == 0 : break
                            if q2 > o2 :
                                ccnt += 1
                                seeked2 = (n2*o2)
                                print('seeked2 nr =  ' , seeked2, '       mult2 = ', o2 )
                                Sum += seeked2
                                break


    print('\nnrs diff = ', ccnt )
    print('\nTotal sum = ' , Sum )
    return Sum

# solution1_lattice_points_on_circle(10**11)      #Total sum =  271204031455541309        Completed in : 15.95 mins
# solution1_lattice_points_on_circle(38e6)


# CLUES : right # of solutions at 5422629
# My code returns 30875234922 for n<=38000000, is it correct?

t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60 , 2), 'mins\n\n')


print('\n========  My SECOND SOLUTION, 9 sec , IMPROVED using second sieve for multipliers  ==========\n')
t1  = time.time()

def solution2_lattice_points_on_circle(up_lim):
    up_lim = int(up_lim)
    min_comb = 5**3 * 13**2 #* 17
    max_prime = int( (up_lim)/min_comb )
    print('max prime = ', max_prime)
    primes = prime_sieve(max_prime)
    print('length primes = ', len(primes))

    primes_mod4_1 = [ i for i in primes if i%4==1  ]
    print('length P_mod4_is_1 = ' , len(primes_mod4_1) )
    print ( primes_mod4_1[-50::]  )
    P4_1 = set(primes_mod4_1)

    # Building sieve for valid multipliers #
    lim = int(up_lim/(5**3 * 13**2 * 17) )+1
    print('non_mod4_1 primes lim = ', lim )
    sieve_non_mod4_1 = [ i for i in range(lim+1) ]

    for p in primes_mod4_1 :
        if p > lim : break
        # print(p)
        sieve_non_mod4_1[p :: p ] = [0] * ( lim//p  )

    print(sieve_non_mod4_1[:100])

    Sum = 0
    for i in range(0, len(primes_mod4_1)):
        p1 = primes_mod4_1[i]
        if p1**3 > up_lim : break
        for j in range(i+1,  len(primes_mod4_1)):
            p2 = primes_mod4_1[j]
            if p1**3* p2**2 > up_lim : break
            for k in range(j+1,  len(primes_mod4_1)):
                p3 = primes_mod4_1[k]
                if p1**3* p2**2 * p3 > up_lim : break

                # print(p1, p2, p3)
                perm = list(itertools.permutations([3,2,1]))
                for l in perm :
                    n = p1**l[0] * p2**l[1] * p3**l[2]
                    if n < up_lim :
                        rng = int(up_lim/n )+1
                        # print(p1, p2, p3 ,'      ',l, '     ', n ,'    rng = ', rng)
                        for o in range(1, rng) :
                            seeked = ( n*sieve_non_mod4_1[o])
                            # print('seeked nr =  ' , seeked, '       mult = ', o )
                            Sum += seeked

    ccnt = 0
    F = [ (7, 3 ) , ( 10, 2 )  ]
    for a in F :
        perm2 = list( itertools.permutations(a) )
        for l2 in perm2 :
            for i2 in range(0, len(primes_mod4_1)):
                p4 = primes_mod4_1[i2]
                if p4**10 > up_lim : break

                for j2 in range(i2+1,  len(primes_mod4_1)):
                    p5 = primes_mod4_1[j2]
                    n2 = p4**(l2[0]) * p5**(l2[1])

                    if n2 > up_lim : break
                    # print(p4, p5)

                    rng2 = int(up_lim/n2)+1
                    # print( p4, p5,'      ', l2 , '       ',n2 ,'      rng2 =  ', rng2, '     ' )

                    for o2 in range(1, rng2) :
                        seeked2 = ( n2*sieve_non_mod4_1[o2])
                        # print('seeked2 nr =  ' , seeked, '       mult2 = ', o2 )
                        Sum += seeked2


    # print('\nnrs diff = ', ccnt )
    print('\nTotal sum = ' , Sum )
    return Sum

solution2_lattice_points_on_circle(10**11)      #   Total sum =  271204031455541309     Completed in : 9.69  s
# solution2_lattice_points_on_circle(38e6)


t2  = time.time()
print('\nCompleted in :', round((t2-t1) , 2 ), ' s\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  AMAZING, Prime sieve and counting sieve. , 10 seconds --------------------------')
t1  = time.time()

# ===Tue, 4 Feb 2014, 17:33, ChopinPlover, Taiwan
# Prime sieve and counting sieve.


class Problem():
    def __init__(self):
        self.problem_range = 10**11
        self.good_primes = []
        self.range_counting = None

        self._init_primes(self.problem_range // (5**3 * 13**2) + 1)
        self._init_range_counting()

    def solve(self):
        n = len(self.good_primes)
        count = 0
        for i in range(n):
            p = self.good_primes[i]
            if p**2 > self.problem_range:
                break
            for j in range(i+1, n):
                q = self.good_primes[j]
                if p**2 * q**2 > self.problem_range:
                    break
                count += self._get_count(p**10 * q**2)
                count += self._get_count(p**2 * q**10)
                count += self._get_count(p**7 * q**3)
                count += self._get_count(p**3 * q**7)
                for k in range(j+1, n):
                    r = self.good_primes[k]
                    good_product = p**3 * q**2 * r
                    if good_product > self.problem_range:
                        break
                    count += self._get_count(good_product)
                    count += self._get_count(p**3 * q * r**2)
                    count += self._get_count(p**2 * q**3 * r)
                    count += self._get_count(p**2 * q * r**3)
                    count += self._get_count(p * q**3 * r**2)
                    count += self._get_count(p * q**2 * r**3)
        print(count)

    def _init_primes(self, sieve_range):
        visited = [False] * sieve_range
        visited[0] = visited[1] = True
        for i in range(2, sieve_range):
            if visited[i]:
                continue
            if i % 4 == 1:
                self.good_primes.append(i)
            for j in range(i+i, sieve_range, i):
                visited[j] = True
        print('Prime of form (4k+1) count:', len(self.good_primes))

    def _init_range_counting(self):
        count_range = self.problem_range // (5**3 * 13**2 * 17) + 1
        visited = [False] * count_range
        visited[0] = True
        for p in self.good_primes:
            for q in range(p, count_range, p):
                visited[q] = True
        self.range_counting = [0] * count_range
        for i in range(1, count_range):
            self.range_counting[i] = self.range_counting[i-1]
            if visited[i] is False:
                self.range_counting[i] += i
        print('Range counting:', len(self.range_counting))

    def _get_count(self, good_product):
        return self.range_counting[self.problem_range // good_product] * good_product


# problem = Problem()
# problem.solve()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 2,  20 sec --------------------------')
t1  = time.time()

# ====Wed, 11 Oct 2017, 00:12, mbh038, England
# About 6.2s in Python, using the sum of squares function applied to 2n22n2
# (arrived at without rescaling the circle - hope that wasn't an error and I just got lucky),
# having transposed the circle centre to the origin. Several days of effort!

import numpy as np
import time

def p233(limit):
    t=time.clock()

    qs=pairs(limit)+trios(limit)

    ns=[]
    for q in qs:
       while q<=limit:
           ns.append(q)
           q*=2

    pgood=notPrime4k1Factor(limit//min(ns)+1)

    nfinal=[]
    for n in ns:
        for p in pgood:
            np=n*p
            if np>limit:
                break
            nfinal.append(np)

    print (sum(nfinal))
    print(time.clock()-t)

#(3,7) and (2,10) cases. No need to consider (1,17) case
def pairs(limit):

    q2s=[]
    plim=int(max((10**11/5**10)**(1/2),(10**11/5**7)**(1/3)))
    pfs=[int(p) for p in primeSieve(plim) if p%4==1]

    #(3,7) case
    for q1 in pfs:

        for q2 in pfs:
            if q2==q1:
                continue

            q2s.append(q1**3*q2**7)

    #(2,10) case - need only consider p^2x5^10 since 5^2x13^10>10^11
    for q1 in pfs[1:]:

        q2s.append(q1**2*9765625)

    return q2s

#(1,2,3) case
#Finds trios of 4k+1 primes: q1*q2^2*q3^3 <= limit
def trios(limit):

    qs=primeSieve(limit//(5**3*13**2)+1)
    qs=qs[qs%4==1]
    trioList=[]

    for q1 in qs:

        q2lim=(limit/(q1*125))**(1/2)
        for q2 in qs:

            if q2==q1:
                continue
            if q2>q2lim:
                break

            q2sq=q2**2
            q3lim=(limit/(q1*q2sq))**(1/3)
            for q3 in qs:

                if q3==q1 or q3==q2:
                    continue
                if q3>q3lim:
                    break
                trioList.append(q1*q2sq*q3**3)

    return trioList

def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

def notPrime4k1Factor(n):
    """return array of numbers not divisible by 2 or primes p = 1 mod 4"""
    sieve=np.ones(n+1,dtype=bool)
    ps=primeSieve(n)
    ps=ps[ps%4==1]
    for i in ps:
        if sieve[i]:
            sieve[i::i]=False
    ps= np.nonzero(sieve)[0]

    return ps[ps%2==1]

# p233(10**11)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# ==== Mon, 18 Apr 2016, 15:40, Avi Levy, USA
# the number of lattice points on the circle is 420
# iff N factors into a product of primes not = 1 mod 4
# times p^a q^b r^c where (2a+1)(2b+1)(2c+1) = 105
# and p, q, r are congruent to 1 mod 4
#
# Possibilities:
#    p^3  q^2 r   7 * 5 * 3 = 105
#    p^7  q^3     15 * 7    = 105
#    p^10 q^2     21 * 5    = 105
#  <too large>    35 * 3    = 105
#
#  Let topNumber = 10^11 / (5^3 * 13^2).
#
#  Using a variant of the Eratosthenes sieve, we
#  produce a list of numbers k <= topNumber that have
#  no 1 mod 4 prime factors.
#
#  For all n <= topNumber we cache the sum of all
#  such k <= n. Then we iterate over each of the
#  three cases above and multiply by the cached
#  sum to conclude.
def solution3():
    import math, time
    start_time = time.time()

    def primesTo(n):
      """
        Returns a list of primes up to
        (and possibly including) n
      """
      primes = [2]
      num = 1
      cur = 3
      while cur <= n:
        isPrime = True
        for p in primes:
          if p*p > cur:
            isPrime = True
            break
          if cur % p == 0:
            isPrime = False
            break
        if isPrime:
          num = num + 1
          primes.append(cur)
        cur = cur + 1
      return primes

    def p1mod4to(n):
      """
        Returns a list of primes congruent to
        1 mod 4 up to (and possibly including) n
      """
      pp = [5]
      num = 1
      cur = 13
      while cur <= n:
        isPrime = True
        for p in primes:
        # use pregenerated list of small primes
          if p*p > cur:
            isPrime = True
            break
          if cur % p == 0:
            isPrime = False
            break
        if isPrime:
          num = num + 1
          pp.append(cur)
        cur = cur + 4
      return pp


    topNumber = 10**11 // (5 ** 3 * 13 ** 2)
    primes = primesTo(int(math.sqrt(topNumber)))
    p1mod4 = p1mod4to(topNumber)

    sieve = set(range(1, topNumber + 1))
    for p in p1mod4:
      for i in range(1, (topNumber // p) + 1):
        if i * p in sieve:
          sieve.remove(i * p)

    partialSums = [0]
    for i in range(1, topNumber + 1):
      partialSums.append(partialSums[i-1])
      if i in sieve:
        partialSums[i] += i

    s = 0
    for i in p1mod4:
      if i ** 3 * 5 ** 2 * 13 > 10 ** 11:
        break
      for j in p1mod4:
        if i ** 3 * j ** 2 * 5 > 10 ** 11:
          break
        if j == i:
          continue
        for k in p1mod4:
          if k == i or k == j:
            continue
          t = i ** 3 * j ** 2 * k
          if t > 10 ** 11:
            break
          s += t * partialSums[10 ** 11 // t]

    for i in p1mod4:
      if i ** 7 * 5 ** 3 > 10 ** 11:
        break
      for j in p1mod4:
        if j == i:
          continue
        t = i ** 7 * j ** 3
        if t > 10 ** 11:
          break
        s += t * partialSums[10 ** 11 // t]

    for i in p1mod4:
      if i ** 10 * 5 ** 2 > 10 ** 11:
        break
      for j in p1mod4:
        if j == i:
          continue
        t = i ** 10 * j ** 2
        if t > 10 ** 11:
          break
        s += t * partialSums[10 ** 11 // t]

    print(s," time: ", time.time() - start_time) # in seconds
    return s
    # 271204031455541309  time:  18.151867




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 4,  VERY ELEGANT , 8 sec --------------------------')
t1  = time.time()

# ===Thu, 30 Mar 2017, 22:03, MuthuVeerappanR, India
#
# Oh my God... Python is so quick... My second program in Python..
# First one was for my solution to Problem 354..
# Modified it to calculate sum rather than count..

Lim = 10 ** 11
K = 105
Ans = 0

def PrimeSieve(n):
  Primes, Primes1, Primes2 = [], [], []
  flag = [0] * (n + 1)
  for i in range(2, n + 1):
    if(flag[i] == 0):
      Primes.append(i)
      if(i % 4 == 1):
        Primes1.append(i)
      else:
        Primes2.append(i)
      for j in range(i * i, n + 1, i):
        flag[j] = 1
  return Primes, Primes1, Primes2

Primes, Primes1, Primes2 = PrimeSieve(int(Lim / (5 * 5 * 5 * 13 * 13)))

tempLim = int(Lim / (5 * 5 * 5 * 13 * 13 * 17))

UnDivs = [0] + [i for i in range(1, tempLim + 1)]

for p in Primes1:
  temp = p
  while(temp <= tempLim):
    UnDivs[temp] = 0
    temp += p

for i in range(1, tempLim + 1):
  UnDivs[i] += UnDivs[i - 1]

def Times(l):
  res = 1
  for k in l:
    res *= k
  return res

def Power(list1, list2):
  assert len(list1) == len(list2)
  return [x ** y for x, y in zip(list1, list2)]

def PrimeSigNums(l, k = 0, m = 1):
  res = 0
  if(len(l) == 0):
    res += m * UnDivs[int(Lim / m)]
    return res

  for i in range(k, len(Primes1)):
      j = Primes1[i:i + len(l)]
      if(len(l) != len(j)):
          break
      if(m * Times(Power(j, l)) > Lim):
          break
      res += PrimeSigNums(l[1:], i + 1, m * (Primes1[i] ** l[0]))
  return res

def PrimeSigRec(n, arr = []):
  global Ans
  if(n == 1):
    Ans += PrimeSigNums(arr)
    return 0
  for i in range(1, n):
    if(n % (2 * i + 1) == 0):
      PrimeSigRec(n // (2 * i + 1), arr + [i])
  return 0

# PrimeSigRec(K)
# print(Ans)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 5,  5 sec --------------------------')
t1  = time.time()

# ===Tue, 19 May 2009, 23:13, Seth Troisi, USA
# I had the weird problem working out how odd N's worked but then I got it out worked it and bam
# some python with classes and abstraction
# 3.541 seconds

#Number of lattice points (x,y) on the circumference of a circle of radius n with center at (0,0).
#http://mathworld.wolfram.com/CircleLatticePoints.html
#see math
from math import sqrt
def sieveOfErat(end):
    if end < 2: return []
    #The array doesn't need to include even numbers
    lng = int((end//2)-1+end%2)
    # Create array and assume all numbers in array are prime
    sieve = [True]*(lng+1)
    # In the following code, you're going to see some funky
    # bit shifting and stuff, this is just transforming i and j
    # so that they represent the proper elements in the array
    # Only go up to square root of the end
    for i in range(int(sqrt(end)) >> 1):
        if not sieve[i]: continue
        # Unmark all multiples of i, starting at i**2
        for j in range( (i*(i + 3) << 1) + 3, lng, (i << 1) + 3):
            sieve[j] = False
    primes = [2]
    primes.extend([(i << 1) + 3 for i in range(lng) if sieve[i]])
    return primes

class lattice():
	def __init__(self, Points, N):
		self.N = N
		self.B = Points // 4
		self.primes = list()
		self.useful = list()							#[5,13,17,29,37...
		self.ignore = list([2])							#[2,49,121,361...
		self.usefulFactorsMin = 		(5**3)*(13**2)*(17**1)		#359125
		self.usefulFactorsMax =		self.N // ((5**3)*(13**2))		#p < 4733726	= 4.74 * 10^6
		self.ignoreFactorsMax =		self.N // self.usefulFactorsMin
		self.factorPrimes()

		self.forms = list()
		self.generateForms()
		self.sumInts = 0

	def factor(self,Number):
		root = int(sqrt(Number)) + 1
		factors = list()
		for prime in self.primes:
			while N % prime == 0:
				factors.append(prime)
				Number /= prime
				if Number == 1:
					return factors

	def factorPrimes(self):
		self.primes = sieveOfErat(self.usefulFactorsMax + 1000)
		self.ignore = [i for i in range(self.ignoreFactorsMax + 1)]
		for prime in self.primes:
			if prime % 4 == 1:
				self.useful.append(prime)
				if prime < self.ignoreFactorsMax:
					for mult in range(1,self.ignoreFactorsMax // prime+1):
						self.ignore[mult * prime] = 0
		for i in range(1, self.ignoreFactorsMax + 1):
			self.ignore[i] += self.ignore[i-1]

	def generateForms(self):
		#factors = self.factor(self.B)
		self.forms +=  ((3,2,1), (17,1), (10,2), (7,3), (52,))


	def test(self, Form, Bases, AddToAnswer):
		number = 1	#need a two to cancel the divide by two
		for i, base in enumerate(Bases):
			number *= self.useful[base] ** Form[i]
			if number > self.N:
				return False

		if AddToAnswer == False:
			return True

		self.sumInts += number * self.ignore[self.N//number]

		return True

	def testForm(self, Form, Numbers, StartPosition, EndPosition):
		while Numbers[:StartPosition].count(Numbers[StartPosition]) >= 1:
			Numbers[StartPosition] += 1
		while self.test(Form, Numbers, StartPosition == EndPosition):
			if StartPosition != EndPosition:
				self.testForm(Form, Numbers[:], StartPosition + 1, EndPosition)
			Numbers[StartPosition] += 1
			while Numbers[:StartPosition].count(Numbers[StartPosition]) >= 1:
				Numbers[StartPosition] += 1
		Numbers[StartPosition] = 0

	def run(self):
		for form in self.forms:
			self.testForm(form, [0] * len(form), 0, len(form)-1)

	def answer(self):
		if self.sumInts == 0:
			self.run()
		return self.sumInts


test = lattice(420, 10**11)
print ("answer 233: %s" %(test.answer()))



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


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

