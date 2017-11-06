#  Created by Bogdan Trif on 17-10-2017 , 1:37 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                            Tangent Circles         -           Problem 510

Circles A and B are tangent to each other and to line L at three distinct points.
Circle C is inside the space between A, B and L, and tangent to all three.
Let rA, rB and rC be the radii of A, B and C respectively.

p510_tangent_circles.png

Let S(n) = Σ ( r_A + r_B + r_C ) , for 0 < r_A ≤ r_B ≤ n where r_A, r_B and r_C are integers.

The only solution for 0 < r_A ≤ r_B ≤ 5 is r_A = 4, r_B = 4 and r_C = 1   ,
so S(5) = 4 + 4 + 1 = 9.

You are also given S(100) = 3072.

Find S(10^9).


'''
import time, zzz
from math import sqrt, gcd
from gmpy2 import is_prime, is_square

def gcd3(a, b, c):
    return gcd(gcd(a, b), c)

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
    # IMPORTANT !!! If we have a straight line always put the radius r2 = 0 at the end like ( 4, 4, 0 )
    if r2 != 0 :
        k0, k1, k2 = 1/r0, 1/ r1, 1/r2
        k4 = k1 + k2 + k0 + 2 * sqrt( k0*k1 + k0*k2 + k1*k2 )
        return 1/k4
    else :
        k0, k1 = 1/r0, 1/ r1
        k4 = k1 + k0 + 2 * sqrt( k0*k1 )
        return 1/k4

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# print('4, 4, 0  = ', get_k4( (4, 4, 0)  ) )

def some_brute_force_first(lim) :
    S_n = 0
    for r_A in range(1, lim+1) :
        for r_B in range(r_A, lim+1) :
            r_C = get_k4( (r_A, r_B, 0 ))
            if r_C %1 == 0 :
                r_C = int(r_C)
                S_n += ( r_A + r_B + r_C)
                # if is_prime(int(r_C)) :
                if (r_B/r_A )%1 != 0  :
                # if not is_square( r_B//r_C )  :
                # if is_square(r_C) :# == False  and is_prime(r_C)== False :
                    print('r_A = ', r_A, ' ,   r_B = ', r_B , ' ,   r_C = ', r_C, '          r_B/r_A =', r_B/r_A ,
                          '        gcd(A,B,C)=  ', gcd3(r_A, r_B, r_C) , '      gcd_A_B = ',gcd(r_A, r_B) , '      gcd_A_C = ',gcd(r_A, r_C), '      gcd_B_C = ',gcd(r_B, r_C) ,'         B/C= ',  r_B/r_C )


    return print('\nS(n) = ', S_n )

some_brute_force_first(20000)


# CASES :
# 1.  r_C - prime => r_A = R_B = R_C *4
# 2. r_C - square =>

# https://www.cut-the-knot.org/pythagoras/TangentCirclesSangaku.shtml
@2017-11-02     -   I need to solve some kind of Pell equation of the form 1/sqrt(r_C) = 1/ sqrt(r_A) + 1/sqrt(r_B)
where r_C is the smallest circlein between the two bigger circles and the line


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

# def first_soln(up):
#     S_n = 0
#     for r_C in range(1, up ) :
#         for k in range( 1,  1000 ):




t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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




