#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Fri, 2 Dec 2016, 19:55
#The  Euler Project  https://projecteuler.net
'''
Triangle containment    -       Problem 102

Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000,
such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing
the co-ordinates of one thousand "random" triangles,
find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.


'''
import time
# from pylab import *
import itertools

filename="pb102_triangles.txt"

def load_file(filename="pb102_triangles.txt"):
    with open(filename) as f:
        triangles = [list(map(int, line.split(","))) for line in f.readlines()]
    f.close()
    return triangles

triangles = load_file(filename)
print(len(triangles), triangles)


def plot_triangle(A, B, C):
    ''':Description: Function to plot a triangle using the pylab module.'''
    import pylab
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


def determine_inside_origin(lst) :
    ''':Description: Function to return if the Origin O(0,0) is contained inside the triangle
    :param lst: list in the form : (x1, y1, x2, y2, x3, y3). The function will transform into three points with
        two coordinates and perform further processing.
    :return:    boolean : True if the Origin is inside the triangle, otherwise False.    '''
    A, B, C = [lst[0], lst[1]],  [lst[2], lst[3]],  [lst[4], lst[5]]
    # print(A,B,C)
    Comb = list(itertools.combinations( (A,B,C), 2 ))
    CR = { 'x' : [] ,  'y' :[] }
    for I in Comb :
        # print(I)
        x1, x2 = I[0][0] , I[1][0]
        y1, y2 = I[0][1] , I[1][1]
        dx, dy = x2 - x1, y2 - y1
        if dy == 0:                   # Case1 :  when derivative = 0, line parallel to X-axis, intersects Y-axis
            x0 , y0, m = min(x1, x2) , y1, 0        # m = dy/dx is the slope of the line (derivative)
            p_y, p_x = 1e10, y0
        elif dx == 0:                 # Case2 : when derivative = ∞ ; line parallel with Y-axis, intersect Y-axis
            x0, y0, m = x1, min(y1,y2), 1e10
            p_y, p_x = x0, -1e10
        else:                               # Case3 : General Case
            m = dy/dx
            x0 = min( x1 , x2 )         # Here we want the starting point to be always at left
            if x0 == x1 : y0=y1
            elif x0 == x2 : y0=y2
            p_y =  - y0/m + x0              # intersection with X-axis, the x for which y=0
            p_x =   -m*x0 + y0              # intersection with Y-axis, the y for which x=0
        # print('dy, dx= ',dy, dx , ' ;  dy/dx= ',m ,' x0, y0 =', x0,y0, ' ;   X-axis=0 : p_x=' ,p_x, ' ;      Y-axis=0 : p_y='  ,p_y   )
        if  min(y1, y2 ) <=  p_x <= max(y1, y2)  :  CR['y'].append(p_x)      # Take only the point which are between min & max
        if  min( x1, x2 ) <=  p_y <= max( x1, x2 )  :   CR['x'].append(p_y)
    # print( 'X Min & Max :  ',min(A[0], B[0], C[0]), max(A[0], B[0], C[0]) )
    # print( 'Y Min & Max :  ', min(A[1], B[1], C[1]), max(A[1], B[1], C[1]) )
    # print('The cross : ',CR)
    # print('---------------------')
    plot_triangle(A, B, C)      # Here we plot each triangle
    if  len(CR['x']) >1 and len(CR['y']) >1 :       # Check if the cuts  of Ox & Oy form a cross :)
        if  max(CR['x']) > 0 and min(CR['x']) < 0 and max(CR['y']) > 0 and min(CR['y']) < 0 :
            return True
    return False


print('\n--------------------------TESTS------------------------------')

# lst= [ -175, 41, -421,-714, 574,-645 ]
# lst = [-340,495, -153,-910, 835,-947 ]
# lst = [-100, 100, 900, 100, 100, -200]        # Case when derivative = 0 ; line paralel with X-axis
lst = [-100, 200, 900, 100, -100, -700]        # Case when derivative = ∞ ; line paralel with X-axis
# lst = [-175, 41, -421, -714, 574, -645]
# lst = [129, 169, 576, 651,-87, -458]

print('\n Test for the function determine_inside_origin: ', determine_inside_origin(lst) )

# A, B, C = [150,100],[-200,180],[-130,-200]
# plot_triangle(A, B, C)


print('\n================  My FIRST SOLUTION,  25 ms ===============\n')
t1  = time.time()


def solution_pb102():
    import os
    counter = 0
    for I in triangles:
        if determine_inside_origin(I) == True :
            # print(' ----------------------- TRUE TRUE TRUE TRUE !!!!!!!!!!!!! -----------------')
            counter +=1
        # else : print(' ----------------------- FALSE FALSE ! -----------------')
        # os.system("pause")
    return print('\nAnswer : ', counter)

solution_pb102()            # Answer :  228

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')      #   Completed in : 26.001453 ms


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')

