#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @ Completed on Tue, 10 Oct 2017, 21:45
#The  Euler Project  https://projecteuler.net
'''
Inscribed circles of triangles with one angle of 60 degrees         -       Problem 195

Let's call an integer sided triangle with exactly one angle of 60 degrees a 60-degree triangle.
Let r be the radius of the inscribed circle of such a 60-degree triangle.

There are 1234 60-degree triangles for which r ≤ 100.
Let T(n) be the number of 60-degree triangles for which r ≤ n, so
T(100) = 1234       ,
T(1000) = 22767     , and
T(10000) = 359912       .

Find T(1053779).


'''
import time
from math import gcd

import math


def gcd3(x, y, z):
    return gcd(gcd(x, y), z)


def Heron_area_perimeter(a,b,c):
    ''' Returns the Heronian Area and the Perimeter of the triangle         '''
    s= (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**(1/2), s

def triangle_primitive_triplets_60_gen_NOTCORRECT(  ) :      # o(^_^)o #  Made by Bogdan Trif @ 2017-02-21, 16:10
    ##### 60 degree TRIANGLES GENERATOR
    # http://www.geocities.ws/fredlb37/node9.html
    ''':Description: GENERATOR for Triangle primitive triplets of 60 degrees
    :param up_lim: integer, the limit to which the sum of sides a,b,c is up to
    :return: the sides of the 60 degree triangle , p ,q, r   '''
    # cnt=0
    m, n = 1, 1
    while True :   # If needed we can set a limit based on m**2-n**2
        for n in range(1, m) :      ### range(1,m) as we need only p > 0 !!!!!!!!
            # if gcd(m,n)==1 and (m-n)%3 !=0  :         #!!!! if we omit the %3 condition we will get duplicates !!!
                a = 2*m*n + m**2
                b = 2*m*n + n**2
                c = m**2+n**2+m*n
                # cnt+=1
                # print(str(cnt)+'.         '  , a, b, c ,'       sum =',  a+b+c ,'            m,n =',m, n)
                yield a, b, c
        m+=1

def triangle_primitive_triplets_60_gen1(  ) :      # o(^_^)o #  Made by Bogdan Trif @ 2017-10-09, 23:10
    #####   60 degree TRIANGLES GENERATOR   ######
# https://en.wikipedia.org/wiki/Integer_triangle#Integer_triangles_with_a_60.C2.B0_angle_.28angles_in_arithmetic_progression.29
# Integer triangles with a 60° angle can also be generated by[34]
# {\displaystyle a=m^{2}-mn+n^{2}\,} a=m^2-mn+n^2 \,
# {\displaystyle b=2mn-n^{2}\,} b=2mn - n^2\,
# {\displaystyle c=m^{2}-n^{2}\,} c=m^2-n^2 \,
# with coprime integers m, n with 0 < n < m (the angle of 60° is opposite to the side of length a).
# From here, all primitive solutions can be obtained by dividing a, b, and c by their greatest common divisor
# (e.g. an equilateral triangle solution is obtained by taking m = 2 and n = 1, but this produces a = b = c = 3,
# which is not a primitive solution). See also [35][36]
# More precisely, If {\displaystyle m=-n\ (mod\ 3)} {\displaystyle m=-n\ (mod\ 3)},
# then {\displaystyle gcd(a,b,c)=3} {\displaystyle gcd(a,b,c)=3},
# otherwise {\displaystyle gcd(a,b,c)=1} {\displaystyle gcd(a,b,c)=1}.
# Two different pairs {\displaystyle (m,n)} (m,n) and {\displaystyle (m,m-n)} {\displaystyle (m,m-n)} generate the same triple.
# Unfortunately the two pairs can both be of gcd=3, so we can't avoid duplicates by simply skipping that case.
# Instead, duplicates can be avoided by {\displaystyle n} n going only till {\displaystyle m/2} m/2.
# Note that we still need to divide by 3 if gcd=3.
# The only solution for {\displaystyle n=m/2} {\displaystyle n=m/2} under the above constraints is
# {\displaystyle (3,3,3)\equiv (1,1,1)} {\displaystyle (3,3,3)\equiv (1,1,1)} for {\displaystyle m=2,n=1} {\displaystyle m=2,n=1}.
# With this additional {\displaystyle n\leq m/2} {\displaystyle n\leq m/2} constraint all triples can be generated uniquely.

    ''':Description: GENERATOR for Triangle primitive triplets of 60 degrees
    :param up_lim: integer, the limit to which the sum of sides a,b,c is up to
    :return: the sides of the 60 degree triangle , p ,q, r   '''
    cnt=0
    m, n = 1, 1
    while True :   # If needed we can set a limit based on m**2-n**2
        for n in range(1, m//2  ) :
            if gcd(m,n)==1 and (m-n)%3 !=0  :
                a =  m**2 - m*n + n**2
                b = 2*m*n - n**2
                c = m**2 - n**2
                cnt+=1
                g= gcd3(a,b,c)
                print(str(cnt)+'.         '  , a//g, b//g, c//g , '       gcd3 = ', gcd3(a,b,c),'       sum =',  a+b+c ,'            m,n =',m, n)
                yield a, b, c
        m+=1




def triangle_primitive_triplets_60_gen2(  ) :      # o(^_^)o #  Made by Bogdan Trif @ 2017-10-09, 23:45
    #####   60 degree TRIANGLES GENERATOR   #####
# https://en.wikipedia.org/wiki/Integer_triangle#Integer_triangles_with_a_60.C2.B0_angle_.28angles_in_arithmetic_progression.29
#     All integer triangles with a 60° angle have their angles in an arithmetic progression. All such triangles are proportional to:[6]
# {\displaystyle a=4mn\,} a=4mn \,
# {\displaystyle b=3m^{2}+n^{2}\,} b=3m^2+n^2\,
# {\displaystyle c=2mn+|3m^{2}-n^{2}|\,} c=2mn+|3m^2-n^2| \,
# with coprime integers m, n and 1 ≤ n ≤ m or 3m ≤ n.
# From here, all primitive solutions can be obtained by dividing a, b, and c by their greatest common divisor.

    ''':Description: GENERATOR for Triangle primitive triplets of 60 degrees
    :param up_lim: integer, the limit to which the sum of sides a,b,c is up to
    :return: the sides of the 60 degree triangle , p ,q, r   '''
    cnt=0
    m, n = 1, 1
    while True :   # If needed we can set a limit based on m**2-n**2
        for n in range(1, 3*m  ) :      ### range(1,m) as we need only p > 0 !!!!!!!!
            # if gcd(m,n)==1 and (m-n)%3 !=0  :         #!!!! if we omit the %3 condition we will get duplicates !!!
            a =  4*m*n
            b = 3*m**2 + n**2
            c = 2*m*n + abs( 3*m**2 - n**2 )
            cnt+=1
            g= gcd3(a,b,c)
            print(str(cnt)+'.         '  , a//g, b//g, c//g , '   gcd3 = ', gcd3(a,b,c),'       sum =',  a+b+c ,'            m,n =',m, n)
            yield a, b, c
        m+=1



def inradius( a, b, c ) :        # #o(^_^)o #  Made by Bogdan Trif @ 2017-10-09, 23:03
    ''' The Inradius of the circle of the Inscribed circle is given by the three bisectors of the triangle.
     There is a relation between Area A, radius r of the inscribed circle and perimeter p:
     r = 2A/ p . By using Heron's formula and having edges a,b,c we can calculate Area and use it
      to find the INRADIUS                                                  '''
    # H =Heron_area_perimeter(a, b, c)
    # A, s = H[0], H[1]
    # By algebraic manipulations we get the formula A = rs => r = A /s = sqrt( (s-a)(s-b)(s-c) / s ) =>
    # => r = s* sqrt( ( 1 - a/s)(1- b/s)(1 - c/s) )
    s = (a+b+c)/2
    return s*( math.sqrt( ( 1-a/s)*(1- b/s)*(1 - c/s) ))

print('test inradius : \t ',  inradius(7,13,15) )


print('\n--------------------------TESTS------------------------------')

def test_1():
    SET1 = set()
    TPT_60_1 = triangle_primitive_triplets_60_gen1(  )
    for i in range(10**2):
        Q = next(TPT_60_1)
        g = gcd3(Q[0], Q[1], Q[2])
        # print(Q, Q[0]//g, Q[1]//g, Q[2]//g)
        SET1.add( ( Q[0]//g, Q[1]//g, Q[2]//g ) )
    print('\nSET1 : ',len(SET1))


print('----------------------')
def test_2() :
    SET2 = set()
    TPT_60_2 = triangle_primitive_triplets_60_gen2(  )
    for j in range(10**2):
        O = next(TPT_60_2)
        g = gcd3(O[0], O[1], O[2])
        # print(O, O[0]//g, O[1]//g, O[2]//g)
        SET2.add( ( O[0]//g, O[1]//g, O[2]//g ) )

    print('SET2 : ',len(SET2))

# print( SET1.difference(SET2) )
# print( SET2.difference(SET1) )

print('\n========= FIRST SOLUTION =============== ')
# @2017-10-10 :00:00 - From these two tests we conclude that the triangle_primitive_triplets_60_gen1  is more efficient
# because it generates with 11 elements more on a 100 iteration generator

t1  = time.time()

def solution_inscribed_triangles(Lim):

    TRF= set()
    cnt = 0
    SCNT = 0
    for m in range(1, int(Lim*3.5) ) :
        if (m >= Lim/200 ) : m_lim = 300
        if (m >= Lim/100 ) : m_lim = 150
        if (m >= Lim/50 ) : m_lim = 75
        if (m >= Lim/20 ) : m_lim = 40
        if (m >= Lim/10 ) :  m_lim = 30
        if (m >= Lim/4  ) : m_lim = 15
        if m >= Lim/2 : m_lim = 6
        if m >= Lim : m_lim = 3
        if m >= Lim*2 : m_lim = 2
        else : m_lim = m//2
        # m_lim = m//2

        for n in range(1, m_lim) :
            # if gcd(m,n)==1  and (m-n)%3 !=0  :
                a =  m**2 - m*n + n**2
                b = 2*m*n - n**2
                c = m**2 - n**2
                cnt+=1
                if m%(10**4) == 0 :    print("cnt = " , cnt , "       m = " , m)
                if a != b :
                    g= gcd3(a,b,c)
                    ga, gb, gc = a//g, b//g, c//g

                    if inradius( ga, gb, gc ) <= Lim :
                        inrad = inradius(ga, ga, ga)
                        key = (ga+gb+gc+inrad)/inrad
                        if not key in TRF :
                            # print(str(cnt)+'.             m,n = ',m, n , '        ', ga, gb, gc , '       gcd3 = ', gcd3(a,b,c),'       sum =',  a+b+c)
                            TRF.add( key )
                            x=1
                            while inradius( ga*x, gb*x, gc*x ) <= Lim :
                                SCNT +=1
                                x += 1

    print('\nTRF : \n' , len(TRF))
    # print(TRF)
    return print('\nTotal triangles = ', SCNT)

# solution_inscribed_triangles(10**4)
# solution_inscribed_triangles(1053779)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)/60,6), 'min\n\n')

print('---------------SECOND SOLUTION , BETTER --------------------')
t1  = time.time()





t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()



def second_solution(Lim):
    cnt, SCNT = 0, 0
    mn = 0
    for m in range(1, int(Lim*3.5)  )  :
        for n in range(1, m) :      ### range(1,m) as we need only p > 0 !!!!!!!!
            if m*n > Lim*3.5 : break
            if gcd(m,n)==1 or (m-n)%3 ==3  :         #!!!! if we omit the %3 condition we will get duplicates !!!
                a = 2*m*n + m**2
                b = 2*m*n + n**2
                c = m**2+n**2+m*n
                cnt+=1
                if m%(10**4) == 0 : print("cnt = " , cnt ,"       m = " , m )
                if a != b :
                    g= gcd3(a,b,c)
                    ga, gb, gc = a//g, b//g, c//g

                    if inradius( ga, gb, gc ) <= Lim :
                        inrad = inradius(ga, ga, ga)
                        # if inrad < Lim :
                        #     if m*n > mn :
                        #         mn = m*n
                        #         print(str(cnt)+'.             m,n = ',m, n , '    mn =    ', m*n, '             ', ga, gb, gc , '       gcd3 = ', gcd3(a,b,c),'       inrad =',  inrad)
                        if m > Lim:
                            print(str(cnt)+'.             m,n = ',m, n , '    mn =    ', m*n, '             ', ga, gb, gc , '       gcd3 = ', gcd3(a,b,c),'       inrad =',  inrad)

                        x=1
                        while inradius( ga*x, gb*x, gc*x ) <= Lim :
                            SCNT +=1
                            x += 1

    return print('\nTotal triangles = ', SCNT)


# second_solution(10**4)
second_solution(1053779)                #       Total triangles =  75085391




t2  = time.time()
print('\nCompleted in :', round((t2-t1), 4), 's\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n---------- SOLUTION 1,  VERY ADVANCED , Many things to learn --------------------------')
t1  = time.time()

from math import sqrt
from itertools import count

def prob195():
  def isqrt(n):
    x = int(sqrt(n * (1 + 1e-14)))
    while True:
      y = (x + n // x) >> 1
      if y >= x:
        return x
      x = y

  def moebius_sieve(N):
    ret = [i for i in range(N + 1)]
    for i in range(2, N + 1):
      if ret[i] != i:
        continue
      for j in range(i, N + 1, i):
        if ret[j] > 0:
          ret[j] = -1
        elif ret[j] < 0:
          ret[j] = 1
      for j in range(i * i, N + 1, i * i):
        ret[j] = 0
    return ret

  def quadratic_curve_count_ab(N, a, b):
    """
    Return the number of (x, y) such that ax^2 + bxy <= N.
    Assume that a >= 1 and b >= 1.
    """
    assert(a >= 1 and b >= 1)
    v = isqrt(N // a)
    ret = 0
    for x in range(1, v + 1):
      n = N - a * x * x
      d = b * x
      ret += n // d
    return ret

  def quadratic_curve_sum_ab(N, a, b):
    """
    Return the \sum _{x=1} _{y=1} \frac{N}{(a*x*x+b*x*y)}

    Assume that a >= 1 and b >= 1.
    """
    assert(a >= 1 and b >= 1)
    if a + b > N:
      return 0

    v = int(max(1, (N // a) ** 0.333))
    ret = 0
    for i in range(1, v):
      ret += quadratic_curve_count_ab(N // i, a, b)
    if v > 1:
      ret -= (v - 1) * quadratic_curve_count_ab(N // v, a, b)

    for x in count(1):
      M = N // x
      ax = a * x
      if M < v * (ax + b):
        break
      k = (M - ax * v) // (b * v)
      for q in count(v):
        nk = (M - ax * (q + 1)) // (b * (q + 1))
        if k - nk <= 1 or nk <= 0:
          break
        ret += q * (k - nk)
        k = nk
      for y in range(1, k + 1):
        ret += M // (ax + b * y)
    return ret

  """
  10 ** 9: 143925152382, 1.384 sec.
  10 ** 10: 1738850045279, 5.146 sec
  10 ** 11: 20663619751288, 22.849 sec.
  10 ** 12: 242178734699119, 105.688 sec.
  10 ** 13: 2805126169645023, 507.452 sec.
  """
  N = 1053779
  M = isqrt(12 * N * N)

  ans = 0
  def S(M):
    ret  = quadratic_curve_sum_ab(M // 1, 1, 3)
    ret -= quadratic_curve_sum_ab(M // 3, 1, 3)
    ret += quadratic_curve_sum_ab(M // 3, 1, 1)
    ret -= quadratic_curve_sum_ab(M // 9, 1, 1)
    return ret

  v = isqrt(M)
  mu = moebius_sieve(v)
  for i in range(1, v + 1):
    if i % 3 != 0 and mu[i]:
      ans += mu[i] * S(M // (i * i))
  print(ans)

prob195()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

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
