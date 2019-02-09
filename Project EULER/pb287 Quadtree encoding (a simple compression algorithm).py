#  Created by Bogdan Trif on 02-11-2017 , 11:36 PM.
# © o(^_^)o  Solved by Bogdan Trif  @   Completed on Tue, 8 Jan 2019, 17:59
#The  Euler Project  https://projecteuler.net
'''
        Quadtree encoding (a simple compression algorithm)          -           Problem 287

The quadtree encoding allows us to describe a 2N×2N black and white image as a sequence of bits (0 and 1).
Those sequences are to be read from left to right like this:

-   the first bit deals with the complete 2N×2N region;
-   "0" denotes a split:
the current 2n×2n region is divided into 4 sub-regions of dimension 2^(n-1) × 2^(n-1),
the next bits contains the description of the top left, top right, bottom left and bottom right sub-regions - in that order;
-   "10" indicates that the current region contains only black pixels;
-   "11" indicates that the current region contains only white pixels.

Consider the following 4×4 image (colored marks denote places where a split can occur):

p287_quadtree.gif

This image can be described by several sequences, for example : "001010101001011111011010101010", of length 30, or
"0100101111101110", of length 16, which is the minimal sequence for this image.

For a positive integer N, define DN as the 2N×2N image with the following coloring scheme:

=   the pixel with coordinates x = 0, y = 0 corresponds to the bottom left pixel,
=   if (x - 2^(N-1))^2 + (y - 2^(N-1))^2 ≤ 2^(2N-2) then the pixel is black,
=   otherwise the pixel is white.
What is the length of the minimal sequence describing D_24 ?


'''
import time, zzz
# import numpy as np
# import matplotlib.pyplot as plt
from math import sqrt

def generate_pixels( N, plot = False ):
    cnt = 0
    X, Y = [], []
    for x in range(0, 2**N + 1) :
        Z = []      # used to display y max
        for y in range(0, 2**N + 1) :
            if  ( x - 2**(N-1) )**2 + ( y - 2**(N-1) )** 2 <= ( 2**(2*N-2)) :
            # if  ( x )**2 + ( y  )** 2 <= ( 2**(2*N-2)) :
                cnt += 1
                X.append(x+0.5) ; Y.append(y+0.5)
                Z.append(y)

        y_max = max(Z)
        print( str(cnt)+ '.      x, y =  ', x , y_max ,'        x^2= ', ( x - 2**(N-1) )**2,  '       y^2=' , ( y_max - 2**(N-1) )** 2 , '        R^2 = '  ,( 2**(2*N-2))  )

    if plot == True :
        ######     START PLOT    ###########
        fig = plt.figure(figsize=(12 , 12))
        ax = fig.add_subplot( 1,1,1    ) #, aspect='equal')
        plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)


        major, minor, x1, x2, y1, y2 = 1, 10, 0, 2**N, 0, 2**N

        # major ticks every 5, minor ticks every 1
        major_ticks = np.arange(x1, x2, major)
        minor_ticks = np.arange(y1, y2, minor)

        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        ax.set_yticks(major_ticks)
        ax.set_yticks(minor_ticks, minor=True)


        plt.xlim([x1 , x2])
        plt.ylim([y1, y2])

        # and a corresponding grid
        # ax.grid(which='both')

        # or if you want differnet settings for the grids:
        # ax.grid(which='minor', alpha=0.2)
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=1.5)

        ax.grid(which='both')
        # ax.axis('equal')
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')

        plt.grid(True)

        plt.scatter(X, Y, color = 'slateblue', marker = 's' , s = 500  )

        plt.show()


# generate_pixels( 4 , True )

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

uncompressed = lambda N : sum([ 2**(2*i) for i in range(0, N)  ]) + 2*2**(2*N)          # CORRECT !

'''

print('uncompressed : ', uncompressed(5)  )

N = 5
for x in range( 2**N):
    z = int(sqrt( ( 2**(2*N-2)) - ( x- 2**(N-1) )**2  ))
    y_max = z + 2**(N-1)
    y_min = 2**N - y_max
    pix = min( y_max-y_min+1, 2**N  )
    print('x = '  ,x, '     y_min = ' ,y_min, '     y_max = ' ,y_max, '      pixels =  ' , pix )

'''
'''
# @2017-11-13,  It remains to solve this problem via recursion when I will master it better than
# I am right now ! When it will come that day ? I AM curious ! 

### STUDY CASE :
# D5 :  minimal length =  499

@2019-01-07, 12:00  -   The problem is simple. Just build a recursive quad, not necessarily
to build a quad tree data structure because we will process each square.
We will represent a square only with two vertices :  
- its bottom left vertex (x1, y1) = P1  
- its top right vertex (x2, y2) = P2
From those two we can for the other 2 points

# @2019-01-08, 16:00WELL, it took me
# 1 year to finally solve this. # But I did it ! I can say now that I master recursion properly !

'''





