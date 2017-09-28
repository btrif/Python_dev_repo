


import random, functools, operator, time

test_nr= functools.reduce( operator.mul,  [  (random.randint(100000,500000)) for i in range(10) ] )
print('the number for test is : ',test_nr)



print('\n------------------ 1  ----------------')
t1  = time.time()

import pyprimes
print( list( pyprimes.factorise(test_nr))  )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

#################### #####################

print('\n--------------- 2 ------------------')
t1  = time.time()

import sympy
print( sympy.factorint(test_nr) )



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



#################### #####################

print('\n--------------- 3  much to slow------------------')
t1  = time.time()

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
        self.prime_table = PrimeTable(500000)

    def get(self, n):
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

# F = Factorization()
#
# print('nice class writing' , F.get(test_nr) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def get_factors2(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    X =[]
    for i in factorise(n) :  X += [i[0]]*i[1]
    return X

print('\n--------------- 4  get_factors variant 1------------------')
t1  = time.time()


print(get_factors(test_nr))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------- 5  get_factors variant 2------------------')
t1  = time.time()


print(get_factors2(test_nr) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




#################### #####################


print('\n----------- PAIR FACTORING OF A NUMBER -------------------')


def pair_Factors(n):
    todo, combis = [(n, 2, [])], []
    while todo:
        n, i, combi = todo.pop()
        while i * i <= n:
            if n % i == 0:
                combis += combi + [i, n//i],
                todo += (n//i, i, combi+[i]),
            i += 1
    return combis

def pair_Factors_rec(n):
    def factor(n, i, combi, combis):
        while i * i <= n:
            if n % i == 0:
                combis += combi + [i, n//i],
                factor(n//i, i, combi+[i], combis)
            i += 1
        return combis
    return factor(n, 2, [], [])







# n = 16*15*49*13*27
n = 16*15*498*28

print('\n------------------ 1  ------    pair_Factors  ----------')
t1  = time.time()


print('pair_Factors_rec : ',  pair_Factors(n)  ,'\n', len(pair_Factors(n)))



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

#################### #####################

print('\n--------------- 2  ---   pair_Factors_rec ---------------')
t1  = time.time()


print('pair_Factors_rec : ',len(pair_Factors_rec(n))  ,'\n', pair_Factors_rec(n))



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#################### #####################

