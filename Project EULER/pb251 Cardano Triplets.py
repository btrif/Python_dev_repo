#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @ Completed on Wed, 27 Sep 2017, 19:00
#The  Euler Project  https://projecteuler.net
'''
Cardano Triplets            -           Problem 251

A triplet of positive integers (a,b,c) is called a Cardano Triplet if it satisfies the condition:

                (a + b*(c)**(1/2) )**(1/3) + (a - b*(c)**(1/2) )**(1/3) = 1

For example, (2,1,5) is a Cardano Triplet.

There exist 149 Cardano Triplets for which a+b+c ≤ 1000.

Find how many Cardano Triplets exist such that a+b+c ≤ 110,000,000.


'''
import time, zzz
import gmpy2
from math import floor, sqrt
from pyprimes import factorise
import itertools, functools, operator

# http://math.stackexchange.com/questions/1885095/parametrization-of-cardano-triplet

#  (a + b* c **(1/2) )**(1/3) + (a - b* c **(1/2) )**(1/3) = 1
#
# can be written as :   ( http://www.wolframalpha.com/input/?i=((a%2Bbsqrt(c))%5E(1%2F3))+%2B+((a-bsqrt(c))%5E(1%2F3))+%3D+1 )
#
# 8*a**3 + 15*a**2 + 6*a - 27*b**2*c = 1
#
# That is really faster to compute for higher numbers than the previous form, but it goes up really
# fast and I need BigInteger (Java) that slows down again the code.
# I found on google that this formula can be parametrized with
# a = 3*k + 2
# and
# b**2* c= (k+1)**2 * (8*k+5)
# http://stackoverflow.com/questions/36727886/how-do-i-write-this-equation-in-python
# https://www.math.ucdavis.edu/~kkreith/tutorials/sample.lesson/cardano.html
# http://www.wolframalpha.com/input/?i=((a%2Bbsqrt(c))%5E(1%2F3))+%2B+((a-bsqrt(c))%5E(1%2F3))+%3D+1
# https://proofwiki.org/wiki/Cardano%27s_Formula
# https://en.wikipedia.org/wiki/Cubic_function#Cardano.27s_method


def is_cardano_triplet(a, b, c):
    return (a + 1)**2 * (8*a - 1) - 27*b**2*c == 0

print('is_cardano_triplet: \t' , is_cardano_triplet(2, 1, 5) )
print('is_cardano_triplet: \t' , is_cardano_triplet(5, 4, 13) )

is_square = lambda x :  int( x**(1/2) )**2 == x

def get_divisors(n):      ### ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST     MUST BE IMPROVED !! It is a sqrt(n) Algorithm
    from math import sqrt
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)

def square_factoring(nr) :          # o(^_^)o ©by Bogdan Trif @ 2017-09-26, 14:00
    ''' Factorizing the squares of a number '''
    F = list(factorise(nr))
    # print( F )
    L, R = [], set()
    for i in F :
        j = i[1]//2
        for k in range(j):
            L.append(i[0])
    # print(L)
    if len(L) ==1 :
        return set([1]+L)
    else :
        for o in range(1, len(L)+1 ) :
            C = list(itertools.combinations(L, o))
            # print(C)
            for q in C :
                K =  functools.reduce(operator.mul, q)
                # print(K)
                R.add(K)
        return sorted(R.union({1}))



def square_factoring_pair(nr1 , nr2 ) :     # o(^_^)o ©by Bogdan Trif @ 2017-09-26, 18:00
    ''':Description: take two separate numbers nr1 & nr2 . nr1 is taken as a square but for
        simplicity its root is factorized and then the factor powers multiplied by two. nr2 is taken
        as it is. After the factorizations the factoriations are composed resulting the factorization
        in its SQUARES  of a BIG NUMBER to the form nr1*nr1*nr2
     :Scope:    factorize in its SQUARES a number of the form nr1*nr1*nr2
     :return:   lst, of factors with their corresponding powers
     '''
    F = []
    for l in list(factorise(nr1)) :
        F.append( (l[0], l[1]*2) )