t2  = time.time()
print('\n# Completed in :', round((t2-t1), 2 ), 's\n\n')

print('\n========  My FIRST SOLUTION,  RECURSION, 30 min in pypy without any optimization  ============\n')
t1  = time.time()

#@2019-01-08 - I could optimize it using symetry of the  TL (Top Left) with BR(bottom Right )

def midPoint(square) :
    ''':Description: Returns the midpoint of a square of the form :
    [ (x_bottom_left, y_bottom_left, ) , (x_top_right, y_top_right ) ]
    :param square:
    :return:  (x, y) int, midpoint                     '''
    x = square[0][0] + (square[1][0]- square[0][0])//2
    y = square[0][1] + (square[1][1]- square[0][1])//2
    return (x, y )

def in_Circle (x, y, N):
    ''':Description:    Detects if a point x,y is within a circle with equation :
        (x-a)^2 + (x-b)^2 = R^2, where :
            a = 2^(N-1), b = 2^(N-1)  , N- being the exponent power
            R = 2**(2*N-2)

            **(x - 2^(N-1))^2 + (y - 2^(N-1))^2 = 2^(2*N-2)**
    :param N:int, exp power of 2
    :return: boolean, True of False                                     '''

    # print( 'x^2= ',(x - 2**(N-1))**2 , '  ;  y^2= ', ( y - 2**(N-1) )**2 )
    # print('x^2+y^2 = ' , (x - 2**(N-1))**2 + ( y - 2**(N-1) )**2 , ';    R^2 = ' ,2**(2*N-2)  )
    return ( x - 2**(N-1))*( x - 2**(N-1)) + ( y - 2**(N-1) )*( y - 2**(N-1) ) <= 2**(2*N-2)


def circle_square_intersection( square, N ):       # o(^_^)o   Made by Bogdan Trif @ 2019-01-07; WORKS GREAT !!
    ''':Description: Given the square, we check if  one of the 4 points
        is within the Circle. There 3 cases :
            1.  None of the 4 points is within the circle : return False
            2.  All the 4 points are within the circle : return False
            3.  Between 1 and 3 points are within the circle : return True
                                    A-----B
                                    |          |
                                    |          |
                                    C-----D
    :param square: input [(x1, y1) (x2, y2)]
    :return: boolean : True or False                        '''

    x_A, y_A = square[0][0], square[1][1]-1
    x_B, y_B = square[1][0]-1, square[1][1]-1
    x_C, y_C = square[0][0], square[0][1]
    x_D, y_D = square[1][0]-1, square[0][1]

    # print('x_A, y_A = ' , x_A, y_A )
    # print('x_B, y_B = ' , x_B, y_B )
    # print('x_C, y_C = ' , x_C, y_C )
    # print('x_D, y_D = ' , x_D, y_D )

    Bool = [ in_Circle(x_A, y_A, N) , in_Circle(x_B, y_B, N) , in_Circle(x_C, y_C, N) , in_Circle(x_D, y_D, N) ]
    # print('Bool = ', Bool)

    if (x_B - x_A) == 2**N :
        if len(set(Bool)) == 1 : return True

    if len(set(Bool)) > 1 : return True
    return False


def within_circle(x, y, N ):
    ''':Description: for a Point (x, y) determine if is within circle with this particular equation
        N - the power of the circle
    :return: True or False, boolean                 '''
    return (x-2**(N-1))**2 + (y - 2**(N-1))**2 <= 2**(2*N-2)

def count_pixels( square, N ) :
    ''':Description: Count how many pixels are inside a square and the Circle with
        that particular equation from above
    :return: int , count                        '''
    count = 0
    for x in range(square[0][0], square[1][0] ) :
        for y in range(square[0][1], square[1][1] ) :
            if within_circle(x, y, N) :
                count += 1
            # print(x, y , '   ', within_circle(x, y, N)  )
    return count


C = lambda x, y, N : ( x - 2**(N-1))**2 + ( y - 2**(N-1) )**2
print()


