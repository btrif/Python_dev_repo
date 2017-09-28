#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Tue, 21 Mar 2017, 21:16
#The  Euler Project  https://projecteuler.net
'''
Investigating Gaussian Integers     -       Problem 153

As we all know the equation x2=-1 has no solutions for real x.
If we however introduce the imaginary number i this equation has two solutions: x=i and x=-i.
If we go a step further the equation (x-3)2=-4 has two complex solutions: x=3+2i and x=3-2i.
x=3+2i and x=3-2i are called each others' complex conjugate.
Numbers of the form a+bi are called complex numbers.
In general a+bi and a−bi are each other's complex conjugate.

A Gaussian Integer is a complex number a+bi such that both a and b are integers.
The regular integers are also Gaussian integers (with b=0).
To distinguish them from Gaussian integers with b ≠ 0 we call such integers "rational integers."
A Gaussian integer is called a divisor of a rational integer n if the result is also a Gaussian integer.
If for example we divide 5 by 1+2i we can simplify  in the following manner:
Multiply numerator and denominator by the complex conjugate of 1+2i: 1−2i.
The result is :
5/1+2i  = 5/i+2i * 1-2i/1+2i = 5(1-2i) / 1-(2i)**2 = 5(1-2i) / 1-(-4) = 5(1-2i) / 5 = (1-2i)

So 1+2i is a divisor of 5.
Note that 1+i is not a divisor of 5 because  5/1+i  = 5/2 - 5i/2
Note also that if the Gaussian Integer (a+bi) is a divisor of a rational integer n, then its complex conjugate (a−bi) is also a divisor of n.

In fact, 5 has six divisors such that the real part is positive: {1, 1 + 2i, 1 − 2i, 2 + i, 2 − i, 5}.
The following is a table of all of the divisors for the first five positive rational integers:

            +--------------------------------------------------+
           | n | Gaussian integer divisors    | Sum s(n) of      |
           |   | with positive real part        | these    divisors |
           |---+------------------------------+---------------|
           | 1 |      1                                      | 1                   |
           |---+------------------------------+---------------|
           | 2 |     1, 1+i, 1-i, 2                      | 5                   |
           |---+------------------------------+---------------|
           | 3 |     1, 3                                   | 4                  |
           |---+------------------------------+---------------|
           | 4 |     1, 1+i, 1-i, 2, 2+2i, 2-2i,4    | 13                |
           |---+------------------------------+---------------|
           | 5 |    1, 1+2i, 1-2i, 2+i, 2-i, 5      | 12                  |
           +--------------------------------------------------+

For divisors with positive real parts, then, we have: .

For 1 ≤ n ≤ 10**5, ∑ s(n)=17924657155.

What is ∑ s(n) for 1 ≤ n ≤ 10**8?

'''
import time
from math import gcd

print('\n--------------------------TESTS------------------------------')

import numpy, cmath


def divisor_sum_sieve(n):
    import numpy as np
    # sieve = np.array([0] * (n + 1) )
    sieve = [0] * (n + 1)
    # sieve[4 :: 2]= [2]*len(sieve[4 :: 2])   #### ATTENTION !!!! MODIFICATION for Gaussian Integer
    limit =  int( n**(1/2) ) + 1
    for i in range(1, limit):
        sieve[i * i] += i
        temp = i + 1
        for j in range(i * i + i, n + 1, i):
            sieve[j] += i  +  temp
            temp += 1
#     print('Divisors Sum sieve ', sieve)
    return sieve




t1  = time.time()

# a= numpy.complex(3,3 ) - numpy.complex(1,4)
# print(a)

print( numpy.complex(2342345)/numpy.complex(1234, 274754654))



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

################
t1  = time.time()

# z = 1-2j
# print(z, z.conjugate() , z.imag, abs(z)   )
# print( 5/(z) )
# print()
#
# a = 3+4j
# print(a, a.conjugate() , a.imag, abs(a)   )
# print( 25/(a) )
#
# print()
# b = 2+2j
# print(b ,b.conjugate() ,  b.real ,b.imag, abs(b)   )
# print( 4/(b) )


print()
c = 15+8j
print(c, c.conjugate() ,  c.real ,c.imag, abs(c)   )
print( 289/(c) )



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------MY FIRST SOLUTION,  VERY SLOW, 1 hour------------------------------')
t1  = time.time()

# 2016-12-18 17:48
# OBSERVATION : The problem Reduces in finding to a number n, decompose it into 2 parts a & b such that:
# a**2+b**2 = n
# You must decompose a number in two perfect squares. Must solve other problems first
# Can you predict from what kind of numbers 3+4i will be a divisor? And 3-4i    ?
# @2017-03-18, 01:30 missed divisors of 10 : look in the notebook : their total sum = 38 (for 10)


