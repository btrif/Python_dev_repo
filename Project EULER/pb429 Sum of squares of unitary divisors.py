#  Created by Bogdan Trif on 18-05-2018 , 10:37 AM.
# © o(^_^)o  Solved by Bogdan Trif  @       Completed on Wed, 30 Jan 2019, 22:28
#The  Euler Project  https://projecteuler.net
'''
            Sum of squares of unitary divisors          -           Problem 429

A unitary divisor d of a number n is a divisor of n that has the property gcd(d, n/d) = 1.

The unitary divisors of 4! = 24 are 1, 3, 8 and 24.

The sum of their squares is 12 + 32 + 82 + 242 = 650.

Let S(n) represent the sum of the squares of the unitary divisors of n. Thus S(4!)=650.

Find S(100 000 000!) modulo 1 000 000 009.


'''
import time, zzz
# from math import gcd, floor, ceil, sqrt
# from gmpy2 import comb, fac
# from pyprimes import factorise
# import numpy

'''
n = 24, div = [1, 2, 3, 4, 6, 8, 12 , 24 ] => gcd( 1, 24/1 ) =1, gcd( 2, 24/2 ) =2 , gcd( 3, 24/3 ) =1 ,     
'''


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

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def get_divisors(n):      ### ( ͡° ͜ʖ ͡°)  SECOND FASTEST ,  MUST BE IMPROVED !! It is a sqrt(n) Algorithm
    from math import sqrt
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)