counter = 0

def quad( square , N ) :    # @ Made by Bogdan Trif @ 2019-01-07, 22:40 --> RECURSION ! IT WORKS !!
    # LESSON REMINDER !!!! IN RECURSION ALWAYS USE VAR modification in the scope of the function !!
    # DO not ASSIGN IT before like :
    # square  = [ (  square[0][0] , midPoint(square)[1] ) , ( midPoint(square)[0], square[1][1] )]
    # and then make the recursive call :   quad( square )   NEVER !!!
    # USE ONLY : quad( [ (  square[0][0] , midPoint(square)[1] ) , ( midPoint(square)[0], square[1][1] )] )

    global counter

    ### BASE CASE, the minimum square  [ (0,0), (2,2) ]
    if ( square[1][0] - square[0][0] ) <= 2 :       # dimension, side of the square
        # print('SQUARE : ', square ,'  ...   do something with it '  )
        if circle_square_intersection(square, N ) :
            counter += 9
        else :
            # AS.append(2)
            counter += 2

        return  ;

    ### CASE 1 - When square is at least [ (0,0),(4,4) ] there is no need to subdivide it
    if not circle_square_intersection( square, N )  :
        if ( square[1][0] - square[0][0] ) < 2**N :
            # print('no intersection : ' , 2 , '   square = ' , square )
            # AS.append(2)
            counter += 2

    ### CASE 2 - When there is an intersection -- SUBDIVIDE it in 4 parts
    if circle_square_intersection( square, N ) or ( square[1][0] - square[0][0] ) == 2**N   :
        # AS.append(1)
        counter += 1

        # top left: x1 = square[0][0]   y1 = midPoint(square)[1]   x2 = midPoint(square)[0]   y2 = square[1][1]
        # print('top left = ', square )
        quad( [ (  square[0][0] , midPoint(square)[1] ) , ( midPoint(square)[0], square[1][1] )], N )

        # top right:   x1 = midPoint(square)[0]   y1 = midPoint(square)[1]   x2 = square[1][0]   y2 = square[1][1]
        # print('top right = ', square  )
        quad( [ ( midPoint(square)[0] , midPoint(square)[1] ) , ( square[1][0], square[1][1] ) ] , N)

        # bottom left :  x1 = square[0][0]  y1 = square[0][1]  x2 = midPoint(square)[0]  y2 = midPoint(square)[1]
        # print('bottom left = ', square )
        quad( [ ( square[0][0] , square[0][1] ) , ( midPoint(square)[0], midPoint(square)[1] ) ], N  )

        # bottom right :  x1 = midPoint(square)[0]  y1 = square[0][1]  x2 = square[1][0] y2 = midPoint(square)[1]
        # print('bottom right = ', square )
        quad( [ ( midPoint(square)[0] , square[0][1] ) , ( square[1][0], midPoint(square)[1] ) ], N  )



N = 15
print('N = ', N )
square = [ (0, 0), (2**N, 2**N) ]

# quad(square, N )


print('\nANSWER : ' ,   counter  )            #   ANSWER : ', 313135496   # Completed in :', 1885.25, 's

t2  = time.time()
print('\n# Completed in :', round((t2-t1),2), 's\n\n')

print('\n======  My SECOND SOLUTION,  Improved RECURSION,   ============\n')
t1  = time.time()

