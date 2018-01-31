#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
47-smooth triangular numbers            -       Problem 581

A number is p-smooth if it has no prime factors larger than p.
Let T be the sequence of triangular numbers, ie T(n) = n(n+1)/2.

Find the sum of all indices n such that T(n) is 47-smooth.


'''
import time, zzz

# import gmpy2
import itertools

import sys


import numpy
def prime_sieve_numpy(n):                       ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    """ Input n>=6, Returns a array of primes, 2 <= p < n
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188 """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3    :: 2*k ] = False
            sieve[ k*(k-2*(i&1)+4)//3 :: 2*k ] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def prime_sieve(n):       # SECOND FASTEST        o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [2] + [i for i in range(3, n , 2) if sieve[i] ]

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def triangle_number_gen():
    n=1
    while True :
        t = n*(n+1)//2
        yield t
        n+=1



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
        f = []
        for p in self.prime_table.primes:
            if d == 1 or p > d:
                break
            e = 0
            while d % p == 0:
                d = d // p
                e += 1
            if e > 0:
                f += [p]*e
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




print('factors =  ', get_factors(18085704))




print('\n--------------------------TESTS------------------------------')
t1  = time.time()

### Understanding the principle ! @ 2017-03-12
# We first try to understand with smaller case, and we take the biggest factor to be 5
# Q : What is the LAST n for which T(n) has the biggest factor to be 5 !
# A : From the brute force test it seems it is 80 !!!
# Now we must analyze why and find the underlying cause for this

def brute_force_testing( prime, lim ) :
    primes = set(prime_sieve(lim))
    # print(primes)
    F  = Factorization(lim)
    S = 3
    n =  2
    while 1 :
        # if not gmpy2.is_prime(n) or not gmpy2.is_prime(n+1) :
        if n not in primes or n+1 not in primes:
            if n% 2 ==0 :
                # f1, f2 = get_factors(n//2), get_factors(n+1)
                f1, f2 = F.get_factors(n//2), F.get_factors(n+1)
            else :
                # f1, f2 = get_factors(n), get_factors((n+1)//2)
                f1, f2 = F.get_factors(n), F.get_factors((n+1)//2)

            f_12 = sorted(f1 + f2)
            T = n*(n+1)//2

            # print('n=', n , '      n+1=' , n+1 ,'       T(n) = ' , T,'          n=',f1 , '        n+1= ',f2 ,'         f_12=',f_12 )# ,'       fact(n) =', get_factors(n) )

            if max(f_12) <= prime :
                print('n=', n , '      n+1=' , n+1 ,'       T(n) = ' , T,'          n=',f1 , '        n+1= ',f2 ,'         f_12=',f_12 )# ,'       fact(n) =', get_factors(n) )
                S+=n
        n+=1
        if n == lim : break

    print('\nAnswer : \t', S )
    return S

# brute_force_testing(31, 10**4)

# until     2*10**7         :           1253782342
# ('n=', 18113535, '      n+1=', 18113536, '       T(n) = ', 164050084154880L, '          n=', [3, 3, 5, 11, 23, 37, 43], '        n+1= ', [2, 2, 2, 2, 2, 2, 2, 2, 2, 7, 7, 19, 19], '         f_12=', [2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 5, 7, 7, 11, 19, 19, 23, 37, 43])
# ('n=', 18366425, '      n+1=', 18366426, '       T(n) = ', 168662792823525L, '          n=', [5, 5, 7, 7, 11, 29, 47], '        n+1= ', [3, 3, 3, 3, 3, 3, 3, 13, 17, 19], '         f_12=', [3, 3, 3, 3, 3, 3, 3, 5, 5, 7, 7, 11, 13, 17, 19, 29, 47])
# ('n=', 18703790, '      n+1=', 18703791, '       T(n) = ', 174915889533945L, '          n=', [5, 7, 7, 7, 7, 19, 41], '        n+1= ', [3, 3, 3, 3, 17, 17, 17, 47], '         f_12=', [3, 3, 3, 3, 5, 7, 7, 7, 7, 17, 17, 17, 19, 41, 47])
# ('n=', 19826575, '      n+1=', 19826576, '       T(n) = ', 196546548028600L, '          n=', [5, 5, 23, 29, 29, 41], '        n+1= ', [2, 2, 2, 7, 7, 11, 11, 11, 19], '         f_12=', [2, 2, 2, 5, 5, 7, 7, 11, 11, 11, 19, 23, 29, 29, 41])
# ('n=', 19936224, '      n+1=', 19936225, '       T(n) = ', 198726523657200L, '          n=', [2, 2, 2, 2, 3, 3, 7, 11, 29, 31], '       n+1= ', [5, 5, 19, 19, 47, 47], '         f_12=', [2, 2, 2, 2, 3, 3, 5, 5, 7, 11, 19, 19, 29, 31, 47, 47])
# ('\nAnswer : \t', 1253782342)


t2  = time.time()
print('\nCompleted in :', round((t2-t1) , 4 ), 's\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

def smooth_triangular_numbers(max_p, lim ) :
    sieve = [True]*lim
    primes = prime_sieve_numpy(lim)
    print(primes[:30])
    # print(sieve)

    for p in primes :
        # print( p  , ((lim-1)//(p)) )

        if p > max_p :
            # sys.stdout.write('\r' + str(p) +'              '+  str(round((time.time() - t1), 2) ) +'  sec'   )   # Font Segoe UI Semibold
            i=1
            while p**i < lim :
                r = (lim-1) %  p**i
                k =  lim-1-r-p**(i)
                # print( p**i  ,' k=', k ,'   cnt=', k //(p**i) ,' r=' ,  r ,'    start = ' , p**(i) )
                sieve[p**i :: p**i ] = [False]  * ( k //(p**i)+1 )

                i += 1
                # print(sieve)

    print( sieve[:100] )
    S = [ i for i in range(1, len(sieve)-1 )  if ( sieve[i] == True and sieve[i+1] == True)  ]
    print( S[::-100] )
    for a in range(lim-1, 0, -1 ) :
        if sieve[a] ==True and sieve[a-1] == True :
            print('Largest number = ', a-1 )
            break

    print('\n Answer :    ' ,  sum(S) )
    return sum(S)

smooth_triangular_numbers(31, 3*10**9)
# Answer :     11188231245

# @2017-11-14     -   I need 16 GB for this problem       !!!!!!!!!
# @2017-11-20 - Actually, the solution of the problem is other. CANNOT BE DONE with sieving
# as the numbers 47-th are too large

t2  = time.time()
print('\nCompleted in :', round((t2-t1),4) ,  ' s\n\n')


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