#         print(F)
    F =  F + list(factorise(nr2))

    # print( F )
    L, R = [], set()
    for i in F :
        j = i[1]//2
        for k in range(j):
            L.append(i[0])
    # print(L)
    if len(L) ==1 :
        return set([1]+L)
    else :
        for o in range(1, len(L)+1 ) :
            C = list(itertools.combinations(L, o))
#             print(C)
            for q in C :
                K =  functools.reduce(operator.mul, q)
#                 print(K)
                R.add(K)
        return R.union({1})

print('\nsquare_factoring : \t' ,square_factoring(2041200) )



print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def brute_force_test( lim) :
    cnt = 0
    for a in range(1, lim//2 ) :
        for b in range(1, lim ) :
            if a + b > lim : break
            for c in range(1, lim-a-b+1 ) :
                if is_cardano_triplet(a,b,c) and (a+b+c) <= lim :
                    cnt+=1
                    print(str(cnt)+'.      a=',a, '    b=',b, '     c=',c ,'             bbc=', b**2*c)


    return print('Brute Force Result : \t', cnt )

# brute_force_test( 10**3 )           # Brute Force works fine

print('------------------------')



t2  = time.time()
print('\nCompleted in :', round((t2-t1),2), 's\n\n')

print('\n================  My FIRST SOLUTION,  VERY SLOW ===============\n')
t1  = time.time()

def first_solution( up) :
    S, cnt = 0, 0
    for k in range( up//6  ) :
    # for k in range(10**6 , up//6  ) :
        a = 3*k + 2
        a1, a2 = k+1 , 8*k+5
        bbc = a1*a1*a2
        F = square_factoring_pair(a1, a2)
        # F = square_factoring(bbc)
        for b in F :
            c = bbc //(b*b)
            if is_cardano_triplet(a, b, c) and  a+b+c <= up :
                cnt+=1
                if k%10**5 == 0 :
                    print(str(cnt)+'.      k= ', k, '        a , b, c = ', a,'   ' , b,'   ', c ,'          s= ', a+b+c,'        bbc= ',bbc  )


    return print('\nAnswer : \t', cnt)


# @ 2017-04-22 - For now this is FAR TOO SLOW

# first_solution(10**5)

# first_solution(11*10**7)              #Answer : 	 18946051       Completed in : 24832.5773 s
# zzz.au_clair_de_la_lune()

t2  = time.time()
print('\nCompleted in :', round((t2-t1) , 4 ), 's\n\n')


#===== IDEAS ==========
# === Wed, 24 Jun 2009, 16:39, daniel.is.fischer, Germany
# First, like everybody, I found
# a = 3k+2
# b2*c = (k+1)2*(8k+5).
# For fixed k, a+b+c is minimal if b = 2c, which is then approximately 24/3*k,
# so the smallest possible sum for fixed k is about 3*(1+21/3)*k,
# giving an approximate limit of N/6.78 for k (an exact limit takes some fiddling, with N/6.77 you're on the safe side).
# But the largest possible value for the sum is obtained for b = 1, when
# a+b+c [gt] 8k3, and on the other end, when b is as large as possible, it is typically of order k3/2.
# So for large k, most of the possible values of b lead to sums exceeding the limit.
#
# The question is then, is it worth the trouble to factorise (k+1) and (8k+5) for all interesting k?
# The answer is, sadly, "apparently not".
# It takes longer to collect the factors and then combine them,
# than it takes to just let some variable traverse the admissible range and check if it's good by a trial division -
# at least if you organise that properly.
#
# If we look again at b2*c = (k+1)2*(8k+5), we see that we must write 8k+5 = s*u2 with a squarefree s,
# then b can be any divisor of u*(k+1) and c = s*((u*(k+1))/b)2.
# Now, if we base our algorithm on k, we have to find s and u, that is, factorise 8k+5.
# That's not good, avoiding the factorisations is our goal.
#
# So we base our algorithm on s (and then u).
# If 8k+5 = s*u2 with squarefree s, then s ≡ 5 (mod 8) and u is odd. Conversely, if u is odd and m ≡ 5 (mod 8), then m*u2 ≡ 5 (mod 8).
#
# The first step is finding the squarefree s ≡ 5 (mod 8) which are small enough to generate triplets below the limit. That's
#
#
# If s = 8i+5 is squarefree, the samllest sum of a Cardano triplet derived from s is
# (3i+2) + (i+1) + (8i+5) = 12i+8. 12i+8 ≤ N means i [lt] (N+4)/12.
#
# Next, for a squarefree s = 8i+5, count the triplets.
# Determine the largest u so that 8k+5 = (8i+5)*u2 can generate a legitimate triplet, i.e. k < N/6.77 (or something of the sort).
# Outer loop over odd u from 1 to that limit.
# Given s*u2 = 8k+5, we easily find (k+1) = (s*u2+3)/8, a = (3*s*u2+1)/8 and set b0 = u*(k+1).
# Then all Cardano triplets with that a have c = s*d2, b = b0/d for some divisor d of b0.
# We need N ≥ a+b+c = a + b0/d + s*d2 ≥ a + b0/d + s,
# hence d ≥d1 = ceiling(b0/(N-a-s)). If b0 is odd and d1 even, increment d1.
# Then we know that a + b + c ≥ a + b0/d + s*d12, hence d ≥ d2 = ceiling(b0/(N-a-s*d12)).
# Iterate once more to have the starting value of d close to the first that gives a sum not exceeding the limit.
# Inner loop over d, incrementing by 2 for odd b0.
# If d is a divisor of b0 and the sum is small enough,
# count, break when the upper end of the range of possible d is reached.

# === Wed, 24 Jun 2009, 20:39, Yuval Dor, ISrael
# (lots of edits...)
#
# I too tried to look at b^2*c first but there's a faster approach.
#
# Let:
#
# k = 0
# b = 1
# c = 5
#
# In every step, increment b by 1, c by 8, and k by 1.
#
# a = 3*k + 2
#
# This always yields a solution that satisfies the equation but not necessarily the condition. It's provable by induction.
#
# To find other solutions, find the square part of c (the square part of 24, for example, is 2, because 24 = 2^3*3).
# It is very easy to find the square part of a number because you only have to scan primes, p, such that p^3 is smaller than the number.
#
# Divide c by its square part (squared), multiply b by the square part of c.
# This yields the maximum value of b and the minimal value of c for this particular value of a.
# Can't make c smaller than this: the square root of all of its divisors is irrational.
# If this doesn't satisfy the condition, no other pair will: because b0 is smaller than c0,
# and we multiply c0 by a square factor and b by same factor not squared.
#
# You don't have to factor b*(square part of c), it's easier to just go through numbers and
# see if they divide it and if they satisfy the condition, and break the loop if c*(divisor)^2 > max - happens very fast,
# because usually the square part of c is 1. For every divisor of b, of course, the triplet (a, b/divisor, c*(divisors^2)) is valid.
#
# To make things faster I stored all square divisors of all numbers that equal 5 modulo 8 (i.e, possible c's)
# in a dictionary except "trivial" prime square divisors less than 100 to save space (checked manually for these). Works pretty fast.
#
# That is all. Nice question.


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()


# === Fri, 26 Sep 2014, 18:08, ChopinPlover, Taiwan
#
# Brute force some small cases to get patterns: a=2k+3 and b^2⋅c=(2k+1)^3+(3k+2)^2=(k+1)^2 * (8k+5) .
#
# Next I want to do prime-factorization on k+1 and prime-square-factorization on 8k+5.
# Naive factorization is too slow, and thus I do sieve on k+1 and 8k+5  for 1≤k≤(N−2)/3 .
#  Excellent problem!


import itertools


class PrimeTable():
    def __init__(self, bound):
        self.factorization = [{} for _ in range(bound + 1)]
        self.special_factorization = [{} for _ in range(bound + 1)]
        self.primes = []
        self._sieve(bound)

    def _sieve(self, bound):
        visited = [False] * (bound + 1)
        visited[0] = visited[1] = True
        for i in range(2, bound + 1):
            if visited[i]:
                continue
            self.primes.append(i)
            for j in range(i, bound + 1, i):
                visited[j] = True
                self.factorization[j][i] = 1
            d = i**2
            while d <= bound:
                for j in range(d, bound + 1, d):
                    self.factorization[j][i] += 1
                d *= i

            # Sieve on (8k+5)-type number
            if i == 2 or 8 * bound + 5 < i**2:
                continue
            k = (-5 * self._mod_inverse(8, i**2)) % i**2
            if k > bound:
                continue
            for j in range(k, bound + 1, i**2):
                self.special_factorization[j][i] = 1
            d = i**4
            while d <= bound:
                k = (-5 * self._mod_inverse(8, d)) % d
                for j in range(k, bound + 1, d):
                    self.special_factorization[j][i] += 1
                d *= i**2
        print('Sieve completed:', len(self.primes))

    def _mod_inverse(self, a, mod):
        g, x, y = self._extended_gcd(a, mod)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % mod

    def _extended_gcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self._extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)

class Factorization():
    def __init__(self, bound):
        self.prime_table = PrimeTable(bound)

    def factorize(self, n):
        return self.prime_table.factorization[n]

    def get_all_divisor(self, factorization):
        unpacking = [[p**e for e in range(factorization[p] + 1)] for p in factorization]
        return [self._product(divisor) for divisor in itertools.product(*unpacking)]

    def get_problem251(self, k):
        first_part = self.factorize(k + 1) # (k + 1)^2
        second_part = self._get_square_divisor(k) # (8k + 5)
        return self._merge_two_factorization(first_part, second_part)

    def _get_square_divisor(self, k):
        return self.prime_table.special_factorization[k]

    def _merge_two_factorization(self, x, y):
        for p in y:
            if p not in x:
                x[p] = 0
            x[p] += y[p]
        return x

    def _product(self, list):
        result = 1
        for number in list:
            result *= number
        return result

class Problem():
    def __init__(self):
        self.factorization = None

    def solve(self):
        self.get_count(10**5)

    def get_count(self, bound):
        max_k = (bound - 2)//3
        self.factorization = Factorization(max_k + 1)

        count = 0
        for k in range((bound - 2)//3 + 1):
            a = 3*k + 2
            x = (k + 1)**2 * (8 * k + 5) # where x = b^2 c
            if 4 * (bound - a)**3 < 27 * x:
                break
            x_good_factorization = self.factorization.get_problem251(k)
            for b in self.factorization.get_all_divisor(x_good_factorization):
                c = x // b**2
                if a + b + c <= bound:
                    count += 1
                    if count % 1000 == 0:
                        print(count, "=>", a, b, c)
        print(count)
        return count


problem = Problem()
problem.solve()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 2,   6 min --------------------------')
t1  = time.time()

# === Sat, 20 Jun 2009, 12:03, tolstopuz, Russia
# 2'42" on E8400.

def tolstopuz() :
    import math

    nmax = 110000000

    sf = (nmax // 2 + 1) * [True]

    for i in range(1, nmax + 1, 2):
        if sf[i // 2]:
            j = 3
            while True:
                ii = i * j ** 2
                if ii > nmax:
                    break
                sf[ii // 2] = False
                j += 2

    s = 0

    for c in range(5, nmax + 1, 8):
        if sf[c // 2]:
            d = int(math.sqrt(nmax // c))
            for bb in range(1, nmax + 1, 2):
                a = (1 + 3 * bb ** 2 * c) // 8
                b = (3 * bb + bb ** 3 * c) // 8
                if a + b // d + c > nmax:
                    break
                for dd in range(1, min(b, d) + 1):
                    if b % dd == 0 and a + b // dd + c * dd ** 2 <= nmax:
                        s += 1

    print(s)

tolstopuz()

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
#
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

