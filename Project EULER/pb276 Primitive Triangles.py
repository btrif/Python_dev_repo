#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                    Primitive Triangles     -       Problem 276

Consider the triangles with integer sides a, b and c with a ≤ b ≤ c.
An integer sided triangle (a,b,c) is called primitive if gcd(a,b,c)=1.
How many primitive integer sided triangles exist with a perimeter not exceeding 10 000 000 (10**7) ?
'''
import time
from math import gcd
from pyprimes import factorise
import functools, operator, itertools



def gcd(a, b):      # GCD
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a


def gcd3(a, b, c):
    return gcd(gcd(a, b), c)

def get_factors(n):       # From mhb038, England, Euler Forum
    """returns the prime factors of n"""
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else :
            n //= i
            factors.add(i)
    if n > 1  :
        factors.add(n)

    return factors


print('\n--------------------------TESTS------------------------------')
t1  = time.time()


def Primitive_integer_sided_triangles(perim) :
    cnt, p = 0, perim
    for a in range(1, p//3+1) :
    # for a in range(30, 31) :
        print(" ========= size " , a, " ========== " )
        for b in range(a, (p-a)//2 + 1 ) :
        # for b in range(a, 31 ) :
        #     print(" a= ",  a , "  ;  b = ", b ,end ='   ')

                    # CASE 1
            if gcd(a,b)  == 1 :
                cnt += p-a-2*b+1
                if ( a+b <= p/2 )  :      # we substract the cases like a,b,c = 1,1,2 to a,b,c = 25,25,50
                    cnt -= 1
                # print("  cnt0 = ", p-a-2*b , '       ',cnt )

                    # CASE 2
            if ( gcd(a,b) != 1   ) :
                cnt +=  p - a- 2*b+1
                g = gcd(a,b)
                F =  list(set(get_factors(g)))
                # print(F)
                for i in range(1, len(F)+1) :
                    C = list( itertools.combinations( F, i ) )
                    # print(list(C))
                    for j in C :
                        f = functools.reduce( operator.mul , j)
                        # print(" i = ", i ,"    ",f )
                        if i%2 == 1 :
                            cnt -= ((p-a-2*b)//f) +1
                            # print( " - cnt1 = " , ((p-a-2*b)//f) +1,'     ', cnt  )
                        if i%2 == 0 :
                            cnt +=  ((p-a-2*b)//f) +1
                            # print( " + cnt2 = " , ((p-a-2*b)//f) +1 ,'     ', cnt  )
    return print ('\nAnswer : \t', cnt)

Primitive_integer_sided_triangles(10**4)



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()

















# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')
#