class QuadtreeEncoding():
    def __init__(self, N, square):
        self.N = N
        self.square = square

    def midPoint(self, square) :
        ''':Description: Returns the midpoint of a square of the form :
        [ (x_bottom_left, y_bottom_left, ) , (x_top_right, y_top_right ) ]
        :param square:
        :return:  (x, y) int, midpoint                     '''
        x = square[0][0] + (square[1][0]- square[0][0])//2
        y = square[0][1] + (square[1][1]- square[0][1])//2
        return (x, y )

    def in_Circle (self, x, y, N):
        ''':Description:    Detects if a point x,y is within a circle with equation :
            (x-a)^2 + (x-b)^2 = R^2, where :
                a = 2^(N-1), b = 2^(N-1)  , N- being the exponent power
                R = 2**(2*N-2)

                **(x - 2^(N-1))^2 + (y - 2^(N-1))^2 = 2^(2*N-2)**
        :param N:int, exp power of 2
        :return: boolean, True of False                                     '''

        # print( 'x^2= ',(x - 2**(N-1))**2 , '  ;  y^2= ', ( y - 2**(N-1) )**2 )
        # print('x^2+y^2 = ' , (x - 2**(N-1))**2 + ( y - 2**(N-1) )**2 , ';    R^2 = ' ,2**(2*N-2)  )
        return ( x - 2**(N-1))*( x - 2**(N-1)) + ( y - 2**(N-1) )*( y - 2**(N-1) ) <= 2**(2*N-2)


    def circle_square_intersection(self,  square, N ):       # o(^_^)o   Made by Bogdan Trif @ 2019-01-07; WORKS GREAT !!
        ''':Description: Given the square, we check if  one of the 4 points
            is within the Circle. There 3 cases :
                1.  None of the 4 points is within the circle : return False
                2.  All the 4 points are within the circle : return False
                3.  Between 1 and 3 points are within the circle : return True
                                        A-----B
                                        |          |
                                        |          |
                                        C-----D
        :param square: input [(x1, y1) (x2, y2)]
        :return: boolean : True or False                        '''

        x_A, y_A = square[0][0], square[1][1]-1
        x_B, y_B = square[1][0]-1, square[1][1]-1
        x_C, y_C = square[0][0], square[0][1]
        x_D, y_D = square[1][0]-1, square[0][1]

        # print('x_A, y_A = ' , x_A, y_A )
        # print('x_B, y_B = ' , x_B, y_B )
        # print('x_C, y_C = ' , x_C, y_C )
        # print('x_D, y_D = ' , x_D, y_D )

        Bool = [ in_Circle(x_A, y_A, N) , in_Circle(x_B, y_B, N) , in_Circle(x_C, y_C, N) , in_Circle(x_D, y_D, N) ]
        # print('Bool = ', Bool)

        if (x_B - x_A) == 2**N :
            if len(set(Bool)) == 1 : return True

        if len(set(Bool)) > 1 : return True
        return False


    def within_circle(self, x, y, N ):
        ''':Description: for a Point (x, y) determine if is within circle with this particular equation
            N - the power of the circle
        :return: True or False, boolean                 '''
        return (x-2**(N-1))**2 + (y - 2**(N-1))**2 <= 2**(2*N-2)

    def quad(self,  square , N ) :    # @ Made by Bogdan Trif @ 2019-01-07, 22:40 --> RECURSION ! IT WORKS !!
        # LESSON REMINDER !!!! IN RECURSION ALWAYS USE VAR modification in the scope of the function !!
        # DO not ASSIGN IT before like :
        # square  = [ (  square[0][0] , midPoint(square)[1] ) , ( midPoint(square)[0], square[1][1] )]
        # and then make the recursive call :   quad( square )   NEVER !!!
        # USE ONLY : quad( [ (  square[0][0] , midPoint(square)[1] ) , ( midPoint(square)[0], square[1][1] )] )

        ### BASE CASE, the minimum square  [ (0,0), (2,2) ]
        if ( square[1][0] - square[0][0] ) <= 2 :       # dimension, side of the square
            if circle_square_intersection(square, N ) :
                return 9
            else :
                return 2

        ### CASE 1 - When square is at least [ (0,0),(4,4) ] there is no need to subdivide it
        if not circle_square_intersection( square, N )  :
            if ( square[1][0] - square[0][0] ) < 2**N :
                return 2

        ### CASE 2 - When there is an intersection -- SUBDIVIDE it in 4 parts
        if circle_square_intersection( square, N ) or ( square[1][0] - square[0][0] ) == 2**N  :

            return 1 + self.quad( [ (  square[0][0] , midPoint(square)[1] ) , ( midPoint(square)[0], square[1][1] )], N ) + \
                   self.quad( [ ( midPoint(square)[0] , midPoint(square)[1] ) , ( square[1][0], square[1][1] ) ] , N) +  \
                   self.quad( [ ( square[0][0] , square[0][1] ) , ( midPoint(square)[0], midPoint(square)[1] ) ], N  ) +  \
                   self.quad( [ ( midPoint(square)[0] , square[0][1] ) , ( square[1][0], midPoint(square)[1] ) ], N  )


N = 10
square = [ (0, 0), (2**N, 2**N) ]

Sol = QuadtreeEncoding(N, square)
print('ANSWER = ',Sol.quad(square , N) )

# print( 'ANSWER :   N = ' + str(N) +',       Length = ' ,  quad(square, N ) )


