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


def plot_triangle(A, B, C):
    ''':Description: Function to plot a triangle using the pylab module.'''
    from pylab import plt, np
    import itertools
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1 ) #, aspect='equal')

    def grid(major,minor, x1,x2,y1,y2):     #Plotting the grid
        # major ticks every 5, minor ticks every 1
        major_ticks = np.arange(x1, x2, major)
        minor_ticks = np.arange(y1, y2, minor)

        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        ax.set_yticks(major_ticks)
        ax.set_yticks(minor_ticks, minor=True)

        # and a corresponding grid
        ax.grid(which='both')

        # or if you want different settings for the grids:
        # ax.grid(which='minor', alpha=0.2)
        ax.grid(which='minor', alpha=0.8)
        ax.grid(which='major', alpha=1)


    ax.grid(which='both')
    x1 , x2, y1, y2 = -1000, 1000, -1000, 1000
    # ax.set_ylim([-x1, x2])
    # ax.set_xlim([-y1, y2])
    ax.autoscale_view(True, True ,True)

    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

    grid(200, 50, x1, x2, y1, y2)

    all_data = [ A, B, C ]
    plt.plot(*zip(*itertools.chain.from_iterable(itertools.combinations(all_data, 2)))  , color = 'red', marker = 'o',  linewidth=2.5 )

    plt.ylabel('Triangle points')
    plt.show()

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

LIM = 2

Q_0 = Quad_I_points(LIM)
Q_1 = [ (i[0], i[1] ) for i in Q_0   ]
print('\nQuad_1 : \t',Q_1[:50] )
Q_2 = [ (-i[0], i[1] ) for i in Q_0 if i[0] != 0  ]
print('Quad_2 : \t',Q_2[:50] )
Q_3 = [ (-i[0], -i[1] ) for i in Q_0 if i[1] != 0   ]
print('Quad_3 : \t',Q_3[:50]  )
Q_4 = [ ( i[0], -i[1] ) for i in Q_0 if ( i[0] != 0  and  i[1] !=0 ) ]
print('Quad_4 : \t',Q_4[:50] )

print('\n--------------------------')

############  CASE 1    -  2 points in Quad 1, 1 point in Quad 3 :
D = {}
filter = 1.5
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
                X = relative_center( x1, y1, x2, y2, x3, y3)
                Z = set([ int(i) for i in str(X) ])
                T = get_triangle_sides( x1, y1, x2, y2, x3, y3 )
                Y = sorted(T)
                signature = ''.join([str(i) for i in Y ]) +'.' +str(X)
                print('case 1 : ' , Q_1[i] , Q_1[j] , Q_3[k], '       ', X )

                if len(set(T)) == 1 :     CNT[signature] = 1
                if len(set(T)) == 2 :     CNT[signature] = 4
                if len(set(T)) == 3 :    CNT[signature] = 8

