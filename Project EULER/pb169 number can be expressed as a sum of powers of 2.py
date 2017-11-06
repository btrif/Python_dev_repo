#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Exploring the number of different ways a number can be expressed as a sum of powers of 2    -   Problem 169

Define f(0)=1 and f(n) to be the number of different ways n can be expressed as a sum of integer powers of 2
using each power no more than twice.

For example, f(10)=5 since there are five different ways to express 10:

1 + 1 + 8
1 + 1 + 4 + 4
1 + 1 + 2 + 2 + 4
2 + 4 + 4
2 + 8

What is f(10**25)?

'''
import time
from functools import lru_cache
from math import log2

D = { 1 : 1}

print('log base 2 of 10 :\t',log2(10))
print('log base 2 of 20 :\t',log2(20))
print('log base 2 of 50 :\t',log2(50))
print('log base 2 of 100 :\t',log2(100))

print('\n--------------------')

def decompose_number(n):
    N = []
    while n >= 1 :
        x = int(log2(n))
        N.append(2**x)
        n = n%(2**x)
        # print(n)
    return N


print('function decompose_number testing : \t',decompose_number(10**3))

print('\n--------------------')

#
# x=1
# for i in range(16):
#     print(x<<i, end='  ')


def partition_nr_into_given_set_of_nrs(nr, S,  lim=10 ):
    nrs = sorted(S, reverse=True)
    def inner(n, i, lim ):
        if lim >= 0 :
            if n == 0:
                yield []
            for k in range(i, len(nrs)):
                if nrs[k] <= n:
                    for rest in inner(n - nrs[k], k , lim-1 ):

                        yield [nrs[k]] + rest
    return list(inner(nr, 0, lim))

S = []
i = 0
while 2**i < 10**25 :
    print(str(i)+'.  ', 2**i )
    S.append(2**i)
    i+=1

print('\n--------------------------TESTS------------------------------')
t1  = time.time()


##### The Recursive algorithm translated from  C++  http://euler.stephan-brumme.com/169/
#   Works until 10**5

@lru_cache()            # improves performance by a factor of 2x
def solve(x, minAdd =1) :
    if x == 0 : return 1

    result = 0
    current = minAdd

    while current <= x :
        # try to remove current 2^k once
        result += solve(x- current , current*2 )

        if x >= 2* current :
            result += solve(x-2*current, current*2 )

        # process 2^(k+1)
        current *= 2

    return result


print(   solve(10**5, 1)  )

# http://sieverything.blogspot.ro/2011/10/problem-169-projecteulernet.html

t2  = time.time()
print('\nCompleted in :', round((t2-t1) , 4), 's\n\n')

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
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
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