t2  = time.time()
print('\n# Completed in :', round((t2-t1),2), 's\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

''' ===         Tue, 27 Sep 2011, 01:59, tolstopuz, Russia
'''

def solution_toloptuz(n) :


    def f(x, y):
        return (x - 2 ** (n - 1)) ** 2 + (y - 2 ** (n - 1)) ** 2 <= 2 ** (2 * n - 2)

    def q(x, y, n):
        if n == 1:
            return 2
        a, b, c, d = f(x, y), f(x, y + n - 1), f(x + n - 1, y), f(x + n - 1, y + n - 1)
        if a and b and c and d or not a and not b and not c and not d:
            return 2
        n2 = n // 2
        return 1 + q(x, y, n2) + q(x, y + n2, n2) + q(x + n2, y, n2) + q(x + n2, y + n2, n2)

    nn = 2 ** (n - 1)

    return print(1 + q(0, 0, nn) + q(0, nn, nn) + q(nn, 0, nn) + q(nn, nn, nn))

# solution_toloptuz(5)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 2,  Simple and Old Iteration     --------------------------')
t1  = time.time()

''' ==== Thu, 21 Nov 2013, 21:36, Germany
Animus
Reached level 15 with this old one.

The code length is only dependend on the number of mixed pixeled squares (regardless of size). 
So instead of using recursion I just divide each quadrant into stripes of size 2, 4, 8, ... 
From the intersection with the circle line I easily get the number of mixed squares of that size for each stripe.

Runs in 2.2 sec in PyPy.
'''

from math import sqrt


def solution_animus(N):

    R=2**(N-1)
    su=9
    for adx in [0,1]:
        for ady in [0,1]:
            for i in range(1,N ):
                dd = 2**i
                dx = 0
                while dx < R :
                    y1 = int(sqrt(R*R-(dx+adx)*(dx+adx)))-ady
                    if y1 == R :
                        y1 = R-1
                    y2=int( sqrt(R*R-(dx+adx+dd-1)*(dx+adx+dd-1))) + 1-ady
                    su+=7*(y1//dd+1-y2//dd)
                    dx += dd

    print( su)
    return su

# solution_animus(5)



t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 3,   Multiprocessing, Must fix it --------------------------')
t1  = time.time()

from multiprocessing import Pool
from numbers import Integral

def quadrant( xc, yc, r, q) :
    # This function calculates the encoded length of one of the
    # first four subsquares of the circle image. The subsquares are
    # treated as if it is transformed such that its farthest corner
    # from the center of the circle is (0, 0), and the center is
    # (xc, yc). r and q is cached values for the radius and the square
    # of the radius.
    def rec(xb, yb, xe, ye, sym):
        # (xb, yb): bottom-left, (xe, ye): top-right
        far_x = xb - xc
        far_y = yb - yc
        near_x = xe - xc
        near_y = ye - yc
        if far_x * far_x + far_y * far_y <= q or \
                near_x * near_x + near_y * near_y > q:
            return 2        # '10' or '11'
        elif xe - xb == 1:  # 2-by-2 square
            return 9        # '0wwxxyyzz'
        else:
            xp = (xb + xe + 1) >> 1
            yp = (yb + ye + 1) >> 1
            # arguments for each subsquares
            sub0 = rec(xb, yp, xp - 1, ye, False)    # top-left
            sub1 = rec(xp, yp, xe, ye, sym)          # top-right
            sub2 = rec(xb, yb, xp - 1, yp - 1, sym)  # bottom-left
            # bottom-right
            sub3 = sub0 if sym else rec(xp, yb, xe, yp - 1, False)
            return 1 + sub0 + sub1 + sub2 + sub3
    return rec(0, 0, r - 1, r - 1, xc == yc)

def circle_encoded_length(n, serial=False):
    if n < 0 or not isinstance(n, Integral):
        message = 'n must be a non-negative integer; given %s' % str(n)
        raise ArithmeticError(message)
    if n == 0:
        return 2  # '10'
    m = n - 1
    r = 1 << m  # the radius of the circle
    q = r << m  # the square of the radius of the circle
    args = [(r, r, r, q), (r - 1, r - 1, r, q), (r, r - 1, r, q)]
    if not serial:
        pool = Pool()
        result = pool.map_async(quadrant, args).get()
    else:
        result = [quadrant(x) for x in args]
    return 1 + sum(result) + result[2]

def solve():
    print(circle_encoded_length(12))

# solve()

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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




