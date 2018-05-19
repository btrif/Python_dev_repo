#  Created by Bogdan Trif on 31-10-2017 , 10:23 PM.
# © o(^_^)o  Solved by Bogdan Trif  @       Completed on Fri, 3 Nov 2017, 16:46
#The  Euler Project  https://projecteuler.net
'''
                Obtuse Angled Triangles         -           Problem 210

Consider the set S(r) of points (x,y) with integer coordinates satisfying |x| + |y| ≤ r.
Let O be the point (0,0) and C the point (r/4,r/4).
Let N(r) be the number of points B in S(r), so that the triangle OBC has an obtuse angle,
i.e. the largest angle α satisfies 90°<α<180°.

So, for example, N(4) = 24              and
                        N( 8 ) = 100.

What is N ( 1,000,000,000 )  B( 10^9 ) =  ?


'''
import time, zzz
from math import sqrt
# import numpy as np
# import matplotlib.pyplot as plt


def Triangular(n):
    '''  Computes the triangular number of n '''
    return n*(n+1)//2

def is_obtuze_triangle( p1, p2, p3 ) :
    a = sqrt( ( p1[0] - p2[0])**2  + ( p1[1] - p2[1])**2  )
    b = sqrt( ( p1[0] - p3[0])**2  + ( p1[1] - p3[1])**2  )
    c = sqrt( ( p2[0] - p3[0])**2  + ( p2[1] - p3[1])**2  )

    # print(a, b, c)
    X =  [ a, b , c ]
    z = max(a, b, c )
    X.remove(z)
    # print('X : ' ,X, '        max = ', z)
    # print( 'x^2+y^2 = ',(X[0]**2 + X[1]**2) , ' ;   z^2 =  ', z*z)
    if  ( (X[0]**2 + X[1]**2) <  z*z ) and abs((X[0]**2 + X[1]**2) -z*z) > 1e-10 :

        return True

    return False

print( is_obtuze_triangle( (0,0) , (1, 1), (0, 1)  ) )

from math import pi, sqrt, ceil, floor
def Gauss_circle_problem(r):      # Inefficient algorithm
    '''  Implementation of this # http://www.wolframalpha.com/input/?i=gauss%E2%80%99s+circle+problem
    http://mathworld.wolfram.com/GausssCircleProblem.html               '''
    S = 1
    i = 0
#     while floor((r*r) /(4*i+1)) != floor((r*r) /(4*i+3)) :
    while  floor((r*r) /(4*i+1)) != 0 :

        S += 4* (  floor((r*r) /(4*i+1)) - floor((r*r) /(4*i+3))  )
#         print(str(i)+'.    ',S , '      ', floor((r*r) /(4*i+1)), floor((r*r) /(4*i+3))  )
        i+=1

        if floor((r*r) /(4*i+1)) == 0 :
            print(str(i)+'.    ',S , '      ', floor((r*r) /(4*i+1)), floor((r*r) /(4*i+3)))

    return S


# print('\nGauss_circle_problem = ' ,Gauss_circle_problem(3557 ) )


def Heronian_angles_area_after_coordinates( p1, p2, p3 ) :
    from math import sqrt, cos, sin, pi, acos, asin
    a = sqrt( (p1[0]-p2[0])**2 +  ( p1[1]-p2[1] )**2  )
    b = sqrt( (p1[0]-p3[0])**2 +  ( p1[1]-p3[1] )**2 )
    c = sqrt(  (p2[0]-p3[0])**2 +  ( p2[1]-p3[1] )**2 )
    angleC =  acos( ( a**2 + b**2 - c**2) / (2*a*b) )*180/pi
    angleA =  acos(( b**2 + c**2 - a**2) / (2*b*c))*180/pi
    angleB =  acos( (c**2 + a**2 - b**2) / (2*c*a))*180/pi
    return angleC, angleB, angleA , angleC+ angleB+ angleA



print('\n--------------------------TESTS------------------------------')
t1  = time.time()


def manual_lattice_points_inside_circle(r) :
    cnt = 0
    for x in range(0, r +1 ) :
        for y in range(0, r +1 ) :
            if x*x + y*y <= r*r :
                cnt +=1

    return (cnt - int(r)-1 )*4 +1


def above_y1(x, y):
    y1 = lambda x : -x
    if y > y1(x) :
        return True
    return False

def under_y2(x, y, d):
    y2 = lambda x, d : -(x- d )
    if y < y2(x, d) :
        return True
    return False


