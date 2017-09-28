#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
47-smooth triangular numbers            -       Problem 581

A number is p-smooth if it has no prime factors larger than p.
Let T be the sequence of triangular numbers, ie T(n)=n(n+1)/2.

Find the sum of all indices n such that T(n) is 47-smooth.


'''
import time, zzz

import gmpy2


def prime_sieve(n):       # SECOND FASTEST        o(^_^)o
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[ i*i :: 2*i ] = [False] * ( (n-i*i-1) // (2*i) +1 )
    return set([2] + [i for i in range(3, n , 2) if sieve[i] ])

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

primes = prime_sieve(10**7)
# print(primes[:30])

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

### Understanding the principle ! @ 2017-03-12
# We first try to understand with smaller case, and we take the biggest factor to be 5
# Q : What is the LAST n for which T(n) has the biggest factor to be 5 !
# A : From the brute force test it seems it is 80 !!!
# Now we must analyze why and find the underlying cause for this

def brute_force_testing( prime ) :
    S = prime * (prime+1)//2
    TG = triangle_number_gen()
    n = prime + 1
    while 1 :
        if not gmpy2.is_prime(n) or not gmpy2.is_prime(n+1) :
            if n% 2 ==0 :
                f1, f2 = get_factors(n//2), get_factors(n+1)
            else :
                f1, f2 = get_factors(n), get_factors((n+1)//2)

            F = sorted(f1 + f2)
            T = n*(n+1)//2
            # F = get_factors( T  )
            if max(F) <= prime :
                print('n=', n ,'       T(n) = ' , T,'          n=',f1 , '        n+1= ',f2 ,'         F=',F )# ,'       fact(n) =', get_factors(n) )
                S+=n
        n+=1
        if n == 5*10**3 : break

    return print('\nAnswer : \t', S)

brute_force_testing(7)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


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

