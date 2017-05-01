#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Golomb's self-describing sequence           -           Problem 341

The Golomb's self-describing sequence {G(n)} is the only non-decreasing sequence of natural numbers
such that n appears exactly G(n) times in the sequence.

The values of G(n) for the first few n are :

                              n	1	2	3	4	5	6	7	8	9	 10  11	  12 	13	 14	15	…
                            G(n)	1	2	2	3	3	4	4	4	5	 5	   5     6	    6	  6	   6	…

You are given that G(10**3) = 86, G(10**6) = 6137.

You are also given that Σ G(n**3) = 153506976 for 1 ≤ n < 10**3.

Find ΣG(n**3) for 1 ≤ n < 10**6.                    ...........   => the range is actually (1 --> 10**18 )


'''
import time, zzz
from math import log

G = dict()
G[1] =1

phi = (1+ 5**(1/2))/2

a = lambda n : phi**(2-phi) * n**(phi-1)        # Approximative Asimptotic Function


print('Test for a_n function : \t', a(10**3))
print('\nTest for a_n function : \t', a(10**6))     # Error
print('Test for a_n function : \t', a(719845))      # Here we already get Errors
print('Test for a_n function : \t', a(91374964))
print('Test for a_n function : \t', a(919986484788))        # Huge Error


print('\n--------------------------TESTS------------------------------')
t1  = time.time()

#  INFO
# https://en.wikipedia.org/wiki/Golomb_sequence
# http://planetmath.org/sites/default/files/texpdf/40245.pdf
# http://www.sciencedirect.com/science/article/pii/0022314X9290024J


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

