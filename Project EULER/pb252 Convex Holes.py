#  Created by Bogdan Trif on 16-10-2017 , 10:35 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                Convex Holes        -       Problem 252
Given a set of points on a plane, we define a convex hole to be a convex polygon having as vertices
any of the given points and not containing any of the given points in its interior
(in addition to the vertices, other given points may lie on the perimeter of the polygon).

As an example, the image below shows a set of twenty points and a few such convex holes.
The convex hole shown as a red heptagon has an area equal to 1049694.5 square units,
which is the highest possible area for a convex hole on the given set of points.


For our example, we used the first 20 points (T2k−1, T2k), for k = 1,2,…,20,
produced with the pseudo-random number generator:

S0	= 	290797
Sn+1	= 	Sn2 mod 50515093
Tn	= 	( Sn mod 2000 ) − 1000
i.e. (527, 144), (−488, 732), (−454, −947), …

What is the maximum area for a convex hole on the set containing the first 500 points in the pseudo-random sequence?
Specify your answer including one digit after the decimal point.

'''
import time, zzz
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import mpl_scatter_density

def pseudo_random_number_generator():           # EFFICIENT GENERATOR
    '''     s_0 = 290797
            s_(n+1) = s_n×s_n (modulo 50515093)
            t_n = s_n (modulo 2000) - 1000                 '''
    s = 290797
    while True :
        s = pow(s, 2 , 50515093 )
        t = (s % 2000 ) - 1000
        yield t


print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def plot_points1():

    fig = plt.figure(num=None, figsize=(12, 12), dpi=80, facecolor='w', edgecolor='k')
    # ax = fig.add_subplot(1,1,1)
    ax = fig.add_subplot(1, 1, 1, projection='scatter_density')

    A = pseudo_random_number_generator()
    B =[]

    hmax, vmax = 1000 , 1000
    for g in range(500):
        x, y = next(A), next(A)
        B.append((x,y))
        print(x,y)



    #     if hmax < abs(x) :
    #         hmax = abs(x)
    #     if vmax < abs(y) :
    #         vmax = abs(y)
    #
    # print('hmax , vmax = ', hmax, vmax)

    # x0 = [i[0] for i in B]
    # y0 = [i[1] for i in B]
    # ax.scatter_density(x0, y0 )

    def grid(hmax , vmax):
        # major ticks every 5, minor ticks every 1
        major_ticks = np.arange(-hmax, hmax, 100)
        minor_ticks = np.arange(-vmax, vmax, 20)

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

    grid(hmax , vmax)


    plt.axis([-hmax-1, hmax+1, -vmax-1, vmax+1 ])
    plt.grid(True)

    for k in B :
        plt.scatter(k[0], k[1], s=5 , c='red' , marker="s")



    plt.show()

# plot_points1()


def plot_points2():
    A = pseudo_random_number_generator()
    B =[]

    hmax, vmax = 1000 , 1000
    for g in range(500):
        x, y = next(A), next(A)
        B.append((x,y))
        # print(x,y)


    fig = plt.figure(num=None, figsize=(12, 12), dpi=80, facecolor='w', edgecolor='k')
    ax = fig.add_subplot(1,1,1)

    def grid(hmax , vmax):
        # major ticks every 5, minor ticks every 1
        major_ticks = np.arange(-hmax, hmax, 100)
        minor_ticks = np.arange(-vmax, vmax, 20)

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

    grid(hmax , vmax)


    plt.axis([200, 800, -1000, -500 ])
    plt.grid(True)

    for k in B :
        if k[1] < -500 and 200 < k[0] < 800 :
            print('points :     (', k[0] , ',' , k[1],')' )
            plt.scatter(k[0], k[1], s=5 , c='red' , marker="s")

    plt.show()

# plot_points2()


https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.Delaunay.html
https://docs.scipy.org/doc/scipy-0.19.1/reference/generated/scipy.spatial.ConvexHull.html
https://www.google.ro/search?dcr=0&q=hull+convex&oq=hull+convex&gs_l=psy-ab.3..0l3j0i22i30k1l7.2170.3072.0.3680.7.7.0.0.0.0.138.625.5j2.7.0....0...1.1.64.psy-ab..0.7.624...0i67k1j0i10k1.0.vQzL5aKjgGU
https://en.wikipedia.org/wiki/Convex_hull
http://scipy-cookbook.readthedocs.io/items/Finding_Convex_Hull.html
https://www.google.ro/search?dcr=0&q=scipy+convex+hull&oq=scipy+convex&gs_l=psy-ab.3.0.0l7j0i22i30k1l3.62986.64672.0.65521.12.12.0.0.0.0.107.1012.11j1.12.0....0...1.1.64.psy-ab..0.12.1007...0i67k1.0.wc672LvISlU

lst = [(222, -659), (306, -615), (343, -756), (417, -604), (532, -873), (604, -603), (644, -630), (682, -944), (700, -933), (720, -780)]

T1 = [ [(222, -659), (306, -615), (343, -756)], [(306, -615), (343, -756), (417, -604)] , [(343, -756), (417, -604),(532, -873) ],
       [(417, -604),(532, -873), (604, -603) ], [ (532, -873), (604, -603), (682, -944) ],[ (604, -603), (682, -944), (644, -630) ],
       [  (682, -944), (644, -630), (700, -933) ] , [ (644, -630), (700, -933),  (720, -780) ]                  ]

lst2 = [( -582 ,974), ( -553 , 900 ), ( -389 , 938 ), ( -342 , 707 ), ( -282 , 671 ), ( -228 , 816 ),( -105 , 569 ),( -36 , 652 ), ( 17 , 553 )    ]

T2 = [ [ ( -582 ,974), ( -553 , 900 ), ( -389 , 938 ) ], [( -553 , 900 ), ( -389 , 938 ),( -342 , 707 ) ] ,
         [( -389 , 938 ),( -342 , 707 ),  ( -228 , 816 ) ] , [( -342 , 707 ),  ( -228 , 816 ), ( -282 , 671 ) ],
         [ ( -228 , 816 ), ( -282 , 671 ),( -36 , 652 ) ] , [ ( -282 , 671 ),( -36 , 652 ), ( -105 , 569 ) ],
         [( -36 , 652 ), ( -105 , 569 ), ( 17 , 553 ) ] ]

T3 = [ [(222, -659), (306, -615), (343, -756)], [(306, -615), (343, -756), (417, -604)] , [(343, -756), (417, -604), (604, -603) ],
       [(343, -756), (604, -603),(532, -873) ], [(604, -603),(532, -873), (644, -630)], [(532, -873), (644, -630), (682, -944)],
       [(644, -630), (682, -944), (700, -933)], [(644, -630), (700, -933), (720, -780) ]       ]

def compute_Heron_area_after_coordinates( p1, p2, p3 ) :
    a = sqrt( (p1[0]-p2[0])**2 +  ( p1[1]-p2[1] )**2  )
    b = sqrt( (p1[0]-p3[0])**2 +  ( p1[1]-p3[1] )**2 )
    c = sqrt(  (p2[0]-p3[0])**2 +  ( p2[1]-p3[1] )**2 )
    s = (a+b+c)/2

    return sqrt( s*(s-a)*(s-b)*(s-c) )

def polygon_area(triang_list) :
    A = 0
    for cnt, coord in enumerate( triang_list ) :
        area = compute_Heron_area_after_coordinates( coord[0], coord[1], coord[2]  )
        A += area

        print(str(cnt+1)+'.        area= ', area )

    return print('\nTotal area = ', A , '      ', round(A, 1),'\n')


# polygon_area(T1)
polygon_area(T2)
polygon_area(T3)

# A1 = Total area =  97588.99999999997
# A2 = Total area =  82332.0        82332.0

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




