#  Created by Bogdan Trif on 22-09-2017 , 9:48 PM.

# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                    Maximum length of an antichain      -       Problem 386

Let n be an integer and S(n) be the set of factors of n.

A subset A of S(n) is called an antichain of S(n) if A contains only one element or if
none of the elements of A divides any of the other elements of A.

For example: S(30) = {1, 2, 3, 5, 6, 10, 15, 30}
{2, 5, 6} is not an antichain of S(30).
{2, 3, 5} is an antichain of S(30).

Let N(n) be the maximum length of an antichain of S(n).

Find ΣN(n) for 1 ≤ n ≤ 10^8

'''
import time, zzz
import functools, operator
import itertools
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

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


class PrimeTable():    #  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
    def __init__(self, bound):
        self.bound = bound
        self.primes = []
        self._sieve()

    def _sieve(self):
        visited = [False] * (self.bound + 1)
        visited[0] = visited[1] = True
        for i in range(2, self.bound + 1):
            if not visited[i]:
                self.primes.append(i)
            for j in range(i + i, self.bound + 1, i):
                visited[j] = True
        print('Prime count:', len(self.primes))

class Factorization():
    ''' Based on a prebuilt prime sieve, and we must pay attention that the prime up range is not
    to low, so that we don't miss a prime when we first factor . As default the value is set to 10.000   '''
    def __init__(self):
        self.prime_table = PrimeTable(10**5)

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

primes = prime_sieve_numpy(100)
print(primes)

class sieve_factorization():         #   o(^_^)o  Made by Bogdan Trif @ 2019-01-30
    def __init__(self, lim):
        self.lim = lim
        self.n = int( lim**(1/2) )+1
        self.Primes = self.prime_sieve()
#         print(list(self.Primes))

    def prime_sieve (self):
        P = [ False if i % 2 == 0 else True for i in range (self.lim) ]
        yield 2
        for i in range (3, self.lim):
            if P[i]:
                for j in range (i*i, self.lim, i):
                    P[j] = False
                yield i


    def sieve_factorize ( self ):
        F = [ [] for _ in range (self.lim) ]
        for p in self.Primes:
            for x in range (p, self.lim, p):
                F[x] += [p]
            ### Add powers
            i = 2
            while  p**i <  self.lim :
                for x in range(p**i, self.lim, p**i):
                    F[x] += [p]

                i+=1

        return F


# SD = sieve_factorization(10**7)
#
# F = SD.sieve_factorize()
# x = 5648944
# print(' factors of '+str(x) +'  :  '  , F[x]  )


print('\n--------------------------TESTS------------------------------')
t1  = time.time()


for i in range(1, 10):
    l = primes[:i]
    n = functools.reduce(operator.mul, primes[:i])
    print( len(str(n)), '   ', n , l)

print('-----------')


# F = Factorization()
# print(F.get_divisors(120120))

def brute_force_check(up_lim):
    N = 0

    FA = Factorization()
    for n in range(1, up_lim+1):
        F = FA.get_divisors(n)


        print(str(n)+'.     ', F ,'      len = ', len(F))
        if len(F) == 1 : N +=1

        if len(F) > 1 :
            for i in range(2, len(F)//2+1  ) :
                C = list( itertools.combinations( F, i  ) )
                print('C : ', C)
                max_val = 1
                for J in C :
                    print(j)
                    MUST FINISH THIS !!!



    return print('\nResult : \t', N,'\n')


brute_force_check(10**2)

# CHECK ANSWER : 30 longest antichain   correct for 120120

print(get_factors(120120))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()


def antichain(up_lim):
    primes = prime_sieve_numpy(up_lim)
    sieve = numpy.zeros(up_lim+1, dtype=int)
    print(sieve)
    for p in primes :
        sieve[::p]+=1
    sieve[0]=0
    sieve[1]=1
    print(sieve[:100])

    return print('\nResult :  ', sum(sieve))

# antichain(10**2)



SD = sieve_factorization(10**2)

F = SD.sieve_factorize()
# x = 5648944
# print(' factors of '+str(x) +'  :  '  , F[x]  )
print(F)

@2019-01-30 - Must write an antichain exponents evaluation. For example :
# 30 = [2, 3, 5] --> Divisors = [2, 3, 5, 6, 10, 15, 30] --> {2, 3, 5} is the longest antichain
# 60 = [2, 2, 3, 5] --> Divisors = [2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60] --> {4, 6, 10, 15} is the longest antichain
# 90 = [2, 3, 3, 5] --> Divisors = [2, 3, 5, 6, 9, 10, 15, 18, 30, 45, 60,90] --> {6, 9, 10, 15} is the longest antichain
# 36 = [2, 2, 3, 3] --> Divisors = [2, 3, 4, 6, 9, 12, 18, 24, 36] --> {4, 6, 9} is the longest antichain
# 72 = [2, 2, 2, 3, 3] --> Divisors = [2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72] --> {4, 6, 9} is the longest antichain
# 144 = [2, 2, 2, 2, 3, 3] --> Divisors = [2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 36, 48, 72, 144] --> {4, 6, 9} is the longest antichain

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')




