#  Created by Bogdan Trif on 21-03-2018 , 3:29 PM.

import itertools
from functools import reduce
from gmpy2 import is_prime
import time


def prime_sieve(n):       # FOURTH      o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [2] + [i for i in range(3, n , 2) if sieve[i] ]

def factorise( nr):
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return list(factorise(nr))

def invphi(m):
    ''' Returns the sorted list of numbers n such that phi(n) = m '''
    # some special cases
    if m <= 0:
        return [0]
    elif m == 1:
        return [1, 2]
    elif m > 1 and m%2 != 0:
        return []

    # phi(p^d) with p prime
    def phipd(p, d):
        return (p-1) * (p**(d-1))

    # returns a decreasing ordered list of all primes p such that p-1 | n
    def primesFromDivisors(n):
        divs = set()
        factors, exps =  zip(* (factorise(n) )   )
        for i in itertools.product(*(range(x+1) for x in exps)):
            pp = reduce(lambda x, y : x*y, (factors[j] ** i[j] for j in range(len(i))), 1) + 1
            if is_prime(pp):
                divs.add(pp)
        return sorted(divs, reverse = True)

    # prepares a small table of phis (phi^(-1) sets, to aid the calculation)
    def smallTable(mmax):
        M = 2**62
        primes = prime_sieve(mmax)
        nnum, nden, nmax = 1, 1, 0
        for p in primes:
            nnum, nden = nnum * p, nden * (p-1)
            if nnum > mmax:
                nnum, nden = nnum // p, nden // (p-1)
                nmax = (mmax * nnum) // nden
                break
        tmphi = list(range(nmax + 1))
        sf = [M] * (nmax + 1)
        for pr in primes:
            for p in range(pr, nmax + 1, pr):
                tmphi[p] = (tmphi[p] * (pr - 1)) // pr
                if pr < sf[p]:
                    sf[p] = pr
        for n, m in enumerate(tmphi):
            if m > mmax:
                continue
            if not m in phis:
                phis[m] = []
            phis[m].append([n, sf[n]])
        phis[1][0][1] = M

    # does the calculation (recursively if needed)
    def calc(m, M):
        divs = primesFromDivisors(m)
        if not m in phis:
            phis[m] = []
        for p in divs:
            d = 1
            ppd = phipd(p, d)
            while ppd <= m:
                if m % ppd == 0:
                    x = m // ppd
                    if x == 1 or x % 2 == 0:
                        if not x in phis:
                            calc(x, M)
                        for v in phis[x]:
                            t = (p**d) * v[0]
                            if v[1] > p:
                                phis[m].append([t, p])
                                if m == M:
                                    res.add(t)
                d += 1
                ppd = phipd(p, d)

    # inner vars
    # results set
    res = set()
    # invphi table
    phis = {}
    # invphi table dimension
    mmax = int(m**0.5) + 100
    smallTable( min(mmax, 5000) )
    calc(m, m)
    # return sorted results list
    return sorted(res)


#############################           METHOD II       ##############

def Miller_Rabin(p, k = 50):  # Miller-Rabin primality test
    import random
    if p == 2: return True
    if p < 2 or p & 1 == 0: return False

    d = (p - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for i in range(k):
        a = random.randint(1, p - 1)
        t = d
        y = pow(a, t, p)
        while t != p - 1 and y != 1 and y != p - 1:
            y = pow(y, 2, p)
            t <<= 1
        if y != p - 1 and t & 1 == 0:
            return False
    return True


class PrimeTable():    #  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
    def __init__(self, bound):
        self.bound = bound
        self.primes = []
        self._sieve()

    def _sieve(self):       # FOURTH      o(^_^)o
        sieve = [True] * self.bound
        for i in range(3, int(self.bound**0.5)+1, 2):
            if sieve[i]:
                sieve[ i*i :: 2*i ] = [False] * ( (self.bound-i*i-1) // (2*i) +1 )
        self.primes = [2] + [i for i in range(3, self.bound , 2) if sieve[i] ]
        print('Prime count:', len(self.primes) ,'           ATTENTION , LARGEST PRIME Included = ', self.primes[-1] ,'       !!!!!!!!!!!! ' )




class Factorization():

    ''' Based on a prebuilt prime sieve, and we must pay attention that the prime up range is not
    to low, so that we don't miss a prime when we first factor . As default the value is set to 10.000
      So we need uprange /2         '''
    def __init__(self, bound):
        self.prime_table = PrimeTable(bound)

    def get_factors(self, n):
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
        return f


    def get_divisors(self, n) :
        f = self.get_factors(n)
        unpacking = [[p**e for e in range(f[p] + 1)] for p in f]
        return sorted([self._product(divisor) for divisor in itertools.product(*unpacking)])


    def _product(self, list):
        result = 1
        for number in list:
            result *= number
        return result


F = Factorization(10**2)

def inverse_phi(N, a=1):
    saved = []

    if N < 1:
        raise ValueError

    if N == 1:
        if a > 1:
            return [1]
        return [1, 2]

    divisors = F.get_divisors(N)


    for div in divisors :
        if (div < a) or (not Miller_Rabin(div + 1)):
            continue
        N_ = N / div
        div += 1
        P = div

        while True:
            saved += map(lambda x: x*P, inverse_phi(N_, div))
            if N_ % div:
                break
            P *= div
            N_ /= div

    return sorted(saved)





print('\n--------------- 1 ------------------')
t1  = time.time()

print(  invphi(3645000) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# # #################### #####################

print('\n--------------- 2 -- MY METHOD ------------------')
t1  = time.time()

print(  inverse_phi(3645000) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# # #################### #####################