# @2017-04-05- I left here. I must work with the triangle shifting margins to see if the shifted triangle for the
# same edges still are within the circle

                    # if len(Z) in [1,2] : CNT[signature] = 8
                    # if len(Z) == 3 : CNT[signature] = 12
                # if Area == filter :
                #     print('case 1 : ' , (x1, y1), (x2, y2), (x3, y3) ,'      area=' ,  Area , '     ', X, '    sides = ', Y,'    type=', len(set(T)) ,'      sign=' , signature,'  ',CNT[signature]  )
                    # plot_triangle(Q_1[i], Q_1[j],Q_3[k] )      # Here we plot each triangle

                if int(Area*2) not in D :
                    D[int(Area*2)] = [X]  ;
                    if len(set(T)) == 1 :                        count += 1
                    if len(set(T)) == 2 :                        count += 4
                    if len(set(T)) == 3 :                        count += 8

                elif int(Area*2) in D :
                    if X not in D[int(Area*2)] :
                        D[int(Area*2)].append(X)

                        if len(set(T)) == 1 :                             count += 1
                        if len(set(T)) == 2 :                            count += 4
                        if len(set(T)) == 3 :                            count += 8



     ################ CASE 2   ######################  Q1, Q2, Q3
    for l in range(len(Q_2)) :
        for m in range(len(Q_3)) :
            (x4, y4), (x5, y5) =  Q_2[l] , Q_3[m]
            X2 = relative_center( x1, y1, x4, y4, x5, y5)
            if cartesian_to_barycentric(x1, y1, x4, y4, x5, y5):
                CNT['0'] += 1
                print('case 2 : ' , Q_1[i] , Q_2[l] , Q_3[m] , '       ', X2)
                # Area = triangle_area( x1, y1, x2, y2, x3, y3 )
                # Y = make_abs_coord( (x1, y1), (x2, y2), (x3, y3)  )
                # X = relative_center( x1, y1, x2, y2, x3, y3)
                # T = get_triangle_sides( x1, y1, x2, y2, x3, y3 )
                # Y = sorted(T)
                # Z = set([ int(i) for i in str(X) ])
                # signature = ''.join([str(i) for i in Y ]) +'.' +str(X)
                #
                # if len(set(T)) == 1 :
                #     # if len(Z) == 1 :
                #         CNT[signature] = 1
                #     # if len(Z) == 2 :  CNT[signature] = 2
                #     # if len(Z) == 3 :  CNT[signature] = 4
                # if len(set(T)) == 2 :
                #     # if len(Z) == 2 :
                #         CNT[signature] = 4
                #     # if len(Z) == 3 :  CNT[signature] = 8
                #
                # if len(set(T)) == 3 : CNT[signature] = 8
                #
                # if Area == filter :
                #     print('case 2 : ' , (x1, y1), (x2, y2), (x3, y3) ,'      area=' ,  Area , '     ', X, '    sides = ', Y,'    type=', len(set(T))  ,'      sign=' , signature,'  ',CNT[signature]  )
                #     # plot_triangle( Q_1[i], Q_2[l], Q_3[m])      # Here we plot each triangle




                # if int(Area*2) not in D :
                #     D[int(Area*2)] = [X]  #; CNT[int(Area*2)] = 0
                #
                #     if len(set(T)) == 1 :                        count += 1
                #     if len(set(T)) == 2 :                        count += 4
                #     if len(set(T)) == 3 :                        count += 8
                #
                #
                # elif int(Area*2) in D :
                #     if X not in D[int(Area*2)] :
                #         D[int(Area*2)].append(X)
                #
                #         if len(set(T)) == 1 :                            count += 1
                #         if len(set(T)) == 2 :                            count += 4
                #         if len(set(T)) == 3 :                            count += 8

        #############    CASE 3            #############
        for n in range(len(Q_4)) :
            (x6, y6) = Q_4[n]
            # Area = triangle_area(  x1, y1, x4, y4, x6, y6 )
            X3 = relative_center( x1, y1, x4, y4, x6, y6)
            # T = get_triangle_sides(  x1, y1, x4, y4, x6, y6 )
            # Y = sorted(T)
            # signature = ''.join([str(i) for i in Y ]) +'.' +str(X)
            if cartesian_to_barycentric( x1, y1, x4, y4, x6, y6):
                CNT['0'] += 1
                print( 'case 3 : ' ,Q_1[i] , Q_2[l] , Q_4[n] , '       ', X3)
                # if Area == filter :
                #     print('case 3 : ' , (x1, y1), (x2, y2), (x3, y3) ,'      area=' ,  Area , '     ', X, '    sides = ', Y, '    type=', len(set(T)) ,'      sign=' , signature  )
                # s = str(X)
                #
                # if len(set(T)) == 1 : CNT[signature] = 1
                # if len(set(T)) == 2 : CNT[signature] = 4
                # if len(set(T)) == 3 : CNT[signature] = 8
                #
                # if int(Area*2) not in D :
                #     D[int(Area*2)] = [X] #;  CNT[int(Area*2)] = 0
                #
                #     if len(set(T)) == 1 :                        count += 1
                #     if len(set(T)) == 2 :                        count += 4
                #     if len(set(T)) == 3 :                        count += 8
                #
                #
                # elif int(Area*2) in D :
                #     if X not in D[int(Area*2)] :
                #         D[int(Area*2)].append(X)
                #
                #         if len(set(T)) == 1 :                            count += 1
                #         if len(set(T)) == 2 :                            count += 4
                #         if len(set(T)) == 3 :                            count += 8


# @2017-03-10, 18: 00 - I left here that I must analyze why for I3 I obtain 108 results instead of 90
# @2017-03-21, 23: 00 - I still miss 48 elements which I need to analyze where they are lost
# @2017-03-24, 14:00  - Now I get with 4 triangles in + I must find from where they come  Answer :	 364

print('\n',D.get( filter*2 ) )
print(D )



# for k,v in D.items() :
#     # print(k, v)
#     for l in v :
#         tip =  set([ int(i) for i in str(l) ])
#         if k not in CNT : CNT[k] = 0
#         if len(tip) == 1 : CNT[k] += 1
#         if len(tip) == 2 : CNT[k] += 4
#         if len(tip) == 3 : CNT[k] += 8

print('\nCNT : \n',CNT)
Total = sum([v for k,v in CNT.items() ])
print('\nTotal = ', Total, '  <-- this one matters')


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

