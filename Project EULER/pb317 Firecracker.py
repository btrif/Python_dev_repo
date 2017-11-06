#  Created by Bogdan Trif on 27-10-2017 , 6:21 PM.
# © o(^_^)o  Solved by Bogdan Trif  @       Completed on Sun, 29 Oct 2017, 21:39
#The  Euler Project  https://projecteuler.net
'''
                                Firecracker         -       Problem 317

A firecracker explodes at a height of 100 m above level ground.
It breaks into a large number of very small fragments, which move in every direction;
all of them have the same initial velocity of 20 m/s.

We assume that the fragments move without air resistance, in a uniform gravitational field with g=9.81 m/s^2.

Find the volume (in m^3) of the region through which the fragments move before reaching the ground.
Give your answer rounded to four decimal places.


'''
import time, zzz
from math import sin, cos, sqrt, pi
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

def plot_parabola(a,b,c) :

    time = []
    Y = []

    # for t in range(0, 13000, 1 ):
    for t in range(0, 1400, 1 ):
        y =  a * (t/10)**2 + b *(t/10) + c
        time.append(t/10)
        Y.append(y)

    ax.plot( time , Y )




g = 9.81         #  m/s^2
v_init = 20          # m/s
h0 = 100        #  m

# v_init = 100          # m/s
# h0 = 50        #  m

def quadratic(a, b, c):
    x1 = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b * b - 4 * a * c)) / (2 * a)
    return x1, x2

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def get_trajectory_points( α, h0, v_init, g ) :

    v0 = [  v_init * cos(α*pi/180), v_init * sin(α*pi/180)   ]
    # print(' initial velocity  v_x , v_y =   ', v0 ,'            check:' ,   sqrt(v0[0]**2 + v0[1]**2) )

    a, b, c = -g/2 , v0[1], h0
    t1, t2 = quadratic(a,b,c)

    # print('t1, t2 =  ', t1, t2)

    t_total = max(quadratic(a,b,c))

    # print('t_total   =  ', t_total, '     ( total time, the missile hits the ground )' )


    x_max = t_total * v0[0]

    t_mid = -b/(2*a)
    # print('t_mid = ' , t_mid ,'s        ( time at which y= y_max , KE=0,  after rising just before falling to ground )')

    y_max = a* t_mid**2 + b*t_mid + c
    x_mid = v0[0] * t_mid


    # print('y_max = ', y_max , '      x_mid = ', x_mid  ,'    m              (maximum height ) ')

    # print('x_max = ', x_max , '    m           (maximum x distance travelled ) ')

    return x_mid , y_max , x_max



def get_parabola_a_b_c(x_mid, y_max, x_max):
    A = np.array([ [ -x_mid**2, 1], [ x_max**2 - 2*x_max*x_mid, 1 ] ])
    B = np.array([ y_max, 0 ])
    a, c = np.linalg.solve(A,B)

    b = -x_mid*2*a
    return a, b, c

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()


fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1,1,1 ) #, aspect='equal')


def my_solution(max_angle, min_angle, step , plot = False) :


    def grid( major, minor, x1, x2, y1, y2):
        # major ticks every 5, minor ticks every 1
        major_ticks = np.arange(x1, x2, major)
        minor_ticks = np.arange(y1, y2, minor)

        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        ax.set_yticks(major_ticks)
        ax.set_yticks(minor_ticks, minor=True)

        # and a corresponding grid
        ax.grid(which='both')


        # or if you want differnet settings for the grids:
        # ax.grid(which='minor', alpha=0.2)
        ax.grid(which='minor', alpha=0.8)
        ax.grid(which='major', alpha=1)


    yM, xM = 0, 0
    ratio = -1/step
    for alpha in range( int(max_angle*ratio) , int(min_angle*ratio), int(step*ratio) ) :

        alpha = alpha/ratio

        x_mid , y_max , x_max = get_trajectory_points( alpha, h0, v_init, g )
        print('\nα =  ', alpha , '         x_mid , y_max , x_max  =  ', x_mid , y_max , x_max )
        print('-------------------------------')


        if y_max > yM :        yM = y_max
        if x_max > xM :     xM = x_max

        ax.grid(which='both')
        ax.axis('equal')
        x1 , x2, y1, y2 = 0 , 130, -1, 120
        # x1 , x2, y1, y2 = 0 , 1300, -1, 600
        plt.xlim([x1 , x2])
        plt.ylim([y1, y2])
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        grid(10 , 50, x1, x2, y1, y2)
        # grid(100 , 20, x1, x2, y1, y2)


        a, b, c = get_parabola_a_b_c(x_mid , y_max , x_max )
        plot_parabola(a, b, c)

    print('\ny_max = ', yM, '       x_max = ', xM)


    a2, b2, c2 = get_parabola_a_b_c(0 , yM , xM )
    plot_parabola(a2, b2, c2)


    yM =  120.38735983690111
    a = -yM/(xM)**2
    G = lambda y : pi*(y - yM)/a
    I = integrate.quad(G, 0, yM)

    print('---'*30)
    print('\nVolume calculated with scipy.integrate.quad paraboloid of rotation   = ',  I ,'          ', round(I[0], 4 ) )

    print('---'*30)
    V = (pi/2)*yM * xM**2

    print('\nVolume calculated with formula of paraboloid of rotation  = ', V , round(V , 4) )

    H = lambda y :  pi*  ( ((2*v_init**2)/g)  * ( ( v_init**2/(2*g) + h0 ) - y  )  )
    J = integrate.quad( H , 0, yM )

    print('---'*30)

    # https://de.wikipedia.org/wiki/Wurfparabel#Einh.C3.BCllende_Wurfparabel
    print('\n Volume calculated with Envelope of the throwing parabola with common initial velocity \n'
          'J = ', J, '             ANSWER  =  ',  round(J[0], 4) )

    if plot == True :    plt.show()

    return round(V, 4)

my_solution(90, 0, -1, True)      #   ANSWER  =   1856532.8455
# my_solution(22.5, 22.3, -0.001, True )      #   ANSWER  =   1856532.8455

# https://www.desmos.com/calculator
# https://math.stackexchange.com/questions/1049239/how-to-find-the-equation-for-a-parabola-for-which-you-are-given-two-points-and-t
# @2017-10-28 - I am off with the required result by a factor of 10
# https://de.wikipedia.org/wiki/Wurfparabel#Einh.C3.BCllende_Wurfparabel

t2  = time.time()
print('\n# Completed in :', round((t2-t1) , 2), 's\n\n')



# WRONG : Volume of paraboloid of rotation  =  265280.1814506931 265280.1815


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




