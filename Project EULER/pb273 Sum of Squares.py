#  Created by Bogdan Trif on 11-11-2017 , 9:11 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                    Sum of Squares          -           Problem 273

Consider equations of the form: a^2 + b^2 = N ,    0 ≤ a ≤ b,   a, b and N integer.

For N=65 there are two solutions:
a=1, b=8        and
a=4, b=7.

We call S(N) the sum of the values of a of all solutions of a^2 + b^2 = N,        0 ≤ a ≤ b, a, b and N integer.

Thus S(65) = 1 + 4 = 5.

Find ∑S(N), for all squarefree N ONLY divisible by primes of the form 4k+1 with 4k+1 < 150.


'''
import time, zzz
from math import sqrt, ceil, floor
from itertools import combinations
from functools import reduce
from operator import mul

def prime_sieve_generator(lower, upper):      #FIFTH FASTEST
    """  Sieve of Eratosthenes
    Create a candidate list within which non-primes will be marked as None.         """
    cand = [i for i in range(3, upper + 1, 2)]
    end = int(upper ** 0.5) // 2

    # Loop over candidates (cand), marking out each multiple.
    for i in range(end):
        if cand[i]:
            cand[cand[i] + i::cand[i]] = [None] * ( (upper // cand[i]) - (upper // (2 * cand[i])) - 1 )
    # Filter out non-primes and return the list.
    return [2] + [ i for i in cand if i and i > lower ]


primes = [ i for i in prime_sieve_generator( 2, 150) if  i%4 == 1  ]
print(primes)

is_square = lambda x :  int( x**(1/2) )**2 == x

# https://en.wikipedia.org/wiki/Brahmagupta#Pell.27s_equation
# https://projecteuler.chat/viewtopic.php?f=50&t=1793&start=20

def decompose_prime_4k_1(p):
    n = int(floor( sqrt(p) ))

    while True :
        a = p - n*n
        if is_square(a)  :
            # if a > n :  return n, a
            return int(sqrt(a)), n

        n -= 1

A = dict()
for cnt, p in enumerate(primes) :
    a, b = decompose_prime_4k_1(p)
    A[p] = []
    A[p].append( (a, b) )
    print(str(cnt+1) +'.         p= ', p  ,'       a= ', a, '   b= ', b  )

print('\nA :', A)


# def combine_primes( P, A ) :
#     X=[]
#     N1, N2 = reduce(mul,  P[:-1]), P[-1]
#     print('N=' ,  N1*N2    ,'            N1 , N2 = ', N1, N2 )
#     for i in A[N1] :
#         for j in A[N2] :
#             X.append(i*j)
#     return N1*N2,  X



print('\n--------------------------TESTS------------------------------')
t1  = time.time()


# print('\nA :', A)

def brute_force_composed_prime( x, A ):
    X = A[x]
    print('\nx : ', x , '      X = ' ,X )
    up = int( sqrt(x) )
    down = int( sqrt(x/2) )

    for a in range(up, down, -1) :
        b = x - a*a
        if is_square(b) :
            print('x = ', x,'      a=  ' , a ,'      b = ' , int( sqrt(b)) )


# brute_force_composed_prime(251426921, A )


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n=========  My FIRST SOLUTION,  Brahmagupta Identity,  1 min  ===============\n')
t1  = time.time()

'''
@ 2019-01-26 - 10:20 - GENERAL IDEA
By using Brahmaputra Property we have that :
p1 = a^2 + b^2
p2 = c^2 + d^2

5*13 = p1 *p2 = (a^2 + b^2) * (c^2 + d^2)
= (ac)^2 + (ad)^2 + (bc)^2 + (bd)^2 = (ac)^2 + (bd)^2 + (bc)^2 + (ad)^2  =
= (ac + bd)^2 - 2abcd + (ac - bd)^2 + 2abcd =
= (ac + bd)^2 + (ac - bd)^2
'''

def solution_Sum_of_Squares() :

    for i in range(2, 17 ) :
        comb = list(combinations(primes, i) )
        print(str(i)+'.     ' ,  len(comb),'      ', comb[:10]  )
        for J in comb :
            N1, N2 = J[:-1], J[-1]
            p1 = reduce(mul, N1)
            x = reduce(mul, J)

            # print('x=  ', x , '    ',J,'       N1 =' , N1,'       N2 =' , N2, '    ', A[p1],'      ' ,A[N2] )
            for P1 in A[p1] :
                for P2 in A[N2] :
                    a, b, c, d = P1[0], P1[1], P2[0], P2[1]
                    x1, x2, x3, x4 = abs(a*c + b*d), abs(a*d - b*c) , abs(a*c - b*d), abs(a*d + b*c)
                    # print(P1, P2, '    , a, b, c, d = ', a, b, c, d ,'        ', (x1, x2),'     ', (x3, x4)  )
                    if x not in A :    A[x] = []
                    A[x].append( (x1, x2)  )
                    A[x].append( (x3, x4)  )


    # print('\nA : ', A)

    Sum = 0
    for k,V in A.items() :
        min_val = [ min(i) for i in V  ]
        # print('k= ', k, '   V= ', V[:2], min_val )
        Sum += sum(min_val)

    print('\nANSWER : ', Sum )
    return Sum

solution_Sum_of_Squares()                       #ANSWER :  2032447591196869022

t2  = time.time()
print('\n# Completed in :', round((t2-t1),2), 's\n\n')                  # Completed in : 53.3 s


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




