#!/usr/bin/python                   ( ͡° ͜ʖ ͡°)
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Factorial trailing digits       -       Problem 160

For any N, let f(N) be the last five digits before the trailing zeroes in N!.
For example,

9! = 362880 so f(9)=36288
10! = 3628800 so f(10)=36288
20! = 2432902008176640000 so f(20)=17664

Find f(1,000,000,000,000)


'''
import time
from math import factorial
from gmpy2 import fac
import operator, functools

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


def prime_sieve(n):       # SECOND FASTEST        o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [2] + [i for i in range(3, n , 2) if sieve[i] ]


def factorial_digits_2_5_factors(n):
    '''return the number of factors of 2 & 5 found in a factorial
    :param n:  factorial
    :return: tuple, factors of 2 and 5    '''
    arr = []
    for p in [2,5] :
        e , cnt = 1, 0
        pe = p**e
        while pe <= n :
            cnt += n // pe
    #         print(str(e)+'.   ', pe,  n/pe, '   ', n//pe)
            e+=1
            pe = p**e
        arr.append(cnt)
    return arr


def factorial_non_zero(b):
    ''' Manually finds the last ten non-zero elements of a factorial '''
    s = 1
    for i in range(1, b+1):
        s *= i
        while not s % 10:
            s //= 10
        s = s % 10**10
    return s

# 2017-02-03, 12:06 --> Miss the idea  completely !

print('\n--------------------------Preliminary TESTS------------------------------')
t1  = time.time()

print('factorial_digits_2_5_factors : \t' ,factorial_digits_2_5_factors(10) )


print('\n-------------')
print('10             ',factorial_non_zero(10**1))
print('100           ',factorial_non_zero(10**2))
print('1.000          ',factorial_non_zero(10**3))
print('10.000          ',factorial_non_zero(10**4))
print('100.000        ',factorial_non_zero(10**5))
# print('1.000.000        ',factorial_non_zero(10**6))

# f(               10)=36288
# f(              100)=16864
# f(            1,000)=53472
# f(           10,000)=79008
# f(          100,000)=56096
# f(        1,000,000)=12544
# f(       10,000,000)=28125


# http://mathforum.org/library/drmath/view/71768.html     !!!!!!!!!!!!!!!!!!
# https://www.reddit.com/r/math/comments/4fjmt1/finding_the_last_nonzero_digits_of_ginormous/
# http://math.stackexchange.com/questions/130352/last-non-zero-digit-of-a-factorial
# http://mathcentral.uregina.ca/qq/database/qq.09.07/s/mukesh1.html
# http://www.mathpages.com/home/kmath489.htm
# https://comeoncodeon.wordpress.com/2009/06/20/lastnon-zero-digit-of-factorial/

# print('\n' , len(str(fac(10**4))) , str(factorial(10**4)) )                   # 27753472


def factorial_trailing_digits(n) :
    '''Actually n  is powers of ten !!!!!!!! '''
    o = 1
    a = factorial_non_zero( 10**(n-o) )
    b = factorial_digits_2_5_factors( 10**n )
    c = factorial_digits_2_5_factors( 10**(n-o) )
    d = [ i-j for i, j in zip(b,c)  ]
    diff = d[0]-d[1]
    res = (   pow( a , 10**(o) , 10**7 ) * ((diff)%10**7)        )   %10**7
    print(a,  '      ', (a**(10**o) )%10**6 , '      ', b, c,'     ', d, diff , '      res = ', res , '      ', n )

factorial_trailing_digits(2)


### CONCEPT BUILDING  ####
q = 36288
for i in range(11, 100+1):
    # if i % 10 != 0 and i %5 !=0 :
    if i % 10 == 0 :
        q //=10
    else :
        if i % 25 == 0 and i% 3 ==0 :
            q *= 3
            q //=4
            print(i,'--->     ', q % 10**30 , '               ',  factorial_non_zero(i))
            continue
        if i % 25 == 0 and i%2==0 :
            q //= 4
            continue
    q*=i
    print(i,'     ', q % 10**30 , '               ',  factorial_non_zero(i)  )


print('\n Res : ', (q// 10**0) %10**30)

print('obladioblada :' , (pow( 36288, 10, 10**5 )*2**67 ) %10**5    )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()


https://en.wikipedia.org/wiki/Wilson%27s_theorem

    # else :
    #     if q %25 == 0 :
    #         q /= 4
    #     if q%5 == 0 and q%25 !=0 :
    #         q /= 2


# def factorial_trailing_digits(n) :
#     # primes = [2, 3, 5, 7]
#     primes = prime_sieve(10**5)
#     F = []
#     for p in primes :
#         e = 1
#         pe = p**e
#         f = 0
#         while pe <= n :
#             if p == 5 :
#                 F[0][1] = F[0][1]-n//pe
#             else : f+= n//pe
#             # print(p , 'exp=', e, '    ',p**e ,'     ',n//pe  )
#             e+=1
#             pe = p**e
#         F .append([p,f ] )
#     # print(F)
#     # F[0][1] = F[0][1]-fives
#     # F.pop(2)
#     # print(F[:50])
#
#     return functools.reduce( operator.mul , [ i[0]**i[1] for i in F ] ) %10**5


# res = factorial_trailing_digits(10**2)
# print('res=' , res)
# print('pow mod : \t' ,pow( g , 10**1, 10**5 )  )
#
# print(factorial_trailing_digits(10**4))
# print('pow mod : \t' ,pow( factorial_trailing_digits(10**4) , 10**0, 10**5 )  )


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
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
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
