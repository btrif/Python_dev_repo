#  Created by Bogdan Trif on 20-03-2018 , 10:50 PM.
# © o(^_^)o  Solved by Bogdan Trif  @       Completed on Tue, 20 Mar 2018, 23:19
#The  Euler Project  https://projecteuler.net
'''
                            Prime Frog          -       Problem 329

Susan has a prime frog.
- Her frog is jumping around over 500 squares numbered 1 to 500.
- He can only jump one square to the left or to the right, with equal probability,
and he cannot jump outside the range [1;500].

(if it lands at either end, it automatically jumps to the only available square on the next move.)

When he is on a square with a prime number on it, he croaks 'P' (PRIME) with probability 2/3
or 'N' (NOT PRIME) with probability 1/3 just before jumping to the next square.

When he is on a square with a number on it that is not a prime he croaks 'P' with probability 1/3
or 'N' with probability 2/3 just before jumping to the next square.

Given that the frog's starting position is random with the same probability for every square,
and given that she listens to his first 15 croaks,

what is the probability that she hears the sequence PPPPNNPPPNPPNPN?

Give your answer as a fraction p/q in reduced form.


'''
import time, zzz
from functools import lru_cache

import numpy
import gmpy2

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


def prime_sieve(n):       # FOURTH      o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [2] + [i for i in range(3, n , 2) if sieve[i] ]


primes = frozenset(prime_sieve(500))
print(primes)



print('\n--------------------------TESTS------------------------------')
t1  = time.time()

seq = 'PPPPNNPPPNPPNPN'

@Memoize
def frog_jump( k, seq ) :
    cur_pos, rest_seq = seq[0], seq[1:]

    if k in primes :
        probabil = gmpy2.mpq( 2, 3) if cur_pos == 'P' else gmpy2.mpq(1, 3)
    else :
        probabil = gmpy2.mpq( 2, 3) if cur_pos == 'N' else gmpy2.mpq(1, 3)


    if  len(rest_seq) ==0 :
        return probabil

    elif k == 1 :
        return probabil * frog_jump( 2, rest_seq )

    elif k == 500 :
        return probabil * frog_jump( 499, rest_seq )

    else :
        return probabil * (  frog_jump( k-1 , rest_seq ) +  frog_jump( k+1 , rest_seq ) ) /2


F = frog_jump(3, seq)
print('\nF : ', F)


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,  Recursion with Memoization   ===============\n')
t1  = time.time()

# Taken from https://github.com/dzhou/project-euler/commit/7b42a4a12d11f8167bd204619eb360f0d657ed41

seq = 'PPPPNNPPPNPPNPN'

@Memoize
def frog_jump( k, seq ) :
    cur_pos, rest_seq = seq[0], seq[1:]

    if k in primes :
        probabil = gmpy2.mpq( 2, 3) if cur_pos == 'P' else gmpy2.mpq(1, 3)
    else :
        probabil = gmpy2.mpq( 2, 3) if cur_pos == 'N' else gmpy2.mpq(1, 3)


    if  len(rest_seq) ==0 :
        return probabil
    elif k == 1 :
        return probabil * frog_jump( 2, rest_seq )
    elif k == 500 :
        return probabil * frog_jump( 499, rest_seq )
    else :
        return probabil * (  frog_jump( k-1 , rest_seq ) +  frog_jump( k+1 , rest_seq ) ) /2



Sum = 0
for i in range(1, 501) :
    F = frog_jump(i, seq)
    print(str(i)+'.     ', F )
    Sum += F

res = Sum / 500
# print( res )
print('\nResult : ', Sum / 500, '     gcd = ', gmpy2.gcd( res.numerator, res.denominator ) )

# Answer:     199740353/29386561536000


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')



print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  Hidden Markov model, forward algorithm. --------------------------')
t1  = time.time()

# === Thu, 25 Jul 2013, 10:39, sh_012, finland
# Hidden Markov model, forward algorithm.

em = {('P', True) : 2, ('P', False) : 1, ('N', True) : 1, ('N', False) : 2}

def p329(N, seq):
    primes = prime_sieve(500)
    a = [0] + [em[(seq[0], j in primes)] for j in range(1, N + 1)]
    for i in range(1, len(seq)):
        na = [0] * (N + 1)
        na[1] = a[2]
        na[N] = a[N-1]
        na[2] = 2 * a[1] + a[3]
        na[N-1] = 2 * a[N] + a[N-2]
        for n in range(3, N - 1):
            na[n] = a[n-1] + a[n+1]
        for j in range(1, N + 1):
            na[j] *= em[(seq[i], j in primes)]
        a = na
    g = gmpy2.gcd(sum(a), N * 2**i * 3**(i+1))
    return str(sum(a)//g) + '/' + str(N * 2**i * 3**(i+1)//g)

print(p329(500, 'PPPPNNPPPNPPNPN'))

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
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

