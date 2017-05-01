#!/usr/bin/python
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                                                    The Mouse on the Moon      -       Problem 314

The moon has been opened up, and land can be obtained for free, but there is a catch.
You have to build a wall around the land that you stake out, and building a wall on the moon is expensive.
Every country has been allotted a 500 m by 500 m square area, but they will possess only that area which
they wall in. 251001 posts have been placed in a rectangular grid with 1 meter spacing.
The wall must be a closed series of straight lines, each line running from post to post.

The bigger countries of course have built a 2000 m wall enclosing the entire 250 000 m2 area. The Duchy of Grand Fenwick,
has a tighter budget, and has asked you (their Royal Programmer) to compute what shape would get best maximum
enclosed-area/wall-length ratio.

You have done some preliminary calculations on a sheet of paper.
For a 2000 meter wall enclosing the 250 000 m**2 area the enclosed-area/wall-length ratio is 125.
Although not allowed , but to get an idea if this is anything better: if you place a circle inside the square area touching
the four sides the area will be equal to π*2502 m**2 and the perimeter will be π*500 m,
so the enclosed-area/wall-length ratio will also be 125.

However, if you cut off from the square four triangles with sides 75 m, 75 m and 75√2 m the total area becomes 238750 m**2
and the perimeter becomes 1400+300√2 m.
So this gives an enclosed-area/wall-length ratio of 130.87, which is significantly better.

