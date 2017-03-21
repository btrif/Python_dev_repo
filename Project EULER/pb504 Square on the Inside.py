#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Thu, 23 Feb 2017, 10:39
#The  Euler Project  https://projecteuler.net
'''
Square on the Inside            -       Problem 504

Let ABCD be a quadrilateral whose vertices are lattice points lying on the coordinate axes as follows:

A(a, 0), B(0, b), C(−c, 0), D(0, −d), where 1 ≤ a, b, c, d ≤ m and a, b, c, d, m are integers.

It can be shown that for m = 4 there are exactly 256 valid ways to construct ABCD.
Of these 256 quadrilaterals, 42 of them strictly contain a square number of lattice points !!!!!!!!!!!!!!!!!

How many quadrilaterals ABCD strictly contain a square number of lattice points for m = 100?


'''
import time
import gmpy2
from math import gcd
import itertools







print('\n------------------ My First Solution using PICK-s  THEOREM, SLOW 3 min------------------------------')
t1  = time.time()

def Using_Picks_Theorem(m):
    ''':The formula of Pick's Theorem is: : **A = i + b/2 - 1**, where
        i - lattice points inside the polygon;
        b - lattice points on the edges of the polygon including the vertices
    :param m: int, limit
    :return:int, the number of lattice points inside the quadrilateral
    '''
    cnt=0
    for a in range(1, m+1) :
        print(a)
        for b in range(1, m+1) :
            for c in range(1, m+1) :
                for d in range(1, m+1) :
                    A = a*b/2 + b*c/2+ c*d/2+d*a/2
                    B = gcd(a,b)+gcd(b,c)+gcd(c,d)+gcd(d,a)
                    i = int(A-(B/2)+1)
                    if gmpy2.is_square(i) :
                        cnt+=1
                        # print(str(cnt)+'.        ',a, b, c, d,'        area=', A, '      b=', B, '      inside=', i )
    return print('\nAnswer : ', cnt)

# Using_Picks_Theorem(m=100)              #   Answer :  694687

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

#### IDEA --
# https://en.wikipedia.org/wiki/Pick%27s_theorem

# TRIED       :   Answer :  3651406, 694687


print('\n==============  My FIRST SOLUTION, IMPROVED  ===============\n')
t1  = time.time()


def Using_Picks_Theorem_2(m):
    ''':The formula of Pick's Theorem is: : **A = i + b/2 - 1**, where
        i - lattice points inside the polygon;
        b - lattice points on the edges of the polygon including the vertices
    :param m: int, limit
    :return:int, the number of lattice points inside the quadrilateral
    '''
    cnt=0
    for a, b, c, d in itertools.product(range(1, m+1), repeat=4 ) :
        A = a*b/2 + b*c/2+ c*d/2+d*a/2
        B = gcd(a,b)+gcd(b,c)+gcd(c,d)+gcd(d,a)
        i = int(A-(B/2)+1)
        if gmpy2.is_square(i) :
            cnt+=1
            # print(str(cnt)+'.        ',a, b, c, d,'        area=', A, '      b=', B, '      inside=', i )
    return print('\nAnswer : ', cnt)

Using_Picks_Theorem_2(m=100)              #




t2  = time.time()
print('\nCompleted in :', round((t2-t1), 6), 's\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, ELEGANT  INSIGHT WITH itertools--------------------------')
t1  = time.time()


# === Wed, 15 Jun 2016, 23:07, Knight-erraunt
# It surprises me that some people still use nested for loops, I personally
# extremely like itertools, they make solution to this problem fairly short
# and elegant. The problem itself was easy.
#
# EDIT:
# I really like the insights about the symmetries, feel shame I did not think
# about it, but well, there are little time constraints and the program ran
# less than a minute under pypy (not speaking about the C++ equivalent).

from math import gcd
from itertools import product

M = 100

squares = {x**2 for x in range(2 * M + 1)}

result = 0

for a, b, c, d in product(range(1, M+1), repeat=4):
    on_boundary = gcd(a, b) + gcd(b, c) + gcd(c, d) + gcd(d, a)
    area = (a * b + b * c + c * d + d * a) // 2
    int_points = area - on_boundary // 2 + 1
    if int_points in squares:
        result += 1

print(result)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2, NICE OPTIMIZATION, but not correct  --------------------------')
t1  = time.time()

def lattice(m):
    square_num = set(i**2 for i in range(int(20000**0.5)))

    tri_table = [[[0]*101 for i in range(101)] for j in range(101)]
    for a in range(101):
        for h in range(101):
            for c in range(101):
                A2 = (a+c)*h
                B = gcd(a, h) + gcd(h, c) + a + c
                tri_table[a][h][c] = (A2 + B)//2 + 1

    s = 0
    for a in range(1, m+1):
        for c in range(1, a+1):
            r = 1
            if c != a: r *= 2 # a,c symmetry
            for b in range(1, m+1):
                abc_ = tri_table[a][b][c] + a + c - 1
                for d in range(1, b+1):
                    if abc_ + tri_table[a][d][c] in square_num:
                        if d != b: s += 2*r # b,d symmetry
                        else: s += r

    return s

print(lattice(100))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# ===== Mon, 2 Mar 2015, 10:38, eidanch, Israel
# Go Pick's Theorem!

from math import sqrt

def count_lattice_points(a, b, c, d):
    A = (a*b + b*c + c*d + d*a)/2
    boundary = gcd(a,b) + gcd(b,c) + gcd(c,d) + gcd(d,a)
    i = A - boundary/2 + 1
    return i

def test(a,b,c,d):
    i = count_lattice_points(a,b,c,d)
    sqrti = sqrt(i)
    return int(sqrti)**2 == i

def e504(m):
    count = 0
    for a in range(1, m+1):
        for b in range(1, m+1):
            for c in range(1, m+1):
                for d in range(1, m+1):
                    if test(a,b,c,d):
                        count += 1
    return count

if __name__ == '__main__':
    print (e504(100))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# === Thu, 5 Mar 2015, 19:44, KORENA, USA
# Runs in under 20s in pure Python.


size = 101
lattices = [[-1] * size for n in range(size)]

def lattice(p1, p2):
    if lattices[p1][p2] == -1:
        f = gcd(p1, p2) + 1
        lattices[p1][p2] = f
        lattices[p2][p1] = f
    return lattices[p1][p2]

def area(a, b, c, d):
    total = (a - c) * (b - d)
    return total / 2

def interior(a, b, c, d):
    lattice_edges = lattice(a, b) + lattice(b, -c)
    lattice_edges += lattice(-c, -d) + lattice(-d, a) - 4
    return area(a, b, c, d) - lattice_edges / 2 + 1

interiors = [-1 for n in range(area(size, size, -size, -size))]

def isSquare(n):
    s = n ** .5
    return s == int(s)

t = time.time()
count = 0
for a in range(1, size):
    for b in range(a, size):
        for c in range(a, size):
            for d in range(b, size):
                i = interior(a, b, -c, -d)
                if interiors[i] == -1:
                    interiors[i] = isSquare(i)
                if interiors[i] == True:
                    x = 1
                    if not a == b:
                        x <<= 1
                    if not a == c:
                        x <<= 1
                    if not b == d:
                        x <<= 1
                    count += x

print (count)

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
