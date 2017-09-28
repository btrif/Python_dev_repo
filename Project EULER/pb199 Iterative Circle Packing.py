#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Sun, 17 Sep 2017, 19:50
#The  Euler Project  https://projecteuler.net
'''
Iterative Circle Packing            -       Problem 199

Three circles of equal radius are placed inside a larger circle such that each pair of circles
is tangent to one another and the inner circles do not overlap.
There are four uncovered "gaps" which are to be filled iteratively with more tangent circles.


At each iteration, a maximally sized circle is placed in each gap,
which creates more gaps for the next iteration.
After 3 iterations (pictured), there are 108 gaps and the fraction of the area
which is not covered by circles is 0.06790342, rounded to eight decimal places.

What fraction of the area is not covered by circles after 10 iterations?
Give your answer rounded to eight decimal places using the format x.xxxxxxxx .


'''
import time
from math import sqrt, pi
from gmpy2 import comb
from itertools import combinations
from copy import deepcopy

# http://www.sciencedirect.com/science/article/pii/S0925772102000998
# https://en.wikipedia.org/wiki/Circle_packing_theorem
# https://theses.lib.vt.edu/theses/available/etd-05082008-175931/unrestricted/draft.pdf
# http://www.grasshopper3d.com/forum/topics/circle-packing-in-grasshopper-of-fixed-radius
# https://books.google.ro/books?id=38PxEmKKhysC&pg=PA293&lpg=PA293&dq=Iterative+Circle+Packing&source=bl&ots=z20FpIUJAS&sig=v75cx2IKeE-akKryzqSzL9lIe7c&hl=en&sa=X&ved=0ahUKEwic7JLsnrbSAhXsCJoKHZrxAuk4ChDoAQgoMAY#v=onepage&q=Iterative%20Circle%20Packing&f=false

# ASTA-I BAZA , Cu astea se rezolva  :
# https://en.wikipedia.org/wiki/Descartes%27_theorem
# https://brilliant.org/wiki/descartes-theorem/
# https://www.youtube.com/watch?v=_bXpkABpAFA

def get_k4( rad_array ):
    # compute_circle_radius_between_three_circles
    ''':Description: Based on the formula :

        .. math::           $ k_4 = k_1 + k_2 + k_3 \pm 2 \sqrt{k_1k_2 +k_1k_3+k_2k_3} $

        where k is the curvature and radius  r is :
         .. math::            $ r = \pm 1/k $

        :param rad_array: array, list, with 3 elements representing the radius of the three circles
        :param r0: int, radius of the biggest circle, for a circle which contains the other ones  curvature k is negative,
            therefore we put radius r as negative
        :param r1: int
        :param r2: int
        :return: the radius of the 4-th circle which is in between them     '''

    r0, r1, r2 = rad_array
    k0, k1, k2 = 1/r0, 1/ r1, 1/r2
    k4 = k1 + k2 + k0 + 2 * sqrt( k0*k1 + k0*k2 + k1*k2 )
    return 1/k4

# @2017-09-17,, 12:45    Mda, folosesc formula gresit !!! I'm tired'

# print('\n--------------------------TESTS------------------------------')
# t1  = time.time()
#
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,  Using Descartes Theorem  ===============\n')
t1  = time.time()

def Iterative_circle( iterations) :
    r = lambda k :   ( k *( 3 - 2 * sqrt(3) ) )
    a0 = -1
    b0 = r(a0)
    print('Radius of the basic 3 circles : \t ', b0 )

    print('compute_circle_radius_between_three_circles :\t',  get_k4( [-1 , b0, b0 ]) )
    print('compute_circle_radius_between_three_circles :\t',  get_k4( [b0 , b0, b0 ] ) )

    print('---'*10, '\n')
    ## Initial Array Vector
    print('--- STEP 1 --- INITIALIZATION -------------')

    Arr_0 = [a0, b0, b0, b0 ]
    print('Initial State Vector, Level 0 Array : \t', Arr_0 ,'\n' )
    # print(comb(8 , 3) )

    B0 = list(combinations( Arr_0, 3) )
    ARR = Arr_0[:]
    Arr_1 = []
    for i in B0 :
        Arr_1.append( get_k4(i) )
        # print('B0 circles  =    ' ,i ,'   ;       C  radius = ' , get_k4(i) )

    print ('\nArr_1 computed LEVEL 1 array : \t', Arr_1 )

    Area =  (3* pi * b0**2 )
    print('LEVEL 0 Initial Filled  Percent Area = ',  Area  / (pi * a0**2) )
    Mem =[ [   Arr_1[0] , ( a0, b0, b0 ) ] ,  [   Arr_1[0] , ( a0, b0, b0 ) ] ,  [   Arr_1[0] , ( a0, b0, b0 ) ] ,  [ Arr_1[3] , ( b0, b0, b0) ] ]
    for J in Mem : Area += pi*J[0]**2
    print('LEVEL 1 Covered  Area = ', Area)
    print('LEVEL 1 Initial Filled  Percent Area = ',  Area  / (pi * a0**2) )
    print('Mem :\t  ',Mem,'\n')
    level = 2
    for u in range(iterations-1) :
        print('\n--------------    LEVEL ' + str(level) +'   ----------------\n')
        new_Mem = []
        scnt = 0
        for cnt, T in enumerate(Mem) :
            Comb = list (combinations( T[1], 2))
            # print(str(cnt+1)+'.     ', T , '      ', Comb)
            for  Q in  Comb :
                scnt +=1
                new_T = list(Q) + [ T[0] ]
                new_rad = get_k4(new_T)
                new_Mem.append( [ new_rad , tuple(new_T)]  )
                # print(str(scnt)+'.         key = '  ,T[0],'          new vector =  ', new_T, '        new rad = ', new_rad)
                Area += pi* new_rad**2
        Mem = deepcopy(new_Mem)
        print('\n' , len(Mem)  ,Mem[:30])
        print(' Cumulative Filled Area = ', Area,'      AREA FILLED PERCENT = ', Area / (pi * a0**2)  , '     Gaps Area = ',  round(1- (Area / (pi * a0**2)) ,8) )
        level+=1

    gapsArea = round( 1- (Area / (pi * a0**2)), 8)
    return print('\nArea not covered by circles ( Gaps Area ) = ', gapsArea )      # Area not covered by circles ( Gaps Area ) =  0.00396087

