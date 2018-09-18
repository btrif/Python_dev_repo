#  Created by Bogdan Trif on 10-11-2017 , 8:12 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                Squares under a hyperbola           -       Problem 247

Consider the region constrained by 1 ≤ x and 0 ≤ y ≤ 1/x.


Let S1 be the largest square that can fit under the curve.
Let S2 be the largest square that fits in the remaining area, and so on.

Let the index of Sn be the pair (left, below) indicating the number of squares to the left
of Sn and the number of squares below S_n.


The diagram shows some such squares labelled by number.
S_2 has one square to its left and none below, so the index of S_2 is (1,0).

It can be seen that the index of S_32 is (1,1) as is the index of S50.
50 is the largest n for which the index of Sn is (1,1).

What is the largest n for which the index of S_n is (3,3)?


'''
import time, zzz
from math import sqrt


print('\n--------------------------TESTS------------------------------')
t1  = time.time()

###         Solution            ###
# 1.  we consider (x0,y0) to be the bottom left side of the square and the (x1, y1) the top right part of
# if square. Therefore the horizontal side will be : x1-x0 and the vertical side size = y1-y0 and they are equal
#
# x1 - x0 = y1 - y0           (1)
#
# the equation of the hyperbola is y=1/x and we note that it intersects the square in the point (x1,y1)
# Therefore :
# y1 = 1/x1       (2)
#
# Putting (2) into (1) =>
# x1 - x0 = 1/x1 - y0   (3)
# Now we solve for x1 because we want to find the coordinate of x1 and as a consequence the side x1-x0
#
# x1-1/x1 = x0-y0  <=>
# ( x1^2 - 1 ) /x1 = x0-y0  <=>
# x1^2 - 1 = x1( x0-y0)  <=>
# x1^2 - (x0-y0)*x1 - 1 = 0   (4)     and we have a 2-nd degree equation on x1 variable
#
# x_1,2 = -b/2a +/- sqrt(b^2 - 4*a*c)/2a   =>
#
# x_(1,2) = -(x0-y0)/2 +/- sqrt((x0-y0)^2+4) / 2      (5)
#
# Note : we must take only the positive root of x1


def get_x1(x0, y0) :
    x11 = (x0-y0) /2 + sqrt( (x0-y0)**2+4) / 2
    x12 = (x0-y0) /2 - sqrt( (x0-y0)**2+4) / 2
    # print('x11 = ', x11, '      x12 = ', x12 )
    return x11

get_x1(1, 0)

Memo = dict()
x0, y0 = 1, 0       #  0.6180339887498948
side = 1e9
cnt = 0
index = [ 0 ,0 ]
while index[0]  <= 3  :
    x1 = get_x1(x0, y0 )
    y1 = 1/x1
    side = x1-x0
    Memo[ (cnt, index[1] )] = (side, x0, y0 )
    cnt +=1
    print(str(cnt)+'.   x0 = ', round(x0,4) , '     y0 = ', round(y0,4) , '     x1=' , round(x1,4) , '     y1 =  ', round(y1,4) ,  '    side = ', side )

    x0, y0 = x1, 0  #   0.6180339887498948
    index[0] += 1

print('\nMemo : ', Memo)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

# @2018-06-28 - METHOD TO SOLVE
# 1.  First find all the sides (areas) of the (3,3) squares under the hyperbola.
# Because we must find the largest n for which the index S_n = (3,3) this means that the side is the smallest.

# 2. Observation : Since there is only 1 square with (left,right) (0,0 ) and 2 squares with (1,1) =>
# there are 3 squares with (2,2) and THEREFORE 4 squares with index (3,3)
# Find all and choose the smallest side(area). We can use sides instead of areas.
#
# 3. Once we found the smallest of the 4 squares (3,3 ) we must FIND ALL SQUARES
# which are SMALLER than this special square.
#
# 4. We must use a data structure which will hold the (x0, y0)  and repeatedly compute the rows of squares
# to the right and to the left.
#     The difficulty here is the fact that there are multiple values for a speciffic index and we must search through all

# 5.  A nice recursion function can do the job :
#         -   one recursive call to go to RIGHT
#         -   one recursive call to go UP

# 5.
# Actually New  METOHD :
# a. First find the (3,3) -th squares .Which means :
#     Go to all rows up to (3,3)
#     - (0,0), (1,0), (2,0), (3,0) --> put them into a dictionary . Also put the holes into a dictionary, meaning
#     for (0, 0) will be the up hole with coord left bottom of (0,1) representing the left-top of (0,0)
#     Therefore holes will be (0,1), (1,1), (2,1), (3,1)
#     do this reapeatedly until you get (3,3)
#
# find all the 4 squares and compute the smallest area .
#
# b.   Now you do a new iteration based on the area which should be < than (3,3) smallest area.
#     This process must have the same approach as previously but must have the condition of AREA
#     rather than coefficients of the (left, below) area.





index = [ 0, 0 ]

def recurse( x, y ):
    if x == 2 or y == 2 :
        print('x, y = ', x, y )
        return (x, y)
    else :

        recurse( x +1 , y )
        recurse (x, y+1)


recurse( 0 , 0 )

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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