def gaussian_integers_sol_1(lim = 10**2) :
    spec_value = 52
    up = int( lim**(1/2))
    GI = divisor_sum_sieve( lim )
    # print( 'Gaussian Integers init list : ' ,len(GI) ,GI[:20], GI[-20::] ,'\n' )
    print( '\nSpecial value check of the value : \t ' , spec_value , '     ' ,GI[spec_value] ,'\n' )

    for i in range(1, up+1 ):
        for j in range(1, i+1 ) :
            if gcd(i,j) ==1 :
                q = i**2+j**2
                if q > lim  : break

                factor = q
                print(' ===   q= ', q ,'       i, j =  ', i, j ,'       factor= '  ,  factor ,'=======')
                while q <= lim :

                    for k in range(q  ,lim+1, q ) :
                        if i == j :
                            add = (i+j) * k//q
                        if i != j :
                            add = 2*(i+j) * k//q

                        GI[k] +=add

                        # print('--- q = ', k,'     incr= ', k//q,'     factor = ', factor, '     i, j = ' ,i*k//q, j*k//q, '          Add : ' ,   add )

                    q += factor

    print( '\nGaussian Integers final list : ' ,len(GI) ,GI[:20],'\n' ,GI[-20::] ,'\n' )
    # print( '\nSpecial value check of the value : \t ' , spec_value , '      ' ,GI[spec_value] ,'\n' )

    return print('\nAnswer : \t', sum(GI)  )


# gaussian_integers_sol_1(10**8)              #   Answer : 	 17971254122360635


# CHECK VALUES :
# 10: 161       # 100: 16749           # 1000: 1752541          # 10000: 178231226          # 100000: 17924657155


t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60,6), 'min\n\n')                   #     Completed in : 3735.53666 s

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()






# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, 5 sec  --------------------------')
t1  = time.time()

# ==== Tue, 22 Mar 2016, 09:24, Min_25, Japan
# Here is an O(n3/4)O(n3/4) solution.
# We can speed up the calculation by computing the weighted number of lattice points within a circle.
# Theoretically, we can compute the answer in O(n**2/3(log log n)**1/3) time.
#
# The answer is
# S1(N)+2⋅⎛⎝⎜∑i=1v(C2(⌊Ni⌋)−C2(⌊Ni+1⌋))
#
# where, v is arbitrary and
# T(n):=n(n+1)2,
# T(n):=n(n+1)2,
#
# S1(N):=∑i=1Nσ1(i)=∑i=1N√(i⌊Ni⌋+T(⌊Ni⌋))−T(⌊N−−√⌋)⌊N−−√⌋,
#
#
# C1(N):=∑x=1N√∑y=1N√[x2+y2≤N]⋅x=∑x=N2√+1N√(x⌊N−x2−−−−−−√⌋+T(⌊N−x2−−−−−−√⌋))+T(⌊N2−−−√⌋)⌊N2−−−√⌋,
#
#
# C2(N):=∑x=1N√∑y=1N√[gcd(x,y)=1∧x2+y2≤N]⋅x=C1(N)−∑g=2N√g⋅C2(⌊Ng2⌋).
#
# Here are some additional values with PyPy 5.0:
# - 10**8: 17971254122360635, 0.242 sec.
# - 10**9109: 1797231035470229962, 0.586 sec.
# - 10**10 179726445633260218662, 2.140 sec.
# - 10**11: 17972750272542089793485, 9.971 sec.
# - 10**12: 1797278370292056629263518, 47.969 sec.
# - 10**13: 179727942749349269842849984, 256.118 sec.
# - 10**14: 17972797618149553612725849755, 1310.278 sec.
# - 10**15: 1797279867536915847122255529479, 6802.619 sec.


from math import sqrt

