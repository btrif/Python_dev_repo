#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
            Primonacci      -       Problem 304

For any positive integer n the function next_prime(n) returns the smallest prime p
such that p>n.

The sequence a(n) is defined by:
a(1)=next_prime(10^14) and a(n)=next_prime(a(n-1)) for n>1.

The fibonacci sequence f(n) is defined by:
f(0)=0, f(1)=1 and f(n)=f(n-1)+f(n-2) for n>1.

The sequence b(n) is defined as f(a(n)).

Find ∑b(n) for 1≤n≤100 000. Give your answer mod 1234567891011.


'''
import heapq
import time, gmpy2
from decimal import *
getcontext().prec = 100


class FIBONACCI():
    # def __init__(self):       # We don't initialize with values

    def zero_matrix( self, m, n):
        return [[0 for row in range(n)] for col in range(m)]

    def matrix_mul(self,  matrix1, matrix2, mod=None):
        if len(matrix1[0]) != len(matrix2[0]):
            raise Exception("Matrices dimension must be m*n and n*p to multiple")

        new_matrix = self.zero_matrix(len(matrix1), len(matrix2[0]))
        # multiply if dimension is correct
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    new_matrix[i][j] += matrix1[i][k]*matrix2[k][j]
                # optional modulus
                if mod is not None:
                    new_matrix[i][j] = new_matrix[i][j] % mod

        return new_matrix


    def fibonacci_matrix(self, n, mod=None):
        """
        Calculate large fib value using matrix form in log(n) steps
        """
        from functools import reduce
        def matrix_mul2(m1, m2):
            return self.matrix_mul(m1, m2, mod )

        b = [int(d) for d in bin(n)[2:]]
        b.reverse()
        p = zip(b, range(len(b)))
        m = { 0: [[1,1],[1,0]] }
        for i in range(1, len(b)):
            m[i] = matrix_mul2(m[i-1], m[i-1])
        ms = [m[y] for (x,y) in p if x == 1]
        return reduce(matrix_mul2, ms)[0][1]




def Fibonacci_Binet(n_th) :
    ''':Description:    Returns the Fibonacci corresponding to the number  and uses the Binet Formula.
        http://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html
        :param n_th: F_nth Fibonacci in sequence
        :return: str, first 9 digits of the Fibonacci number
    '''
    # phi = Decimal((5**(1/2)+1)/2)
    # phi_ = Decimal((1- 5**(1/2))/2)
    m = 1234567891011
    phi = (1+5**(1/2))/2
    phi_ = (1-5**(1/2))/2
    a =  (  (phi**n_th)% m  - ( phi_**n_th)% m  ) / ( phi % m - phi_ %m )
    # a = str(((phi**n_th)-(phi_)**n_th)/( phi - (phi_)))[0:10].replace( '.' , '')
    # b =   ( (( 1 + np.sqrt(5))/2)**n_th - ((1 - np.sqrt(5))/2)**n_th  ) /np.sqrt(5)
    return a

def fibonacci_gen():
    """Fibonacci numbers generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# def fib(x) :
#     a = matrix(GF, [0, 1])
#     b = matrix(GF, [[0, 1],
#                     [1, 1]])
#     return (a * b88(x - 1))[0][1]

# http://www.topcoder.com/tc?module=Static&d1=features&d2=010408
# b(1)=428,562,224,098 mod 1234567891011

t1  = time.time()

nr = 10**3
mod = 10**20
print( FIBONACCI().fibonacci_matrix( nr , mod)  )


test = gmpy2.next_prime(10**14)
print('\ngmpy2 next prime : \t', test)
print('\ngmpy2 next prime : \t',gmpy2.next_prime(test) )




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------TESTS------------------------------')
t1  = time.time()


# 2017-02-26. 11:15 - Finally understood what the problem asks for :
# you take next_prime(10**14) term of the Fibonacci serie
# I think that it can be done ONLY with Binet Formula

F = fibonacci_gen()
next(F)


def test() :
    p = p2 = gmpy2.next_prime(10**14)
    p0 = gmpy2.next_prime(10**14)-1
    p1 = p0+1

    fib = FIBONACCI()
    mod , MOD = 10**20, 1234567891011

    B = [fib.fibonacci_matrix(p0, MOD ), fib.fibonacci_matrix(p1, MOD ) ]
    heapq.heapify(B)
    print(p0, p1 , ' fib= ', B ,'\n')

    cnt, rng = 1, 0
    S = 0
    # S1 = 0
    for i in range(0, 10**5):
        F = fib.fibonacci_matrix(p, MOD)
        # for l in range(rng):
        #     heapq.heappush(B, sum(B)  )
        #     heapq.heappop(B)
            # print(B)
        # B = [ k%MOD for k in B ]
        print(str(cnt) +'.      ' ,p ,'      fib  =     ', F , '      rng = ' , rng )
        p2 = gmpy2.next_prime(p)
        rng = p2 - p
        cnt += 1
        p = p2
        S += F%MOD
        # S1 += B[-1]%MOD


    return print('\n Answer : \t' , S,'      ' ,S%MOD )# ,'\n',S1 , '      ' , S1%MOD )


t2  = time.time()
print('\nCompleted in :', round((t2-t1), 2), 's\n\n')


 # ====  IDEAS =======
# Thu, 5 Jun 2014, 18:09, leonid, Japan
# I used Cassini's identity to find the fibonacci value, and miller-rabin to test primality.
# https://en.wikipedia.org/wiki/Fibonacci_number#Other_identities


print('\n================  My FIRST SOLUTION, SLOW, 3 min  ===============\n')
t1  = time.time()

def first_solution():

    fib = FIBONACCI()
    MOD =  1234567891011
    cnt  = 1
    S = 0
    p =  gmpy2.next_prime(10**14)
    for i in range(0, 10**5):
        F = fib.fibonacci_matrix(p, MOD)
        print(str(cnt) +'.      ' ,p ,'      fib  =     ', F  )
        p = gmpy2.next_prime(p)
        cnt += 1
        S += F%MOD

    return print('\n Answer : \t     ' , S%MOD )     #   Answer : 	      283988410192

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      # Completed in : 178.42 s




print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  Similar to mine --------------------------')
t1  = time.time()

# ==== Tue, 5 Oct 2010, 14:05, djcomidi, Belgium


from gmpy2 import next_prime

def solution1() :
    LIMIT = 1234567891011

    fibs = {0: 0, 1: 1}
    def fib(n):
      if n in fibs: return fibs[n]
      if n % 2 == 0:
        fibs[n] = ((2 * fib((n / 2) - 1)) + fib(n / 2)) * fib(n / 2)
      else:
        fibs[n] = (fib((n - 1) / 2) ** 2) + (fib((n+1) / 2) ** 2)
      fibs[n] %= LIMIT
      return fibs[n]

    p = 10**14
    total = 0
    for n in range(1,10**5+1):
      p = next_prime(p)
      total += fib(p)
    # if n % 1000 == 0:
    #   print n, total % LIMIT
    return print (total % LIMIT)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ===== Tue, 5 Oct 2010, 18:07, Yuval Dor, Israel
# Easy and nice. Fibonacci numbers by matrix exponentiation, get primes by scanning the range using smaller primes just above 10^7.

import math

xx = [True] * 5 * 10 ** 6
primes = [True] * 2 * 10 ** 7
mod = 1234567891011
n = 10 ** 14

for x in range(2, int(math.sqrt(len(primes))) + 1):
    if primes[x]:
        for y in range(x ** 2, len(primes), x):
            primes[y] = False

primes = [x for x in range(2, len(primes)) if primes[x]]

for p in primes:
    for i in range(-n % p, len(xx), p):
        xx[i] = False

def mul(x, y):
    return [[sum(a * b for a, b in zip(r, c)) % mod for c in zip(*y)] for r in x]

def exp(a, n):
    x = [[1, 0], [0, 1]]
    while n:
        if n & 1:
            x = mul(a, x)
        n >>= 1
        a = mul(a, a)
    return x



def solution2():
    fibs = exp([[1, 1], [1, 0]], n)
    x = mul(fibs, [[1], [0]])
    a, b = x[0][0], x[1][0]
    bb = 10 ** 5
    c = 0

    for x in xx:
        if x:
            c += b
            bb -= 1
        if bb == 0:
            break
        a, b = (a + b) % mod, a

    return print(c % mod)

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
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
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
