#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Prime triples and geometric sequences       -       Problem 518

Let S(n) = Σ a+b+c over all triples (a,b,c) such that:

a, b, and c are prime numbers.
a < b < c < n.
a+1, b+1, and c+1 form a geometric sequence.

For example, S(100) = 1035 with the following triples:

(2, 5, 11), (2, 11, 47), (5, 11, 23), (5, 17, 53), (7, 11, 17), (7, 23, 71), (11, 23, 47), (17, 23, 31), (17, 41, 97), (31, 47, 71), (71, 83, 97)

Find S(10**8).


'''
import time, zzz
from gmpy2 import mpq, is_prime
from math import ceil, floor, sqrt
from pyprimes import factorise
from itertools import combinations
from operator import mul
from functools import reduce

import numpy
def prime_sieve_numpy(n):                       ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    """ Input n>=6, Returns a array of primes, 2 <= p < n
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188 """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]



def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]


print('\n------------------ Concept Testing--------------------------')
test = [(2, 5, 11), (2, 11, 47), (5, 11, 23), (5, 17, 53), (7, 11, 17), (7, 23, 71), (11, 23, 47), (17, 23, 31), (17, 41, 97), (31, 47, 71), (71, 83, 97)]

for i in test :
    a, b, c = i
    print( 'a, b, c = ', a, b, c,'          diff= ' ,  b-a, c-b,'         ' , mpq(b+1, a+1), mpq(c+1, b+1),    )

# http://math.stackexchange.com/questions/1218821/find-all-prime-triples-a-b-c-such-a1-b1-c1-form-a-geometric-sequence


def greatest_root_factor(n) :
    f = factorise(n)
    f2 = [   i[0]** (i[1]//2)  for i in f  ]
    f3 = reduce(mul, f2)
    # print(f, f2, f3 )
    return f3


print( 'greatest_root_factor : \t',greatest_root_factor( 80 ),'\n')


print('\n------------------ My First Solution , 1 hour------------------------------')
t1  = time.time()


def prime_triples ( lim) :
    primes = prime_sieve_numpy(lim)
    print(primes[:100],'\n')

    S = 0
    for p in primes :
        # print('=====',p)
        f = list(factorise(p+1))
        b = int( greatest_root_factor(p+1) )
        # for i in range(1, len(f3)+1 ):
        #     # print( list(combinations (f3, i)) )
        #     for j in  combinations (f3, i) :
        #         b = reduce(mul, j)
        # print(b,'------------', type(b) )
        for a in range(b+1, ceil(b * sqrt( (lim+1)/(p+1) ))  ) :
            # print('a=', a ,'    ', type(a) )
            k = mpq( a, b)
            p2, p3 = int( (p+1)*k-1) , int((p+1)*k*k-1)
            if is_prime(p2) and is_prime(p3) :
                print(p,'            p+1 =', f ,  '        k =' , k,'        p1, p2, p3 = ', p, p2, p3 )
                S +=p+p2+p3

    return print('\nAnswer : \t', S)

prime_triples(10**8)                #   Answer : 	 100315739184392

t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60, 6), 'ms\n\n')

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

