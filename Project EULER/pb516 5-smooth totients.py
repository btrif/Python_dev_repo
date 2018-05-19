#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
            5-smooth totients       -           Problem 516

5-smooth numbers are numbers whose largest prime factor doesn't exceed 5.
5-smooth numbers are also called Hamming numbers.

Let S(L) be the sum of the numbers n not exceeding L such that
Euler's totient function φ(n) is a Hamming number.

S(100)=3728.

Find S(10**12). Give your answer modulo 2**32.

'''
import time, zzz, itertools
from functools import reduce
from gmpy2 import is_prime
import time
# import _primes_work_tool

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def euler_totient(n):           # Remark : For large array better use Sieve approach
    """returns Euler totient (phi) of n = Φ (n)
        Uses the formula of the Totient  : Φ (n) =  Π {p | n}  n *(1 - 1/p) ;
        where p are each prime factors and n is the number  for which we compute
        In number theory, Euler's totient function counts the positive integers up to a given integer n
        that are relatively prime to n. It is written using the Greek letter phi as φ(n) or ϕ(n),
        and may also be called Euler's phi function.
        Example : Φ (12) = 4 =   [1,5,7,11]
        https://en.wikipedia.org/wiki/Euler's_totient_function
        http://marcharper.codes/2015-08-07/totients.html            """
    phi = n
    pfs = set(get_factors(n))
    for pf in pfs:
        phi*=(1-1/pf)
    return int(phi)

print(euler_totient(14))
print(euler_totient(21))
print(euler_totient(28))
print(euler_totient(35))
print(euler_totient(7*97))
print(euler_totient(7*7*2))

# @ 2017-05-04 --> We use the formula of the totient to get the numbers we need.
# Example:
# Let's say we have the expanded totient as : Φ (42) = ( 1-1/2 )( 1-1/3 )( 1-1/7 ) * (2*3*7) = 2/7 * 42  = 12
# ==> then we can get all the numbers which are multiple of 7 < 10**12
#  but not of 7**2 or 7**3 ...etc... => inclusion exclusion

# Inverse Totient : what numbers can we find which have the totient 40 ???

# == > then we make combinations of (1-1/2)(1-1/5)
# in fact we need all combinations from 1 --> 3 inclusive and then add another prime
# Vezi problema 204 and 248


# In number theory, these numbers are called 5-smooth, because they can be characterized as having only 2, 3, or 5 as prime factors.



print('\n--------------------------TESTS , Conceptualization------------------------------')
t1  = time.time()

X = 0
Totients = set()
for i in range(1, 100+1 ) :
    tot = euler_totient(i)
    f = get_factors(tot)
    if max(f) <= 5 :
        print(str(i)+'.       tot = ', tot, '       factors : ' , f )
        Totients.add(tot)
        X += i

print('Totients : ', sorted(Totients) )
print('\nAnswer : ', X )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()



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

def invphi(m, lim):
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
                                if m == M :
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




next = 0
num = [1]
c2 = c3 = c5 = 0
SMOOTH = {1, 2 }

lim = 10**7
while next < lim :
    next = min(2*num[c2], 3*num[c3], 5*num[c5])
    num.append(next)
    if next == 2 * num[c2] : c2 += 1
    if next == 3 * num[c3] : c3 += 1
    if next == 5 * num[c5] : c5 += 1

    Ns = set([i for i in invphi(next) if i <=lim ] )

    if len(Ns) > 0 :
        print('totient = ', num[-1], '         Ns with tot : ',  Ns )
        SMOOTH.update( Ns )


# print('\n',SMOOTH)
print('\nS(' +str(lim)+') = ', sum(SMOOTH) )

@2018-03-21 - Must improve this algorithm ! Works until 10**6

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
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