# I used the rule "a point is contained in a polygon, if the number of intersections of some line drawn from
# this point with the sides of the polygon is odd".
# I used the positive x-axis as this line, after checking that no edge lies on the x-axis
# (and made some trivial errors in computing the intersection points ;-) ).
# My code (in Java) runs in 33ms

print('\n--------------------------SOLUTION 1,  SIMPLEST & BEST SOLUTION, neuron04, USA   --------------------------')
t1  = time.time()
# Same approach as most other people, slightly easier/simpler code

file_working = open(filename, 'r')
# print(file_working)
count = 0

for line in file_working :
    # print(line)
    ax, ay, bx, by, cx, cy =  map(int, line.split(','))
    print(ax, ay, bx, by, cx, cy)
    p = ax*by - ay*bx > 0       # Computing individual Triangles
    q = bx*cy - by*cx > 0
    r = cx*ay - cy*ax > 0
    print(p, q, r)
    count += p == q == r        # Here he uses the property that the partial areas must be either Positive or Negative

print (count)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 2,  VERY SHORT & GOOD SOLUTION, Hyakumanten,   --------------------------')
t1  = time.time()

answer = 0

with open(filename, "r") as data_file:
	ts = [line.rstrip().split(",") for line in data_file]

for i in ts:
	x1, y1, x2, y2, x3, y3 = map( int, i)
	A = 0.5 * (-y2*x3 + y1*(-x2+x3) + x1*(y2-y3)+ x2*y3)    # Using expanded determinant to calculate area of the triangle
	s = 1/(2*A) * (y1*x3 - x1*y3)
	t = 1/(2*A) * (x1*y2 - y1*x2)
	if s>0 and t>0 and 1-s-t>0:
		answer +=1

print(answer)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, Interesting Approach ,higgsmass, USA --------------------------')
t1  = time.time()
# I used the rule for a triangle to contain the origin to solve this problem.

import math

def p102_area(d):
    #d 0  1   2  3   4   5
    #  xa ya  xb yb  xc  yc

    d = [ int(i) for i in d ]
    ## area of AOB + BOC + AOC (where O is the origin)
    a = 0.5*(math.fabs( d[2]*d[5] - d[4]*d[3]))
    a += 0.5*(math.fabs( d[4]*d[1] - d[0]*d[5]))
    a += 0.5*(math.fabs( d[0]*d[3] - d[2]*d[1]))

    ## area of ABC
    b = 0.5*( math.fabs( d[0]*d[3] - d[0]*d[5] + d[2]*d[5] - d[2]*d[1] + d[4]*d[1] - d[4]*d[3] ))

    ## if triangle contains origin, ABC = AOB + BOC + AOC
    if math.fabs(a-b) < 1.e-5:
        return True
    else:
        return False


def Problem0102():
    outp = """102) find the number of triangles for which the interior contains the origin"""
    with open(filename, 'r') as f:
        c = 0
        for l in f:
            d = l.strip().split(',')
            if p102_area(d):
                c += 1
    outp += "\nAnswer: " + str(c) + '\n'
    return print(outp)

Problem0102()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4, rockyroer  , USA    --------------------------')
t1  = time.time()

# I had just described to my precalculus students that the determinant of a 3x3 matrix can be used to
# find the area of a triangle -- specifically, if the vertices are A(x1, y1), B(x2, y2) and C(x3, y3) then the area of the triangle
# is one half of the determinant of the matrix:
#
#     x1, y1, 1
#     x2, y2, 1
#     x3, y3, 1
#
#
# With that in mind, I found the areas of triangles AOB, BOC, COA,
# and added them to see if they equaled the area of triangle ABC.
#
# I also graphed them -- but only because I was curious how to graph using the graphics.py module for python.

# from graphics import *
# win = GraphWin("Triangles", 400, 400)
# win.setCoords(-1000,-1000,1000,1000)

file = open(filename, 'r')
triangles = file.readlines()
file.close
# triangle = Polygon(Point(1,1),Point(2,2),Point(1,2))
# triangle.draw(win)

def Determinant3x3(a,b,c,d,e,f,g,h,i):
	return a*(e*i-f*h)-b*(d*i-g*f)+c*(d*h-g*e)

count = 0

for t in triangles:
	t = t.strip()
	[x1,y1,x2,y2,x3,y3] = t.split(',')
	[x1,y1,x2,y2,x3,y3] = [int(x1),int(y1),int(x2),int(y2),int(x3),int(y3)]
	Area012 = .5*abs(Determinant3x3(x1,y1,1,x2,y2,1,0,0,1))
	Area023 = .5*abs(Determinant3x3(x2,y2,1,x3,y3,1,0,0,1))
	Area013 = .5*abs(Determinant3x3(x1,y1,1,x3,y3,1,0,0,1))
	Area123 = .5*abs(Determinant3x3(x1,y1,1,x2,y2,1,x3,y3,1))


	if Area012+Area023+Area013 == Area123:
		# triangle.undraw()
		# triangle = Polygon(Point(x1,y1),Point(x2,y2),Point(x3,y3), Point(x1,y1))
		# triangle.setFill('green')
		# triangle.draw(win)
		# Circle(Point(0,0),10).draw(win)
		# print ("***********")
		# print (x1, y1)
		# print (x2, y2)
		# print( x3, y3)
		count += 1
		#raw_input()

