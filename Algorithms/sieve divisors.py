#  Created by Bogdan Trif on 17-05-2018 , 8:02 PM.

# Here we build a Sieve with divisors but all without 2 :
# The disadvantage is that when we use divisors we must do inclusion exclusion
# for odd/ even terms + /- and we do not know which divisors are composed of 2,3,4 primes.
# Example : [3, 21, 7, 93, 651, 217, 31] , we may know the primes (1 terms with Rabbin - Muller )
# but to test again for terms composed from 2,3,4 terms it takes computational resources.
# THE SOLUTION is to use it in conjuction with Mobius Sieve :

import time


t1  = time.time()

def prime_sieve(n):       # FOURTH      o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return [i for i in range(3, n , 2) if sieve[i] ]

#### TOOOO MUCH MEMORY !!!!!!  Better to construct a factors sieve, NOT divisors !!!

def sieve_special_divisors(lim):         #   o(^_^)o  Made by Bogdan Trif @ 2018-05-17
    ''':Description: sieve with divisors but without number 2. Was needed for the Euler problem 540
        Uses a prime sieve. Can be generalized to add number 2 and divisors *2 by modifying the prime_sieve :
        to return [2] + [i for i in range(3, n , 2) if sieve[i] ]
    :param lim: int, up_limit
    :return: sieve with lists of divisors                           '''
    sieve = [[] for i in range((lim+1))]
    primes = prime_sieve(lim)
#     print(len(sieve), sieve,'   ' ,sieve[30], '\n')
    for p in primes :
        for a in range(1, lim//p +1 ) :
#             print(a)
            if len(sieve[a*p]) == 0 :
                sieve[a*p].append(p)
            else :
                tmp =[]
                for b in sieve[a*p] :
                    tmp.append(b*p)
#                     print(b ,'   ', a*p, sieve[a*p] ,'    to_Add=', b*p , '  tmp=', tmp)

                sieve[a*p].extend(tmp)
                sieve[a*p].append(p)



    print(sieve[:1000])
    return sieve

lim =  56049977
# lim = 10**7

# sieve_special_divisors( lim )


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n------------------         Sieve of Factors, Factorization   -----------------   ')
t1  = time.time()

class sieve_factorization():         #   o(^_^)o  Made by Bogdan Trif @ 2019-01-30
    def __init__(self, lim):
        self.lim = lim
        self.n = int( lim**(1/2) )+1
        self.Primes = self.prime_sieve()
#         print(list(self.Primes))

    def prime_sieve (self):
        P = [ False if i % 2 == 0 else True for i in range (self.lim) ]
        yield 2
        for i in range (3, self.lim):
            if P[i]:
                for j in range (i*i, self.lim, i):
                    P[j] = False
                yield i


    def sieve_factorize ( self ):
        F = [ [] for _ in range (self.lim) ]
        for p in self.Primes:
            for x in range (p, self.lim, p):
                F[x] += [p]
            ### Add powers
            i = 2
            while  p**i <  lim :
                for x in range(p**i, self.lim, p**i):
                    F[x] += [p]

                i+=1

        return F


SD = sieve_factorization(10**7)

F = SD.sieve_factorize()
x = 5648944
print(' factors of '+str(x) +'  :  '  , F[x]  )

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

#####       PROJECT EULER, PROBLEM 540  , 177 seconds for 56* 10**6    ######### Can be improved

t1  = time.time()

def prime_sieve (n):
    s = [ False if i % 2 == 0 else True for i in range (n) ]
    yield 2
    for i in range (3, n):
        if s[i]:
            for j in range (i*i, n, i):
                s[j] = False
            yield i


def sieve_factorize (M, s):
    f = [ [] for _ in range (M) ]
    for p in s:
        for x in range (p, M, p):
            f[x] += [p]
    return f

# N = 3141592653589793
N = 10**6
lim = int( N**(1/2) )+1
s = prime_sieve( lim )
f = sieve_factorize( lim, s )

print('f : ', f[:100])


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')



#########################       ANOTHER ONE , Taken from internet   , SLOW    #############
# https://codereview.stackexchange.com/questions/18346/optimizing-divisor-sieve
# https://stackoverflow.com/questions/13280198/optimizing-divisor-sieve

t1  = time.time()


from math import sqrt
def divisorSieve(lim):
    divs = [[] for j in range(lim + 1)]
    nsqrt = int(sqrt(lim))
    for i in range(1, nsqrt + 1):
        divs[i*i].append(i)
        for j in range(i, i*i, i):
            divs[j].append(j//i) #If j/i is replaced by i, a good improvement is seen. Of course, that would be wrong.
            divs[j].append(i)
    for i in range(i+1, lim+1):
        for j in range(i, lim+1, i):
            divs[j].append(j//i)
            divs[j].append(i)
    return divs

def numdivisorSieve(n):
    divs = [1] * (n + 1)
    divs[0] = 0
    nsqrt = int(sqrt(n))
    for i in range(2, nsqrt + 1):
        divs[i*i] += 1
        for j in range(i, i*i, i):
            divs[j] += 2
    for i in range(i+1, n+1):
        for j in range(i, n+1, i):
            divs[j] += 2
    return divs

# A = divisorSieve(10**6)
# print(A[:100])


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


