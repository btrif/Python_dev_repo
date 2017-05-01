#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Sun, 19 Mar 2017, 10:44
#The  Euler Project  https://projecteuler.net
'''
Investigating progressive numbers, n, which are also square         -       Problem 141

A positive integer, n, is divided by d and the quotient and remainder are q and r respectively.

In addition d, q, and r are consecutive positive integer terms in a geometric sequence, but not necessarily in that order.

For example, 58 divided by 6 has quotient 9 and remainder 4.
It can also be seen that 4, 6, 9 are consecutive terms in a geometric sequence (common ratio 3/2).
We will call such numbers, n, progressive.

Some progressive numbers, such as 9 and 10404 = 102**2, happen to also be perfect squares.
The sum of all progressive perfect squares below one hundred thousand is 124657.

Find the sum of all progressive perfect squares below one trillion (10**12).

'''
import time, gmpy2
from math import sqrt, ceil, floor, gcd
from pyprimes import factorise
from itertools import combinations, permutations
import functools, operator
from decimal import *
getcontext().prec = 50

import numpy
def prime_sieve_numpy(n):                       ### o(^_^)o  FASTEST  o(^_^)o  ###  Highly Efficient !!!
    """ Input n>=6, Returns a array of primes, 2 <= p < n
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188 """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def pair_Factors(n):        # VERY EFFICIENT !!!! SUPER INTELLIGENT ALGORITHM
    todo, combis = [(n, 2, [])], []
    while todo:
        n, i, combi = todo.pop()
        while i * i <= n:
            if n % i == 0:
                combis += combi + [i, n//i],
                # todo += (n//i, i, combi+[i]),       # If needed only PAIRS (a,b) comment this line !!!
            i += 1
    return combis

def get_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''

    return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]

def binary_search(n, List):        # VERY FAST ALGORITHM
    ''':Description: Search for an element in the list and returns the index of it. If it not finds it returns
        the index of the element closest to its left, the smaller number.
    :param: **n**- integer, the number to find
                **List** - lst type, the list to search for
    :returns:   int, the index of the element
    '''
    left = 0
    right = len(List) -1

    while left <= right:
        midpoint = (left+right)//2
        if List[midpoint] == n: return midpoint
        elif List[midpoint] > n: right = midpoint-1
        else: left = midpoint+1
    if n > List[midpoint]: return midpoint
    else: return (midpoint-1)

def naive_gen(lim=100):
    P = [2,3,5,7]
    N = []

    for i in P:
        o=i
        while i < 100 :
            N.append(i)
            i*=o
    # print(N)

    for i in P :
        for j in N :
            if j%i != 0 :
                if i*j < 100 and i*j not in N :
                    N.append(i*j)
    N.sort()
    return N


def inverse_farey( n, max_ratio ):      ####  o(^_^)o  FASTEST  ( ͡° ͜ʖ ͡°)  ### !!! Best Farey Sequence
    ''':Description: Generates INCREASING FAREY SEQUENCE
        taken from http://pythonfiddle.com/farey-series-generator/
        Modified by Bogdan Trif @2017-02-28, 14:00     '''
    F , asc = [], True
    if asc:
        a, b, c, d = 0, 1, 1, n
    else:
        a, b, c, d = 1, 1, n-1, n
    i=1
#     print ("%d/%d" % (a,b),)
    while (asc and c <= n) or (not asc and a > 0):
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
#         print ("%d/%d" % (a,b),end=' ')
        if b/a <= max_ratio :
            F.append((b,a))
        i+=1
    return F

print(inverse_farey(18, 5 ) )

print('\n--------------------------TESTS------------------------------')

# SUMS as checks
#                 10^5: 124657
#                 10^6: 700738
#                 10^8: 171436696

t1  = time.time()


# @ 2017-02-25, 20:00 . This is tooooo SLOW !!!!
# A cannot relate on the ratio k, because I have irrational k like 4.44444444444444444444444
# Brute force attempt is really taking tooooo much
# Also other approach was not successful
#
# I NEEEEEED an insight !  Otherwise this problem is NOT SOLVABLE !!!!
# Imagine that until 10**4 I need 80 seconds . So probably for 10**6 I would need at least 10 hours !!!


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')


