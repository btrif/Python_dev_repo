#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
        Almost right-angled triangles I     -       Problem 223

Let us call an integer sided triangle with sides a ≤ b ≤ c barely acute if the sides satisfy
a^2 + b^2 = c^2 + 1.

How many barely acute triangles are there with perimeter ≤ 25,000,000  (25*10**6)  ?


'''
import time
from gmpy2 import mpq
from math import gcd, sqrt

import math
from pyprimes import factorise

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

is_square = lambda x :  int(sqrt(x))**2 == x

print('\n-----------------------  BRUTE FORCE TESTS  ------------------------------')
t1  = time.time()


def brute_force( up_lim) :       # @2017-09-23 - Brute Force method was corrected ! Works
    u = up_lim//2
    cnt=0
    for b in range(1, u):
        for a in range(4, b+1):
            c_sq = a*a + b*b - 1
            # print('a, b, c_sq = ' , a, b, c_sq)
            if  is_square(c_sq) :
                c = int(sqrt(c_sq))

                if a+b+c <= up_lim :
                    cnt+=1
                    print(str(cnt)+'.      a = ', a, '    b=' ,  b, '     c=',c,'      perim=', a+b+c , '         c^2+1 = ', c**2+1)


    return print('\nAnswer : \t', cnt +u - 1 )

up_lim = 10**3
# up_lim = 25*10**4
brute_force(  up_lim )



t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1 =  time.time()

# http://echochamber.me/viewtopic.php?t=45132




def my_first_soln( lim) :
    A = [ x*x  for x in range(0, lim//2 ) ]
    C = [i*i+1 for i in range(0, lim//2 )]


    # print( len(A) ,A[::-50] ,'\n')
    # print( len(C) ,C[::-50])


    cnt=0
    for i in range(4,  len(C) ):
        high = i -1
        low =  math.floor( sqrt( (C[i]-1)/2) )
        if i%10000 == 0 :
            # print(str(i)+'.       high   =  ', i, high ,  '  Sq1 = ' ,Sq1[i] , '    c_sq+1=', Sq1[i] ,'  high=' ,Sq[high] ,'    low=', low , '   time = ', round((time.time()-t1 ),2),' s' )
            t3 = time.time()

        for j in range(high, low, -1) :
            # print( Sq[j]  )
            b_sq = A[j]
            if is_square( (C[i] - b_sq) ) :
                a = int(sqrt(C[i] - b_sq))
                b = int(sqrt(b_sq))
                c = int(sqrt(C[i]-1 ))
                if a+b+c <= lim :
                    cnt+=1
                    # print(str(cnt)+'.      a = ', a, '    b=' ,  b, '     c=',c,'      perim=', a+b+c , '         c^2+1 = ', c**2+1,'           (c-b)/(a-1)= (a+1)/(c+b)= ' , mpq(c-b, a-1) )

    return print('\nAnswer : \t', cnt +lim//2 - 1)

# my_first_soln( 25*10**2 )
# my_first_soln( 10**4 )


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')



t1  = time.time()


def my_second_soln( lim) :
    A = [ x*x  for x in range(0, lim//2 ) ]
    C = [i*i+1 for i in range(0, lim//2 )]
    # print( len(A) ,A[::-50] ,'\n')
    # print( len(C) ,C[::-50])

    cnt=0
    for a in range(4,  len(A) ):
        if a > lim /3 : break
        if a%10000 == 0 :
            print(str(a)+'.        ', a,  '  A = ' ,A[a] , '   time = ', round((time.time()-t1 ),2),' s' )
            t3 = time.time()
        a_sq = A[a]
        for b in range(a, len(A) ) :
            if a+b > 2*lim /3 : break
            if  2*b +2 > a*a : break
            b_sq = A[b]
            if is_square( a_sq + b_sq -1 ) :
                c = int(sqrt(a_sq + b_sq -1 ))


                if a+b+c <= lim :
                    cnt+=1
                    # print(str(cnt)+'.      a = ', a, '    b=' ,  b, '     c=',c,'      perim=', a+b+c , '         c^2+1 = ', c**2+1,'           (c-b)/(a-1)= (a+1)/(c+b)= ' , mpq(c-b, a-1) )

    return print('\nAnswer : \t', cnt +lim//2 - 1)


# my_second_soln( 10**4 )






# @2017-03-28 - I left here, I must use the a**2 -1 decomposition
## CHECKS
# solutions for perimeter < 10^4 is equal to 13656
#  <= 20,000 that would make 29257 triangles

# https://arxiv.org/pdf/1508.07562.pdf        !!!
# https://benvitalenum3ers.wordpress.com/2015/12/09/diophantine-equation-x2-y2-z2-1-almost-pythagorean-triples/       !!!


# https://www.geeksforgeeks.org/check-whether-number-can-represented-sum-two-squares/

for t in range(1, 10) :
    x1, x2 = 3*t + 2 ,  3*t  + 1
    y1, y2 = 4*t + 1 ,  4*t + 3
    z1, z2 = 5*t + 2 ,   5*t + 3
    print('APT 1 : ',  x1, y1, z1  )
    print('APT 2 : ',  x2, y2, z2  )


@2018-05-15 - The above is only a part of the solution. the problem can be solved as following :
1. Generate Primitive Pythagorean Triplets (PTT) of the form : (2i − 1, 2i^2 − 2i, 2i^2 − 2i + 1) with i ≥ 2
2. Use them to generate two kinds of APT (Almost Pythagorean Triplets)
to generate the system of 6  linear equations .

Sugestion : try to use a linear solver linalg to solve the system. Otherwise you can already use the already
    solved ones https://arxiv.org/pdf/1508.07562.pdf


t2  = time.time()
print('\nCompleted in :', round((t2-t1),2), 's\n\n')


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
