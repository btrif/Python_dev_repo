#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Right-angled triangles that share a cathetus        -       Problem 176

The four right-angled triangles with sides (9,12,15), (12,16,20), (5,12,13) and (12,35,37)
all have one of the shorter sides (catheti) equal to 12.

It can be shown that no other integer sided right-angled triangle exists with one of the catheti equal to 12.

Find the smallest integer that can be the length of a cathetus of exactly 47547 different integer sided right-angled triangles.


'''
import time
import gmpy2
from sympy import ntheory


def get_divisors(n):      ### ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
    from math import sqrt
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)

def Pythagorean_triplets_gen():    # by Bogdan Trif
    ''':Usage:      >>> pyt = gen_Pythagorean_triplets()
                        # >>> next(pyt)
                        # >>> for i in gen_Pythagorean_triplets(): print(i)
    :param i:   i
    :param j:   j
    :return:    a,b,c - pythagorean triplet
    '''
    m = 1
    while True :
        for n in range(1, m):      ### range(1,m) as we need only a > 0 !!!!!!!!
            a = m**2-n**2
            b = 2*m*n
            c = m**2 + n**2
            # if a > 0:
            # print(' m n = \t',m, n,'            a,b,c =\t',sorted((a,b,c)))
            yield a,b,c
        m+=1

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]



@2017-03-23 - get_factors(47547) =  [3, 3, 3, 3, 587]
we need to find the smallest triangles with 3, 3, 3, 3 shared cathetus and find the largest with 587 cathetus
We then must multiply all these to obtain the desired trainagle !!

@2017-04-29 - Actually we need to find a x which in combinations with other numbers y smaller or bigger than x
=> x**2 + y**2 is a perfect square.  In the example given :
(9,12,15), (12,16,20), (5,12,13) and (12,35,37) => x=12 form with 4 different y's perfect squares
in this case the range of y's is :   9 <= y <= 35


print('\n--------------------------TESTS------------------------------')
t1  = time.time()


# G = Pythagorean_triplets_gen()
# Q = set()
#
n = 5040*3
#
# cnt=0
# for i in range( n*n//8 ):
#     PT = next(G)
#     print(PT)
#     if PT[0] == n or PT[1] == n or n % PT[0] == 0 or n%PT[1] == 0 :
#         cnt+=1
#         print(str(i)+'.    ', PT,'         ' ,cnt)
#     if PT[0] == n or PT[1] == n :
#         Q.add(PT[2])
#     if n % PT[0] == 0 :
#         Q.add(PT[2]* n//PT[0] )
#     if n%PT[1] == 0  :
#         Q.add(PT[2]* n//PT[1] )
#
#
# print('\n', n,'---> ',len(Q),'   ' ,get_factors(n))

# 30 --->  4     [2, 3, 5]
# 60 --->  13     [2, 2, 3, 5]
# 120 --->  22     [2, 2, 2, 3, 5]

# 240 --->  31     [2, 2, 2, 2, 3, 5]
# 360 --->  37     [2, 2, 2, 3, 3, 5]
# 600 --->  37     [2, 2, 2, 3, 5, 5]

# 210 --->  13     [2, 3, 5, 7]
# 420 --->  40     [2, 2, 3, 5, 7]
# 840 --->  67     [2, 2, 2, 3, 5, 7]
# 1680 --->  94     [2, 2, 2, 2, 3, 5, 7]

# 2520 --->  112     [2, 2, 2, 3, 3, 5, 7]      #######

# 5040 --->  157     [2, 2, 2, 2, 3, 3, 5, 7]
# 7560 --->  157     [2, 2, 2, 3, 3, 3, 5, 7]
# 12600 --->  187     [2, 2, 2, 3, 3, 5, 5, 7]
# 17640 --->  187     [2, 2, 2, 3, 3, 5, 7, 7]

# 15120 --->  220     [2, 2, 2, 2, 3, 3, 3, 5, 7]       #    5040*3

# 2310 --->  40     [2, 3, 5, 7, 11]        #######
# 4620 --->  121     [2, 2, 3, 5, 7, 11]
# 9240 --->  202     [2, 2, 2, 3, 5, 7, 11]

# 6300 --->  112     [2, 2, 3, 3, 5, 5, 7]

# 6930 --->  67     [2, 3, 3, 5, 7, 11]
# 11550 --->  67     [2, 3, 5, 5, 7, 11]
# 16170 --->  67     [2, 3, 5, 7, 7, 11]

# 10080 --> 202       [2, 2, 2, 2, 3, 3, 5, 7]

def small_brute_force_test(nr):
    cnt = 0
    for b in range(3, 2000*nr):
        if  gmpy2.is_square( nr**2 + b**2 ) :
            cnt+=1
            print(str(cnt)+'.     ',nr, b, pow(nr**2 + b**2, 1/2) )
    return print('\nAnswer : \t', cnt)

nr = 2*2*3*5*7*11*13
small_brute_force_test(nr)
print('Its Totient : \t',ntheory.totient(nr) )


# 357.      60060 100200091 100200109.0    Answer : 	 357     Its Totient : 	 11520    Completed in : 235.903493 s

@2017-03-09 - This must be done with some kind of totient type method.
OBSERVATION : I observed that the totient number is in some kind of correlation with
the number of pythagorean triplets that share a cathetus. Must find some kind of relation

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's')

# print('\n----------Get Divisors------------\n')
# t1  = time.time()
#
# for i in (n, n+1):
#     print( i, get_divisors(i) ,'    Divisors : ', len(get_divisors(i))-2 , '       Totient :\t',ntheory.totient(i) )
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n================  My FIRST SOLUTION,   ===============\n')
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
