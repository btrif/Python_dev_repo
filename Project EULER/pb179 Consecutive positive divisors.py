#!/usr/bin/python
# Solved by Bogdan Trif @ Completed on Sat, 17 Dec 2016, 23:44
#The  Euler Project  https://projecteuler.net
'''
                    Consecutive positive divisors       -   Problem 179

Find the number of integers 1 < n < 10**7, for which n and n + 1 have the same number of positive divisors.

For example, 14 has the positive divisors 1, 2, 7, 14   while   15 has  1, 3, 5, 15.
'''


import time, sys
import gmpy2
from math import sqrt

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

print(get_factors(1979197919791979))
#print(list(i[0] for i in list(factorise(3932273))))


def  calculate_divisors(nr):
    '''**©** Made by Bogdan Trif @ 2016-12-08, 16:30.
        :Description: Functions which computes the number of divisors of a number.
                It uses the Numbers of Divisors Theorem :which says : if N=a**x*b**y*c**z => divisors_nr=(x+1)(y+1)(z+1)
            Example: N = 216 = 2**3 * 3**3 => divisors_nr = (3+1)(3+1) = 16
    :param nr: int, nr
    :return: int, divisors_number                   '''
    import functools, operator
    from pyprimes import factorise
    def factors(nr):
        ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
        return [i for i in factorise(nr)]
    N = factors(nr)
    return  functools.reduce( operator.mul , [ (i[1]+1) for i in N ])



print('\n--------------------------TESTS------------------------------')


print('\n======== My FIRST SOLUTION,  Need Improvement ,VERY SLOW 26 min ===============\n')
t1  = time.time()

def my_first_solution(up_range) :
    h, counter = 0, 0
    I_last=2
    for i in range(3, up_range+1 ):
        if gmpy2.is_prime(i) :
            I_n = 2
        else :
            I_n = calculate_divisors(i)
        if I_n == I_last :
            counter+=1
        # print(str(i)+' :   ' ,  I_last  , '    ', str(i+1)+' :   '  , I_n, '        Cnt:'  ,counter)
        I_last = I_n            # Important Line
        if i*100 //up_range  > h-1 :        # Progress Bar #
            h += 1
            # sys.stdout.write("\r%d%%-" %h )
            sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(220-22*h//10) +']' )   # Font Segoe UI Semibold
            # sys.stdout.write('\r' + str(h)+' % ['+'#'*h+str(' ')*(100-h) +']' )         #  Calibri, Adjust the numbers, for the font of your configuration
            # sys.stdout.flush()
    return print('\nAnswer : ',counter)

# my_first_solution(10**7)            # Answer :  986262


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')        # Completed in : 1586.758758 s



print('\n======== My SECOND SOLUTION, 22 secs, Copied drom FJ_Sevilla ===============\n')
t1  = time.time()


def pb179(limit):

    divisors = [0]*(limit)
    for i in range(2, int(sqrt(limit))):
        s = i**2
        divisors[s] += 0.5
        for j in range( i+s, limit, i):
            divisors[j] += 1
    return print(sum(divisors[i] == divisors[i - 1] for i in range(3, limit)))

pb179(10**7)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')        # Completed in : 1586.758758 s





print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, VERY INNOVATIVE & ELEGANT  15 secs --------------------------')
t1  = time.time()

# ===== Tue, 24 May 2016, 17:22, FJ_Sevilla , Spain
# Python 3 It is not as fast but is simple :)

from math import sqrt
def FJ_Sevilla():
    limit = 10**7
    divisors = [0]*(limit)
    for i in range(2, int(sqrt(limit))):
        s=i**2
        divisors[s] += 0.5
        for j in range(i+s, limit, i):
            divisors[j] += 1
    return print(sum(divisors[i] == divisors[i - 1] for i in range(3, limit)))

# FJ_Sevilla()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, Brute Force,  27 sec  --------------------------')
t1  = time.time()
# =====  Mon, 5 Oct 2015, 03:22, elvischen

def elvischen() :
    Limit = 10**7
    x = [2]*Limit
    for i in range(2,int(Limit**0.5)):
        for j in range(i*i,Limit,i):
            x[j] += 2
    for i in range(2,int(Limit**0.5)):
        x[i**2] -= 1

    result = 0
    for i in range(2,Limit-1):
        if x[i]== x[i+1]:
            result += 1
    return print('Result:   ' , result)

# elvischen()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# ====== Mon, 20 Oct 2014, 14:46, fioi, France

def fioi():
    upper = 10 ** 7
    nb_divs = [1] * upper

    for i in range(2, upper):
        if nb_divs[i] == 1:
            for j in range(i, upper, i):
                k, l = 0, j
                while l % i == 0:
                    l //= i
                    k += 1
                nb_divs[j] *= k + 1

    ans = 0

    for i in range(1, upper - 1):
        if nb_divs[i] == nb_divs[i + 1]:
            ans += 1

    return print(ans)

fioi()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, 1 min  --------------------------')
t1  = time.time()

# ===== Mon, 31 Oct 2016, 05:58, mbh038  , England
# 33 s in Python. I use a sieve to determine the number of divisors.

import time
import numpy as np

def p179(limit=100):
    t=time.clock()
    a1=np.ones( limit, dtype=int )
    for divisor in range(1,limit):
        a1[divisor :: divisor] += 1
    print(sum([a1[i] == a1[i+1] for i in range(2,len(a1)-1)]))
    print (time.clock()-t)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
