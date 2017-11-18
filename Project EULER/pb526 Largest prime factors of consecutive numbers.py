#  Created by Bogdan Trif on 16-11-2017 , 12:43 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
    Largest prime factors of consecutive numbers            -       Problem 526

Let f(n) be the largest prime factor of n.

Let g(n) = f(n) + f(n+1) + f(n+2) + f(n+3) + f(n+4) + f(n+5) + f(n+6) + f(n+7) + f(n+8),

the sum of the largest prime factor of each of nine consecutive numbers starting with n.

Let h(n) be the maximum value of g(k) for 2 ≤ k ≤ n.

You are given:

        f(100) = 5,       f(101) = 101 ,....   =>       g(100) = 409

                But the largest is not g(100) , instead it is : g(99) = 514

                and therefore  =>                   h(100) = 417

h(10^9) = 4896292593

Find h(10^16).

'''
import time, zzz
import numpy
from collections import deque

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
        print('Prime count:', len(self.primes) ,'           ATTENTION , LARGEST PRIME Included = ', self.primes[-1] ,'       !!!!!!!!!!!! \n' )

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

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


# === IDEA --> Here we need the density of primes in a span of 8 numbers because :
# For the example given :
# g(100) = f(100) + f(101) +  f(102) + f(103) +  f(104) + f(105) +  f(106) + f(107) + f(108) =
# 5 + 101 + 17 + 103 + 13 + 7 + 53 + 107 + 3 = 409
# But this means that there is some other 8 span numbers with larger sum. Here are 3 large primes !
# Question : Are there 4 large primes whose sum is greater. Let's check !
#                 And... it seems that g(99) = 417 . QED !!!!

# ===== IDEA TO SOLVE THE PROBLEM !!!
# We must find the span of 8 numbers which have the greatest large primes :
# similar to 101, 103, 107 which are primes
# For this we need a function to check the density of primes ! The problem is that factorization  impossible
# and the primes are always certainly above 10^15


#####   PROOF OF CONCEPT  ###########

F  = Factorization(10**4)

def proof_of_concept(lim) :
    h = 0
    queue_9 = deque()
    for i in range( 2, lim + 9 ):
        f = max( get_factors(i))
        if len(queue_9) == 9 : queue_9.popleft()
        queue_9.append(f)
        g = sum(queue_9)
        if g > h :   h = g
        print(str(i)+'.   ',   f ,    ' g('+str(i-8)+') =  ' , g          , '       queue9  =   ' , queue_9 )

    return print('\nAnswer: \t h = ', h)

proof_of_concept(100)


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