print('\n--------------------------TESTS------------------------------')



print('\n================  SECOND BRUTE FORCE   ===============\n')
t1  = time.time()

def yet_another_brute_force(up) :
    up_lim = up*2/3
    R = set([r**2 for r in range(1, int( up**(1/2)) )  if r**2 <= up_lim ] +
                [r**3 for r in range(2, int(up**(1/3)) ) if r**3 <= up_lim  ] +[ r**5 for r in range(2, int(up**(1/5)) ) if r**5 <= up_lim] )
    R = sorted(list(R))

    print(len(R),'\n' ,R[:100] ,'\n\n')
    S = set()
    for m in range(3 , up) :
    # for m in range(98640 , 98641) :
    # for m in range(200000 , up) :
        r_ind = binary_search(m//100, R  )
        if m < 100 : r_ind = 0
        # print(m, r_ind, R[r_ind])
        for r in R[r_ind:] :
        # for r in R :
            if r >= m : break
            n = m*m
            # k = ( gmpy2.mpq((n-r),(r*r)) ** (1/3) )
            k = pow (  ((n-r) /(r*r))  , 1/3  )
            if k >1 :
                d = r*k
                # if  r == 50625 and m== 98640  :
                #     print('k: ', k, '    r:', r ,'     d : ', d, round(d) , '     error d:',abs(d - round(d) ) ,' q: ' , d*k, '  n:',n , '   error n:', abs(n - round(n) ) )
                # if abs(d - round(d ) ) < 1e-10 :
                if abs(d - round(d ) ) < 1e-8 :
                    q = d*k
                    m2 = pow( (k**3*r**2+r) , 1/2 )
                    # if  r == 50625 and m== 98640  :
                    #     print('k: ', k, '    r:', r ,'     d : ', d, round(d) , '     error d:',abs(d - round(d) ) ,' q: ' , d*k, '  n:',n , '   error n:', abs(n - round(n) ) )
                    if abs(m - m2 ) < 1e-10 :
                    # if abs(n - round(n) ) < 1e-5 :
                        if gmpy2.is_square(round(n)) :
                            if m not in S : # and n < up**2 :
                                S.add(m)
                                d, q = round(d), round(q)
                                print( 'm='+str(m)+'.      r=',r, '     d=',d, '     q=' ,q , '  ; n=', round(n),'   ;     k=', k ,'     r=',get_factors(r), '    d=',get_factors(d) , '  ;   error m:', abs(m - m2 ) )

    print('\nElements : \t', S )

    return print('\nAnswer : \t', sum([i**2 for i in S]) )


# yet_another_brute_force(10**6)


def brute_force (up_bound) :
    S = 0

    for d in range( 2, up_bound ) :
        for r in range(d-1, 0, -1 ) :
            if d/r >12 : break
            n = d**3 /r + r
            if  (n**(1/2)) % 1 != 0 : continue
            if  (n**(1/2)) % 1 == 0 and n < up_bound**2 :
                q , k  = d**2//r , d/r
                S += n
                print('   r =  ',r , '     d=',d , '       q=',q , '     n=',n,'     ratio =', k ,'       r = ', get_factors(r))

    return print('\nAnswer : \t', S)

# brute_force( 10**6  )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60, 6), 'min\n\n')


print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()


def progressive_numbers(up) :
    up_lim = up*3//5
    # up_lim = up
    R = set([r**2 for r in range(2, int( up_lim**(1/2) ) )  if r**2 <= up_lim ]  )

    tmp=[]
    for n in range(2, 10**3) :
        for r in sorted(list(R)) :
            if  n* r <  up_lim :
                tmp.append(n*r)
    R |= set(tmp)
    R = sorted(list(R))
    print(len(R),  max(R) ,R[:50], R[-50::]  , '\n')

    S, cnt = 9, 1

    for d in range( 2, 7*up//8) :

    # for d in range( up*8//10,  up ) :
        if d% 10**4 == 0 : print(d)
        if gmpy2.is_prime(d) : continue
        if d <= 10**4 : f = d//12
        if  d > 10**4 : f = d//4
        if  d > 5*10**5 : f = d//1.6
        ind_r = binary_search(f, R)

        for r in R[ind_r:] :
        # for r in R :
            if r > d  : break
            if gcd (d , r) == 1 : continue
            n = d**3 /r + r
            if  (n**(1/2)) % 1 == 0 and n < up**2 :
                q , k  = d**2/r , d/r
                if q % 1 == 0 :
                    S += n
                    cnt+=1
                    print(str(cnt)+'.     r =  ',r , '     d=',d , '       q=',q , '     n=',n,'     ratio =', k ,'       r = ', get_factors(r),'     ' , S)

    return print('\nAnswer : \t', S )


# progressive_numbers( 10**6  )
# progressive_numbers( int((10**5)**(1/2) )+1  )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60, 6), 'min\n\n')


print('\n================  My SECOND SOLUTION,   ===============\n')
t1  = time.time()

def second_solution( lim ):
    S = 0
    cnt =  0

    for a in range(2, lim + 1 ):
        for b in range(1, a) :
            if gcd(a,b) == 1 :
                c= 1
                while 1 :
                    n = a**3*b*c**2 + b**2*c
                    if n > 10**12 : break
                    if gmpy2.is_square(n) :
                        r , d, q, k = c*b**2, a*b*c, a**2*c,  a/b
                        cnt+=1
                        S+=n
                        print(str(cnt)+'.     r =  ',r , '     d=',d , '       q=',q , '     n=',n,'     ratio =', k ,'       r = ', get_factors(r),'     ' , S , '        a,b,c = ',a,b,c)

                    c+=1
        if a%10**3 == 0 : print(a)

    return print('\nAnswer : \t', S)

# second_solution(10**4)              #       Answer : 	 878454337159

t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60, 6), 'min\n\n')

