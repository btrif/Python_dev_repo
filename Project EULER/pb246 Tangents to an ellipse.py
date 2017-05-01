#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Sat, 22 Apr 2017, 19:21
#The  Euler Project  https://projecteuler.net
'''
Tangents to an ellipse          -           Problem 246

A definition for an ellipse is:
Given a circle c with centre M and radius r and a point G such that d(G,M)<r,
the locus of the points that are equidistant from c and G form an ellipse.

The construction of the points of the ellipse is shown below.

Given are the points M(-2000,1500) and G(8000,1500).
Given is also the circle c with centre M and radius 15000.
The locus of the points that are equidistant from G and c form an ellipse e.
From a point P outside e the two tangents t1 and t2 to the ellipse are drawn.
Let the points where t1 and t2 touch the ellipse be R and S.


For how many lattice points P is angle RPS greater than 45 degrees?


'''
import time, zzz
import sympy
import math


## === OBSERVATIONS before starting :   2017-04-08, 21:30
# 1.  M, G are the foci of the ellipse => we must determine the equation of the ellipse based on those two foci
# 2. From a point P outside e (ellipse ) the two tangents t1 and t2 to the ellipse are drawn , but does not specify that
# must be within the circle ==> we must take all the exterior to the ellipse points
# 3.



def point_outside_ellipse(ellipse, P ) :
    x, y = symbols("x y ")
    x0, y0 = P
    E = sympy.lambdify( ( x,y), ellipse )
    val = E(x0,y0)
    # print(x0 , y0 , '    ',ellipse, '       ', val )
    if val > 0 : return True
    return False

def point_inside_big_ellipse( P ) :
    big_ellipse = lambda x,y : (x )**2 / (15439.83)**2  + (y )**2/ (18949.9087**2)  - 1
    x0, y0 = P
    val = big_ellipse(x0,y0)
    # print(x0 , y0 , '    ',big_ellipse, '       ', val )
    if val < 0 : return True
    return False

def point_outside_small_ellipse( P ) :
    small_ellipse = lambda x,y : (x )**2 / (7500**2) + (y )**2 / (5590.169943749474)**2  - 1
    x0, y0 = P
    val = small_ellipse(x0,y0)
    # print(x0 , y0 , '    ',small_ellipse, '       ', val )
    if val > 0 : return True
    return False



def point_outside_director_circle(director_circle, P ) :
    x, y = symbols("x y ")
    x0, y0 = P
    DC = sympy.lambdify( ( x,y), director_circle )
    val = DC(x0,y0)
    # print(x0 , y0 , '    ',ellipse, '       ', val )
    if val > 0 : return True
    return False




print('\n-------------------------- MECHANICAL , Mathematical ,TESTS------------------------------')
t1  = time.time()

# http://www.wolframalpha.com/input/?i=plot+(x%5E2%2B2*y%5E2%3D6,+y%2B(13%2F5)*(x-1)-4%3D0,+y-(x-1)-4%3D0+)
# http://www.wolframalpha.com/input/?i=solve(+x%5E2%2B2*((-13%2F5)*(x-1)%2B4+)%5E2+)+-6%3D0&t=crmtb01
# http://www.nabla.hr/Z_MemoHU-029.htm

print('\n---------------- Equation Manipulations, Math variable Substitution, Lambdify ')

from sympy import *
x, y, z, m = symbols("x y z m")

# The main equation, we substitute y=f(x) = x into it
expr = ( x-0 )**2 + 2*(y-0)**2 - 6


# The main equation, we substitute y=f(x) = x/2 into it, ##### actually we do x=2*y
w1 = expr.subs( y, m*(x-1)+4 )
print('The SUBSTITUTED expression : \t' , w1 )

# Expand, Put in standard form
w2 = sympy.expand (w1)
print('The EXPANDED expression : \t' ,  w2 )

# Lambdify, which means that we create a function from the previous expression
J =  sympy.lambdify(x, w2)


# we find the roots of the quadratic equation :
x = sympy.Symbol('x')
# print('Solving quadratic, finding its roots : \t', sympy.solve( w2, x ) )

zc = collect(w2, x , evaluate=False)
print('Collecting similar terms corresponding to coeffs a,b,c of the quadratic eqn : \t',  zc )
print( 'Separated terms :         x^2 :   ', zc[x**2] ,'   ;    x :    ', zc[x]  , '       others 1 :  ' ,zc[1] )

print('\n-----------Tangent 1----------')

# The main equation, we substitute y=f(x) = x into it
expr = ( x-0 )**2 + 2*(y-0)**2 - 6

# The main equation, we substitute y=f(x) = x/2 into it, ##### actually we do x=2*y
w1 = expr.subs( y, -(13/5)*(x-1)+4 )
print('The SUBSTITUTED expression : \t' , w1 )

