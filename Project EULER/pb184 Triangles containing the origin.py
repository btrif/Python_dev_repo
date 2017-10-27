#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                Triangles containing the origin         -       Problem 184

Consider the set Ir of points (x, y) with integer co-ordinates in the interior of the circle with radius r,
centered at the origin, i.e. x**2 + y**2 < r**2 .

For a radius of 2, I2 contains the nine points (0,0), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1) and (1,-1).
There are eight triangles having all three vertices in I2 which contain the origin in the interior.
Two of them are shown below, the others are obtained from these by rotation .

For a radius of 3, there are 360 triangles containing the origin in the interior and having all vertices in I3
and for I5 the number is 10600 .

How many triangles are there containing the origin in the interior and having all three vertices in I105 ?


'''
import time, zzz
from pylab import plt, np
import itertools, collections


# How many point inside I105 ?
def Quad_I_points(lim) :
    cnt, P  = 0, []
    for x in range(0, lim ):
        for y in range(0, lim ):
            r = (x**2+y**2)**(1/2)
            if r > lim : break
            else :
                cnt+=1
                # print(str(cnt)+'.         x=', x,'     y=' ,y , '    radius = ', r,   )
                P.append((x,y))
    P.pop(0)
    # print('\n',P)
    return P

def cartesian_to_barycentric(x1, y1, x2, y2, x3, y3):
    """Convert cartesian coordinates to barycentric coordinates and return all > 0.
    Reference: https://en.wikipedia.org/wiki/Barycentric_coordinate_system_(mathematics)
    """
    if (x1==x2==0) or (x1==x3==0) or (x2==x3==0) : return False
    if (y1==y2==0) or (y1==y3==0) or (y2==y3==0) : return False
    if ( x1==-x2 and y1==-y2 ) or ( x1==-x3 and y1==-y3 ) or ( x2==-x3 and y2==-y3 ) : return False

    try :
        alpha = (((y2 - y3) * (0 - x3) + (x3 - x2) * (0 - y3)) /   ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)))
    except :
        alpha = 10**15
        ZeroDivisionError
    try :
        beta = (((y3 - y1) * (0 - x3) + (x1 - x3) * (0 - y3)) /   ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)))
    except :
        beta = 10**15
        ZeroDivisionError

    gamma = 1 - alpha - beta
    # print('alpha=', alpha, '    beta=', beta, '   gamma=', gamma)
    if gamma < 1e-10 : return False

    return alpha > 0 and beta > 0 and gamma > 0

def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(0.5 * (-y2*x3 + y1*(-x2+x3) + x1*(y2-y3)+ x2*y3))

def make_abs_coord( t1, t2, t3 ):
    A = [ tuple([ abs(i)for i in t1]), tuple([ abs(i)for i in t2])
         , tuple([ abs(i)for i in t3]) ]
    A = sorted(A)[::-1]
    A = [ i for j in A for i in j ]
#     print( ''.join(str(i)for i in A) )
    A = ''.join(str(i)for i in A)
    return int(A)

def relative_center(x1, y1, x2, y2, x3, y3 ):
    ''':Description: calculates the relative center of a triangle.
        In some cases the area of a triangle can be the same but they are shifted. However, the relative center
        changes thus making those triangles different.
    :param x1, y1, x2, y2, x3, y3: ints, the Cartesian points of the triangle
    :return: int, composed of the squares of  x1**2+y1**2, x2**2+y2**2, x3**2+y3**2 joined    '''

    lst = sorted([ x1*x1+y1*y1, x2*x2+y2*y2, x3*x3+y3*y3])[::-1]
    lst = ''.join(str(i)for i in lst)
    return int(lst)

def get_triangle_sides(x1, y1, x2, y2, x3, y3):
    ''':Scope: Given the set cartesian points of the triangle, computes its a, b, c sides
    :param: x1, y1, x2, y2, x3, y3
    :return: a,b,c - the sides of the triangle    '''
    a = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    b = ((x3-x2)**2 + (y3-y2)**2)**(1/2)
    c = ((x3-x1)**2 + (y3-y1)**2)**(1/2)
    return round(a, 4), round(b,4), round(c,4)

from math import sqrt
# (1, 0), (-1, 2), (-2, -1)
def isoscel_triangle_8_symmetry( p1,  p2, p3  ) :
    ''' Returns True if it is a 8 symmetry, Return False if it is a 4 symmetry '''

    rel_p1 = p1[0]**2 + p1[1]**2
    rel_p2 = p2[0]**2 + p2[1]**2
    rel_p3 = p3[0]**2 + p3[1]**2
    # print('relative centers : ' , rel_p1, rel_p2, rel_p3 )
    if len({rel_p1, rel_p2, rel_p3} ) ==3 :
        return True

    if rel_p1 == rel_p2 : rel_p = rel_p3
    if rel_p2 == rel_p3 : rel_p = rel_p1
    if rel_p1 == rel_p3 : rel_p = rel_p2

    # print('the unique relative center : ', rel_p)

    # first we find the point of the equal edges
    a = round(sqrt( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 ),4)
    b = round(sqrt( (p2[0]-p3[0])**2 + (p2[1]-p3[1])**2 ),4)
    c = round(sqrt( (p1[0]-p3[0])**2 + (p1[1]-p3[1])**2 ),4)
    # print( a , b , c)

    if a == b :  P = p2
    if b == c :  P = p3
    if a == c :  P = p1
    # print('the 2 equal edges Point is : ', P)
    # relative center, if the 2 equal edges point relative center length is unique => 4 symmetry
    # if not => 8 symmetry
    if ( P[0]**2 + P[1]**2 ) == rel_p :
        return False

    return True


# isoscel_triangle_8_symmetry( (2, 1) ,(-2, 2) ,(-1, -2)    )


def plot_triangle(A, B, C):
    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(1,1,1 ) #, aspect='equal')

    def grid(major,minor, x1, x2, y1, y2):
        # major ticks every 5, minor ticks every 1
        major_ticks = np.arange(x1, x2, major)
        minor_ticks = np.arange(y1, y2, minor)

        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        ax.set_yticks(major_ticks)
        ax.set_yticks(minor_ticks, minor=True)

        # and a corresponding grid
        # ax.grid(which='both')


        # or if you want differnet settings for the grids:
        # ax.grid(which='minor', alpha=0.2)
        ax.grid(which='minor', alpha=0.8)
        ax.grid(which='major', alpha=1)


    ax.grid(which='both')
    ax.axis('equal')


    x1 , x2, y1, y2 = -5, 5, -5, 5
    # ax.set_xlim([-x1, x2])
    # ax.set_ylim([-y1, y2])
    # ax.autoscale_view(True, True ,True)
    plt.xlim([x1 , x2])
    plt.ylim([y1, y2])

    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

    grid(1 , 5, x1, x2, y1, y2)

    all_data = [ A, B, C ]
    plt.plot(*zip(*itertools.chain.from_iterable(itertools.combinations(all_data, 2)))  , color = 'red', marker = 'o',  linewidth=2.5 )

    # plt.plot([1, 2, 3, 4], linestyle='--', color='m')
    # plt.scatter(10, 10 , s=20 ,  marker='o' , linewidths=2.5  )
    # plt.scatter(-15, 20 , s=20 ,  marker='o' , linewidths=2.5  )
    # plt.plot( [ 15, 20], [-10, -15]   ,'bo-' , linewidth=2.5  )
    # plt.plot([3, 1.2, 1, 3], linestyle='--',  linewidth=4.5)
    # plt.plot([8, 3, 1, 5], 'ro-.')
    plt.ylabel('Triangle points')
    plt.show()

print('\n--------------------------TESTS------------------------------')
t1  = time.time()




def triangles_containing_origin_solution( LIM ) :

    Q_0 = Quad_I_points( LIM )
    Q_1 = [ (i[0], i[1] ) for i in Q_0   ]
    print('\nQuad_1 : \t',Q_1[:50] )
    Q_2 = [ (-i[0], i[1] ) for i in Q_0 if  ( i[0] != 0  and  i[1] !=0 )  ]
    print('Quad_2 : \t',Q_2[:50] )
    Q_3 = [ (-i[0], -i[1] ) for i in Q_0 if  ( i[0] != 0  and  i[1] !=0 )  ]
    print('Quad_3 : \t',Q_3[:50]  )
    Q_4 = [ ( i[0], -i[1] ) for i in Q_0 if ( i[0] != 0  and  i[1] !=0 ) ]
    print('Quad_4 : \t',Q_4[:50] )

    print('\n--------------------------')

    ############  CASE 1    -  2 points in Quad 1, 1 point in Quad 3 :
    TRIANG = []
    area_filter = 14.5
    count, CNT = 0, { '0': 0 }
    for i in range(len(Q_1)) :
        (x1, y1) = Q_1[i]
        for j in range(i+1, len(Q_1)) :
            (x2, y2) = Q_1[j]
            for k in range(len(Q_3)) :
                (x3, y3) =  Q_3[k]
                 # BARYCENTRIC COORDINATES
                if cartesian_to_barycentric(x1, y1, x2, y2, x3, y3):
                    # A = tuple(sorted(( (x1, y1), (x2, y2), (x3, y3) )))
                    # a1, a2, a3, a4, a5, a6 = A[0][0], A[0][1], A[1][0], A[1][1], A[2][0], A[2][1]
                    Area = triangle_area( x1, y1, x2, y2, x3, y3 )
                    X = relative_center( x1, y1, x2, y2, x3, y3)        # relative center
                    Z = set([ int(i) for i in str(X) ])
                    T = get_triangle_sides( x1, y1, x2, y2, x3, y3 )
                    Y = sorted(T)
                    # signature = ''.join([str(i) for i in Y ]) +'|' +str(Area)+'|' +str(X)
                    signature = ''.join([str(i) for i in Y ]) +'|'  +str(X)
                    # print('case 1 : ' , Q_1[i] , Q_1[j] , Q_3[k], '       ', X ,'                  ' )

                    if signature not in CNT :
                        if Area == area_filter :
                            TRIANG.append( ((x1, y1), (x2, y2), (x3, y3))  )

                        count += 1
                        if len(set(T)) == 2 :
                            if isoscel_triangle_8_symmetry(  (x1, y1), (x2, y2), (x3, y3) ) : CNT[signature] = 8
                            else : CNT[signature] = 4

                        if len(set(T)) == 3 :           CNT[signature] = 8
                        print('case 1 : ' , (x1, y1),',' ,(x2, y2), ',',(x3, y3),'    symm = ', CNT[signature]  ,'        area=' ,  Area , '     rel_center : ', X, '    sides = ', Y,'    type=', len(set(T)) ,'      sign=' , signature,'        cnt=', count )
                        # plot_triangle(Q_1[i], Q_1[j],Q_3[k] )      # Here we plot each triangle

    # @2017-04-05- I left here. I must work with the triangle shifting margins to see if the shifted triangle for the
    # same edges still are within the circle

         ################ CASE 2   ######################  Q1, Q2, Q3
        for l in range(len(Q_2)) :
            for m in range(len(Q_3)) :
                (x4, y4), (x5, y5) =  Q_2[l] , Q_3[m]
                X2 = relative_center( x1, y1, x4, y4, x5, y5)
                if cartesian_to_barycentric(x1, y1, x4, y4, x5, y5):
                    # print('case 2 : ' , Q_1[i] , Q_2[l] , Q_3[m] , '       ', X2)
                    Area2 = triangle_area( x1, y1, x4, y4, x5, y5 )
                    Y2 = make_abs_coord( (x1, y1), (x4, y4), (x5, y5)  )
                    X2 = relative_center( x1, y1, x4, y4, x5, y5)
                    T2 = get_triangle_sides( x1, y1, x4, y4, x5, y5 )
                    Y2 = sorted(T2)
                    Z2 = set([ int(i) for i in str(X2) ])
                    signature2 = ''.join([str(i) for i in Y2 ]) +'|' +str(X2)
                    # signature2 = ''.join([str(i) for i in Y2 ]) +'|' +str(Area2)+'|' +str(X2)


                    if signature2 not in CNT :
                        if Area == area_filter :
                            TRIANG.append( ( (x1, y1), (x4, y4), (x5, y5) )  )
                        count += 1
                        if len(set(T2)) == 2 :
                            if isoscel_triangle_8_symmetry(  (x1, y1), (x4, y4), (x5, y5) ) : CNT[signature2] = 8
                            else : CNT[signature2] = 4
                            # centers2 = collections.Counter( str(X2) )
                            # if len(centers2) == 3 : CNT[signature2] = 8
                            # else : CNT[signature2] = 4
                        if len(set(T2)) == 3 :          CNT[signature2] = 8

                        print('case 2 : ' , (x1, y1), ',' ,(x4, y4), ',',(x5, y5) ,'    symm = ', CNT[signature2]  ,  '      area=' ,  Area2 , '     rel_center : ', X2, '    sides = ', Y2,'    type=', len(set(T2))  ,'      sign=' , signature2, '        cnt=', count)
                        # plot_triangle( Q_1[i], Q_2[l], Q_3[m])      # Here we plot each triangle


    print()

    print('\nCNT : \n',CNT)
    Total = sum([v for k, v  in CNT.items() ])


    print('\nnr of types of triangles count = ', count )

    print('\nTotal Triangles = ', Total, '  <-- the result')
    print ('Triangles : \n',TRIANG )

triangles_containing_origin_solution(10)


# @2017-03-10, 18: 00 - I left here that I must analyze why for I3 I obtain 108 results instead of 90
# @2017-03-21, 23: 00 - I still miss 48 elements which I need to analyze where they are lost
# @2017-03-24, 14:00  - Now I get with 4 triangles in + I must find from where they come  Answer :	 364
# @2017-10-08 - I dont know how many particular cases this fucking problem has more !
# I left here that I must one by one verify each triangle and see what particular case is missing again !
# VERY HARD PROBLEM  !!!
# I already spent very much time on this fucking problem !!!
# But I guess that if I find those cases, finally I am done with this problem !
# @2017-10-09 - i FOUND THE PROBLEM - It is the relative center rel_center :  855 when they depass the
# 1 character limit --> like 10165 --> Must correct it !  It worked for the radius =3 case because individual
# squares are always < 10
@2017-10-09-22:00, UPDATE - I must rehink totally the problem. The number of cases are : 10**12 and
my algorithm is undeasable !
LINKS :
https://stackoverflow.com/questions/33293828/algorithm-to-find-if-triangles-formed-by-set-of-points-contains-origin-or-not-an

#     I5 =      Total Triangles =  15304   <-- the result


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