##### IDEAS #############
# ===== Sun, 4 Jan 2015, 04:10, dawghaus, USA
# n=dq+r
#
# Since r is the remainder we have r<d and, without loss of generality, we can assume d<q; that is, r<d<qr
# When I used the common ratio as drdr to get n=d(d**2/r)+r=(d**3/r)+r, the r in the denominator caused me a lot of grief.
# I decided to let the common ratio be represented by ab,GCD(a,b)=1.
#
# That leads to :
#       r=r
#       d=ar/b
#       q=a**2r/b**2
#
# Since GCD(a,b)=1 the equation for q tells us b**2|r and there exists an integer cc such that cb2=rc
#
# That gives,
#       d=abc
#       q=a**2c
#       n=a**3bc**2+cb**2 with GCD(a,b)=1,a>b,c≥1
#
# Since n<10**12,a<10**4, which provides a nice bound on a.
#
# On edit:  I notice 10^12 doesn't display properly.  How does one display a multi-digit exponent?
# On second edit:  Figured out how to display multi-digit exponents - uses braces; for example 10^{12}


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, 28 sec  --------------------------')
t1  = time.time()

# ==== Mon, 11 May 2015, 06:49 , squidaction, USA
# Here's my python code which ran in 24 seconds. Same basic algorithm as many of the others

from math import *
from math import gcd

def solution_1():
    MAX = 1e12

    sum = 0
    for a in range(1,floor(MAX**(1/3))):
         a3 = a**3
         for c in range(1, floor(sqrt(MAX/a3))):
            for b in range(1,a):
                    if gcd(a,b) > 1: continue
                    N = c*b*(c*a3+b)
                    if N > MAX: break
                    n = sqrt(N)
                    if floor(n) == n:
                            sum += N

    return print(sum)

# solution_1()

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n--------------------------SOLUTION 2,  6 sec --------------------------')
t1  = time.time()

# === Tue, 14 Jul 2015, 05:32, bukebuer, China
# Reached n=k**3*t ( c**3 + t) =m**2 as most people.
# Then using brute search, while having some generator techniques to accelerate the code.

