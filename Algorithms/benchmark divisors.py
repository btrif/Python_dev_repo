import time


def get_divisors_2(n):       ### o(^_^)o  #  More powerfull for numbers > 10**10
    ''' first it decomposes the number in prime factors , then makes combinations of all the factors
    to get all the divisors '''
    from pyprimes import factorise
    from itertools import combinations
    from functools import reduce
    from operator import mul
    import heapq
    L = [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]
    # print(L)
    D={1}
    for i in range(1, len(L)+1):
        # print( list(combinations(L,i)) )
        for j in list(combinations(L,i)) :
            D.add ( reduce(mul, j)   )
    return list(sorted(D))

######################

def get_divisors(n):      ### ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST     MUST BE IMPROVED !! It is a sqrt(n) Algorithm
    from math import sqrt
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)

######################

import itertools

class PrimeTable():
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





########         NUMBERS TO TEST        ############

N = [ 123456789000, 9876543200, 2335823596, 95677576617, 89896811175  ]




##############    ALGORITHM 1

t1  = time.time()

for n in N :
    print(get_divisors(n))



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')

###################     ALGORITHM 2  -MUCH BETTER

t1  = time.time()


for n in N :
    print(get_divisors_2(n))



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')

##################     ALGORITHM 3  -Using a predefined Sieve

t1  = time.time()

F  = Factorization()
for n in N :
    print( F.get_divisors(n) )




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n')

