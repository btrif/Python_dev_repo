#  Created by Bogdan Trif on 06-11-2017 , 8:26 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
Geometric triangles         -           Problem 370

Let us define a geometric triangle as an integer sided triangle with sides a ≤ b ≤ c so that
its sides form a geometric progression, i.e. b^2 = a · c .

An example of such a geometric triangle is the triangle with sides a = 144, b = 156 and c = 169.

There are 861.805 geometric triangles with perimeter ≤ 10^6 .

How many geometric triangles exist with perimeter ≤ 2.5·10^13 ?


'''
import time, zzz
from pyprimes import factorise
from gmpy2 import is_prime

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


#print(list(i[0] for i in list(factorise(3932273))))


import itertools
class PrimeTable():    #  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
    def __init__(self, bound):
        self.bound = bound
        self.primes = []
        self._sieve()

    def _sieve(self):
        visited = [False] * (self.bound + 1)
        visited[0] = visited[1] = True
        for i in range(2, self.bound + 1):
            if not visited[i]:
                self.primes.append(i)
            for j in range(i + i, self.bound + 1, i):
                visited[j] = True
        print('Prime count:', len(self.primes) ,'           ATTENTION , LARGEST PRIME Included = ', self.primes[-1] ,'       !!!!!!!!!!!! ' )

class Factorization():

    ''' Based on a prebuilt prime sieve, and we must pay attention that the prime up range is not
    to low, so that we don't miss a prime when we first factor . As default the value is set to 10.000
      So we need uprange /2         '''
    def __init__(self, bound):
        self.bound = bound
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


F  = Factorization( 100000 )
print( F.get_divisors(36) )



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