def isqrt(n, dblcutoff=1<<52):
  if n < dblcutoff:
    return int(sqrt(n))
  x = int(sqrt(n * (1 + 1e-14)))
  while True:
    y = (x + n // x) >> 1
    if y >= x:
      return x
    x = y

def icbrt(n):
  if n <= 0:
    return 0

  x = int(n ** (1. / 3.) * (1 + 1e-12))
  while True:
    y = (2 * x + n // (x * x)) // 3
    if y >= x:
      return x
    x = y

def prob153(N=10**8):
  """
  10 **  9: 1797231035470229962, 0.586 sec.
  10 ** 10: 179726445633260218662, 2.140 sec.
  10 ** 11: 17972750272542089793485, 9.971 sec.
  10 ** 12: 1797278370292056629263518, 47.969 sec.
  10 ** 13: 179727942749349269842849984, 256.118 sec.
  """
  def S(n):
    v = isqrt(n)
    ret = 0
    for i in range(v, 0, -1):
      t = n // i
      ret += t * (2 * i + t + 1)
    ret -= v * v * (v + 1)
    return ret >> 1

  def C(n):
    v = isqrt(n)
    w = isqrt(n // 2)
    ret = 0
    for i in range(v, w, -1):
      t = isqrt(n - i * i)
      ret += t * (2 * i + t + 1)
    ret += w * w * (w + 1)
    return ret >> 1

  def sum_imaginary_numbers(N):
    def T(n):
      return n * (n + 1) // 2

    def calc_coprime(n):
      ret = smalls[n] if n < w else larges[N // n]
      u = icbrt(n)
      prev = T(isqrt(n))
      for i in range(1, u + 1):
        curr = T(isqrt(n // (i + 1)))
        ret -= (prev - curr) * smalls[i]
        prev = curr
      for i in range(2, isqrt(n // (u + 1)) + 1):
        d = n // (i * i)
        ret -= i * (smalls[d] if d < w else larges[N // d])
      return ret

    v = isqrt(N)
    w = N // v

    larges = [0] + [C(N // i) for i in range(1, v + 1)]
    smalls = [0] + [C(i) for i in range(1, w)]

    for i in range(1, w):
      smalls[i] = calc_coprime(i)

    for i in range(v, 0, -1):
      larges[i] = calc_coprime(N // i)

    for i in range(1, v):
      larges[i] -= larges[i + 1]
    larges[v] -= smalls[w - 1]
    for i in range(w - 2, 0, -1):
      smalls[i+1] -= smalls[i]

    ret = 0
    for i in range(1, w):
      if smalls[i] > 0:
        ret += smalls[i] * S(N // i)
    for i in range(1, v + 1):
      ret += larges[i] * S(i)
    return 2 * ret

  ans = sum_imaginary_numbers(N) + S(N)
  return ans

# print(prob153(10 ** 8))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Wed, 7 Jan 2009, 01:03, tolstopuz, Russia
# 126s on E8400.

def solution_2() :
    import math, fractions

    nmax = 10 ** 8

    def ss(x):
        s = 0
        i = 1
        while i <= x:
            j = x // i
            ii = x // j
            s += (ii + i) * (ii - i + 1) * j // 2
            i = ii + 1
        return s

    s = ss(nmax)

    for a in range(1, int(math.sqrt(nmax)) + 1):
        for b in range(1, min(a, int(math.sqrt(nmax - a * a))) + 1):
            if math.gcd(a, b) == 1:
                s += ss(nmax // (a * a + b * b)) * 2 * (a if a == b else a + b)

    return print(s)

solution_2()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

import math
import sys

class Problem():
    def solve(self, n):
        rational_sum = self._rational_sigma_sum(n)
        print('Rational sum:', rational_sum)
        gaussian_sum = self._gaussian_sigma_sum(n)
        print('Gaussian sum:', gaussian_sum)
        print('Total sum:', rational_sum + gaussian_sum)

    def _rational_sigma_sum(self, n):
        rv = 0
        i = 1
        while i <= n:
            q = n // i
            min_i = n // (q+1)
            max_i = n // q
            rv += self._arithmetic_series_sum(min_i, max_i) * q
            i += (max_i - min_i)
        return rv

    def _gaussian_sigma_sum(self, n):
        rv = 0
        i = 1
        while 2*i <= n:
            q = n // (2*i)
            min_i = n // (q+1) - n // (q+1) % 2
            max_i = n // q - n // q % 2
            rv += self._arithmetic_series_sum(min_i, max_i, 2) * q
            i += (max_i - min_i) // 2

        for a in range(1, n+1):
            print('Current a =>', a)
            if a**2 > n:
                break
            for b in range(a+1, n+1):
                c = a**2 + b**2
                if c > n:
                    break
                if math.gcd(a, b) > 1:
                    continue
                i = 1
                while c*i <= n:
                    q = n // (c*i)
                    min_i = n // (q+1) - n // (q+1) % c
                    max_i = n // q - n // q % c
                    rv += self._arithmetic_series_sum(min_i // c, max_i // c) * q * 2 * (a + b)
                    i += (max_i - min_i) // c
        return rv

    def _arithmetic_series_sum(self, lower_bound, upper_bound, step=1):
        return (step + upper_bound) * (upper_bound // step) // 2 \
                - (step + lower_bound) * (lower_bound // step) // 2

def main():
    problem = Problem()
    problem.solve(5)
    problem.solve(10**5)
    problem.solve(10**8)

if __name__ == '__main__':
    sys.exit(main())

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
