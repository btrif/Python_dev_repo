#  Created by Bogdan Trif on 16-05-2018 , 6:23 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                Scary Sphere            -               Problem 360

Given two points (x1,y1,z1) and (x2,y2,z2) in three dimensional space,
the Manhattan distance between those points is defined as :
|x1-x2|+|y1-y2|+|z1-z2|.

Let C(r) be a sphere with radius r and center in the origin O(0,0,0).
Let I(r) be the set of all points with integer coordinates on the surface of C(r).
Let S(r) be the sum of the Manhattan distances of all elements of I(r) to the origin O.

E.g. S(45) = 34518.

Find S(10^10)

'''
import time, zzz
from math import sqrt

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

Manhattan = lambda x1, y1, z1, x2, y2, z2 : abs(x1-x2)+ abs(y1-y2)+abs(z1-z2)

def brute_force(R) :
    cnt = 0
    eps = 1e-9
    S = 0

    for x in range(0, R+1 ) :
        for y in range(0, int(sqrt( R*R - x*x ))+1 ) :
            z = sqrt( R*R - x*x - y*y)
            if abs( z - round(z) ) < eps :
                z = int(z)
                M = Manhattan(x, y, z, 0, 0, 0 )
                if ((x == 0 ) and ( y!=0  and z!= 0)) or ((y == 0 ) and ( x!=0  and z!= 0)) or ((z == 0 ) and (  x!=0  and y!= 0)) :
                    S += 4*M
                    cnt += 4

                if (( x==0 and y==0 ) and z!= 0) or (( y==0  and z==0 ) and x!= 0) or (( x==0  and z==0 ) and y!= 0)  :
                    S += 2*M
                    cnt += 2

                elif x!=0 and y!=0 and z!=0 :
                    S += 8*M
                    cnt += 8

                print(str(cnt)+'.        x , y,  z = ', x, y, z , '        Manh = ', M ,'        R^2 = ', sqrt(x*x+y*y+z*z) )


    return print('\nS = ', S , '          ' , '    Correct value = ', 34518 ,'   the nr of points = ', cnt )   # And number of points is 510.

brute_force(41)     # It works GOOD !


# LINKS :
# https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem
# https://www.ams.org/journals/proc/1957-008-02/S0002-9939-1957-0085275-8/S0002-9939-1957-0085275-8.pdf
# https://arxiv.org/abs/math/0502007
# https://mathoverflow.net/questions/110239/is-there-an-algorithm-for-writing-a-number-as-a-sum-of-three-squares/
# https://mathoverflow.net/questions/104322/efficient-computation-of-integer-representation-as-a-sum-of-three-squares
https://brilliant.org/wiki/fermats-sum-of-two-squares-theorem/
https://math.stackexchange.com/questions/2361586/express-355-as-a-sum-of-three-squares


@2018-05-16 - Did a brute force check to verify the problem.
The strategy to solve is to use HermiteSerret Algorithm to decompose a number n in sum of two squares :
n = x^2 = y^2
then use Brahmagupta Fibonacci identity and a Factorization Algorithm

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()





# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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

