#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
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

