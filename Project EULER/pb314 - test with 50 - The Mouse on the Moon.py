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

You have done some preliminary calculations on a sheet of paper. For a 2000 meter wall enclosing the 250 000 m2 area
the enclosed-area/wall-length ratio is 125.
Although not allowed , but to get an idea if this is anything better: if you place a circle inside the square area touching
the four sides the area will be equal to π*2502 m**2 and the perimeter will be π*500 m, so the enclosed-area/wall-length ratio will also be 125.

However, if you cut off from the square four triangles with sides 75 m, 75 m and 75√2 m the total area becomes 238750 m**2
and the perimeter becomes 1400+300√2 m. So this gives an enclosed-area/wall-length ratio of 130.87, which is significantly better.

Find the maximum enclosed-area/wall-length ratio.
Give your answer rounded to 8 places behind the decimal point in the form abc.defghijk.
'''
import time

print('--------------------------TESTS------------------------------')


from math import pi, sqrt, cos, sin, floor

def toRadians(degrees):
        return (degrees / 180.0) * pi

def radians_to_degrees(radians) :
    '''radians_to_degrees, Radians to Degrees ,radians to degrees, RADIANS TO DEGREES, rad_to_deg, rad to deg    '''
    return radians * 180 /pi

def positive_rad(radian) :
    ''':Description: Transform a negative radian to positive radian '''
    if radian < 0 :
        return radian + 2*pi

def positive_deg(degrees) :
    ''':Description: Transform a negative radian to positive radian '''
    if degrees < 0 :
        return degrees + 360


def polar_to_X(r, theta):
    alpha = (theta / 180.0) * pi
    x = r * cos(alpha)
    return x

def polar_to_Y(r, theta):
    alpha = (theta / 180.0) * pi
    y = r * sin(alpha)
    return y


print('toRadians Function Test : ', toRadians(30))
print('polar_to_X Function Test : ', polar_to_X(1, 1))
print('polar_to_Y Function Test : ', polar_to_Y(1, 1))

D = lambda deg : (deg / 180.0) * pi
X = lambda r, theta :  r * cos(theta *pi / 180)
Y = lambda r, theta :  r * sin(theta *pi / 180)

print('lambda function to transform degrees to radians : ', D(180))
print('lambda function to compute x coordinate : ', X(1, 90))
print('lambda function to compute y coordinate : ', Y(1, 90),'\n')


def trapez_path_area( coord1 , coord2 ):
    a = abs( coord1[1] - coord2[1] )
    b = abs( coord2[0] - coord1[0] )
    c = sqrt(a*a+b*b)   # path
    d = min( coord1[1], coord2[1]  )
    Area = b*d + a*b/2
    return Area, c

coord1 = (0, 50)
coord2 = (3, 50)
print('\n Test for trapez_path_area Function Test : ' , trapez_path_area(coord1, coord2))   # Looks good


print('\n-------------------------------')
A =[]
epsilon=0.1
for theta in range(1, 91):
    theta = theta/2
    x = X(50, theta)
    y = Y(50, theta)
    error = sqrt(  (abs(x - round(x)) )**2 + (abs(y - round(y)) )**2 )
    print('x= ',X(50, theta),'    y= ' ,Y(50, theta) ,'            x_=', abs(x - round(x)) , '   y_= ',abs(y - round(y))   , '   xy_= ',error  )
    if theta < 45 :
        if error < 0.25 : #( abs(x - round(x)) < epsilon  and   error < 0.25 ) :
            xye = (round(x), round(y), error  )
            A.append(xye)
            print('------------            ' , round(x) , round(y),  '            -----------  x_ ', abs(x - round(x)) , '   y_  ',abs(y - round(y))   , '   xy_  ',error,'\n')
    # if theta > 45 :
    #     if error < 0.25 : #( abs(y - round(y)) < epsilon and   error < 0.25 ) :
    #         print('------------            ' , round(x) , round(y),  '            -----------  x_ ', abs(x - round(x)) , '   y_  ',abs(y - round(y))   , '   xy_  ',error,'\n')

print('\n\nInitial A array : ', A)
print('\n---------------- LIST COMPREHENSION CONSTRUCTION & TEST ------------------ ')

print('Minimum error in the entire list: ', [ i for i in A if i[2] == min( [j[2] for j in A ] )    ]   )
print(  'Only errors with x=50 : ' ,     [    i  for i in A if  i[0]==50     ] ,'\n' )

# SUPER TARE LIST COMPREHENSION, @ 2016-11-21, by Bogdan Trif
print('Smallest error for x=50 : ',[ i for i in [ k  for k in A if  k[0]==50 ]  if i[2] == min( [ k[2]  for k in A if  k[0]==50 ])] )  #@ 2016-11-21, by Bogdan Trif

vals = (sorted(set([i[0] for i in A])))[::-1]
print('\nOnly the filtered values that we need : ',vals )

print('\n----------Extracting only the UNIQUE values with smallest deviation -----------')
B=[]
for val_ in vals :
    SLC = [ i[0:2] for i in [ k  for k in A if  k[0]== val_ ]  if i[2] == min( [ k[2]  for k in A if  k[0]==val_ ])]
    B.append(SLC[0])
print('\nOnly the ( 0, pi/4 ) theta range integer values for the circle : \n',B)
for i in reversed(range(len(B))):
    B.append( ( B[i][1] , B[i][0])  )

B.append((0,50))        # We append the starting point (0,50)
B = B[::-1]             # we reverse it as we start from theta =pi/2 and go clockwise
print('\n All the values from the I-st quarter of the trigonometric circle : \n', B)





print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

Area, Edges = 0, 0
for i in range(1, len(B)) :
    coord2 = B[i]
    coord1 = B[i-1]
    polygon = trapez_path_area(coord1, coord2)
    Area += polygon[0]
    Edges += polygon[1]
    print('Coordinates :   ',coord1, coord2, '          ; Polygon:   s ',polygon)
Edges += abs(B[1][0]-B[0][0])       # Here we add the last edge which was not calculated because the ending coordinate is missing
print('\n\nTotal Area : ', Area ,'        Total Edges run : ' , Edges , '\nRatio :  ', Area/Edges)

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
