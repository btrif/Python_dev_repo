#  Created by Bogdan Trif on 03-10-2017 , 10:54 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
Counting numbers with at least four distinct prime factors less than 100        -       Problem 268

It can be verified that there are 23 positive integers less than 1000 that are divisible by at least four distinct primes less than 100.

Find how many positive integers less than 10^16 are divisible by at least four distinct primes less than 100.
'''

import time, zzz
import itertools,  functools, operator
import gmpy2
import numpy, math

def binary_search(n, List):        # VERY FAST ALGORITHM
    ''':Description: Search for an element in the list and returns the index of it. If it not finds it returns
        the index of the element closest to its left, the smaller number.
    :param: **n**- integer, the number to find
                **List** - lst type, the list to search for
    :returns:   int, the index of the element
    '''
    left = 0
    right = len(List) -1

    while left <= right:
        midpoint = (left+right)//2
        if List[midpoint] == n: return midpoint
        elif List[midpoint] > n: right = midpoint-1
        else: left = midpoint+1
    if n > List[midpoint]: return midpoint
    else: return (midpoint-1)

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

def get_unique_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]
    # return  [ i[0] for i in factorise(n) ]

print(get_unique_factors(360))

# === MAIN IDEA ====
# Combine 4 factors
# [2, 3, 5, 7 ] *8, 9 , 10 ,11 , ....
# [2, 5, 7, 11]
#
# [5, 11, 23, 29 ]
#
# to not overwrite the number we must take only bigger numbers than the biggest

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def brute_force_concept(up_lim) :
    # NR = []
    cnt = 0
    for i in range(2, up_lim+1) :
        F =  get_unique_factors(i)
        S1 = set(F)
        if len(set( F ))  >= 4  :
            S2 = set(sorted(list(S1))[:4])
            S = S1.intersection(S2)
            if max(S) < 100 :
                # cnt += 1
                # if (2 in F) and (3 in F)  and (5 in F) and (7 in F ):
                    cnt += 1
                    # print(str(i) +'.     ', F , '      cnt= ', cnt,'              ', S )

    print('\nWith BRUTE FORCE There are ', cnt, ' numbers')
    # return set(NR)
    return cnt

# BF = brute_force_concept(10**4)
# print( len(BF) )

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n============  My FIRST SOLUTION, Very Slow,  4 hours  ===============\n')
t1  = time.time()


def intermediary_solution(up_lim):
    IS = []
    primes_rng = 100
    primes = prime_sieve_numpy(primes_rng)
    print(primes)
    D = { primes[i]:i for i in range(len(primes)) }
    E = { i : primes[i] for i in range(len(primes)) }
    print('D :',D)
    print('E :', E)
    L = list(itertools.combinations(primes, 4 ) )
    print(len(L), L[:50], '\n')
    Count = 0


    for I in L :
        # if I[0] == 2 and I[1] == 3 and I[2] == 5 and I[3] == 7 :
            n = functools.reduce( operator.mul, I )
            m = math.floor(up_lim/n)
            if m > 0 :
                print('\n', I ,'     n= ' , n ,'         m= ', m  )
                Count += m
                mxp = max(I)
                P2 = set(primes[0 : D[mxp]+1 ] )
                P1 = set(I)
                P = sorted(list(P2.difference(P1)))
                print( mxp , D[mxp] , '       P1 = ',P1 , '         P2 = ',P2 , '   diff primes ' ,P )
                rng = min( len(P), 10 )
                for i in range(1, rng+1) :
                    comb = list( itertools.combinations(P, i)  )
                    # print( i, len(comb) , comb[:30]  )
                    for j in comb :
                        semi_p = functools.reduce(operator.mul, j)
                        if i % 2 == 1 : Count -= m//semi_p
                        if i % 2 == 0 : Count += m//semi_p

    print('\nResult = ', Count)
    return Count


# intermediary_solution( up_lim = 10**16 )    #Result =  785478606870985


# @2017-10-04, 13:30 -> Now I must find the intersecting cases :
# for 10**4 there are :  943 - 927 = 16 cases
# must look at the primes involved
# example :  duplicate entry
# (2, 3, 5, 7)     n=  210       47.619047619        m=  47  --> 47
# (2, 3, 5, 47)      n=  1410       7.09219858156        m=  7  --> 7
# when (2, 3, 5 ,7 47 ) and (2, 3, 5, 47, 7)

# @ 2017-10-04 --> Must include the cases like (2,3,11,13) *5,7   <=> (2, 3, 5, 11)*13 and (2, 3,7, 13 )*11
# Until now I excluded only common terms in the last prime, but I must do for the 1st 2nd and 3-rd
# @2017-10-06 , 18:00 - Cannot find some  index problems, to the case [2,3, 5] works fine
# but not for [2,3]
# https://en.wikipedia.org/wiki/Tetrahedral_number
# https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle


t2  = time.time()
print('\n# Completed in :', round((t2-t1)/60 , 2), 'mins\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, MUST LEARN IT , 1 min  --------------------------')
t1  = time.time()

# ==== Fri, 14 Mar 2014, 07:41, ChopinPlover, Taiwan
# Similar to Problem 1.

import itertools
import math
import sys

class Problem():
    def __init__(self):
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.signed_duplicate_count = []
        self._init_signed_duplicate_count()

    def _init_signed_duplicate_count(self):
        n = len(self.primes)
        for i in range(n):
            self.signed_duplicate_count.append(math.factorial(4 + i) // math.factorial(4) // math.factorial(i))
        for i in range(n-1):
            self.signed_duplicate_count[n-i-1] -= self.signed_duplicate_count[n-i-2]
        for i in range(n):
            self.signed_duplicate_count[i] *= (-1)**(i % 2)

    def solve(self):
        print(self.count(10**16))

    def count(self, bound):
        rv = 0
        for i in range(4, len(self.primes) + 1):
            is_first_set = True
            for factor_set in itertools.combinations(self.primes, i):
                j = self._multiply(factor_set)
                if is_first_set:
                    is_first_set = False
                    if j >= bound:
                        break
                    print(factor_set, j)
                if j >= bound:
                    continue
                rv += (bound // j) * self.signed_duplicate_count[i-4]
        return rv

    def _multiply(self, factor_set):
        rv = 1
        for factor in factor_set:
            rv *= factor
        return rv


problem = Problem()
# problem.solve()


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 2,      Inclusion - Exclusion  , 2 min       --------------------------')
t1  = time.time()

'''==== Sat, 15 Dec 2018, 23:27, cfranck , South Korea
Inclusion - Exclusion, like others. Evaluated coefficients for PIE with separate code. ~30s in total.

'''


from itertools import combinations

def PE268():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    coeff = [0, 0, 0, 0, 1, -4, 10, -20, 35, -56, 84, -120, 165, -220, 286]

    limit = 10**16
    grand_total = 0
    for i in range(4, 15):
        total = 0
        for each in combinations(primes, i):
            target = 1
            for k in range(i):
                target *= each[k]
            total += limit // target
        grand_total += total * coeff[i]
    return grand_total

print(PE268())


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
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