def brute_force_acknoledgement( rad , plot = False ) :
    cnt = 0
    circle_cnt = 0
    y1 = lambda x : -x
    d = rad/2
    y2 = lambda x, d : -(x- d )

    X, Y = [], []


    for i in range(-rad , rad+1 ) :
        for j in range(-rad+abs(i) , rad-abs(i)+1 ) :
            if i != j :
                if is_obtuze_triangle( (0,0), (rad//4, rad//4 ), (i,j)  ) :
                    cnt +=1
                    # print(str(cnt)+ '.          x, y =  ' , i , j )
                    ### Needed for plotting, DO NOT DELETE
                    X.append(i) ; Y.append(j)

                    if   above_y1(i, j)  and  under_y2(i, j, d)   :
                        # print('circle points :     x= ', i,'       y= ' ,j ,'        y1 =  ', y1(i) , '    y2 = ' , y2(i, d)  )
                        circle_cnt += 1

    if plot == True :
        ######     START PLOT    ###########
        fig = plt.figure(figsize=(12 , 12))
        ax = fig.add_subplot( 1,1,1    ) #, aspect='equal')
        plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)


        major, minor, x1, x2, y1, y2 = 1, 10, -rad, rad, -rad, rad

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

        data = [i for i in range(-rad, rad+1 )] , [i for i in range(-rad, rad+1 )]
        plt.plot( data[0] , data[1], color ='gold' , marker = 'D' , linestyle = '--')

        data1 = [i for i in range(0, rad//4+1 )] , [i for i in range(0, rad//4+1 )]
        plt.plot( data1[0] , data1[1], color='r', linewidth=4.0 )

        data2 = [i for i in range(-rad, rad+1 )] , [i for i in range(rad, -rad-1, -1 )]
        plt.plot( data2[0] , data2[1],  color='olive' , linestyle='-' , linewidth = 1.0 )

        data3 = [i for i in range(-rad//2, rad+1 )] , [i for i in range(rad, -rad//2-1, -1 )]
        plt.plot( data3[0] , data3[1],  color='olive' , linestyle='-' , linewidth = 1.0 )

        plt.scatter(X, Y, color = 'slateblue', marker = 'o' , s = 1  )

        plt.show()
        ###########         END PLOT        #############

    print('\nCircle points = ', circle_cnt )
    print('without circle = ', cnt-circle_cnt )
    print('Result = ', cnt  )

    return cnt

# brute_force_acknoledgement(  10**3 , False  )

# @2017-11-01 - I left here that I must compute integer lattice points inside the circle  with radius r//8 == 1.25*10**8
# https://en.wikipedia.org/wiki/Sum_of_squares_function
# https://en.wikipedia.org/wiki/Gauss_circle_problem
# http://www.wolframalpha.com/input/?i=gauss%E2%80%99s+circle+problem
# http://oeis.org/A000328/b000328.txt
# http://mathworld.wolfram.com/GausssCircleProblem.html


t2  = time.time()
print('\n# Completed in :', round((t2-t1) , 4), 's\n\n')

print('\n=============   My FIRST SOLUTION,  with pypy - 1.7 min     ,python 8 min  ===============\n')
t1  = time.time()

# http://www.wolframalpha.com/input/?i=gauss%E2%80%99s+circle+problem

def manual_lattice_points_inside_circle(orig_rad) :     #  orig_rad must be multiple of 8   !!!!!!!!!
    '''  :Description: An O(n)  algorithm to calculate lattice points inside circle '''

    from math import floor, sqrt, ceil

    rad = orig_rad//8

    sub =  rad-1
    print(rad , sub , 2*rad*rad)
    cnt = 0
    for x in range(1, int(floor(rad*sqrt(2))) +1 ) :
        if x%10**7 == 0 : print(x//10**7)
        ys = (2*rad*rad - x*x)
        y = sqrt(ys)
        if floor(y) == y :
            cnt += int(floor(y))
            # print('x = ', x ,'    y = ', floor(y) , '      y = ',(y) ,'      ys =  ' , ys ,'      SPEC case')
        else :
            cnt += int(floor(y)+1)
            # print('x = ', x ,'    y = ', floor(y)+1 , '      y = ',(y) ,'      ys =  ' , ys , '      usual case')

    print('\nIntermediar counting = ' , cnt*4 - sub*2 )
    return cnt*4 - sub*2



def obtuse_triangles( rad ) :
    S = 0
    one  =  ( Triangular(rad//2) * 4 - rad ) *2
    two = ( Triangular(rad//4) * 4 - rad//4 *2 ) * 4
    circle  = manual_lattice_points_inside_circle( rad )
    print('one = ',one, '    two = ', two , '   circle = ', circle )
    S = (one+ two + circle)
    print('without circles = ', one+two)

    return S

# print('\nObtuse_triangles =  ' , obtuse_triangles(    10**9   ) )
#   Answer : 1598174770174689458        # Completed in : 510.3932 s







t2  = time.time()
print('\n# Completed in :', round((t2-t1)/60 , 4 ) , ' mins\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ==== Wed, 5 Jun 2013, 16:38, tom.wheldon, England
# Until I looked in the forum I thought this was quite a simple problem.
# It appears that I unintentionally avoided the precision problems by using ceiling instead of floor.

def solution1():
    from math import sqrt,ceil

    r = 10**9
    radius = sqrt(r*r/32)
    r2 = r*r/32

    ans = 3*r*r//2
    quad = 0
    for x in range(1,ceil(radius)):
        quad += ceil(sqrt(r2 - x*x))
    ans += 4*quad - 2*r//8 + 2

    return ans

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 2,  Gauss Circle Problem,  Quite SLOW  --------------------------')
t1  = time.time()


# ==== hu, 25 Sep 2014, 19:13, ChopinPlover, Taiwan
# Gauss circle problem + Problem 233

class PrimeTable():
    def __init__(self, bound):
        self.bound = bound
        self.primes = []
        self._sieve()

    def _sieve(self):
        visited = [False] * (self.bound + 1)
        visited[0] = visited[1] = True
        for i in range(2, self.bound + 1):
            if not visited[i]:
                self.primes.append(i)
            for j in range(i + i, self.bound + 1, i):
                visited[j] = True

class Factorization():
    def __init__(self):
        self.prime_table = PrimeTable(100)

    def get(self, n):
        d = n
        rv = []
        for i in range(len(self.prime_table.primes)):
            p = self.prime_table.primes[i]
            if d == 1 or p > d:
                break
            count = 0
            while d % p == 0:
                d = d // p
                count += 1
            if count > 0:
                rv += [(p, count)]
        if d > 1:
            raise Exception('prime factor should be small')
        return rv

class ProjectEulerProblem233():
    def __init__(self):
        self.factorization = Factorization()

    def get(self, n):
        rv = 4
        factors = self.factorization.get(n)
        for p, e in factors:
            if p % 4 == 1:
                rv *= (2 * e + 1)
        return rv

class GaussCircleProblem():
    def get(self, n):
        N = 2 * (n // 8)**2
        floor_r = self._int_sqrt(N)
        sum = 0
        for x in range(floor_r + 1):
            sum += self._int_sqrt(N - x**2)
        return 4 * sum + 1

        n = N
        sum = 0
        for i in range(n // 4 + 1):
            sum += n // (4*i + 1) - n // (4*i + 3)
        return 1 + 4 * sum

    """
    http://www.codecodex.com/wiki/Calculate_an_integer_square_root
    """
    def _int_sqrt(self, n):
        guess = (n >> n.bit_length() // 2) + 1
        result = (guess + n // guess) // 2
        while abs(result - guess) > 1:
            guess = result
            result = (guess + n // guess) // 2
        while result * result > n:
            result -= 1
        return result

class Problem():
    def __init__(self):
        self.gauss_circle_problem = GaussCircleProblem()
        self.project_euler_problem = ProjectEulerProblem233()

    def solve(self):
        self.validate_by_projecteuler_forum()
        print(self.get(10**9))

    def validate_by_projecteuler_forum(self):
        assert(self.benchmark(8) == 100)
        assert(self.get(8) == 100)
        assert(self.get(1000) == 1597880)
        assert(self.get(2000) == 6392158)
        assert(self.get(10000) == 159814790)
        assert(self.get(20000) == 639264906)
        assert(self.get(100000) == 15981722482)
        assert(self.get(1000000) == 1598174519142)

    def get(self, n):
        square = 2 * n**2 + 2 * n + 1
        stripped = (n + 1) * (n // 4 + 1) + n * (n // 4)
        gauss_circle = self.gauss_circle_problem.get(n)
        on_circle = self.project_euler_problem.get(n // 4)
        line = n + 1
        result = square - stripped + gauss_circle - on_circle - line + 2
        print(n, square, stripped, gauss_circle, on_circle, line, result)
        return result

    def benchmark(self, n):
        import itertools
        square, stripped, gauss_circle, on_circle, line = 0, 0, 0, 0, 0
        for x, y in itertools.product(range(-n, n+1), repeat=2):
            if abs(x) + abs(y) > n:
                continue
            # On square
            square += 1
            # On the line
            if x == y:
                line += 1
            # On the stripped area
            if x + y >= 0 and x + y <= n // 2:
                stripped += 1
            # On the circle
            if (x - n // 8)**2 + (y - n // 8)**2 == 2 * (n // 8)**2:
                on_circle += 1
            # Inside the circle
            if (x - n // 8)**2 + (y - n // 8)**2 <= 2 * (n // 8)**2:
                gauss_circle += 1
        result = square - stripped + gauss_circle - on_circle - line + 2
        print(n, square, stripped, gauss_circle, on_circle, line, result)
        return result


# problem = Problem()
# problem.solve()




t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 3, VEry simple  --------------------------')
t1  = time.time()


# ===Mon, 19 Jan 2009, 17:28, tolstopuz, Russia

def toloptuz() :
    import math

    n = 10 ** 9

    rr = n ** 2 // 32

    c = 0

    sq = int(math.sqrt(rr))

    for i in range(int(math.sqrt(rr)) + 1):
        while sq ** 2 + i ** 2 >= rr:
            sq -= 1
        c += sq

    return print(4 * c - (n - 1) // 8 * 2 + 3 * n ** 2 // 2)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ==== Mon, 23 Nov 2009, 20:17, yurip , USA
# Python, just under 1m on a higher-end box.

def solution4():
    from math import sqrt
    N=10**9
    cnt = 0
    T = N**2/32
    for x in range(N//8+1, int(N*(2**.5)//8+1)):
        y = math.sqrt(T - x**2)
        yi = int(y)
        if y == yi:
            cnt += 2*yi - 1
        else:
            cnt += 2*yi + 1
    return print (cnt*4 + N/4*(N/4+1) - 2 + N**2*3/2)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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




