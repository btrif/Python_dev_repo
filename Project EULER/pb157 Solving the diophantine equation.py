#  Created by Bogdan Trif on 18-09-2017 , 7:20 PM.
#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
            Solving the diophantine equation 1/a+1/b= p/10**n     -       Problem 157

Consider the diophantine equation 1/a+1/b= p/10**n with a, b, p, n positive integers and a ≤ b.
For n=1 this equation has 20 solutions that are listed below:

1/1+1/1=20/10	        1/1+1/2=15/10	        1/1+1/5=12/10	        1/1+1/10=11/10	    1/2+1/2=10/10
1/2+1/5=7/10	        1/2+1/10=6/10	        1/3+1/6=5/10	        1/3+1/15=4/10	        1/4+1/4=5/10
1/4+1/20=3/10	        1/5+1/5=4/10	        1/5+1/10=3/10       	1/6+1/30=2/10	        1/10+1/10=2/10
1/11+1/110=1/10	    1/12+1/60=1/10	    1/14+1/35=1/10	    1/15+1/30=1/10	    1/20+1/20=1/10

How many solutions has this equation for 1 ≤ n ≤ 9?

'''
import time, zzz, itertools
from gmpy2 import mpq

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
        print('Prime count:', len(self.primes))

class Factorization():
    ''' Based on a prebuilt prime sieve, and we must pay attention that the prime up range is not
    to low, so that we don't miss a prime when we first factor . As default the value is set to 10.000   '''
    def __init__(self):
        self.prime_table = PrimeTable(10**4)

    def get_divisors(self, n):
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
        unpacking = [[p**e for e in range(f[p] + 1)] for p in f]
        return sorted([self._product(divisor) for divisor in itertools.product(*unpacking)])

    def _product(self, list):
        result = 1
        for number in list:
            result *= number
        return result


F  = Factorization()
print( F.get_divisors(180180) )







print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def the_brutest_of_forces( n ) :
    cnt=0
    for b in range(1, 51*n +1 ) :
        for a in range(1, b+1 ) :
            c = mpq(1,a) + mpq(1,b)
            if c.denominator == 10 or (  n % c.denominator   == 0  ):
                cnt+=1
                print(str(cnt)+'.     a = ', a, '  b = ', b ,'     p=', c.numerator , '  denom = ' , c.denominator )

the_brutest_of_forces(10)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')

