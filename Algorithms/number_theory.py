from functools import reduce

import itertools

from pyprimes import factorise


def egcd(a, b):         #Extended Euclidian Algorithm
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def extendedEuclid(a, b):
    if b == 0:
        return a, 1, 0
    k, q = a // b, a % b # a = kb + q
    g, xp, yp = extendedEuclid(b, a % b)
    # g = xp * b + yp * q
    #   = xp * b + yp * (a - kb)
    #   = (xp - k*yp) * b * yp * a
    return g, yp, xp - k * yp


def modinv(a, m):       # Modular Inverse
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

print('modinv Modular Inverse :\t', modinv(7, 31))
print('modinv Modular Inverse :\t', modinv(17, 43))

######################################


def Euler_totient(n):   # o(^_^)o  @2017-01-23, 10:30 by Bogdan Trif
    ''':Works without errors !
        https://en.wikipedia.org/w/index.php?title=Euler%27s_totient_function&action=edit&section=3
    :param n: int
    :return: int, Euler Phi, Euler Totient
    '''
    def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        from pyprimes import factorise
        return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]
    F = set(get_factors(n))
    for i in F :
        n*=(1-1/i)
    return round(n)

N = 100001051
print('\nEuler_totient function : \t N=',N ,'\t' ,Euler_totient(N))


import math
import sys

class ChineseRemainderTheorem():
    """
    Solve
        x = a (mod m)
        x = b (mod n)
    where m and n are coprime.
    """
    def solve(self, a, m, b, n):
        q = m*n
        (x, y) = self._extended_gcd(m, n)
        root = a + (b - a) * x * m
        return ((root % q) + q) % q

    def _extended_gcd(self, a, b):
        (x, y) = (0, 1)
        (last_x, last_y) = (1, 0)
        while b != 0:
            (q, r) = divmod(a, b);
            (a, b) = (b, r)
            (x, last_x) = (last_x - q * x, x)
            (y, last_y) = (last_y - q * y, y)
        return (last_x, last_y)

class ModInverse():
    """
    Solve ax = 1 (mod m).
    """
    def get(self, a, m):
        g, x, y = self._extended_gcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def _extended_gcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self._extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)


def is_pandigital(n):
    if len(str(n)) == 10 :
        N = list([int(i) for i in str(n)])
#         print(N, len(set(N)))
        if len(set(N)) == 10 :
            return True
    return False



print('\n-------------- INVERSE PHI, phi ------------------\n')


def prime_sieve(n):       # FOURTH      o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [2] + [i for i in range(3, n , 2) if sieve[i] ]

from gmpy2 import is_prime

# ==== Sun, 7 Jun 2009, 22:28, gianchub, England
# Google was my friend on this one. It turned up this paper:
# www.new.dli.ernet.in/rawdataupload/upload/insa/INSA_2/20005a81_22.pdf...
# That paper is really interesting:
# Within my library:

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


def main2() :
    from math import factorial
    res = invphi( 2*3*4*5*6 )
    print(res )

main2()



############ Inverse Phi - Version II ##############

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def inverse_phi(N, a=1):
    saved = []

    if N < 1:
        raise ValueError

    if N == 1:
        if a > 1:
            return [1]
        return [1, 2]

    divisors = get_divisors(N)


    for div in divisors :
        if (div < a) or (not is_prime(div + 1)):
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

    return saved

# print(  inverse_phi(240) )



print('\n ##################### Moebius Function ################# ')

import numpy as np

def primeSieve(n):
    """returns array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

def moebiusSieve(limit):
    """returns array of moebius numbers 1<=n<=limit"""
    P=primeSieve(limit+1) # or any sieve
    L = np.ones(limit+1).astype(int)
    for p in P:
        L[::p] *= -1
        L[::p**2] = 0
    return L[1:]

print(moebiusSieve(100))