#  Created by Bogdan Trif on 18-05-2018 , 10:37 AM.
# © o(^_^)o  Solved by Bogdan Trif  @
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
from math import gcd

'''
n = 24, div = [1, 2, 3, 4, 6, 8, 12 , 24 ] => gcd( 1, 24/1 ) =1, gcd( 2, 24/2 ) =2 , gcd( 3, 24/3 ) =1 ,     
'''

def get_divisors(n):      ### ( ͡° ͜ʖ ͡°)  SECOND FASTEST ,  MUST BE IMPROVED !! It is a sqrt(n) Algorithm
    from math import sqrt
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)

def unitary_divisor_concept(n) :
    div = get_divisors(n)
    for d in div :
        print('n=', n,'     d= ', d, '      n/d = ', n//d ,'       gcd( ' +str(d)+', ' +str(n//d)+' ) = ', gcd(d, n//d) )

unitary_divisor_concept(8*9*7)

# @2018-05-18 - Basically : if we have a unique prime factor of a number and we remove it, we will obtain gcd(d, n/d) =1
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
Therefore, the problem reduces to factorize 100.000.000! More precisely :
counting the numbers of 2's, 3's, ... up to 10^8 ( need a prime sieve for this ).
STEP 2 : Remark. MUST DO all operations (mod 10...09)
Must think, must be a clever trick !


print('\n--------------------------TESTS------------------------------')
t1  = time.time()



t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()





# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
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