### Understanding the problem :
def unitary_divisor_concept(n) :
    Sum = 0
    cnt = 0
    div = get_divisors(n)
    print('n  = ', get_factors(n) )
    for d in div :
        if gcd(d, n//d) == 1 :
            cnt += 1
            dsq = d*d
            Sum += dsq
            print('n=', n,'     d= ', d,  '     ' , get_factors(d)   ,'      n/d = ', n//d ,   '       gcd( ' +str(d)+', ' +str(n//d)+' ) = ', gcd(d, n//d) , '    dsq = ', dsq , '    cnt =' , cnt)

    terms = [ comb(len( set( get_factors(n))  ), i) for i in range(len( set( get_factors(n))  )+ 1 ) ]
    print('terms = ', sum(terms) )

    print('\nSum = ', Sum )
# unitary_divisor_concept(8 *9 * 25 * 7 * 11 * 11 )

# unitary_divisor_concept( fac(17) )


# @2018-05-18 -
# Basically : if we have a unique prime factor of a number and we remove it, we will obtain gcd(d, n/d) =1
#     or if it is at some power we must remove the whole power => =1
#     PROOF :
# example 1 :
# n = 32 , div = [1, 2, 4, 8, 16, 32]. Of course GCD(32,1) =1 BUT we take all the powers of 2 => 2^5
#   => gcd(2^5/32, 32) = 1
#
# example2 :
# n = 504 , factors = [2, 2, 2, 3, 3, 7]. Of course GCD(1, 504) =1
# 2^3 = 8 => gcd(2^3 , 504/2^3 ) = 1 same for
# 7^1 = 7 => gcd(7^1 , 504/7^1 ) = 1 same for
# 3^2 = 9 => gcd(3^2 , 504/3^2 ) = 1 same for
#     but also for their combinations like where we remove all combinations of primes to powers   :
# d= 56 = 2^3*7^1 (we took all powers)         n/d =  9        gcd( 56, 9 ) =  1
# d= 63 = 3^2 *7^1 (we took all powers)        n/d =  8        gcd( 63, 8 ) =  1
# d= 72 = 3^2 *2^3 (we took all powers)        n/d =  7        gcd( 72, 7 ) =  1
#
# d=  504 = 3^2 *2^3* 7^1      n/d =  1        gcd( 504, 1 ) =  1
# n= 504      d=  63       n/d =  8        gcd( 63, 8 ) =  1
# n= 504      d=  72       n/d =  7        gcd( 72, 7 ) =  1
# n= 504      d=  7       n/d =  72        gcd( 7, 72 ) =  1
# n= 504      d=  8       n/d =  63        gcd( 8, 63 ) =  1
# n= 504      d=  9       n/d =  56        gcd( 9, 56 ) =  1

# n= 12600      d=  1       n/d =  12600        gcd( 1, 12600 ) =  1
# n= 12600      d=  7       n/d =  1800        gcd( 7, 1800 ) =  1
# n= 12600      d=  8       n/d =  1575        gcd( 8, 1575 ) =  1
# n= 12600      d=  9       n/d =  1400        gcd( 9, 1400 ) =  1
# n= 12600      d=  25       n/d =  504        gcd( 25, 504 ) =  1
# n= 12600      d=  56       n/d =  225        gcd( 56, 225 ) =  1
# n= 12600      d=  63       n/d =  200        gcd( 63, 200 ) =  1
# n= 12600      d=  72       n/d =  175        gcd( 72, 175 ) =  1
# n= 12600      d=  175       n/d =  72        gcd( 175, 72 ) =  1
# n= 12600      d=  200       n/d =  63        gcd( 200, 63 ) =  1
# n= 12600      d=  225       n/d =  56        gcd( 225, 56 ) =  1
# n= 12600      d=  504       n/d =  25        gcd( 504, 25 ) =  1
# n= 12600      d=  1400       n/d =  9        gcd( 1400, 9 ) =  1
# n= 12600      d=  1575       n/d =  8        gcd( 1575, 8 ) =  1
# n= 12600      d=  1800       n/d =  7        gcd( 1800, 7 ) =  1
# n= 12600      d=  12600       n/d =  1        gcd( 12600, 1 ) =  1



# Therefore, the problem reduces to factorize 100.000.000! More precisely :
# counting the numbers of 2's, 3's, ... up to 10^8 ( need a prime sieve for this ).
# STEP 2 : Remark. MUST DO all operations (mod 10...09)
# Must think, must be a clever trick !




print('\n--------------------------TESTS------------------------------')
t1  = time.time()



t2  = time.time()
print('\n# Completed in :', round((t2-t1) , 2 ), 's\n\n')

print('\n=======  My FIRST SOLUTION,  LEGENDRE Formula & Divisor Square Sum ===============\n')
t1  = time.time()

''' === GENERAL IDEA - 2019-01-30, 17:40
http://mathworld.wolfram.com/UnitaryDivisorFunction.html
LEGENDRE FORMULA to find how many exponents dows a prime have :
https://en.wikipedia.org/wiki/Legendre%27s_formula

=== Unitary divisor formula is :

σ_k = ( p_1^α_1 *  p_2^α_2 * ... ) = ( 1 + p_1^(k*α_1) ) * ( 1 + p_2^(k*α_2) ) * ...
 where:  k - the power
 p_i - the prime
 α_i - the exponent of the prime
 
 Example : For k =2 , like in this problem we have that :
 
σ_2 = ( p_1^α_1 *  p_2^α_2 * ... ) = ( 1 + p_1^(2*α_1) ) * ( 1 + p_2^(2*α_2) ) * ...

Concrete Example : Reproducing the example from the problem :
n = 4! = 24 = [2, 2, 2, 3] = 2^3 * 3^1   Demands  the squares of the unitary divisors => Therefore,
k = 2

σ_2 = ( 2^3 *  3^1 ... ) = ( 1 + 2^( 2 * 3 ) ) * ( 1 + 3^(2*1) )  = 65 * 10 = 650 . It verifies !


Then we use the Legendre exponent formula :
https://en.wikipedia.org/wiki/Legendre%27s_formula
In mathematics, Legendre's formula gives an expression for the exponent of the largest power 
of a prime    p that divides the factorial n!
    For n = 6, one has 6!=720=2^4 3^2  5^1  ;
     v_2(6!)= 4 , v_3(6!)= 2 , v_5(6!)= 1
        :Formula:            v_p(n!) = Σ {i=1, Inf } floor( n/p^i )


'''



def prime_sieve(n):       # FOURTH      o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [2] + [i for i in range(3, n , 2) if sieve[i] ]


def solution_unitary_divisors( lim ) :
    Primes = prime_sieve(lim)
    n = len(Primes)
    modulo = 10**9+9
    print(' len(Primes) = ', len(Primes) ,'    ' ,Primes[:30] )
    PROD = 1

    cnt = 0
    ### Applying Legendre Formula
    for p in Primes :
        cnt+=1
        if cnt%10**4 == 1 : print('p = ', p)
        i=1
        exp_sum = 0
        while p**i <= lim :
            exp_sum +=  lim // p**i     # floor
            # print('i= ', i , '    exp_sum= ', exp_sum)
            i+=1


        ### Applying directly  Unitary divisor formula for σ_2 ( squares of divisors )


        x = pow( p , 2*exp_sum , modulo ) + 1
        PROD *=   x
        PROD %= modulo


    print('\nANSWER : ',  PROD % modulo )
    return PROD % modulo


# solution_unitary_divisors( 10**8 )              #       ANSWER :  98792821


t2  = time.time()
print('\n# Completed in :', round((t2-t1) , 2 ), 's\n\n')                           # Completed in : 45.45 s


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  25 sec  --------------------------')
t1  = time.time()

'''     ====Sun, 28 Aug 2016, 19:06, j123, Canada
 Same as everyone else, but this runs faster -- 15 sec on my ancient laptop with interpreted Python
  -- than the other complete Python solutions.  
  Has a clean and relatively fast sieve (that uses itertools so needs adjustment to be fast with pypy).
 '''

from itertools import chain, compress, count

def p_in_fact(n, p):
    '''Returns the exponent of the highest power of prime p in n!
    Equivalently, the sum of the exponent of the highest power of p in i, for i
    ranging from 1 to n inclusive'''
    ans = 0
    while n >= p:
        n //= p
        ans += n
    return ans

def primes(N):
    '''Iterator of primes up to and including N'''
    a, b = 0, N - 1 >> 1
    if b <= 0: return iter(())
    B = bytearray([0]) + bytearray([1]) * b
    for c in count(1, 2):
        a += c - 1 << 1  #a = c * c // 2
        if a > b: return chain([2], compress(count(1, 2), B))
        if B[c >> 1]: B[a::c] = bytearray((b - a) // c + 1)

N, m, ans = 10**8, 10**9 + 9, 1
for p in primes(N):
    ans = ans * (1 + pow(p, 2 * p_in_fact(N, p), m)) % m

print(ans)

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
print('\n--------------------------SOLUTION 3,  1 min --------------------------')
t1  = time.time()

''' === Thu, 18 Jan 2018, 16:13, mbh038, England
About 25 s in Python.
Like pretty much everyone else here, I use the fact that the sum of the squared unitary divisors of N is multiplicative 
and is given by :
∑d2jd|ngcd(d,N/d)=1=∏(1+p2kii)
 
where the p_i^k_i are the prime factors of N, 
each term in the product is the sum of the squared unitary divisors of p_i and the Legendre method
 is used to find the exponents k_i 

'''

import numpy as np
import time

def p429( n, mod ):
    pFactors=pFacnFac(n)

    pProd=1
    for p in pFactors:
        pProd*=1+pow(int(p),2*int(pFactors[p]),mod)
        pProd%=mod
    print(pProd)


def pFacnFac(n):
    """returns prime factors of n!"""
    ps=primeSieve(n)
    factors={}
    for p in ps:
        exp=0
        power=1
        delta=10
        while delta>0:
            delta=n//p**power
            exp+=delta
            power+=1
        factors[p]=exp
    return factors

def primeSieve(n):
    """return array of primes 2<=p<=n"""
    sieve=np.ones(n+1,dtype=bool)
    for i in range(2, int((n+1)**0.5+1)):
        if sieve[i]:
            sieve[2*i::i]=False
    return np.nonzero(sieve)[0][2:]

# p429(10**8, 10**9+9)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

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