# Iterative_circle(10)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  Descartes  --------------------------')
t1  = time.time()


# ==== Thu, 15 May 2014, 18:47, ChopinPlover  aka Meng-Gen, Taiwan
# Descartes' theorem gives all.

from math import sqrt
import sys

class Problem():
    def solve(self):
        k = 1 + 2 / sqrt(3)
        uncovered_area = 1 - 3 * (1/k)**2
        stack = [(-1, k, k), (k, -1, k), (k, k, -1), (k, k, k)]
        for i in range(10):
            next_stack = []
            for k1, k2, k3 in stack:
                k4 = self.get_k4(k1, k2, k3)
                next_stack += [(k1, k2, k4), (k2, k3, k4), (k3, k1, k4)]
                uncovered_area -= (1/k4)**2
            stack = next_stack
            print(uncovered_area)

    def get_k4(self, k1, k2, k3):
        return k1 + k2 + k3 + 2*sqrt(k1*k2 + k2*k3 + k3*k1)


problem = Problem()
problem.solve()



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  soddy circles --------------------------')
t1  = time.time()

# === Mon, 5 Aug 2013, 20:23, ytsr, Python, china
# now using soddy circles. takes 0.5s
# previously, without using soddy circles, takes about 3 hours in matlab...

def Euler199_SoddyCircle(r1,r2,r3,n):
    global area
    e1 = 1/r1[0]*r1[1]
    e2 = 1/r2[0]*r2[1]
    e3 = 1/r3[0]*r3[1]
    ea = (e1+e2+e3)+2*sqrt(e1*e2+e2*e3+e1*e3)
    eb = (e1+e2+e3)-2*sqrt(e1*e2+e2*e3+e1*e3)
    r4 = (min([abs(1/ea), abs(1/eb)]), 1)
    area += r4[0]**2
    if  n>0:
        Euler199_SoddyCircle(r1,r2,r4,n-1);
        Euler199_SoddyCircle(r1,r3,r4,n-1);
        Euler199_SoddyCircle(r3,r2,r4,n-1);


R = [(1,-1),(3/(3+2*sqrt(3)),1),(3/(3+2*sqrt(3)),1),(3/(3+2*sqrt(3)),1)]
global area
area = 3*R[1][0]**2
Euler199_SoddyCircle(R[0],R[1],R[2],9)
Euler199_SoddyCircle(R[0],R[3],R[2],9)
Euler199_SoddyCircle(R[0],R[1],R[3],9)
Euler199_SoddyCircle(R[3],R[1],R[2],9)
print('{:10.8f}'.format(1-area))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, Recursion + explicit cache , SUPER FAST   --------------------------')
t1  = time.time()

# === Wed, 18 Sep 2013, 05:25, bobrovsky.serj, Russia
# Recursion + explicit cache: less then 0.02 sec.

from math import sqrt

def euler199(cnt):
    cache = dict()

    def deeper(hole, cnt):
        if hole in cache:
            return cache[hole]
        c1, c2, c3 = hole
        # c1, c2, c3 and C are curvatures
        C = c1 + c2 + c3 + 2. * sqrt(c1 * c2 + c1 * c3 + c2 * c3)
        tot = 1. / (C * C)
        if cnt:
            cnt -= 1
            tot += deeper((C, c1, c2), cnt) + deeper((C, c1, c3), cnt) + deeper((C, c2, c3), cnt)
        cache[hole] = tot
        return tot

    cnt -= 1
    c1 = 1 + sqrt(4 / 3)
    tot = 1 - 3 / (c1 * c1) - deeper((c1, c1, -1.), cnt) * 3 - deeper((c1, c1, c1), cnt)
    return round(tot, 8)

