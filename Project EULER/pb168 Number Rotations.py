#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Tue, 7 Mar 2017, 22:00
#The  Euler Project  https://projecteuler.net
'''
                                                    Number Rotations        -       Problem 168

Consider the number 142857. We can right-rotate this number by moving the last digit (7)
to the front of it, giving us 714285.

It can be verified that 714285=5×142857.

This demonstrates an unusual property of 142857: it is a divisor of its right-rotation.

Find the last 5 digits of the sum of all integers n, 10 < n < 10**100, that have this property.

'''
import time, itertools
import gmpy2

def circulate_number(A):
      tmp=[]
      for v in range(len(str(A))):
            a , i , s =  str(A), len(str(A)), ''
            for c in range(i):
                  #print(a[(v+c) % j] ,end='  ')
                  s += str(a[(v+c) % i])
            #return s
            tmp.append(int(s))
            #print(s)
            v+= 1
      return tmp #print(tmp)

def right_rotate_number(n):
    n = str(n)
    return int(n[-1]+n[:-1])

def left_rotate_number(n):
    n = str(n)
    return int( n[1:]+n[0] )

print(circulate_number(142857))
print('is_prime :\t',gmpy2.is_prime(142857))
print('right_rotate_number Test :', right_rotate_number(142857142857142857))
print(714285714285714285 / 142857142857142857)

#### IMPORTANT - THE IDEA OF THE PROBLEM  ::  #############
# If we take  102564 and we right-rotate it ==> 410256  = 102564 * 4
# Let's multiply it step by step :
# 4 * 4 = 16                       => 6 keep 1        <<-- Start
# 6 * 4 = 24 + keep 1 = 25 => 5 keep 2
# 5 * 4 = 20 + keep 2 = 22 => 2 keep 2
# 2 * 4 =  8 + keep 2 = 10 => 0 keep 1
# 0 * 4 =  0 + keep 1 = 1 =>  1 keep 0        <<-- End
# 1 * 4  = 4                        => 4 keep 0
# 4 * 4 = 16    an we come back to the beginning ==> nr is : 410256

# Therefore the number is : 410256
# The trick is that this sequence keeps reapeating itself because we have again the 4 which multiplied by 4
# give 16 ==> 6 keep 1 ...and so on and so on :
# Therefore all the numbers of the type 102564, 102564.102564, 102564.102564.102564 repeat themselves
# All we need to do for this problem is to see how many are in 10**100 => digit length = 6 => 100 //6  = 16





print('\n-------------------------BRUTE FORCE  TESTS------------------------------')
t1  = time.time()


# CHECK :



S1, S2, S3, S4 = 0, 0, 0, 0
for i in range(1, 10 ):
    # print(i , str(i)*5 )
    S1 += int(str(i)*2 )
    S2 += int(str(i)*3 )
    S3 += int(str(i)*4 )
    S4 += int(str(i)*5 )

print(S1, S2, S3, S1+S2+S3+S4)

