#  Created by Bogdan Trif on 13-10-2017 , 9:52 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                        Integer Ladders             -           Problem 309

In the classic "Crossing Ladders" problem, we are given the lengths x and y of two ladders
resting on the opposite walls of a narrow, level street.
We are also given the height h above the street where the two ladders cross
and we are asked to find the width of the street (w).

p309_ladders.gif
Here, we are only concerned with instances where all four variables are positive integers.
For example, if x = 70, y = 119 and h = 30, we can calculate that w = 56.

In fact, for integer values x, y, h and 0 < x < y < 200,
there are only five triplets (x,y,h) producing integer solutions for w:

(70, 119, 30), (74, 182, 21), (87, 105, 35), (100, 116, 35) and (119, 175, 40).

For integer values x, y, h and 0 < x < y < 1 000 000, how many triplets (x,y,h) produce integer solutions for w?

'''
import time, zzz
from math import gcd, sqrt
from gmpy2 import mpq




def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)



def Pythagorean_primitive_triplets_gen( lim   ):    # by Bogdan Trif @ 2018-05-17, 09:30     ### ( ͡° ͜ʖ ͡°)  FASTEST  ( ͡° ͜ʖ ͡°)  ###
    '''     :Formulas used: :
                a^2 + b^2 = c^2     ;
                a = m^2 - n^2       ;
                b = 2mn     ;
                c = m^2 + n^2        ;
            k [ a + b + c ] = p = 2 * m * ( m + n ) ]     ;

    :LINK: http://mathforum.org/library/drmath/view/55811.html
    :Usage: >>> next(pythagorean_triple(30))
    Pythagorean triplets with this property that the greatest common divisor of
    any two of the numbers is 1 are called primitive Pythagorean triplets.
    '''
    m = 2
    while m <= pow(lim, 1/2) :
        if m%2 == 1 :            n = 2                 # m - ODD
        if m%2 == 0 :            n = 1                 # m - EVEN

        while n < m :                      ### range(1,m) as we need only a > 0 !!!!!!!!
            if gcd(m,n) ==1 :           #   Assure that we generate ONLY primitive Pythagorean triplets
                a = m**2-n**2
                b = 2*m*n
                if b > lim : break
                # c = m**2 + n**2
                # p = 2*m* (m + n )
                # print(' m, n = \t',m, n,'            a,b,c =\t',sorted((a,b,c))  ,'      gcd3 = ', gcd3(a,b,c),'     gcd(m,n) = ', gcd(m,n) ,'             p = ',  p )
                # yield a, b, c
                # print('m = ', m ,'     n = ', n)
                if a < lim and b < lim :
                    yield a, b

            n+=2
        m+=1




print('\n--------------------------TESTS------------------------------')
t1  = time.time()

# @2019-01-13,21:30 - IDEA :
# 1.  We must generate Pythagorean Triplets PPT.
# 2.  Next we will find PPT and their multiples which share a cathete which is shared
# I will make an image fr illustration
# 3. The build from scratch the value needed for w


# REFERENCES :
# For ladder lengths up to 2500 there are 267 solutions.
# For ladder lengths up to and including 2500 there are 268 solutions.

def find_ladder_configuration(x, y, h) :
    for u in range(3, 100 ) :
        for q in range(2, u ) :
            w = u+q
            r = sqrt( u*u+h*h )
            p = sqrt( q*q+h*h )


            v = h*w/u
            if v%1 ==0 :
                print('u, q, w, v = ', u, q, w, v )


                z = h*w/q


                xx = sqrt( w*w+v*v)
                yy = sqrt( w*w+z*z)

                # if x == xx and y == yy :
                if xx%1 == 0 or yy%1 ==0 :
                    print( 'x, y, h = ', (x , y, h) ,'       u= ', u, '       q= ', q ,'             x, y =  ', xx, yy  )


find_ladder_configuration(74, 182, 21  )
# find_ladder_configuration(70, 119, 30  )

@2019-01-15, 12:07 - I miss something. From (70, 119, 30), (74, 182, 21), (87, 105, 35), (100, 116, 35) and (119, 175, 40)
I only get right results for (70, 119, 30). The others are not with my algorithm.

This is how it is done :
https://en.wikipedia.org/wiki/Crossed_ladders_problem

PROBLEMS : 157, 510, 309 use the same principle (a+b)/ (a*b)
Find a way to solve this. !


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n============  My FIRST SOLUTION   ===============\n')
t1  = time.time()

lim = 250
PPT = []
PPTG = Pythagorean_primitive_triplets_gen( lim )
cnt=0
while True :
    try :
        cnt+=1
        ppt = next(PPTG)
        print(str(cnt)+'.     ', ppt )
        PPT.append(ppt)
    except StopIteration :
        print("\nJust Finished\n")
        break

print('PPT : ', len(PPT),  PPT[:30] )

Pairs = {}
Uniques = {}
count = 0
for i in range(len(PPT)):
    for j in range(i+1, len(PPT) ) :
        a1, b1 = PPT[i]
        a2, b2 = PPT[j]

        # 2019-01-13, 23:00  I am on the right track , All I can do now is to assign the corresponding multipliers
        # and iterate up !
        for a in PPT[i] :
            for b in PPT[j] :
                m1, m2 = lcm(a, b)//a, lcm(a, b)//b
                T1 = tuple(map(m1.__mul__, PPT[i] ))
                T2 = tuple(map(m2.__mul__, PPT[j] ))
                h = list(set(T1) & set(T2))[0]          # Chose HEIGHT as the common cathete between the two triangles
                # print('\n',PPT[i],'      ', PPT[j] , '       a, b =  ', a, b, '     m1, m2 = ', m1, m2,'   T1 =', T1,'   T2 =', T2 , '    h=',h )

                # print('  (u, h, r) = ',  (u, h, r) , '       (q, h, p) = ',  (q, h, p ) , '    ' )

                k = 1
                while k *h < lim :
                    h = h*k                                                   ### multiplied with k
                    T_left = tuple(map(k.__mul__, T1 ))         ### multiplied with k
                    T_right = tuple(map(k.__mul__, T2 ))         ### multiplied with k

                    u, q = (sum(T_left)-h)  , (sum(T_right)-h)

                    if u > 0 and q > 0 :
                        r, p = ( pow(u*u+h*h, 1/2) ) , ( pow(q*q+h*h, 1/2) )      # hypothenuses of the two triangles sharing h

                        # @2019-01-14 ---> RECONSIDER SOME FORMULAS !!! for z,

                        w = u + q
                        v = h*w / u

                        x = pow( w*w + v*v, 1/2 )
                        y = p*w / q

                        s = q * x / w
                        z = h * w / q

                        if x > lim or y > lim : break

                        if  x%1 == 0 and y%1==0 :
                            if (x+y+h) not in Uniques :
                                Uniques[x+y+h] = set()
                            Uniques[x+y+h].add( x*y*h  )

                            print('k=', k,'    h= ', h , '    T1, T2 = ', T_left, T_right , '     (u, h, r) = ',  (u, h, r) , '       (q, h, p) = ',  (q, h, p ) , '    w= ', w ,'     v =', v , '        (x, y, h) =    ' , ( x, y, h )  )

                    k+=1

U = [  len(v)  for k,v in Uniques.items()  ]
print( '\nU : ', U  )
print( sum(U)  )



t2  = time.time()
print('\n# Completed in :', round((t2-t1),2), 's\n\n')


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