print (count, "triangles."	)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 5, aniruddhamurali, USA   --------------------------')
t1  = time.time()
# I found a rather different approach to this problem.
# Instead of using barycentric coordinates, I used area to solve this problem.
# Assume that Point P is the origin, and Points A, B, and C are the vertices of the triangle.
# Then: ABC = APB + APC + BPC
#
# So, if the origin is not inside the triangle, this equation would not be true.
# Using this conditional, the program took only 5 ms.

import math

def main():
    count = 0
    name = filename # file containing all triangles
    file = open(name,'r')

    for line in file:
        coords = line.split(',')  # makes a list of coordinates for each triangle

        # set coordinates as variables
        x1 = int(coords[0])
        y1 = int(coords[1])
        x2 = int(coords[2])
        y2 = int(coords[3])
        x3 = int(coords[4])
        y3 = int(coords[5])

        # calculate areas of the 4 triangles
        area = triangleArea(x1,y1,x2,y2,x3,y3)
        area1 = triangleArea(x1,y1,x2,y2,0,0)
        area2 = triangleArea(x1,y1,x3,y3,0,0)
        area3 = triangleArea(x2,y2,x3,y3,0,0)

        # compare areas
        if area == area1+area2+area3:
            count += 1
    return count

def triangleArea(x1,y1,x2,y2,x3,y3):
    '''Calculates the area of a triangle'''
    area = abs((x1-x3)*(y2-y1) - (x1-x2)*(y3-y1))/2
    return area

print(main())

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6, Barycentric Coordinates  --------------------------')
t1  = time.time()

# ==== Thu, 27 Oct 2016, 09:25, mandeepb, USA
# I also solved the problem using barycentric coordinates.
# I had never heard of them before, but had a lot of fun reading about them.

def cartesian_to_barycentric(x1, y1, x2, y2, x3, y3):
    """Convert cartesian coordinates to barycentric coordinates and return all > 0.

    Reference: https://en.wikipedia.org/wiki/Barycentric_coordinate_system_(mathematics)
    """
    alpha = (((y2 - y3) * (0 - x3) + (x3 - x2) * (0 - y3)) /
             ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)))
    beta = (((y3 - y1) * (0 - x3) + (x1 - x3) * (0 - y3)) /
            ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)))
    gamma = 1 - alpha - beta

    return alpha > 0 and beta > 0 and gamma > 0

count = 0
with open(filename) as text:
    for triangle in text.read().split():
        x1, y1, x2, y2, x3, y3 = [int(coord) for coord in triangle.split(',')]
        if cartesian_to_barycentric(x1, y1, x2, y2, x3, y3):
            count += 1
print(count)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 7,  CLASSES & OOP,   aristarchos, USA --------------------------')
t1  = time.time()

class Triangle(object):
    def __init__(self, line):
        split_line = line.split(',')
        self.vertices = (Point(int(split_line[0]), int(split_line[1])),
                         Point(int(split_line[2]), int(split_line[3])),
                         Point(int(split_line[4]), int(split_line[5])))

    def edge_lines(self):
        for i in range(len(self.vertices)):
            yield EdgeLine(self.vertices[i], self.vertices[(i + 1) % len(self.vertices)])


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class EdgeLine(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def slope(self):
        if self.start.x == self.end.x:
            return 1e10

        return (float(self.start.y) - self.end.y) / (self.start.x - self.end.x)

    def y_intercept(self):
        return self.start.y - self.slope() * self.start.x

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end \
            or self.end == other.start and self.start == other.end


class TriangleFile(object):
    def __init__(self, file):
        self.file = file

    def triangles(self):
        for line in self.file:
            yield Triangle(line)


def y_intercept_is_on_segment(edge_line):
    y_intercept = edge_line.y_intercept()
    return y_intercept >= edge_line.start.y and y_intercept <= edge_line.end.y \
        or y_intercept <= edge_line.start.y and y_intercept >= edge_line.end.y


def contains_origin(triangle):
    edge_lines = list(triangle.edge_lines())
    return any(edge_line.y_intercept() > 0 and y_intercept_is_on_segment(edge_line) for edge_line in edge_lines) \
        and any(edge_line.y_intercept() < 0 and y_intercept_is_on_segment(edge_line) for edge_line in edge_lines)


if __name__ == "__main__":
    with open(filename) as file:
        triangle_file = TriangleFile(file)
        count = 0
        for triangle in triangle_file.triangles():
            if contains_origin(triangle):
                count += 1
        print(count)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