import math
from itertools import takewhile, count

def f(k, t, c):
    return k*k*k * t * (c*c*c + t)

def ep141():
    N = 1e12
    s = set([])
    for k in takewhile(lambda k: f(k, 1, k+1) < N, count(1)):
        for t in takewhile(lambda t: f(k, t, t*k+1) < N, count(1)):
            for c in takewhile(lambda c: f(k, t, c) < N, count(t*k+1)):
                n = f(k, t, c)
                if n in s:
                    continue
                sn = int(math.sqrt(n))
                if sn*sn == n :
                    print (k*k*k*t*t, k*c*c, n)
                    s.add(n)
    return print('\nAnswer : \t',sum(s))

# ep141()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  3 sec,  inamori --------------------------')
t1  = time.time()

# ==== Sat, 28 Apr 2012, 14:36, inamori, Japan

from itertools import *
from math import sqrt
from fractions import gcd
import time

def div_pow(n, d):
    e = 0
    while n % d == 0:
        e += 1
        n /= d
    return e, n

def is_square(n):
    m = int(sqrt(n))
    return m * m == n

def has_square(n):
    squares = takewhile(lambda s: s <= n, (k * k for k in count(2)))
    return any(n % s == 0 for s in squares)

def divide_square_and_not(n, p0 = 2):
    if n == 1:
        return 1, 1
    else:
        for p in takewhile(lambda p: p * p <= n, count(p0)):
            if n % p == 0:
                e, m = div_pow(n, p)
                s, t = divide_square_and_not(m, p + 1)
                return p ** (e / 2) * s, p ** (e % 2) * t
        else:
            return 1, n

def f(t, p, u):
    return p * t ** 3 * (u ** 3 + p)

# solutions of am^2 = bu^3 + c (m <= M, u >= U)
def g(a, b, c, U, M):
    def gcd2(a, c):
        d = gcd(a, c)
        s, t = divide_square_and_not(d)
        return s * t

    def g2(a, b, c, U, M):
        for u in takewhile(lambda u: b * u ** 3 + c <= a * M, count(U)):
            rhs = b * u ** 3 + c
            if rhs % a == 0 and is_square(rhs / a):
                yield int(sqrt(rhs / a)), u

    d1 = gcd(a, b)
    d = gcd(d1, c)
    if d > 1:
        return g(a / d, b / d, c / d, U, M)

    if d1 > 1:
        return ()

    d2 = gcd2(a, c)
    if d2 > 1:
        return ((m, u * d2) for m, u in
                    g(a / d2, b * d2 * d2, c / d2, U / d2, M))

    d3 = gcd2(b, c)
    if d3 > 1:
        return ((m * d3, u) for m, u in g(a * d3, b / d3, c / d3, U, M / d3 ** 2))

    return g2(a, b, c, U, M)

def gen_progressive_perfect_squares(N):
    for t in takewhile(lambda t: f(t, 1, t + 1) < N, count(1)):
        if has_square(t): continue
        for p in takewhile(lambda p: f(t, p, p * t + 1) < N, count(1)):
            for m, u in g(1, p * t ** 3, p * p * t ** 3, p * t + 1, N):
                if t * p < u:
                    print ( t, p, m, u, m * m )
                    yield m * m


N = 10 ** 12
# print (sum(set(gen_progressive_perfect_squares(N))))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  15 sec --------------------------')
t1  = time.time()

# ==== Mon, 4 Mar 2013, 12:28, tom.wheldon, England
# Same analysis as quite a few others.

def solution_4():
    limit = int(1e12)
    squares = {n*n for n in range(1000000)}

    ans = 0
    for s in range(2,10001):
        sc = s**3
        for t in range(1,s):
            if t*sc + t*t >= limit:
                break
            if gcd(s,t) > 1:
                continue
            for k in range(1, 400000):
                n = k*k*sc*t + k*t*t
                if n >= limit:
                    break
                if n in squares:
                    ans += n
    return print(ans)

# solution_4()

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
