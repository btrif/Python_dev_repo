#  Created by Bogdan Trif on 21-11-2017 , 10:01 AM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
            Distinct terms in a multiplication table            -       Problem 466

Let P(m,n) be the number of distinct terms in an m×n multiplication table.

For example, a 3×4 multiplication table looks like this:

                                    ×	1	2	3	4
                                    1	1	2	3	4
                                    2	2	4	6	8
                                    3	3	6	9	12

There are 8 distinct terms {1,2,3,4,6,8,9,12}, therefore P(3,4) = 8.

You are given that:
P(64,64) = 1263,
P(12,345) = 1998, and
P(32,10^15) = 13826382602124302.

Find P( 64 , 10^16 ).


'''
import time, zzz
from gmpy2 import is_prime, is_fibonacci_prp

def gcd(a, b):      # GCD
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

def get_divisors(n):      ### ( ͡° ͜ʖ ͡°)  SECOND FASTEST ,  MUST BE IMPROVED !! It is a sqrt(n) Algorithm
    from math import sqrt
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)[:-1]         # without the number itself

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def small_case_brute_force( h, v ):
    S = set()
    for i in range(1, h +1):
        for j in range(1, v +1):
            S.add(i*j)

    print('\nBF Sol = ', len(S))

small_case_brute_force(8, 11)

print('\n--------------------------   FURTHER  TESTS------------------------------')

# IDEA @2017-11-22
# for the case 11, 8
# We see that for numbers like 6, which has 6 divisors --> [1, 2, 3, 6] the number 6 will appear 4 times
# in 4 different rows :
# 1st row, col 6
# 2nd row, col 3
# 3rd row, col 2
# 6th row, col 1

# case 12 :
# combinations of 6 with 2, 3, 4 gives 12 --> need only 1
#  combinations of 4 with 2, 3 gives 12  --> need only 1
# Question : How to cut the others ?




rows, cols = 8, 11
col = [ i for i in range(1, cols+1 ) ]
M = []
for j in range(1, rows+1) : M.append( list(map(j .__mul__, col )) )
for i in M : print(i)
print('\n--------------------------------------\n')

def first_solution(rows, cols):
    W = rows*cols
    print('Init nr = ', W)
    for i in range(1, rows+1):
        print('------- row', i,'  ------- ')
        for j in range(i+1, rows+1 ) :
            g  = gcd(i, j)

            if g == 1 :         # case (2, 3),   (1,  any number)
                m = i*j
            elif g != 1 :
                if not is_prime(i) and not is_prime(j) :    # case 2, 4
                    m = i*j//g
                else :
                    m = j


            if not is_prime(j) :

                div = get_divisors(j)




            X =  [k for k in range(m , i*cols+1 , m  ) ]

            cnt =  i*cols// m
            W -= cnt

            print(str(j)+'.       m=',m , '     i*cols =  ' ,i*cols   , '       cnt = ' , cnt,'    ', X )

    print('\nSolution = ' , W)
    return W

first_solution(8, 11)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()





# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

