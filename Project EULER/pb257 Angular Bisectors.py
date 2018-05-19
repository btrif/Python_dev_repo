#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
            Angular Bisectors           -           Problem 257

Given is an integer sided triangle ABC with sides a ≤ b ≤ c. (AB = c, BC = a and AC = b).
The angular bisectors of the triangle intersect the sides at points E, F and G (see picture below).


The segments EF, EG and FG partition the triangle ABC into four smaller triangles: AEG, BFE, CGF and EFG.

It can be proven that for each of these four triangles the ratio area(ABC)/area(subtriangle) is rational.

However, there exist triangles for which some or all of these ratios are integral.

How many triangles ABC with perimeter≤100,000,000  (10**8) exist so that the ratio area(ABC)/area(AEG) is integral?


'''
import time, zzz
from math import sqrt, cos, sin, pi, acos, asin

# INFO SOURCES :        Angular Bisectors
# http://www.cut-the-knot.org/triangle/AngleBisectorTheorem.shtml

https://en.wikipedia.org/wiki/Angle_bisector_theorem


def Heron_area_perimeter(a,b,c):
    s= (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**(1/2)

angleC = lambda a,b,c : acos( ( a**2 + b**2 - c**2) / (2*a*b) )*180/pi

angleA =  lambda a,b,c : acos(( b**2 + c**2 - a**2) / (2*b*c))*180/pi

angleB =  lambda a,b,c : acos( (c**2 + a**2 - b**2) / (2*c*a))*180/pi

CE = lambda a,b,c : (sqrt( (a*b)*(a+b+c)*(a+b-c)) )/ (a+b)
BG = lambda a,b,c : (sqrt( (a*c)*(a+c+b)*(a+c-b) ))/ (a+b)

y =  lambda B_G, c, angleB :   sqrt( B_G*B_G + c*c - (2*B_G*c * cos( (angleB*pi)/(2*180) ) ))

x =  lambda C_E, a, angleC :   sqrt(C_E*C_E + a*a - (2*C_E*a * cos( (angleC*pi)/(2*180) ) ))

GE =  lambda x, y, angleA :   sqrt(x*x + y*y - (2*x*y * cos( (angleA*pi)/180 ) ))


def compute_ratio_of_triangles(a,b,c) :
    print('\na, b, c = ',  a,b,c)

    epsilon = 1e-8
    angle_B = angleB(a,b,c)
    angle_C = angleC(a,b,c)
    angle_A = angleA(a,b,c)
    if abs(angle_A - round(angle_A)) < epsilon : angle_A = round(angle_A)
    if abs(angle_B - round(angle_B)) < epsilon : angle_B = round(angle_B)
    if abs(angle_C - round(angle_C)) < epsilon : angle_C = round(angle_C)

    print('BG = ', BG(a,b,c))
    print('CE = ', CE(a,b,c))
    print(' angleB = ', angle_B )
    print(' angleC= ', angle_C )

    B_G = BG(a,b,c)
    C_E = CE(a,b,c)

    y_ = y(B_G, c, angle_B)
    x_ = x(C_E, a, angle_C)
    if abs(y_ - round(y_)) < epsilon : y_ = round(y_)
    if abs(x_ - round(x_)) < epsilon : x_ = round(x_)

    print('y = ',  y_  )
    print('x = ',  x_ )

    G_E = GE(x_, y_, angle_A )
    if abs(G_E - round(G_E)) < epsilon : G_E = round(G_E)
    print('G_E = ', G_E)

    if a+b == c :
        hc2 = sqrt(a*a- (c/2)**2)
        Area_ABC = hc2 * c /2
    elif a+c ==b :
        hb2 = sqrt(a*a- (b/2)**2)
        Area_ABC = hb2 * b /2
    elif b+c == a :
        ha2 = sqrt(b*b- (a/2)**2)
        Area_ABC = ha2 * a /2

    if x_+y_ == G_E :
        hGE2 = sqrt(x_*x_- (G_E/2)**2)
        Area_ABC = hGE2 * G_E /2
    elif x_+G_E == y :
        hy2 = sqrt(x_*x_- (y_/2)**2)
        Area_ABC = hy2 * y_ /2
    elif y_ + G_E == x :
        hx2 = sqrt(y_*y_- (x_/2)**2)
        Area_ABC = hx2 * G_E /2

    else :
        Area_ABC = Heron_area_perimeter(a,b, c)
        Area_AEG = Heron_area_perimeter(x_, y_, G_E)

    print('Area_ABC = ', Area_ABC)
    print('Area_AEG = ', Area_AEG)

    ratio = Area_ABC / Area_AEG
    if abs(ratio - round(ratio)) < epsilon : ratio = round(ratio)
    print( 'Raportul celor 2 triunghiuri = ', ratio )
    return ratio

compute_ratio_of_triangles(6,6,6)

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def some_brute_force_for_understanding(up_lim) :
    cnt = 0
    for a in range(1, up_lim+1):
        for b in range(1, a+1 ):
            for c in range(1, b+1 ):
                cnt+=1

                ratio = compute_ratio_of_triangles(a, b, c)
                if  ratio%1 == 0:
                    print(str(cnt)+ '.      a, b, c   =', a, b, c ,'        ratio = ', ratio )

some_brute_force_for_understanding(10)

# @2017-10-05 - Heron formula gives error for the isosceles triangles because the semiperimeter
#     if a,b,c = 1, 1, 2  => s= 2 => we will have that s-c ==0 => area = 0




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