Find the maximum enclosed-area/wall-length ratio.
Give your answer rounded to 8 places behind the decimal point in the form abc.defghijk.
'''
import time
from math import sqrt, ceil, floor, pi, sqrt, cos, sin
# 501 * 501 = 251001 posts


print('\n---------------   FUNCTIONS   ----------------')

def toRadians(degrees):
        return (degrees / 180.0) * pi

def polar_to_X(r, theta):
    alpha = (theta / 180.0) * pi
    x = r * cos(alpha)
    return x

def polar_to_Y(r, theta):
    alpha = (theta / 180.0) * pi
    y = r * sin(alpha)
    return y

D = lambda deg : (deg / 180.0) * pi
X = lambda r, theta :  r * cos(theta *pi / 180)
Y = lambda r, theta :  r * sin(theta *pi / 180)



def trapez_path_area( coord1 , coord2 ):
    a = abs( coord1[1] - coord2[1] )
    b = abs( coord2[0] - coord1[0] )
    c = sqrt(a*a+b*b)   # path
    d = min( coord1[1], coord2[1]  )
    Area = b*d + a*b/2
    return Area, c

print('--------------------------TESTS------------------------------')

print('toRadians Function Test : ', toRadians(30))
print('polar_to_X Function Test : ', polar_to_X(1, 1))
print('polar_to_Y Function Test : ', polar_to_Y(1, 1))


print('lambda function to transform degrees to radians : ', D(180))
print('lambda function to compute x coordinate : ', X(1, 90))
print('lambda function to compute y coordinate : ', Y(1, 90),'\n')


c1 = trapez_path_area( (0, 250), (175, 250) )
c2 = trapez_path_area( (175, 250), (250, 175) )
print('\nTest for trapez_path_area Function Test : ' , trapez_path_area( (0, 250), (175, 250) )  )      # Looks good
print('Test for trapez_path_area Function Test : ' , trapez_path_area( (175, 250), (250, 175) )  )      # Looks good
#   The result from the Pb Example :                    Area/Path= 130.8746930309140822725709812975
print(' Test Example Area : ',  c1[0]+c2[0] )
print(' Test Example Path : ',  c1[1]*2+c2[1] )
print(' Test Example Area/ Path : ',  (c1[0]+c2[0])/ (c1[1]*2+c2[1])  )

##########################

print('\n---------------- LIST COMPREHENSION CONSTRUCTION & TEST ------------------ ')

T = [(50, 1, 0.12760710918852797), (50, 2, 0.18712193255732423), (50, 3, 0.10698612156756475), (50, 4, 0.17231669455435997), \
     (49, 9, 0.19743351713887505), (49, 10, 0.03182672992502995), (48, 14, 0.22707124932629325), (48, 14, 0.20926071581091635), \
     (47, 17, 0.10216972444784307), (46, 19, 0.23585791148561427), (46, 20, 0.15974973532676542), (45, 22, 0.10133468201072084),\
     (44, 24, 0.1538819817007775), (42, 27, 0.2167603502850745), (42, 27, 0.24128839310243), (40, 30, 0.11353569783893745), \
     (39, 31, 0.18114827894609165)]
print('Minimum error in the entire list: ', [ i for i in T if i[2] == min( [j[2] for j in T ] ) ]   )
print(  'Only errors with x=250 : ' ,     [ i  for i in T if  i[0]==50  ] )

# SUPER TARE LIST COMPREHENSION, @ 2016-11-21, by Bogdan Trif
print('Smallest error for x=250 : ',[ i for i in [ k  for k in T if  k[0]==50 ]  if i[2] == min( [ k[2]  for k in T if  k[0]==50 ])] )  #@ 2016-11-21, by Bogdan Trif

######################################


print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

# X_s = lambda r, theta :  r *  ( cos(theta *pi / 180) )**(29/64)
# Y_s = lambda r, theta :  r * ( sin(theta *pi / 180) )**(29/64)


def mouse_on_the_moon(epsilon, coeff) :
    # for c in range( coeff//2 - coeff//6, coeff//2 +coeff//6 , 1 ) :
        A =[]
        for theta in range(1, 4501):
        # for theta in range(1, 46, 15):
            theta = theta/100
            X_s = lambda r, theta :  r *  ( cos(theta *pi / 180) )#**(c/coeff)
            Y_s = lambda r, theta :  r * ( sin(theta *pi / 180) )#**(c/coeff)
            x = X_s(250, theta)
            y = Y_s(250, theta)
            error = (  (abs(x - round(x)) )**2 + (abs(y - round(y)) )**2 )**(1/2)
            # print('x= ',x,'    y= ' ,y ,'            x_=', abs(x - round(x)) , '   y_= ',abs(y - round(y))   , '   xy_= ',error  )

            if error < epsilon :                #( abs(x - round(x)) < epsilon  and   error < 0.25 ) :
                xye = ( round(x), round(y), error  )
                A.append(xye)
                # print('------------      ' , round(x) , round(y),  '       -----------  x_ ', abs(x - round(x)) , '   y_  ',abs(y - round(y))   , '   xy_  ',error,'\n')

        # print('\n\nInitial A array : ', A)

        vals = (sorted(set([i[0] for i in A])))[::-1]
        # print('\nOnly the filtered values that we need : ',vals )

        # print('\n----------Extracting only the UNIQUE values with smallest deviation -----------')

        B=[]
        for val_ in vals :
            SLC = [ i[0:2] for i in [ k  for k in A if  k[0]== val_ ]  if i[2] == min( [ k[2]  for k in A if  k[0]==val_ ])]
            B.append(SLC[0])
        print('\nOnly the ( 0, pi/4 ) theta range integer values for the circle : \n',B)
        for i in reversed(range(len(B))):   B.append( ( B[i][1] , B[i][0])  )

        B.append( (0,250) )        # We append the starting point (0,250)
        B = B[::-1]             # we reverse it as we start from theta =pi/2 and go clockwise
        B.append( (250,0) )
        print('\n All the values from the I-st quarter of the trigonometric circle : \n', B,'\n')

        #### Calculate AREA #########
        Area, Edges = 0, 0
        for i in range(1, len(B)) :
            coord2 = B[i]
            coord1 = B[i-1]
            polygon = trapez_path_area(coord1, coord2)
            Area += polygon[0]
            Edges += polygon[1]
            print('Coordinates :   ',coord2, coord1, '   ;        Polygon:   ', polygon)
        Edges += abs(B[1][0]-B[0][0])       # Here we add the last edge which was not calculated because the ending coordinate is missing

        print('\nTotal Area : ', Area ,'        Total Edges run : ' , Edges , '     Ratio :  ', Area/Edges,'       ')
        # print('\nTotal Area : ', Area ,'        Total Edges run : ' , Edges , '     Ratio :  ', Area/Edges,'       ', c , coeff)
        return Area, Edges, round( Area/Edges, 8)

print('\nAnswer: ',mouse_on_the_moon(0.10, 64 ),'\n')

# epsilon, MAX = .066, 0
# for i in range(1, 10**2) :
#     eps =  epsilon + i/10**4
#     if mouse_on_the_moon(eps)[2] > MAX :
#         MAX = mouse_on_the_moon(eps)[2]
#     print('epsilon = ', eps, '       ', mouse_on_the_moon(eps), '      ', MAX )
#
# print(MAX)

# max_ratio=0
# for m in range(500, 800):
#     m = m / 10000
#     R = mouse_on_the_moon( m )
#     res = R[2]
#     if res > max_ratio :
#         max_ratio = res
#         print('epsilon :    ', m ,'    Total Area, Total Edges run, Ratio :     '    , R  )
#
# print('\n',max_ratio)

 # ######         ANSWERS :             #########

# epsilon :     0.0666  , theta/100  , Total Area, Total Edges run, Ratio :      (49070.5, 392.69456422334963, 124.95843963882979)
# epsilon :     0.06655                     Total Area, Total Edges run, Ratio :      (49070.5, 392.69456422334963, 124.95843963882979)

# 2016-11-22, 20:20
# Not understood correctly the problem from the first time. I though that the shape must be a polygon as close to a circle,
# but actualy is NOT. Must re-DO

#  @ 2017-03-25  Answer:  (57898.0, 438.5516680303466, 132.02093213)
# I am very close to the solution. The answer is something like 132.52 therefore I miss 0.5 from the Ratio
# http://www.wolframalpha.com/input/?i=(x)%5E(4)%2B(y)%5E(4)%3D8


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')














# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
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
