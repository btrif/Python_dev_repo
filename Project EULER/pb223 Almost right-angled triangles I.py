#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
        Almost right-angled triangles I     -       Problem 223

Let us call an integer sided triangle with sides a ≤ b ≤ c barely acute if the sides satisfy
a**2 + b**2 = c**2 + 1.

How many barely acute triangles are there with perimeter ≤ 25,000,000  (2.5*10**7)  ?


'''
import time
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
        for a in range(2, b+1):
            c_sq = a*a + b*b - 1
            # print('a, b, c_sq = ' , a, b, c_sq)
            if  is_square(c_sq) :
                c = int(sqrt(c_sq))

                if a+b+c <= up_lim :
                    cnt+=1
                    print(str(cnt)+'.      a = ', a, '    b=' ,  b, '     c=',c,'      perim=', a+b+c , '         c^2+1 = ', c**2+1)


    return print('\nAnswer : \t', cnt +u - 1 )

# up_lim = 10**2
up_lim = 25*10**3
# brute_force(  up_lim )



t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1 =  time.time()

# http://echochamber.me/viewtopic.php?t=45132




def my_first_soln( lim) :
    Sq1 = [i*i+1 for i in range(0, lim//2 )]
    Sq = [ x*x  for x in range(0, lim//2 ) ]

    print( len(Sq1) ,Sq1[::-50])
    print( len(Sq) ,Sq[::-50] ,'\n')

    cnt=0
    for i in range(4,  len(Sq1) ):
        high = i -1
        low =  math.floor( sqrt( (Sq1[i]-1)/2) )
        if i%10000 == 0 :
            # print(str(i)+'.       high   =  ', i, high ,  '  Sq1 = ' ,Sq1[i] , '    c_sq+1=', Sq1[i] ,'  high=' ,Sq[high] ,'    low=', low , '   time = ', round((time.time()-t1 ),2),' s' )
            t3 = time.time()
        for j in range(high, low, -1) :
            # print( Sq[j]  )
            b_sq = Sq[j]
            if is_square( (Sq1[i] - b_sq) ) :
                a = int(sqrt(Sq1[i] - b_sq))
                b = int(sqrt(b_sq))
                c = int(sqrt(Sq1[i]-1 ))
                if a+b+c <= lim :
                    cnt+=1
                    print(str(cnt)+'.      a = ', a, '    b=' ,  b, '     c=',c,'      perim=', a+b+c , '         c^2+1 = ', c )

    return print('\nAnswer : \t', cnt +lim//2 - 1)

my_first_soln( 25*10**2 )

# @2017-03-28 - I left here, I must use the a**2 -1 decomposition
## CHECKS
# solutions for perimeter < 10^4 is equal to 13656
#  <= 20,000 that would make 29257 triangles


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