# Expand, Put in standard form
w2 = sympy.expand (w1)
print('The EXPANDED expression : \t' ,  w2 )
# Lambdify, which means that we create a function from the previous expression
J =  sympy.lambdify(x, w2)


# we find the roots of the quadratic equation :
x = sympy.Symbol('x')
print('Solving quadratic, finding its roots : \t', sympy.solve( w2, x ) )


print('\n-----------Tangent 2----------')
# The main equation, we substitute y=f(x) = x/2 into it, ##### actually we do x=2*y
w1 = expr.subs( y, (x-1)+4 )
print('The SUBSTITUTED expression : \t' , w1 )

# Expand, Put in standard form
w2 = sympy.expand (w1)
print('The EXPANDED expression : \t' ,  w2 )
# Lambdify, which means that we create a function from the previous expression
J =  sympy.lambdify(x, w2)


# we find the roots of the quadratic equation :
x = sympy.Symbol('x')
print('Solving quadratic, finding its roots : \t', sympy.solve( w2, x ) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


test_ellipse =  ( x-0 )**2 + 2*(y-0)**2 - 6

print('\npoint_outside_ellipse : \t', point_outside_ellipse(test_ellipse, (-2 , 1 ) ) )
# print('\npoint_outside_director_circle : \t', point_outside_director_circle( ellipse, (-2 , 1 ) ) )

# print('\nget_tangents_from_a_point :  \t' ,get_tangents_from_a_point(test_ellipse, (-100,-400) ) )
# print('\nget_tangents_from_a_point :  \t' ,get_tangents_from_a_point( ellipse , (  15000, 10000 ) ) )

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()



# Determining the properties of the ELLIPSE :
# we have the points of the two foci and the radius of the circle :
M, G, r =  (-2000,1500) , (8000,1500), 15000
# Based on the properties of the ellipse formation via circle we have that  :
# semi-major axis a  = r/2 :
a = r // 2
# c - represents the distance from focus to the center of the ellipse, therefore , MG = 2c :
c = (G[0] - M[0]) //2
# Now we can find the semi-minor axis of the ellipse based on the formula : b**2 = a**2 - c**2
b = ( a**2 - c**2 ) **(1/2)

print('semi-major axis, a  = ' , a)
print('semi-minor axis, b  = ' , b)
print( 'focus  to center distance, c  = ' , c )

# Finding the center of the ellipse :
O = ( (G[0]-M[0])//2+M[0], M[1]  )
print('\nCenter of the ellipse, O(x,y) = ', O)

# We have all the data to form the complete equation of the ellipse :
h, k = O[0], O[1]
print('We center the ellipse : ')
ellipse = ((x )**2) / a**2 + ((y )**2) / b**2 - 1
print('The final equation of the Ellipse : ', ellipse)

#### ELLIPSE DIRECTOR CIRCLE - represents the circle which is formed by two perpendicular
# tangents to the ellipse, has radius R = sqrt( a*a + b*b )
R_d = (a*a+b*b)**(1/2)
print('\nRadius of the Ellipse Director Circle :\t', R_d)

## Ellipse's Director Circle Equation :
director_circle = (x )**2 + (y )**2 - (a*a+b*b)
print('Equation of the Ellipse director Circle : \t', director_circle   )


print()

print('\n--------------Constructing the main function --------------')

def get_tangents_from_a_point(ellipse , P ):
    x0, y0 = P
    x, y, z, m = symbols("x y z m ")

    # The main equation, we substitute y=f(x) = x into it
    # print('the ellipse : \t ',ellipse,'       the point P = ', P )
    # The main equation, we substitute
    Y =  m*(x-x0)+y0
    s1 = ellipse.subs( y,  Y)
    # print('The SUBSTITUTED expression : \t' , s1 )

    # Expand, Put in standard form
    s2 = sympy.expand (s1)
    # print('The EXPANDED expression : \t' ,  s2 )

    col = collect(s2, x , evaluate=False)
    # print('Collecting similar terms corresponding to coeffs a,b,c of the quadratic eqn : \t',  col )
    a, b, c = col[x**2], col[x], col[1]
    # print( 'Separated terms :         x^2 :   ', a ,'   ;    x :    ', b  , '       others 1 :  ' , c )
    delta = b*b - 4*a*c
    # print('delta : ',delta)
    # we find the roots of the quadratic equation :
    delta2 = sympy.expand (delta)
    # Here we exclude terms like m**4, m**3  in the expression of m --> and collect IF EXIST only the terms m**2, m, 1
    col2 = collect(delta2, m , evaluate=False)
    # print('Collecting similar terms in the eqn of m : : \t',  col2 )
    new_delta = 0
    for i in [ m**2, m, 1 ] :
        # print( 'i = ', i,'          ' , col[i] )
        if i in col2 : new_delta += col2[i] * i
    # print('new_delta = \t', new_delta )

    # delta2 = 0
    # for j in [ m**2, m, 1 ] :
    #     if j in col2 : delta2 += col2[j] * j

        # col2[m**2] *m**2 + col2[m]*m + col2[1]
    # print('new_delta = \t', new_delta )

    # print('The EXPANDED new_delta expression : \t' ,  new_delta )
    m = sympy.Symbol('m')
    M = sympy.solve( new_delta, m )
    # print('Solved new_delta : \t', M)
    #     # print('Solving quadratic, finding its roots : \t', m1, m2 )
    #     # # Tangent 1 & 2 :
    #     # print('--------  Finding Tangents points : (actually not needed ) ----------------')
    #     # for i in [m1, m2] :
    #     #     yt = Y.subs(m, i )
    #     #     print('y_tan = ', yt)
    #     #     tan  = ellipse.subs(y, yt )
    #     #     print('Tangent with m='+str(i)+'     = ' , tan)
    #     #     x_tan = sympy.solve( tan, x )
    #     #     y_tan = yt.subs( x, x_tan[0] )
    #     #     print(' Tan x-coord : ', x_tan , '      Tan x-coord : ', y_tan , )
    if len(M) == 1 : return 10**20, M[0]
    return M[0], M[1]


# print('\nAngle_of_two_slopes_director_circle : \t', angle_of_two_slopes_director_circle( ellipse , ( 15540 , 16852 ) , director_circle )        )


print('\n--------------- angle_of_two_slopes_director_circle(ellipse, P, director_circle ):  ------------------')




def angle_of_two_slopes_director_circle(ellipse, P, director_circle ):     # © Made by Bogdan Trif @ 2017-04-10, 12:30
    '''Correct formula with sign convention positive for θ counter-clockwise rotation from
    direction of radius vector 1 to 2 is .
        **tan(θ)= (m2−m1) / (1+m1*m2)**
    This function depends on the function point_outside_director_circle. When I'll have time I must create a class.
    :param m1: slope 1
    :param m2: slope 2
    :return: the obtuze angle if inside the ellipse's Director Circle
        and the acute angle if outside the Ellipse's Director Circle    '''
    m1, m2 = get_tangents_from_a_point( ellipse, P )
    # print(m1, m2)
    try :   theta = math.atan( abs( (m2 -m1) /(1+m1*m2) ) )
    except :
        ZeroDivisionError
        return 90
    if point_outside_director_circle(director_circle, P ) :
        return theta * 180 / math.pi
    else :
        return ( 360 - 2*( theta * 180 / math.pi ) ) /2


# print('\nAngle_of_two_slopes_director_circle : \t', angle_of_two_slopes_director_circle( ellipse , ( 3000 , 20500 ) , director_circle )        )
print('\nAngle_of_two_slopes_director_circle : \t', angle_of_two_slopes_director_circle( ellipse , ( 0 , -18949.9087) , director_circle )        )
print('\nAngle_of_two_slopes_director_circle : \t', angle_of_two_slopes_director_circle( ellipse , ( 0 , 18949. ) , director_circle )  )

print('\nAngle_of_two_slopes_director_circle : \t', angle_of_two_slopes_director_circle( ellipse , ( 15439.83 , 0 ) , director_circle )        )
print('\nAngle_of_two_slopes_director_circle : \t', angle_of_two_slopes_director_circle( ellipse , ( -15439.83, 0 ) , director_circle )  )





# print('\nBIG ELLIPSE Director Properties : ')
# a, b =   18439.83 - 3000, 17449.9087+ 1500
# print('BIG ELLIPSE : \t', '   Semi-major axes y: ', a,'\t      Semi-minor axes x: \t', b)
#
# big_ellipse = (x-3000)**2 / a**2 + (y-1500)**2 / b**2 -1
# print('BIG ELLIPSE Equation : \t', big_ellipse )

# @ 2017-04-08 - REMARK !!!
# The difficulty of the problem stays in the fact that the tan formula of slopes gives always angle <=90
# Deciding if we must take the obtuze or acute angle must be taken relative to the distance from the ellipse.
# This MUST be established , how can we say at what distance we take acute or obtuze angles ?
# Task, Find the shape for which the tangents to the ellipse has exactly 90 degrees
# http://geometryatlas.com/entries/349
# http://math.stackexchange.com/questions/749665/orthogonal-tangents-to-an-ellipse
# http://math.stackexchange.com/questions/33520/the-locus-of-two-perpendicular-tangents-to-a-given-ellipse

# limits : x range(-13000, 19000 )
# limits : y range(-18000, 20500 )

######### STEP  - Find the locus of points of 45 degrees to the original ellipse :

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

t1  = time.time()

def brute_force_check(x, y) :
    cnt = 0
    for x in range(-7500 , 7501 ) :
        if  not point_outside_small_ellipse( (x,y) ) :
            cnt +=1
    return cnt

def calculate_points_inside_ellipse( x, y  ):       # BINARY SEARCH IMPLEMENTATION @ Bogdan Trif , 2017-04-10, 22:00
    CNT, iter = 0, 0
    x_left, x_right =  0,  x
    while 1 :
        iter +=1
        if  point_outside_small_ellipse( (x,y) ) :
            x_right = x
            x = ( x_right - x_left )//2
            # print('1:       x= ' , x ,  '            x_left=', x_left ,'         x_right=', x_right)

        if  not point_outside_small_ellipse( (x,y) ) :
            x = x + ( x_right - x_left )//2
            x_left = x
            # print('2:       x= ' , x ,  '           x_left=', x_left ,'         x_right=', x_right )

        if not point_outside_small_ellipse( (x,y) ) and point_outside_small_ellipse( (x+1,y) )  :
            # print('YES ! We have that ', (x,y) ,'  follows the rule ...    iterations = ' ,iter )
            return 2*x +1

        if x_left == 0 and x_right ==0 : return 0

### AUTOMATED TEST

def automated_test_ellipse() :
    # for y in [ 999, 1345, 1767, 2333, 2998, 3400, 4558, 4989, 5100, 5430, 6101, 7000 ] :
    for y in range(580, 6101, 13 ) :
        bs = calculate_points_inside_ellipse(7500, y)
        bf = brute_force_check(7500, y)
        print('y = ', y ,'Binary search = ', bs, '    brute force = ', bf)

print('calculate_points_inside_ellipse : \t' ,calculate_points_inside_ellipse(7500, 5590 ) )

def inside_ellipse_points():
    cnt = 0
    for y in range(1, 5591) :
        cnt += calculate_points_inside_ellipse(7500, y)
        if y % 1000 == 0 : print(y)
    return cnt*2 + calculate_points_inside_ellipse(7500, 0)



print('\n --------------   Main solution------------------ \n ')


# angle_of_two_slopes_director_circle( ellipse , ( 0 , 18949.9087 ) , director_circle )  )
# angle_of_two_slopes_director_circle( ellipse , ( 15439.83 , 0 ) , director_circle )


def calculate_45_degrees_in_shape( x, y, ellipse, director_circle  ):       # BINARY SEARCH IMPLEMENTATION @ Bogdan Trif , 2017-04-10, 22:00
    CNT, iter = 0, 0
    x_left, x_right =   calculate_points_inside_ellipse(7500, y), x
    # print(' -------  x_left, x_right =  ',x_left, x_right)
    while 1 :
    # for i in range(80) :
        iter +=1

        angle = angle_of_two_slopes_director_circle( ellipse , ( x , y ) , director_circle )
        if  angle <= 45 :
            x_right = x
            x = x_left +( x_right - x_left )//2
            # print('1:       x= ' , x ,  '            x_left=', x_left ,'         x_right=', x_right, '        angle=', angle,'     iter=', iter )

        angle = angle_of_two_slopes_director_circle( ellipse , ( x , y ) , director_circle )
        if  angle > 45 :
            x_left = x
            x = x_left + ( x_right - x_left )//2

            # print('2:       x= ' , x ,  '           x_left=', x_left ,'         x_right=', x_right, '        angle=', angle ,'     iter=', iter )

        if angle_of_two_slopes_director_circle( ellipse , ( x , y ) , director_circle ) > 45 and \
                angle_of_two_slopes_director_circle( ellipse , ( x+1 , y ) , director_circle ) <= 45  :
            # angle = angle_of_two_slopes_director_circle( ellipse , ( x , y ) , director_circle )
            # print('\nYES ! We have that ', (x, y ) ,' = ' , angle   ,' inside shape       iterations = ' ,iter )
            # print(' outside shape  :    x, y = ', (x+1, y),'       angle = ',  angle_of_two_slopes_director_circle( ellipse , ( x+1 , y ) , director_circle )   )
            return 2*x +1


        if x_left == 0 and x_right ==0 : return 0

# print('\n calculate_45_degrees_in_shape : \t', calculate_45_degrees_in_shape( 15440 , 16852, ellipse, director_circle )  )
# print('\n calculate_45_degrees_in_shape : \t', calculate_45_degrees_in_shape( 15440 , 1, ellipse, director_circle )  )
# print('\n calculate_45_degrees_in_shape : \t', calculate_45_degrees_in_shape( 15440 , 18949, ellipse, director_circle )  )
# print('\n calculate_45_degrees_in_shape : \t', calculate_45_degrees_in_shape( 15440 , 18950, ellipse, director_circle )  )

# http://www.wolframalpha.com/input/?i=plot+((x+)%5E2+%2B+(y+)%5E2+%3D+87500000,++(x+)%5E2%2F56250000+%2B+(1%2F(+5590.1699)%5E2)*(y)%5E2+%3D+1+++)

print('\n----------------------------')

def brute_force_shape_outside_ellipse(y) :
    itr = 0
    for x in range(15199, 0, -1) :
        if angle_of_two_slopes_director_circle( ellipse , ( x , y ) , director_circle ) > 45 :
            itr+=1
            angle = angle_of_two_slopes_director_circle( ellipse , ( x , y ) , director_circle )
            print(  '    YES ! We have that ', (x, y) ,' =', angle   , ' is in side the shape        iterations = ' , itr )
            print('\n outside shape  :    x, y = ', (x+1, y),'       angle = ',  angle_of_two_slopes_director_circle( ellipse , ( x+1 , y ) , director_circle )   )

            return 2*x+1


# print('\brute_force_shape_outside_ellipse : \t', brute_force_shape_outside_ellipse( y = 4011 ) )


def inside_shape_points_counter(x) :            #  @2017-04-20,  Binary Search, But I DON'T longer Use it !!!!
    CNT = 0
    y = 1
    y_s = y
    t0 = time.time()
    while y_s <= 18949 :
    # while y_s <= 2 :
        print('==========   y_s= ', y_s ,'  ===========  ', round( ( time.time() - t0 )/60, 6) , ' min')
        t0 = time.time()
        iter = 0
        y_down, y_up =  y_s,  18949
        o = calculate_45_degrees_in_shape( x , y_s, ellipse, director_circle )
        while 1  :
            if  calculate_45_degrees_in_shape( x , y, ellipse, director_circle ) != o :
                y_up = y
                y = y_down + ( y_up - y_down )//2
                iter +=1
                print('1:       y= ' , y ,  '            y_down=', y_down ,'         y_up=', y_up , '      iter=  ' , iter)

            if  calculate_45_degrees_in_shape( x , y, ellipse, director_circle ) == o :
                y_down = y
                y = y + ( y_up - y_down )//2
                iter +=1
                print('2:       y= ' , y ,  '            y_down=', y_down ,'         y_up=', y_up , '      iter=  ' , iter )

            if calculate_45_degrees_in_shape( x , y, ellipse, director_circle ) == o and \
                calculate_45_degrees_in_shape( x , y+1, ellipse, director_circle ) != o :
                print('\nYES ! We have that   y=',  y ,'has ', o ,' lattice points    the y range is : ', (y_s,  y)  ,'   ...    iterations = ' ,iter )
                CNT += ( y - y_s +1 ) * o
                y_s, y = y+1, y+1
                break

            if y_down == 0 and y_up ==0 :
                y_s, y = y+1, y+1

    # for y in range(1, 18950) :
    # # for y in range(1, 10) :
    #     o = calculate_45_degrees_in_shape( 15440 , y, ellipse, director_circle )
    #     scnt += o
    #     print(str(y) +'.      o=', o)

    zero = calculate_45_degrees_in_shape( 15440 , 0, ellipse, director_circle )

    return CNT*2 + zero

def main():
    IEP = inside_ellipse_points()
    print('\n Inside Ellipse Points = ', IEP,'\n')
    CNT = 0
    zero = calculate_45_degrees_in_shape( 15440 , 0, ellipse, director_circle )
    t3 = time.time()
    for y in range(1, 18949+1 ) :
        y_more_45 = calculate_45_degrees_in_shape( 15440 , y, ellipse, director_circle )
        CNT += y_more_45
        print('   y= ' , y ,  '               > 45 degrees points =  ', y_more_45  )
        if y% 10**3 ==0 :
            print(  round((time.time()-t3)/60, 6), 'min\n'   )
            t3 = time.time()

    ISP = CNT*2 + zero
    print('\n Inside_shape_points_counter : \t', ISP)

    return print('\nANSWER, Points in between : \t', ISP - IEP )

# main()


#  Inside_shape_points_counter : 	 942549517
# ANSWER, Points in between : 	 810834388

t2  = time.time()
print('\nCompleted in :', round((t2-t1)/3600, 6), 'hours\n\n')      #   Completed in : 55.86833 hours


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   SUPER FAST  ,143 ms --------------------------')
t1  = time.time()

# ====Thu, 11 Mar 2010, 23:54, yurip , USA
# I just assumed that the envelope would be an ellipse and spent too much time debugging the resulting code.

import math

a = math.pi/8
t = math.tan(a)
R = 15000.
T = 10000.
A2 = R*R/4.
A = R/2.
B2 = (A2 - T*T/4.)
B = math.sqrt(B2)

mx2 = (A2 + B2/t/t)
my2 = (A2/t/t + B2)
mx = math.sqrt(mx2)
my = math.sqrt(my2)

def cnt(y):
    Q = A2*y*y-A2*B2
    S = y*y-A2-B2
    D = (2*S-4*B2)**2 - 4*(S*S-4*Q)
    xb2 = (-(2*S-4*B2) + math.sqrt(D))/2
    xb = math.floor(math.sqrt(xb2))
    if y > B:
        return int(2*xb+1)
    else:
        g = math.sqrt(1.-y*y/B2)*A
        xs = math.ceil(g)
        if (xs == g) : xs += 1
        assert(xb > xs)
        return int(2*(xb-xs+1))

pts = cnt(0)
for y in range(1, int(my)+1):
    pts += 2*cnt(y)

print (pts)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 2,  1/2 sec --------------------------')
t1  = time.time()


# ==== Tue, 21 Aug 2012, 23:00, ving, Python , USA
# If a tangent from (u, v) touches the ellipse x^2/a^2 + y^2/b^2 = 1 at (x, y), then
# (v-y)/(u-x) =  -(x/a^2) / (y/b^2) ==>
#
#     (u/a)*(x/a) + (v/b)*(y/b) = 1
#
# Using the above and the fact that (x, y) lies on the ellipse, we also get
#
#     (v/b)*(x/a) - (u/a)*(y/b) = k
#
# where 1 + k^2 = r^2 = u^2/a^2 + v^2/b^2.
#
# Solving this set of two linear equations for k = +/- sqrt(r^2-1) I find the two points of tangency (x1, y1) and (x2, y2).
# I write the condition for the angle between the tangents to be greater than 45 degrees using the Law of Cosines.
#
# The number of lattice points can be found in no time by following the contours of their locus.

# Easier to deal with the ellipse centered at the origin x^2/a^2 + y^2/b^2 = 1
# Here a = 7500, the distance f from the center to the focus is 5000,
# b = sqrt(a^2 - f^2)
# If a tangent from (u, v) touches the ellipse at (x, y), then
# u/a x/a + v/b y/b = 1
# Since (x, y) is on the ellipse,
# v/b x/a - u/a y/b = k where 1 + k^2 = r^2 = u^2/a^2 + v^2/b^2 ==>
# x = a/r^2 (u/a + kv/b), y = b/r^2(v/b - ku/a)
# The angle between the tangents can be found from the Law of Cosines.

from math import sqrt

a, f = 75, 50  # Answer: 81090
a, f = 7500, 5000  # Answer: 810834388

a2 = a**2
b2 = a2 - f**2
b = sqrt(b2)

def inside(u, v):
    ua, vb = u/a, v/b
    r2 = ua*ua + vb*vb
    return r2 <= 1

def ge45(u, v):
    ua, vb = u/a, v/b
    r2 = ua*ua + vb*vb
    if r2 <= 1:
        return False
    k = sqrt(r2 - 1)
    x1, x2 = a/r2*(ua + k*vb), a/r2*(ua - k*vb)
    y1, y2 = b/r2*(vb - k*ua), b/r2*(vb + k*ua)
    z1 = (u - x1)**2 + (v - y1)**2
    z2 = (u - x2)**2 + (v - y2)**2
    z3 = (x1 - x2)**2 + (y2 - y1)**2
    d = z1 + z2 - z3
    return d < 0 or d**2 < 2*z1*z2

cnt = 0

u = a + 1
while ge45(u, 0):
    u += 1
    cnt += 2
uMax = u

v = int(b) + 1
while ge45(0, v):
    v += 1
    cnt += 2
vMax = v

uMin = a
for v in range(1, vMax):  # follow the contours
    while uMin > 0 and not inside(uMin, v):
        uMin -= 1
    while not ge45(uMax, v):
        uMax -= 1
    cnt += 4*(uMax - uMin)

print(cnt)



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 3, RE-mapping shape into a circle  -----------------------')
t1  = time.time()

# ==== Sat, 2 May 2015, 07:23, stysis, Australia
# That one was fun!
# Like some others, I was misled early into thinking that the boundary of 45 degree angles was going to be another ellipse.
# Realised then that I would need to do some more algebra !
# My method became a lot simpler once I realised I could remap the ellipse and point P as a unit circle.
# It's much easier to find the tangent points for a circle and then un-mapping gives the tangents for the ellipse, R and S.
#
# Runs in about 0.3 seconds.



import time,math

def angle(xp,yp):
    h = ((xp/a)**2 + (yp/b)**2)**0.5
    alpha = math.asin(1/h)
    beta = math.atan((yp/b)/(xp/a))
    gamma1 = -(beta-alpha)
    xt1 = math.sin(gamma1)*a
    yt1 = math.cos(gamma1)*b
    m1 = -(b**2*xt1)/(a**2*yt1)
    gamma2 = -(math.pi-math.pi/2-alpha-beta)
    xt2 = math.cos(gamma2)*a
    yt2 = math.sin(gamma2)*b
    m2 = -(b**2*xt2)/(a**2*yt2)
    return math.atan(abs((m1-m2)/(1+m1*m2)))*180/math.pi

start = time.time()
# Formula for 1st ellipse x1**2/a1**2 + y1**2/b1**2 = 1
a = 7500
b = int((a**2 - (10000/2)**2))**0.5
Psum = 0
# When x=1, find the largest y for angle >= 45
x = 1
y = 18000
while angle(x,y) > 45:
    y += 1
# Save the number of points on the y axis to add in later.
Py = y-1-int(b)
# Sum the points from 1 <= x < a, subtracting the points with E.
for x in range(1,int(a)):
    while angle(x,y) <= 45:
        y -= 1
    Psum += y - int(((1-x**2/a**2)*b**2)**0.5)
# Add the points where x = a (m2 is infinite)
while (angle(7499,y) + angle(7501,y))/2 <= 45:
    y -= 1
Psum += y
# When y=1, find the largest x for angle >= 45
y = 1
x = 10000
while angle(x,y) > 45:
    x += 1
# Save the number of points on the y axis to add in later.
Px = x-1-int(a)
# Sum the points from maximum y >= x > a.
maxy = x-1
y = 1
for x in range(maxy,int(a),-1):
    while angle(x,y) > 45:
        y += 1
    Psum += y - 1
# Account for the 4 quadrants
Psum *= 4
# Add in the x axis and y axis saved earlier
Psum += Py * 2
Psum += Px * 2
print(Psum)
print("This took %0.3f" % (time.time()-start),"seconds")

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()


# ==== Sat, 21 Nov 2015, 15:40, bukebuer, China
# This problem cost me several days to assure every step of my algebra is correct...
#
# However, finally I got:
# (x2+y2−a2−b2)2≤4(b2x2+a2y2−a2b2)
#
# where a and b are from the ellipse x2/a2+y2/b2=1 .
# Replacing x2 with X, and so on. Then solving Y for given X, it results into (just for the upper bound of Y):
#
# Y≤3A+B−X+22A2−(A−B)X−−−−−−−−−−−−−√
#
# Then for X, there are 2 upper bounds:
#
# 2A2−(A−B)X≥0⇒X≤2A2A−B
#
# Y≥0⇒X≤A+(22–√+3)BY≥0⇒X≤A+(22+3)B
#
# For aa and bb given by the problem, A+(22–√+3)B<2A2A−B, which means that the outer space should be convex.
#
# So just loop through xx from 0 to A+(22–√+3)B−−−−−−−−−−−−−√A+(22+3)B, and count y by the upper bound related to x,
# while check carefully on points on x-axis, on y-axis and in ellipse. Then it's done.


def pe246(A=56250000., B=31250000.):
    # it's fortunate that int((A + (8**0.5+3)*B)**0.5)) < int((2*A*A / (A-B))**0.5)
    # which implies that the outer shape is convex
    xmax = int((A + (8**(1/2)+3)*B)**(1/2))

    def ymax(x):
        delta = 2*A*A - (A-B)*x*x
        y2max = 3*A + B - x*x + 2*delta**0.5
        return int(y2max**0.5)

    def ymin(x):
        return int((B * (1 - x*x/A))**0.5)

    # deal with axis
    count = (ymax(0) - int(B**0.5) + xmax - 7500) * 2

    # for other part
    for x in range(1, xmax+1):
        if x <= 7500:
            count += 4 * (ymax(x) - ymin(x))
        else:
            count += 4 * ymax(x)

    return print(count)

pe246(A=56250000., B=31250000.)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 5, 11 secs ,  Similar to mine but FASTER, with BINARY SEARCH --------------------------')
t1  = time.time()

# ==== Sat, 6 Jun 2009, 12:27, zeycus, Spain
# This was fun! I coded a function that given a point calculates the angle from it to the ellipse.
# Then I traversed the plane along the Y axis, and for each line Y=n I used a binary search.
# I was surprised when the shape turned out to be convex. It takes about 20 seconds in my old computer.

import math

bound = 15000
a = 7500
b = 1000 * ( 5 * math.sqrt(5) / 2)


# *********************** FUNCTIONS *************************

def normalise(v):
    module = math.sqrt(sum(c**2 for c in v))
    return tuple(c / module for c in v)

def angle(x0, y0):
    if (x0/a)**2 + (y0/b)**2 <= 1:
        return 180
    h = b**2 * x0**2 + a**2 * y0**2 - a**2 * b**2
    A = 4 * y0**2 * a**4 - 4 * a**2 * h
    B = 8 * x0 * b**2 * y0 * a**2
    C = 4 * x0**2 * b**4 - 4 * b**2 * h
    disc = math.sqrt(B**2 - 4 * A * C)
    if A==0:  # Nyapa para cuando sale indet 0/0.
        return 0.5 * (angle(x0+0.001,y) + angle(x0-0.001,y))
    m1 = (-B + disc) / (2*A)
    m2 = (-B - disc) / (2*A)
    t1 = -(2 * x0 * b**2 + 2 * y0 * m1 * a**2) / (2*(b**2 + a**2 * m1**2))
    t2 = -(2 * x0 * b**2 + 2 * y0 * m2 * a**2) / (2*(b**2 + a**2 * m2**2))
    v1 = normalise( (t1, t1*m1) )
    v2 = normalise( (t2, t2*m2) )
    return (180 / math.pi) * math.acos(v1[0]*v2[0] + v1[1]*v2[1] )


def validInLine(y):
    if angle(0, y) <= 45:
        return 0
    xL = 0
    xR = 15000
    while angle(xR, y) > 45:
        xR += 1000
    while xR - xL > 1:
        xM = (xL + xR) // 2
        if angle(xM, y) <= 45:
            xR = xM
        else:
            xL = xM
    return 2 * xL + 1

def countInsideEllipse(ax1, ax2):
    '''Returns the number of integer points in an ellipse centered in (0,0)
    with axis ax1 and ax2. Points in the border are counted too.'''
    counter = 0
    y = int(ax2)
    while True:
        x = (ax1/ax2) * math.sqrt(ax2**2 - y**2)
        x = 1 + int(x)
        while ax2**2 * x**2 + ax1**2 * y**2 > ax1**2 * ax2**2:
            x -= 1
        counter += (2*x + 1)
        y -= 1
        if y+ax2 < 0:
            return counter


# *********************** MAIN *************************
def main2() :
    counter = 0
    for y in range(20000,0,-1):  # Upper half
        valid = validInLine(y)
        counter += valid
    counter = 2*counter + validInLine(0)  # The Axis y=0 is counter appart.
    print ('Points in the region:', counter)
    pEll = countInsideEllipse(a, b)
    print ('Points in the ellipse:', pEll)
    print ('Solution:', counter - pEll)

# main2()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# ==== Wed, 14 Oct 2009, 11:17, Yuval Dor, Israel
# Hey. There is a much easier way to calculate the slopes of the tangent lines.
#
# If the line y = mx + n is tangent to an ellipse x2/a + y2/b = 1, then it must hold that:
#
# n**2 = m**2a**2 + b**2
#
# Easy to calculate the angle from here: tga = | m1 - m2 / 1 + m1m2 | (because this equation gives two solutions so two possible tangents)
#
# I just set the maximum x for each y and subtract or add if needed ... my code gives for some reason off-by-few error, I had to submit a few solutions :)
#
# I see some people found for each y the appropriate x .. but the differences are so small you can just loop.
#
# Code:

## First set: M = (0, - 5000), G = (0, 5000).
import math
a = 7500
a2 = aa = a ** 2
c = 5000
c2 = cc = c ** 2
b2 = bb = aa - cc
b = math.sqrt(aa-cc)
alpha = 45 * math.pi / 180

def angle(x0,y0) -> "RPS":

    ## if y = mx + n is tangent to e, then
    ## n ^ 2 = (ma)^2 + b^2
    ## we have y0 - mx0 = n
    ## so (y0 - mx0)^2 = (ma)^2 + b ^ 2
    delta = math.sqrt( (4*(x0**2*y0**2) - 4*(aa - x0 ** 2)*(bb - y0**2)))
    try:
        m1 = (-2*x0*y0 + delta) / (2 * (aa - x0 ** 2))
        m2 = (-2*x0*y0 - delta) / (2 * (aa - x0 ** 2))
        tg = abs( (m1 - m2) / (1 + m1*m2) )
        return math.atan(tg)
    except:
        return 0


def solve():
    ymax = int(b / math.sin(math.atan(b / a * math.tan(alpha / 2))))
    xmax = int(a / math.cos(math.atan(b / a * math.tan(alpha * 1.5))))
    tot = 2 * xmax + 2 * ymax
    tot -= 2 * a + 2 * int(b) ## subtract
    n = 0
    y = 1
    while y < b:
        while angle(xmax+1,ymax) > alpha:
            xmax += 1
        while angle(xmax,y) <= alpha:
            xmax -= 1
        n += xmax - int(a * math.sqrt(1 - y ** 2 / bb))
        y += 1
    while y <= ymax:
        while angle(xmax+1,ymax) > alpha:
            xmax += 1
        while angle(xmax,y) <= alpha:
            xmax -= 1
        n += xmax
        y += 1

    tot += n * 4
    return print(tot)

solve()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


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

