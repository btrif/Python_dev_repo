#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
Integer sided triangles for which the area/perimeter ratio is integral      -       Problem 283

Consider the triangle with sides 6, 8 and 10. It can be seen that the perimeter and the area are both equal to 24.
So the area/perimeter ratio is equal to 1.
Consider also the triangle with sides 13, 14 and 15.
The perimeter equals 42 while the area is equal to 84.
So for this triangle the area/perimeter ratio is equal to 2.

Find the sum of the perimeters of all integer sided triangles for which the area/perimeter ratios
are equal to positive integers not exceeding 1000.

'''
import time, zzz, gmpy2
from math import gcd
import itertools
from math import ceil, floor, gcd

# @2017-03-12, 00:15 -   Heron
# Not Heron because we'll have precision errors


# def Pythagorean_Triples_gen(plim):          ### ( ͡° ͜ʖ ͡°)  ### Last Modif  by Bogdan Trif @ 2017-01-21, 20:45
#     ''':Description: Generator for Pythagorean Triplets with their multiples until an up_limit, plim
#         which is the Perimeter of the triangle.
#         :Formulas used: :
#     a^2 + b^2 = c^2     ;
#         a = m^2 - n^2       ;
#     b = 2mn     ;
#         c = m^2 + n^2        ;
#             k [ a + b + c = p = 2 * m * ( m + n ) ]     ;
#
#     :Usage: >>> next(pythagorean_triple(30))
#     Pythagorean triplets with this property that the greatest common divisor of
#     any two of the numbers is 1 are called primitive Pythagorean triplets.
#         :param: **plim** --> int,  limit of the perimeter of the triangle
#     '''
#     m = 1
#     while 2*m**2 < plim:
#         for n in range( 1 + m%2, m, 2):
#             if gcd(m, n) == 1:
#                 p = 2 * m * (m+n)
#                 a, b, c = m**2-n**2  ,    2*m*n ,     m**2+n**2
#                 for k in range(1, plim//p + 1):
#                     yield (k*a, k*b, k*c)
#         m+=1