print(euler199(10))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ==== Sat, 6 Sep 2014, 04:53, muffoosta
#
# I don't know any of these theorems. I did the geometry based on tangency and relative positions of the circles,
# then removing the positions through algebra and some head scratching left me with the relatively simple formula ' \
# for finding the inner circle radius. After that recursion finished it up.

def f(a, b, c):
    r = - 2 * ((a * b * c) ** 3 * (a + b + c)) ** .5
    r += a * b * c * (c * a + b * a + b * c)
    r /= (a * b) ** 2 + (a * c) ** 2 + (b * c) ** 2 - 2 * a * b * c * (a + b + c)
    return r


def rec(a, b, c, i):
    d = f(a, b, c)
    t = d * d
    if i > 1:
        t += rec(a, b, d, i-1)
        t += rec(a, c, d, i-1)
        t += rec(b, c, d, i-1)
    return t


x = f(-1, -1, -1)
r = 3 + rec(1, 1, 1, 10) + rec(1, 1, -x, 10) * 3

print(1 - r / (x * x))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,  Recursion, Descartes Theorem  --------------------------')
t1  = time.time()

# === Tue, 9 Sep 2014, 16:18, Skiracer, England
# This was OK once I found Descarte's theorem.

from math import pi, sqrt
def f(a,b,c):
	return a+b+c-2*(sqrt(a*b+b*c+a*c))

def area(k):
	return pi*(1/k)*(1/k)

total=0
def rec(a,b,c,m,depth):
	depth-=1
	global total

	if(depth==0):
		return
	m1=f(a,b,m)
	m2=f(b,c,m)
	m3=f(a,c,m)

	total=total+area(m1)+area(m2)+area(m3)

	rec(a,b,m,m1,depth)
	rec(b,c,m,m2,depth)
	rec(a,c,m,m3,depth)

largeCircle=sqrt(pi)
innerCircle=largeCircle/(3-2*sqrt(3))

depth=10
rec(largeCircle,innerCircle,innerCircle,f(largeCircle,innerCircle,innerCircle),depth)
total*=3
rec(innerCircle,innerCircle,innerCircle,f(innerCircle,innerCircle,innerCircle),depth)
total+=3*area(innerCircle)+3*area(f(largeCircle,innerCircle,innerCircle))+area(f(innerCircle,innerCircle,innerCircle))

print(1-total)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,  Recursion at the finest level  --------------------------')
t1  = time.time()

# === Sun, 10 Jul 2011, 18:27, MrDrake, New Zeeland
# Great problem once you know Descartes' Theorem!

def descartes(x):
    a, b, c=x
    return a+b+c+2*(a*b+b*c+c*a)**0.5

def f(x, n):
    if not n: return 0
    a, b, c = x
    d=descartes(x)
    return 1/d**2 +f ((a, b, d), n-1 ) +f((a, c, d ), n-1)+f ((b, c, d ) , n-1 )

k = 3 - 2*3**0.5

n = 10
digits = 8

print ( round(1-(3+3*f((k,1,1),n)+f((1,1,1),n))*k**2, digits) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7,  Recursion  --------------------------')
t1  = time.time()

# === Tue, 23 Apr 2013, 23:19, hackleberry, Germany
# Nice problem, my solution seems to be close to the standard, recursive one:

from numpy import pi, sqrt

def Afunc(k):
    ''' area of a circle. '''
    return pi/k**2

def k_big(k1,k2,k3):
    ''' compute inverse radius of circle touching three given ones.
        solution for smaller circle. '''
    return (k1+k2+k3) - 2*sqrt(k1*k2+k1*k3+k2*k3)

def k_small(k1,k2,k3):
    ''' compute inverse radius of circle touching three given ones.
        solution for larger circle. '''
    return (k1+k2+k3) + 2*sqrt(k1*k2+k1*k3+k2*k3)

def compute_subareas(k1,k2,k3,n):
    ''' given three inverse radii,
        compute new inverse radius and
        repeat recursively for each triple of touching circles. '''
    k = k_small(k1,k2,k3)

    A = Afunc(k)
    if n>0:
        for (k1_,k2_,k3_) in [(k1,k2,k),(k1,k3,k),(k2,k3,k)]:
            A += compute_subareas(k1_,k2_,k3_, n-1)

    return A

def solution(n):
    k1 = 1.0
    A_in = compute_subareas(k1,k1,k1, n-1)

    K = k_big(k1,k1,k1)
    A_out = 3*compute_subareas(k1,k1,K, n-1)

    A_covered = A_in + A_out + 3*Afunc(k1)
    return 1.0 - A_covered/Afunc(K)

solution(10)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

