#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Sun, 3 Dec 2017, 23:55
#The  Euler Project  https://projecteuler.net
'''
                    Primitive Triangles     -       Problem 276

Consider the triangles with integer sides a, b and c with a ≤ b ≤ c.
An integer sided triangle (a,b,c) is called primitive if gcd(a,b,c)=1.

How many primitive integer sided triangles exist with a perimeter not exceeding 10 000 000 (10**7) ?
'''

import time

import sys
import functools, operator, itertools



def gcd(a, b):      # GCD
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a


def gcd3(a, b, c):
    return gcd(gcd(a, b), c)

def get_factors_2(n):       # From mhb038, England, Euler Forum
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

def _prod(L):
    s = 1
    for i in  L:
        s*= i
    return s


def custom_sum( a, d, n) :
    ''' :Description: Makes the custom summation of the form :
        a + (a+d) + (a+2d) + (a+3d) + ...
        which is a constant increasing sequence :

            :**Sigma { k=0, n-1  } ( a + kd) =  n/2 * ( 2*a + (n-1)*d )**:

        :Example: : [ 4, 10, 16, 22, 28 ], Sum = 52. We see that first term a=4
        difference d = 6, and there are 5 terms, n = 5

    :param a: int, first term
    :param d: int, difference between terms
    :param n: int, numbers of terms in sequence
    :return: sum                    '''

    return ( 2*a + (n-1)*d  ) * n //2


print('\n--------------------------TESTS------------------------------')
t1  = time.time()