def Heron_area_perimeter(a,b,c):
    s= (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**(1/2), s*2

print('Heron_area test : \t', Heron_area_perimeter(13, 14, 15)  )

def gcd3(a, b, c):
    return gcd(gcd(a, b), c)

def Heronian_triangles_primitives( lim ):
    from math import gcd, ceil, floor
    m = 3
    cnt=0
    while m <= lim :
        for n in range(1, m+1):
            for k in range( int(m* floor( n/(2*m+n))**(1/2))+1 , ceil((m*n)**(1/2)) ):
                # print(m,n,k ,int(m* floor( n/(2*m+n))**(1/2)) +1, ceil((m*n)**(1/2)) )
                if gcd3(m, n, k) == 1 :
                    cnt+=1
                    a, b, c = n*( m**2 + k**2 ) , m*( n**2 + k**2 ), (m+n)*( m*n - k**2 )
                    a, b, c = sorted((a, b, c))
                    s =  m*n * (m+n)
                    A =  m*n*k *(m+n)* (m*n - k**2 )
                    g = gcd3(a,b,c)
                    a1, b1, c1 = a//g, b//g, c//g
                    # print(str(cnt)+'.      m,n,k = ', m,n,k, '       a,b,c =  ',a,b,c , '     gcd(a,b,c)=',g ,'       ', a1,b1,c1 ,'        ' ,m+n+k, a1+b1+c1 ,'    r = ', round((a1+b1+c1)/(m+n+k),2) , '      A,p =  ', A, 2*s,'          A / p = ', A/(2*s) )
                    yield a1, b1, c1, A//g**2, 2*s//g
        m+=1



def pair_Factors(n):        # VERY EFFICIENT !!!! SUPER INTELLIGENT ALGORITHM
    '''Pair Factoring, VERY EFFICIENT !
    :param n:
    :return:     '''
    todo, combis = [(n, 2, [])], []
    while todo:
        n, i, combi = todo.pop()
        while i * i <= n:
            if n % i == 0:
                combis += combi + [i, n//i],
                # todo += (n//i, i, combi+[i]),       # If needed only PAIRS (a,b) comment this line !!!
            i += 1
    return combis


def get_divisors(n):      ### ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ### !! FIRST FASTEST
    from math import sqrt
    factors = set()
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 0:
            factors.add(x)
            factors.add(n//x)
    return sorted(factors)



print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# P = Pythagorean_Triples_gen(100)
# # for i in P:    print( i)
#
# def right_triangles_area_perimeter_ratio( lim, ratio ) :
#     S = 0
#     m = 1
#     while m < lim :
#         for n in range( 1,  m ):
#             p = 2 * m * (m+n)                   # perimeter
#             A = (m**2-n**2  ) *m*n          # Area
#             A_p = (m-n)*n /2       # Area/perimeter ratio
#             if A_p > ratio : break
#             if gcd(m, n) == 1 :
#                 a, b, c = m**2-n**2  ,    2*m*n ,     m**2+n**2
#                 # print(m,n,'      ',a,b,c, '                p, A ,  A/p : ', p, A, A/p)
#                 k=1
#                 while A_p*k <= ratio :
#                     A1, p1 = A*k**2, p*k
#                     A2, p2 = 2*k * A  , 4*k*m**2
#                     A3, p3 = 2*k * A  , 2*k*(m+n)**2
#                     if (A1/p1) %1 == 0 :
#                         print('m,n, k = ',m,n, k ,'         T1:     a, b, c = ' ,k*a, k*b, k*c , '        T1 :  ', A1, p1, A1/p1  )
#                         S+=p1
#                     if (A2/p2) %1 == 0 :
#                         print('T2:      a, b, c = ' ,k*a, k*b, k*c , '        T2 :  ', A2, p2, A2/p2   )
#                         S += p2
#                     if (A3/p3) %1 == 0 :
#                         print('T3:      a, b, c = ' ,k*a, k*b, k*c , '        T2 :  ', A3, p3, A3/p3   )
#                         S += p3
#
#                     k+=1
#         m+=1
#     return print('\nAnswer : \t', S)
#
# right_triangles_area_perimeter_ratio(10**2, 10**1 )

print('\n-------------------------------')

def brute_force_testing( lim):
    cnt = 0
    for a in range(5, lim+1) :
        for b in range(4, a+1):
            for c in range(3, b+1):
                A, p = Heron_area_perimeter(a, b, c)
                if type(A) == float :
                    if (A/p)%1 == 0 and A/p > 0 :
                        cnt+=1
                        print(str(cnt)+'.        a,b,c =  ',  a, b, c ,'          A,p =   ' ,A, p, '          A / p= ', A/p )

# brute_force_testing(20**1)

def find_Heronian_of_ratio_1() :
    Perim = 0
    for i in range(1,100):
        for j in range(1, i):
            for k in range(1,j) :
                A, p = Heron_area_perimeter(i,j,k)
                if A == p :
                    print(i, j, k)
                    Perim+= i+j+k
    return print('\nAnswer : \t', Perim)

find_Heronian_of_ratio_1()

def check_Heronian(m,n,k):
    def gcd3(x, y, z):
        return gcd(gcd(x, y), z)
#     if gcd3(m, n, k) == 1 :
    a, b, c = n*( m**2 + k**2 ) , m*( n**2 + k**2 ), (m+n)*( m*n - k**2 )
    s =  m*n * (m+n)
    A =  m*n*k *(m+n)* (m*n - k**2 )
    g = gcd3(a,b,c)
    # print(g)
    a1, b1, c1, A1, p1 = a//g, b//g, c//g, A//g**2, 2*s//g
    return a1, b1, c1, A1, p1, A1/p1 , g
#     return 0

# cnn = 0
# for i in range(1, 2000):
#     for j in range(1, i+1):
#         cnn+=1
#         iC = check_Heronian(2000, i, j )
#         if iC[5]%1 ==0 and iC[5] < 10**3   :
#             a, b,c , A, p, A_p, g = iC
#             print(str(cnn)+'.       i, j =  ' ,i,j  , '        a,b,c= ',a,b,c,'     A,p, A / p = ', A, p, A_p,'      g=', g   )

print('\n--------------------------FIRST FAILED SOLUTION------------------------------')

def Heronian__integer_area_perimeter_ratio( lim, ratio ):
    from math import gcd, ceil, floor
    m = 3
    cnt=0
    while m <= lim :
        up_n = m+1
        # if m > 1000 : up_n = 251
        for n in range(1, up_n):
            for k in range( int(m* floor( n/(2*m+n))**(1/2))+1 , ceil((m*n)**(1/2)) ):
                # print(m,n,k ,int(m* floor( n/(2*m+n))**(1/2)) +1, ceil((m*n)**(1/2)) )
                # if m*n*k *(m+n)* (m*n - k**2 ) > ratio : break
                if gcd3(m, n, k) == 1 :
                    cnt+=1
                    a, b, c = n*( m**2 + k**2 ) , m*( n**2 + k**2 ), (m+n)*( m*n - k**2 )
                    a, b, c = sorted((a, b, c))
                    s =  m*n * (m+n)
                    A, p =  m*n*k *(m+n)* (m*n - k**2 ), 2*s
                    A_p = A /p
                    if A_p > ratio : continue
                    g = gcd3(a,b,c)
                    # if A_p % 1  == 0 :
                    #     gg = gcd ( g , int(A_p) )
                    #     a ,b, c, A, p = a//gg, b//gg, c//gg,  A//g**2, p//gg

                    # print(str(cnt)+'.     m,n,k = ', m,n,k, '       a,b,c =  ',a,b,c , '     gcd(a,b,c)=',g ,'       a1,b1,c1 = ', a1,b1,c1 ,'         A, p =  ', A1, p1,'          A / p = ', A1/p1)# ,'    ', a2,b2,c2,p2, A2 , A2/p2)
                    print(str(cnt)+'.     m,n,k = ', m,n,k, '       a,b,c =  ',a,b,c , '     gcd(a,b,c)=',g ,'               A, p =  ', A, p,'          A / p = ', A/p)


                    yield a, b, c, A, p
                    # yield a1, b1, c1, A1, p1
        print(m)
        m+=1


def first_solution( lim, ratio) :
    HT = Heronian__integer_area_perimeter_ratio(lim, ratio)
    SS, S = set(), 0
    cnt = 0
    for T in HT :
        a, b, c, A, p = T
        A_p = A/p
        if A_p > ratio : continue
        signature = int(''.join([str(i) for i in T[:3] ] ))
        if signature not in SS :
            SS.add(signature)
            gm = gmpy2.mpq(A, p)
            if gm% 1 == 0 :   s= 1  # ; print('integer', s , gm)
            else :  s = gm.denominator # ; print('fractions :', s,  gm )

            k = s
            while k*A_p <= ratio :
                cnt+=1
                ak, bk, ck = k*a, k*b, k*c
                pk = ak+bk+ck
                Ak = k**2*A
                if cnt %10**5 == 0 :
                    print(str(cnt)+'.     k = ', k,'      a,b,c =  ', ak, bk, ck, '     A, p =  ',Ak, pk,'        A / p =', Ak/pk)
                # if  (Ak/pk)%1 ==0 :
                S += pk
                k += s

    print('\n Dict : \n', len(SS), '\n' )


    return print('\nAnswer : \t', S)

# first_solution(2000, 10**2 )





t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()


def integer_sided_triangles( ratio ) :

    S, cnt  = 0, 0
    for r in range(1, ratio+1) :
    # for m in [23] :
        U = get_divisors(2*r)
        print(2*r, '     ',U)
        for u in U :
            for v in range(1, floor(3**(1/2) *u)+1 ):
            # if u in [1, 2] :  up_v = 2000*u
            # if u in [3, 4] :  up_v = 1000*u
            # if u in [5, 6] :  up_v = 500*u
            # if  7<= u<=50 :  up_v = 100*u
            # if  51<= u<=100 :    up_v = 50*u
            # else : up_v = 25*u
            # for v in range(1, up_v ):
                if gcd(u,v) == 1  :           # !!!!! Don't Touch This !!!
                    F = pair_Factors( 4*r*r*(u**2+v**2) )
                    # print(u, v, F)
                    for delta1, delta2 in F :
                        # print(delta1, delta2)
                        if delta1 <= (2*r*(u**2+v**2)**(1/2)) :
                        # if delta1 <= 2*r*(v*v+u*u)  :
                            if (delta1+2*r*u)%v == 0 and  (delta2+2*r*u)%v == 0 :
                                cnt+=1
                                a = (delta1 + 2*r*u) //v + 2*r*v//u
                                b = (delta2 + 2*r*u) //v + 2*r*v//u
                                c = (delta1+delta2 + 4*r*u) //v
                                p = a+b+c
                                A = p*r             #A =  ( p//2 *(p//2 - a)*(p//2 - b)*(p//2 - c) )**(1/2)
                                # print(str(cnt)+'.     ',m,'        u, v, d1, d2 = ',u, v,  delta1, delta2,'        a,b,c = ', (a,b,c) , '       A,p = ' ,A, p , '      A / p =', A//p )
                                S+= p
                                print(str(cnt)+'.    ratio= ',r,'        u, v, d1, d2 = ',u, v,  delta1, delta2,'        a,b,c = ', (a,b,c) , '       A,p = ' ,A, p , '      A / p =', A//p ,'       S=', S)
                                # if v/u > uv_max : uv_max = v/u
    # print('\nSET Length : \t ', '   v/u max = ', uv_max )
    return print('\nAnswer : \t', S)


integer_sided_triangles(2)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

# zzz.Star_Wars()

# Can anyone confirm that the sum of all the perimeters of of triangles with ratio <= 100 is
# 289.620.027.474    ?  YES !
# triangles with ratio <= 200 is 9.050.416.878.652
# OK! I got the answer with ratio <= 500 after fixing some stupid bugs        it's 878011574949780

#### GENERAL INFO ####
# http://forumgeom.fau.edu/FG2007volume7/FG200718.pdf
# http://www.wolframalpha.com/input/?i=solve+15281%3Dn*(m%5E2%2Bk%5E2),+137825%3Dm*(n%5E2%2Bk%5E2),+152514%3D(m%2Bn)*(m*n-k%5E2)
# http://www.wm-archive.uni-bayreuth.de/fileadmin/Sascha/Publikationen/On_Heronian_Triangles.pdf
# http://math.stackexchange.com/questions/114112/heronian-triangle-generator
# https://arxiv.org/pdf/1312.2318.pdf
# http://www.oocities.org/teufel_pi/papers/gidag.pdf
# https://en.wikipedia.org/wiki/Integer_triangle#Heronian_triangles
http://eulersolutions.fr.yuku.com/topic/99/Problem-283?page=2#.WM7wKVV97RY

# 2017-03-19 - I need to improve the algorithm. I'm not even close !
# http://www.andrewewhite.net/wordpress/2010/05/07/finding-integer-triangles-ratios/    !!!!!!!!!!!
# @2017-03-19  -  I miss one triangle with the above algorithm for the ratio 1 -- Need to really analyze all the steps AGAIN !!!!!

# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
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
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

