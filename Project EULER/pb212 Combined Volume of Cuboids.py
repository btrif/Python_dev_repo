#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                Combined Volume of Cuboids          -       Problem 212

An axis-aligned cuboid, specified by parameters { (x0,y0,z0), (dx,dy,dz) },
consists of all points (X,Y,Z) such that x0 ≤ X ≤ x0+dx, y0 ≤ Y ≤ y0+dy and z0 ≤ Z ≤ z0+dz.
The volume of the cuboid is the product, dx × dy × dz.
The combined volume of a collection of cuboids is the volume of their union
and will be less than the sum of the individual volumes if any cuboids overlap.

Let C1,...,C50000 be a collection of 50000 axis-aligned cuboids such that Cn has parameters

x0 = S6n-5 modulo 10000
y0 = S6n-4 modulo 10000
z0 = S6n-3 modulo 10000
dx = 1 + (S6n-2 modulo 399)
dy = 1 + (S6n-1 modulo 399)
dz = 1 + (S6n modulo 399)

where S1,...,S300000 come from the "Lagged Fibonacci Generator":

For 1 ≤ k ≤ 55, Sk = [100003 - 200003k + 300007k3]   (modulo 1000000)
For 56 ≤ k, Sk = [Sk-24 + Sk-55]   (modulo 1000000)

Thus, C1 has parameters {(7,53,183),(94,369,56)}, C2 has parameters {(2383,3563,5079),(42,212,344)}, and so on.

The combined volume of the first 100 cuboids, C1,...,C100, is 723581599.

What is the combined volume of all 50000 cuboids, C1,...,C50000 ?


'''
import time, zzz

# http://stackoverflow.com/questions/12769386/how-to-calculate-total-volume-of-multiple-overlapping-cuboids
# http://stackoverflow.com/questions/244452/what-is-an-efficient-algorithm-to-find-area-of-overlapping-rectangles          !!!!!!!!!!!
# https://www.reddit.com/r/projecteuler/comments/lzazf/problem_212_combined_volume_of_cuboids/
# https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle
import sys


def Lagged_Fibonacci_Generator_gen():           # EFFICIENT GENERATOR
    '''
    For 1 ≤ k ≤ 55, Sk = [100003 - 200003*k + 300007*k**3] (modulo 1000000) - 500000
    For 56 ≤ k, Sk = [S_(k-24) + S(k-55)] (modulo 1000000) - 500000                      '''
    tmp=[]
    for k in range(1,56) :
        s = (100003 - 200003*k + 300007*k**3) % 1000000
        # print(k, s)
        tmp.append(s)
        yield s
    while True :
        s = (tmp[-24]+tmp[-55])%1000000
        tmp.append(s)
        tmp.pop(0)
        # print(len(tmp) ,tmp)
        yield s


LFG = Lagged_Fibonacci_Generator_gen()

def generate_cuboids( how_many ) :

    for i in range(how_many) :
        s1, s2, s3, s4, s5, s6 = next(LFG), next(LFG), next(LFG), next(LFG), next(LFG), next(LFG)
        x0, y0, z0  = s1 % 10000, s2 % 10000, s3 % 10000
        dx, dy, dz = 1 + (s4 % 399) , 1 + (s5 % 399) , 1 + (s6 % 399)
        # print(str(i+1) +'.    x0, y0, z0, =', (x0, y0, z0 ) , '       dx, dy, dz =', (dx, dy, dz) )

        yield ( x0, x0+dx, y0, y0+dy, z0 , z0+dz  )



print()
def intersect_volumes( C1, C2) :
    ''':Description: Function which gives the volume intersection of two cuboids they share common volume.
        C1, C2 must have the form : C1 =  (x11, x12, y11, y12, z11, z12) , C2 = (x11, x12, y11, y12, z11, z12) ;
        where x12 > x11, y12> y11 ...and so on ...
        returns False if they do not share a common volume:
    :param C1: cuboid1 with x12 > x11, y12> y11 , z12> z11
    :param C2: cuboid 2 with  x22 > x21, y22> y21, z22> z21
    :return: False or the Common Volume (intersection )  in the form (x1, y1, z1), (x2, y2, z2)                             '''
    x11,  x12, y11, y12, z11, z12 = C1
    x21,  x22, y21, y22, z21, z22 = C2

    # print('C1 :   ', x11, y11, z11,'        ' ,x12, y12, z12 )
    # print('C2 :   ',  x21, y21, z21,'        ' ,x22, y22, z22 )
    dx = min(x12, x22) -  max(x11, x21)
    dy = min(y12, y22) -  max(y11, y21)
    dz = min(z12, z22)  -  max(z11, z21)
    # print('dx = ', dx, '      dy = ', dy , '      dz = ', dz  )
    if dx <=0 or dy <= 0 or dz <= 0 :
        return False
    else :
        x = max(x11, x21)
        y = max(y11, y21)
        z = max(z11, z21)
        # print('(x , dx) = ', x , x+ dx , ' ;     (y , dy) = ', y , y+ dy , ' ;    (z , dz) = ', z , z+ dz  )
        return ( x, x+dx, y, y+dy, z , z+dz )




C1 = ( 7, 1001, 53, 1422, 1183, 1239 )
C2 = ( 83, 2425, 563, 3775, 790, 2423 )

print('\nTest intersect_volumes(C1, C2) :  ' ,intersect_volumes(C1, C2) )

def cuboid_volume( C ) :
    x1, x2, y1, y2, z1 , z2   = C
    return (x2-x1)*(y2-y1)*(z2-z1)

print('Cuboid Volume : ', cuboid_volume( C1 ))

print('\n--------------------------TESTS------------------------------')
t1  = time.time()


def BruteForce_check( how_many ) :
    CUB = list(generate_cuboids(how_many))
    print(len(CUB), CUB[:30],'\n')
    UNION = [ ]
    VOLUM = sum([ cuboid_volume(C) for C in CUB ])

    sign = 1
    while len(CUB) > 1 :
        UNION = []
        for i in range(len(CUB)) :
            # sys.stdout.write('\r' + str(sign)+ '       ' + str(i) )   # Font Segoe UI Semibold
            # sys.stdout.flush()
            # print('sign = ', sign,'      ' , i )
            for j in range(i+1, len(CUB)) :
                if CUB[i] != CUB[j] :
                    C =  intersect_volumes( CUB[i] , CUB[j] )
                    if C  :
                        print(i ,j, '      C1 = ' , CUB[i],'       C2 =', CUB[j] )
                        vol = cuboid_volume(C)
                        if sign %2 == 1 : VOLUM -= vol
                        if sign %2 == 0 : VOLUM += vol

                        print('C = ', C ,'      vol = ',   vol )
                        UNION.append(C)

        print('UNION : ', len(UNION) )
        CUB = UNION[:]
        print('sign = ', sign )
        print(' len(CUB) = ', len(CUB),'    ' , CUB[:30] )

        sign += 1
        if sign == 10 : break

    print('\nTotal Union of Cuboids = ', VOLUM )
    return VOLUM

BruteForce_check(1000)


@2018-05-16 :
https://stackoverflow.com/questions/32216606/python-program-to-detect-intersection-of-one-dimensional-line-segments
https://stackoverflow.com/questions/244452/what-is-an-efficient-algorithm-to-find-area-of-overlapping-rectangles
https://github.com/adrianN/line_intersection/blob/master/README.md
http://jeffe.cs.illinois.edu/teaching/373/notes/x06-sweepline.pdf

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


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