def almost_brute_force(perim) :
    cnt, p = 0, perim
    for a in range(2, p//3+1) :
    # for a in range(30, 31) :
    #     print("\n ========= size " , a, " ========== " )
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
                F =  list(set(get_factors_2(g)))
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

    print ('\n\nAnswer almost_brute_force : \t', cnt)
    return cnt

# almost_brute_force(10**3)




print('\n------------------------------')

def ones(lim):
    cnt = 0
    for b in range(1, lim//2) :
        for c in range(b, lim-b ) :
            if 1+b ==c :
                cnt +=1
                print(str(cnt)+'.     ' ,  1, b, c )

# ones(100)


def brute_force_GCDs(up, a) :
    cnt, gcds, colinear = 0, 0, 0
    # for a in range(1, up) :
    all_colinear = 0

    h = 0
    for b in range(a, up) :
        if a+b > 2*up / 3 : break

        # print('-----------')
        for c in range(b, up) :
            # if a+b ==c : continue
            if a+b+c > up : break

            if a+b == c : all_colinear +=1

            if gcd3(a,b,c) != 1 :
                gcds +=1
                h +=1
                if a+b ==c :    colinear +=1
                print('a, b, c  =  ', a, b, c,'       h=', h ,'        gcds=', gcds ,'      colinear =  ', colinear,'      all_colinear =  ', all_colinear )

            if gcd3(a,b,c) == 1  and a+b != c  :
                # print(str(cnt )+'.      ', a, b, c)
                cnt+=1

    print('\ngcds = ', gcds, '           colinear =  ' , colinear ,'          ', cnt - gcds + colinear ,'      all_colinear =  ', all_colinear)
    print('\nbrute_force_GCDs   = ', cnt )

# brute_force_GCDs(10**3, 11   )



def brute_force_count_ALL(up) :
    cnt = 0
    for a in range(2, up) :
        for b in range(a, up) :
            if a+b > 2*up / 3 : break

            # print('-----------')
            for c in range(b, up) :
                # if a+b ==c : continue
                if a+b+c > up : break
                cnt +=1
                # print( str(cnt) +'.      a, b, c  =  ', a, b, c)


    print('\nbrute_force_ALL   = ', cnt )

# brute_force_count_ALL(10**3 )

print('\n------------------   Brute_force_count CORRECTLY   -------------')
t1  = time.time()

def BF(up) :
    cnt  = 0
    # for a in range( 209 , 209 + 1) :
    for a in range( 1 , up + 1) :
        a_cnt = 0
        if a > up/3 : break

        # sys.stdout.write('\r' + str(a) +'              '+  str(round((time.time() - t1),2)) +'  sec'   )   # Font Segoe UI Semibold
        for b in range(a, up) :
            if a+b > 2*up / 3 : break
            for c in range(b, a+b) :
                if a+b+c > up : break
                if gcd3(a,b,c) == 1 and a+b != c :
                    cnt +=1
                    a_cnt +=1
        print('a = ' , a ,'       a_cnt= ', a_cnt , '         a, b, c  =  ', a, b, c  ,'         cnt= ', cnt)

    print('\n\nBF  Primitives Triangles = ', cnt  )
    return cnt

BF(10**1)



t2  = time.time()
print('\nCompleted in :', round((t2-t1) , 2), 's\n\n')

print('\n================  My FIRST SOLUTION,  Must correct it !!  ===============\n')
t1  = time.time()



def compute_gcds(a, lim ) :

    F =  get_factors_2(a)
    # print(F)
    c = lim//2 - a      # here we get the maximum c for which we should exclude. Example
    print('\n------------------- c = ', c)      # (8, 42, 50) => 42 is the last element for which we compensate



    # CASE 1 , primes or primes to powers
    if len(F ) == 1 :

        f = min(F)
        up = ( lim -2*a - a  ) // f +1

        down = 2 - up%2
        nr_terms = (up + down%2)//2

        # here we exclude the colinears
        colinear = ( ( c - c%f - a ) // f ) +1

        substract_gcds = custom_sum(down , 2 , nr_terms  )

        if a > lim//4 : colinear = 0


        print('case 1 :  ', ' up= ', up, ' down= ', down , ' nr_terms=', nr_terms  , ';   substr_gcd= ',substract_gcds , ' ;   colinear = ', colinear, '    Total =  ', substract_gcds-colinear )
        return substract_gcds -colinear

    # CASE 2 , composite numbers
    if len( F ) > 1 :
        Sum, colinear = 0 , 0
        for i in range(1, len(F) +1 ) :
            C = itertools.combinations( F, i )
            for j in C :
                f = _prod(j)
                colin =  ( c - c%f - a ) // f  + 1

                up = ( lim -2*a - a  ) // f  + 1
                down = 2 - up%2
                nr_terms = (up + down%2)//2
                print(' f = ', f,'        up =', up, '        down =', down ,'        nr_terms =', nr_terms, '         colin = ', colin )

                substract_gcds = custom_sum(down , 2 , nr_terms  )

                if i%2 == 1 :
                    Sum += substract_gcds
                    colinear += colin
                if i%2 == 0 :
                    Sum -= substract_gcds
                    colinear -= colin

        if a > lim//4 : colinear = 0

        print('case 2 :     Sum = ', Sum ,'        colinear = ', colinear , '    Total =  ', Sum-colinear)

        return Sum - colinear



# print(  compute_gcds( a=209 , lim = 10**3        ) )

print('\n----------------------------')



def Primitive_integer_sided_triangles( lim ) :
    ALL, colinear =  0, 0

    ones = custom_sum(2, 2, (lim-2)//2 ) - (lim-2)//2
    # print('ones = ' , ones)

    for a in range(2, lim //3+1) :
    # for a in range( 11, 11 +1 ) :

        max_c = lim - 3*a +1
        min_c = 2 - max_c%2
        nr_terms = (max_c + min_c%2)//2

        ###### ALL CASES --> Calculating all possible triangles, including (1,1,2) or (2,3,5)

        add = custom_sum(min_c , 2, nr_terms  )

        ###### ALL COLINEARS , including PRIMITIVES and GCDs
        col = lim//2 - 2*a+1
        if col <0 : col = 0

        ##### we substract the  GCD cases like (2,2,2) , (6,6,10) , ..., (14, 22, 34)
        substract_gcds = compute_gcds( a, lim )


        ALL += add -  substract_gcds - col
        a_cnt = add -  substract_gcds - col

        print('a= ', a, '   max_c= ', max_c, '   min_c= ', min_c ,'   nr_terms= ', nr_terms , '   col= ', col   ,'       add= '  ,add , '       GCDs= '   , substract_gcds ,'        A_CNT =', a_cnt ,'   ')

    print('\nPrimitive Triangles = ', ALL + ones )
    # print('\nPrimitive Triangles = ', ALL  )
    return ALL + ones

Primitive_integer_sided_triangles( 10**2 )

# WRONG   10^7 -->  23108537152325580276


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n================  My SECOND SOLUTION,  After Euler Forum  ===============\n')
t1  = time.time()


def Mobius(n) :
    if n == 1 : return 1
    if  n == 2  or n == 3  :   return -1
    if  n%4 == 0  :           return 0

    Mu = 1
    if n%2 == 0    :
        Mu = Mu * (-1)
        n = n//2

    p=3
    while p*p <= n :
        if n % (p*p) == 0 :
            return 0

        if n % p == 0 :
            Mu = Mu * (-1)
            n = n//p
        p = p+2

    if n>1  :
        Mu = Mu* (-1)

    return Mu

print(' Mobius : ' , Mobius(6) )

def second_solution( limit ) :

    grand = 0

    for i in range(1, limit//3 + 1) :
        limit = limit // i
        total=0
        for a in range(1, limit//3+1) :
            #  For perimeters not exceeding Limit for which it becomes a+b<=c
            min_b = a ;
            max_b = ((limit+1)//2)- a

            min_c = a
            max_c = a

            no_c = (max_b-min_b+1)

            if max_b >= min_b :
                total = total+((min_c+max_c)*(no_c)//2)


 # For perimeters which are exceeding Limit

            min_b = max( a , max_b+1)
            max_b = ((limit+1)//2) - ((a+1)//2)

            min_c = (limit-a-min_b)-(min_b)+1
            max_c = (limit-a-max_b)-(max_b)+1

            no_c = (max_b-min_b+1)

            if max_b >= min_b  :
                total = total + ((min_c+max_c)*(no_c)//2)



        j = Mobius(i)
        grand = grand + j * total
        print('i=  ',i , "     total = ", total ,"    j=  ", j )



    return print("\nAnswer : ", grand )


second_solution( 10**2 )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')




print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# http://mathworld.wolfram.com/IntegerTriangle.html

from math import floor

def int3(n):
    if n%2 == 1:
        return int(round( ( (n+3)**2 )/48.0 ))
    else:
        return int(round( (n**2)/48.0 ))


def solution1( n ) :
    r = 0
    h = [0] * ( n+1 )
    for i in range( 3 , n+1 ):
        u = int3(i) - h[i]
        r += u
        for j in range( 2*i, n+1, i):
            h[j] += u
    print (r)

solution1(10**2)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# === Thu, 25 Apr 2013, 06:55, tlesaul2, USA
# After stumbling upon the fact that the number of integer triangles with perimeter m is the same as the number
# of partitions of m into 3 parts with equal parity (on stackoverflow),
# I derived a formula for 'ordered triangles' using generating functions:
# (x+x^3+x^5+...)^3 + (x^2+x^4+x^6)^3 = (x^3+x^6)/((1-x^2)^3).
#
# To count the (unordered) triangles that we need to count I realized that most triangles were getting counted 6 times
# corresponding to the number of permutations of the sides, but isosceles triangles only got counted 3 times
# and equilateral triangles only got counted once.
#
# A little arithmetic gives a formula for the number of isosceles triangles, so add in 3 times that.
# Now the equilateral triangle needs to be added in two more times (if 3|m).
# The number of triangles is the result divided by 6.
# From there I manually implemented the Mertens/Moebius idea by iteratively subtracting list elements from appropriate slices,
# then summed the final list.  Took 45 seconds.
#
# Not the fastest, but I hope it makes more sense to those afraid of mysterious formulas and the Moebius function (like me).




def numberOfTrianglesWithPerimeter(m):
    # Count 'Ordered triangles with perimeter m' using generating functions and partitions of m into 3 parts of equal parity.
    o = (m**2-1)/8 if m%2 == 1 else (m**2-6*m+8)/8
    # isoceles triangles get counted 3 times, so add them in 3 more times
    o += 3*(int((m-1)/2)-int(m/4))
    # equilateral triangles get counted once, have added them in as isoceles 3 times, so add them in 2 more times
    o += 2*(1 if m%3 == 0 else 0)
    # every triangle is now counted 6 times as an unordered triangle
    return o/6

def solution2( lim) :
    # Construct list of numbers of triangles

    List = [0,0,0]
    for m in range(3, lim +1 ):
        List.append(numberOfTrianglesWithPerimeter(m))
    print(List)
    # Manually remove non-primitive triangles, similar to Mertens/Moebius, but more sieve-like


    for i in range(3, 5*(lim//10)+1):
        for j in range(2*i, lim+1 , i):
            List[j] -= List[i]

    return print( sum(List))

solution2(10**2)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()


# ==== Sat, 6 Jul 2013, 09:28, EdM, France
# I used : http://mathworld.wolfram.com/IntegerTriangle.html

# PE276 : cpt = 5777137137739632912 en 179.829 s
# Appuyer sur ENTREE pour quitter le programme.

from math import *

# ----------------------------------------
def trianglesPerimetre(p):
    if p%2 == 0:
        return int(round((p**2)/48.0))
    else:
        return int(round((p + 3)**2/48.0))
# ----------------------------------------

eMax = 2
nMax = 10**eMax

primitifsPerimetre = (nMax + 1)*[0]
nonPrimitifsPerimetre = (nMax + 1)*[0]

cpt = 0

for n in range(1, nMax + 1):
    primitifsPerimetre[n] = trianglesPerimetre(n) - nonPrimitifsPerimetre[n]
    cpt += primitifsPerimetre[n]
    for p in range(2*n, nMax + 1, n):
        nonPrimitifsPerimetre[p] += primitifsPerimetre[n]



print( "PE276 : cpt =", cpt )



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ==== Thu, 12 Feb 2015, 03:32, pts
# I've figured out a closed formula for the number of triangles independently, without looking at http://oeis.org/A001400 . Here it is:

def tric(m):
  """Returns the number of (a, b, c) integer triplets where
  1 <= a <= b <= c < a + b and a + b + c <= m, i.e. the number of triangles
  with maximum perimeter m.

  http://oeis.org/A001400 contains a similar formula, this one was derived
  independently.
  """
  # Always nonnegative if m >= 0, but not always divisible by 144.
  return (m ** 2 * (m + 6) + (m & 1 and 9 * m) + 36) // 144

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,2), 'ms\n\n')

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