def brute_force_testing() :

    SUMo = 0
    Six = []
    cnt = 0
    for n in range(10, 10**6) :
        a = right_rotate_number(n)
        if  a%n == 0  :
            if  len( set([int(i) for i in str(n)] ) ) > 1 :
                Six.append(n)
                cnt+=1
                print (str(cnt)+'.      n=', n,'     a=', a , '     a / n=', a//n  )
            if len(set(list(str(n))) ) == 1:
                SUMo+= n

    print('\nPartial Sum : \t', SUMo,'\n')

    O = [ int( (str(i)*5 ) ) for i in range(1,10) ]
    print('One digits : \t' , O )
    print('6-digits :\t', Six )

    lim=100
    one_digits = (lim-6) * sum(O) + SUMo
    six_digits = (lim//6  ) * sum(Six)

    print('\nOne digits : ',one_digits  )
    print( '6-digits  : \t', six_digits )

    return print('\nAnswer :\t', (one_digits + six_digits  )%10**5 )

# brute_force_testing()

# TRIED : 40706, 40701

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

def compute_ones(lim, last_dig ) :
    # S = 0
    Q = 0
    # for i in range(2, lim+1 ):
    #     for j in range(1, 10) :
    #         # print( int(str(j)*i)  )
    #         S+=int(str(j)*i)
        # print(str(i)+'.      S : ',S)
    for i in range(2, last_dig+1 ):
        # print('Q : ',Q)
        for j in range(1, 10) :
            Q+=int(str(j)*i)

    if  lim != last_dig :
        Q = Q + (lim-last_dig)* sum([  int(str(i)*5) for i in range(1,10)  ])

    return Q%(10**last_dig ) #, S%(10**last_dig)


def generate_number_rotations(up_lim ) :
    L=[]
    for x in range(1, 10) :
        for m in range(1, 10) :
            T = []
            keep2, keep1 = 0, 0
            a = x*m
            keep1 = (a - a%10) + keep2
            T.insert( 0, a%10   )
            keep2 = keep1//10
            # print((x, m)  , T, '           ' ,  a%10  ,  '        keep2 =',keep2, '       multiplier : ',m)
            for j in range(up_lim+6) :
                a = a%10*m + keep2
                keep1 = (a - a%10) + keep2
                T.insert( 0, a%10   )
                keep2 = keep1//10
                # print(i  , T, '          a%10= ' ,  a%10  ,  '        keep2 =',keep2, '       multiplier : ',m)

            pattern = T[-6::]
            # print('\ncomplete sequence : \t',T, '     ', pattern)
            for k in range(len(T)-2, 2, -1 ):
                if pattern == T[k-6:k] :
                    n =   int(''.join( str(i) for i in  T[k:]))
                    p = left_rotate_number(n)
                    # print( T[k-6:k] , 'the number is : ', T[k:], '  n= '  ,n, '   p=' ,p, '   mod =' ,n%p )
                    if n%p == 0   and len(str(p)) == len(str(n)) and len(set(T[k:])) > 1 :
                        L.append(p)
                        break         # If I do not Interrupt I obtain directly all the numbers and there is no need to
                                                # count again the repeats if the length is < 50

    return L

A = generate_number_rotations(up_lim= 100 )
print('\nNumber of elements : ' , len(A),'     Their Sum mod: \t' ,sum(A)%10**5 , '\n', A[-5::] ,'\n' )

OTHER = 0
for u in A:
    repeats = 100 // len(str(u))
    # print(u,'       ', len(str(u)) ,'            ',repeats)
    OTHER += repeats * u

print('SUM of ALL the repeats : \t ',OTHER%(10**6) )

ONES = compute_ones(100, 5)
print('compute_ones : \t', ONES)

print('\nAnswer : \t',  ( ONES+OTHER )%10**5  )         #       Answer : 	 59206

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

############## SOME GOOD IDEAS ##############
# ==== Thu, 21 Nov 2013, 19:56, dcterr, USA
# This was a very frustrating problem! The basic idea is rather clear.
# Cyclic numbers (i.e. numbers with the specified property) include all numbers of the form n=k(10**d−1)/g,
# where g is an integer from 3 to 100 coprime to 10, d is the multiplicative order of g modulo 10,
# and k is an integer less than g such that n has d digits. However, we need to be careful!
# We must not overcount by adding cases we've already looked at, i.e. cases in which k and g are not coprime.
# We also must include cases involving repeating strings of digits of the above form, i.e. numbers of the form
# n= k*( 10**rd+10**((r−1)d)+⋯+10**d + 1)/g, where r is an integer greater than 1 such that n has at most 100 digits.
# Finally we must include all repdigits, which are trivially cyclic with multiplier 1.
# If we do all these things, we get the right answer.


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# === Wed, 24 Feb 2016, 11:27, jmarot, France


def develop(p,q):
    # returns 2 lists: nonperiodic + periodic part of p/q
    D=[]
    R=[]
    while p not in R:
        D.append((10*p)//q)
        R.append(p)
        p=(10*p)%q
    a=R.index(p)
    return D[:a],D[a:]

funda=list(range(1,10)) # fundamental, i.e. nonperiodic solutions
for k in range(2,10):
    for f in range(k,10):
        S,P=develop(f,10*k-1)
        if S==[] and P[0]!=0:
            funda.append( sum( P[k]*10**(len(P)-k-1)  for k in range(len(P))) )

# Now each fundamental solution can be repeated as many times as we want, not exceeding 100 digits
S=0
digits=100
for f in funda:
    l=len(str(f))
    k=digits//l
    i0=2 if l==1 else 1
    for i in range(i0,k+1):
        n=int(i*str(f))
#         print(n)
        S=S+n
print(S%100000)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n-----------------SOLUTION 2, CHINESE REMAINDER THEOREM , SUPER ELEGANT SOLUTION  --------------------------')
t1  = time.time()

# ==== Sat, 31 Aug 2013, 23:08, Oren, USA
# If x = 10*y + z then the rotation is r(x) 10^(n-1)*z + y where n=#digits in x.
# Thus (10^(n-1)-a)*z = (10a-1)*y where a = r(x)/x.
# For each value of a and n, this can be solved with the Chinese remainder theorem.
# Only solutions with 1 <= z <= 9 and 10^(n-2) <= y < 10^(n-1) are feasible.

from math import ceil, gcd
from functools import reduce

def cyclic_numbers(N):
    '''A generator of numbers who are divisors of their right-rotation in [10,10**N).'''
    for n, a in ((n, a) for n in range(2, N + 1) for a in range(1, 10)):
        U, V = 10 ** (n - 1) - a, 10 * a - 1
        d = gcd(U, V)
        u, v = U // d, V // d
        c_min, c_max = int(ceil(max( 1 / v, 10**(n - 2) / u))), min(9 // v, (10 ** (n - 1) - 1) // u)
        for c in range(c_min, c_max + 1):
            yield c * (10 * u + v)

'''Sum the r-moduli of all numbers of interest in [10,10**N).'''
sum_cyclic = lambda N, r: reduce(lambda x, y: (x + y) % r, cyclic_numbers(N))


print(sum_cyclic(100, 10**(5)))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   WOW--------------------------')
t1  = time.time()

# ==== Wed, 25 Sep 2013, 20:36, ChopinPlover, China
# The number 10**100 is a good hint.

def main():
    sum = 0
    for k in range(1, 100):
        for d in range(1, 10):
            for y in range(1, 10):
                x, r = divmod((10**k - d)*y, 10*d - 1)
                if r != 0 or x < 10**(k-1):
                    continue
                sum += 10*x + y
    print(sum % 10**5)

main()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# === Sun, 3 Nov 2013, 12:21, Richie, France

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 02 23:54:04 2013
author : Richie64
PE168
"""
from math import gcd

S=0
for k in range(2,101):
    for d in range(1,90):
        neuf = 10**k-1
        if neuf % d ==0:
            for delta in range(1,10):
                n = (neuf // d)*delta
                if  delta <= d and d < 10*delta and gcd(delta,d) ==1:
                    if (neuf*(n//10)) % n == 0 :
                        S+=n
print( "S = ",S % 10**5)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# ==== Sat, 25 Jan 2014, 16:41, Nicolas Patrois, France

nb=100
somme=0

for n in range(1,nb):
  for k in range(1,10):
    gauche=10**n-k
    for a in range(1,10):
      b,r=divmod(a*gauche,10*k-1)
      if k==1:
        somme+=int(str(b)+str(a))
        somme%=10**5
      else:
        if r==0 and b>=10**(n-1):
          somme+=int(str(b)+str(a))%10**5
          somme%=10**5

print(somme%10**5)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   must study it --------------------------')
t1  = time.time()

# ==== Mon, 19 Oct 2015, 15:01, PhilLeTaxi, France
# Solution very closed from the one of Ido Nahshon here above
# but more compact, and then slightly faster,
# as I noticed that the ratio cannot be less that the last digit.

def solver():
    somme = 0
    for n in range(1,100):
        puis = 10**n
        for a in range(1,10):
            tmp = puis - a
            div = (10*a) - 1
            for d in range(a,10):
                if (d*tmp) % div == 0:
                    num = ((d*tmp*10) // div) + d
                    somme = (somme + num) % 100000
    print("Somme :",somme)
solver()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()

# ====Sun, 19 May 2013, 22:01, tom.wheldon, England
# It took me far too long to solve this problem.  I immediately recognised 142857
# as the period of decimal 1/7, which sent me up a blind alley involving primitive roots and other bits of number theory.
# I eventually saw the 'obvious' solution and put it on one side until I felt like doing something easy.
# Of course, when I took it up again today I got the wrong answer because I'd forgotten part of the solution
# I'd worked out earlier, that if 142857 is a solution so is 142857142857 etc. All very frustrating.
# Python - runs in 2ms.


total = 0
for m in range(2,10):
    for last in range(m,10):
        n = d = last
        carry = 0
        for i in range(1,100):
            prod = d*m + carry
            if prod == last:
                break
            else:
                carry,d = divmod(prod,10)
                n += d*10**i
        total += n*(100//i)

ones = 11111*96 + 1233
total += ones*45

print(total%10**5)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8,   must study it --------------------------')
t1  = time.time()

# ====Thu, 4 Jul 2013, 19:18, merolish, USA

val = 0
for n in range(1, 10):
    for d in range(1, 10):
        pt = 10
        cur = n * d
        while pt < 10 ** 100:
            a = cur % pt + pt * n
            b = cur % pt * 10 + n
            if b * d == a and b >= pt:
                val += b
            cur = (cur * 10 + n) * d
            pt *= 10
print(val % 100000)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


