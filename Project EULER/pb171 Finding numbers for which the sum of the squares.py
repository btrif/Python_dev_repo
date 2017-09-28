#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Finding numbers for which the sum of the squares of the digits is a square      -           Problem 171

For a positive integer n, let f(n) be the sum of the squares of the digits (in base 10) of n, e.g.

f(3) = 3^2 = 9,
f(25) = 2^2 + 5^2 = 4 + 25 = 29, --> this is not valid, 29 not a square !
f(442) = 4^2 + 4^2 + 2^2 = 16 + 16 + 4 = 36

Find the last nine digits of the sum of all n, 0 < n < 10**20,   such that f(n) is a perfect square.
'''


import time, zzz, gmpy2

def f(n):
    l = sum([ int(i)**2 for i in str(n)])
    return l

print('test f : \t' , f(3) )






print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# # 2017-03-09 - APPROACH : I must identify for a given length of number which is the combination
# of digits whose squares gives another square .
# For example : for a length 2 I would immediately know that wa can use Pytagora. therefore :
# 34, 43 gives the perfect square 25;    68, 86 gives 100, there are also the 10 multiples.
#
# Then we must go to the 3 digit numbers. We already have some from the two's and we add 0, like
# 340 or 430 or 403 or 304 .
#
#
# https://plus.maths.org/content/triples-and-quadruples
# https://en.wikipedia.org/wiki/Pythagorean_quadruple

## IMportant OBSERVATION : maximum number is 10**20 => 20 digits => maximum square will be :
9**2 +....+ 9**2 = 81*20 = 1620
Those numbers must be broken into 2,3,4,.... parts squares such that :
So the problem reduces to ways to partition a square into squares :) NICE :)

Example : in a 4 digit number, let's say that we have the result, the square is 169
must broke into 4 squares : how we do it ?
we try : 169 - 16 = 153 - 36 = 117 - 81 = 36. Therefore we obtained the digits : 4,6,9,6 .
And from here we make permutations of that number. We must take for the zero case
and permutate accordingly

make a dictionary of squares

@2017-09-11 - Must do the recursive partition function, NOT YET FINISHED
In how many ways can we decompose a number into squares, like :
9 = 9
9 = 4,4,1
9 = 4,1,1,1,1,1
9 = 1,1,1,1,1,1,1,1,1


for i in range(1,10**4) :
    if gmpy2.is_square( f(i) ) :
        print(str(i)+'.      ', f(i))




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

