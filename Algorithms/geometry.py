import numpy as np

print('-----Intersection between two infinite  lines given as the endpoints -------------')
def two_infinite_lines_intersection( p1, p2, p3, p4) :
    ''' Given the endpoints of two lines L1(p1,p2) and L2(p3,p4)
    find the intersection point of these two lines
    Example : two_lines_intersection( [0,1], [2,3],[2,2], [-2,2])
    '''

    def line(p1, p2):
        A = (p1[1] - p2[1])
        B = (p2[0] - p1[0])
        C = (p1[0]*p2[1] - p2[0]*p1[1])
        print('A, B, C :\t',A, B,-C)
        return A, B, -C

    L1 = line(p1, p2)
    L2 = line(p3, p4)

    def intersection(L1, L2):
        D  = L1[0] * L2[1] - L1[1] * L2[0]
        Dx = L1[2] * L2[1] - L1[1] * L2[2]
        Dy = L1[0] * L2[2] - L1[2] * L2[0]
        print('D, Dx, Dy :\t',D, Dx, Dy)
        if D != 0:
            x = Dx / D
            y = Dy / D
            return x,y
        else:
            return False

    R = intersection(L1, L2)
    if R:         return R
    else:        return False


print( 'Intersection between two lines :\t',two_infinite_lines_intersection( [0,1], [2,3],[2,2], [-2,2]))



#
# line segment intersection using vectors
# see Computer Graphics by F.S. Hill
#
from numpy import *
def perp( a ) :
    b = empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b

# line segment a given by endpoints a1, a2
# line segment b given by endpoints b1, b2
# return
def seg_intersect(a1,a2, b1,b2) :
    da = a2-a1
    db = b2-b1
    dp = a1-b1
    dap = perp(da)
    denom = dot( dap, db)
    num = dot( dap, dp )
    return (num / denom)*db + b1

p1, p2 = array([27, 44]) , array([12, 32])
p3, p4 =  array([46, 53]) , array([17, 62])

print (seg_intersect( p1,p2, p3,p4))



####################     LINE SEGMENTS INTERSECTION   ###############

print('\n --------------------     LINE SEGMENTS INTERSECTION   --------------------')


class Point:
    """    Simple class for representing a point in a Cartesian coordinate system.    """
    def __init__(self, x, y):
        """        Create a new Point at x, y.        """
        self.x = x
        self.y = y
    def translate(self, dx, dy):
        """        Translate the point by dx and dy in the x and y direction.        """
        self.x += dx
        self.y += dy
    def __str__(self):
        return("Point at [%f, %f]" % (self.x, self.y))

def onSegment(p, q, r ):
    ''' Given three colinear points p, q, r, the function checks if
         point q lies on line segment 'pr'   '''
    if (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and
        q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y)) :
       return True

    return False

def orientation(p, q ,r) :
    ''':Description:   To find orientation of ordered triplet (p, q, r).
                The function returns following values :
            :0: --> p, q and r are colinear
            :1: --> Clockwise
            :2: --> Counterclockwise
    --> See http://www.geeksforgeeks.org/orientation-3-ordered-points/   for details of below formula.  '''
    val  = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if (val == 0):  return 0   # colinear
    if (val > 0): return 1     # clock or counterclock wise
    if (val < 0): return 2

def doIntersect(p1, q1, p2, q2) :
    ''' The main function that returns true if line segment 'p1q1' and 'p2q2' intersect.
    '''
#  Find the four orientations needed for general and  special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

#  General case:
    if (o1 != o2 and o3 != o4) : return True

#  Special Cases :
#        p1, q1 and p2 are colinear and p2 lies on segment p1q1
    if (o1 == 0 and onSegment(p1, p2, q1)) : return True

#       p1, q1 and p2 are colinear and q2 lies on segment p1q1
    if (o2 == 0 and onSegment(p1, q2, q1)) : return True

#       p2, q2 and p1 are colinear and p1 lies on segment p2q2
    if (o3 == 0 and onSegment(p2, p1, q2)) : return True

#      p2, q2 and q1 are colinear and q1 lies on segment p2q2
    if (o4 == 0 and onSegment(p2, q1, q2)) : return True

    return False           # Doesn't fall in any of the above cases

p1 , q1 = Point( 27, 44) , Point (12, 32)
p2 , q2 = Point(46, 53) , Point(17, 62)
p3,  q3 =  Point(46, 70) , Point(22, 40)

# print( two_lines_intersection( 27, 44, 12, 32) )
print( ' L1 & L2 two_lines_intersection test : ', doIntersect( p1, q1, p2, q2)      )
print( ' L2 & L3 two_lines_intersection test : ', doIntersect( p2, q2, p3, q3)      )
print( ' L1 & L3 two_lines_intersection test : ', doIntersect( p1, q1, p3, q3)      )

####################################

# The solution involves determining if three points are listed in a counterclockwise order.
# So say you have three points A, B and C. If the slope of the line AB is less than the slope of the line AC
# then the three points are listed in a counterclockwise order.
# This is equivalent to:

def ccw(A, B, C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

# You might be wondering how does this help? Think of two line segments AB, and CD.
# These intersect if and only if points A and B are separated by segment CD and points C and D are separated by segment AB.
# If points A and B are separated by segment CD then ACD and BCD should have opposite orientation
# meaning either ACD or BCD is counterclockwise but not both.
# Therefore calculating if two line segments AB and CD intersect is as follows:

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)


####### COmplete CODE

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

def ccw(A,B,C):
	return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)

def intersect(A,B,C,D):
	return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

a = Point(0,0)
b = Point(0,1)
c = Point(1,1)
d = Point(1,0)

print (intersect(a, b, c, d))
print (intersect(a, c, b, d))

################################

from math import gcd

SMOD = 50515093
TMOD = 500

def blum(pmod=TMOD):
    s = 290797
    while True:
        s = pow(s, 2, SMOD)
        yield s % pmod

class Range(object):
    #__slots__ = 'start', 'end'

    @staticmethod
    def create(a,b):
        return Range(min(a,b), max(a,b))

    def __init__(self, a, b):
        self.start, self.end = a, b

    def intersect(self, other):
        return Range(max((self.start, other.start)), min((self.end, other.end)))

    def __contains__(self, p):
        num,z = p
        if z<0:
            num, z = -num, -z
        return self.start*z <= num <= self.end*z

    def __bool__(self):
        return self.start < self.end

    def __str__(self):
        return "Range(%(start)d, %(end)d)" % self.__dict__
    __repr__ = __str__


def cartesianproduct(self, other):
    return (self.b*other.c-other.b*self.c,
             other.a*self.c-self.a*other.c,
             self.a*other.b-other.a*self.b)


print(' -------------------- CLASS Line ------------------------')
class line(object):
    def __init__(self, x1, y1, x2, y2):
        self.lowp, self.highp = (x1,y1),(x2,y2)
        A = -(y1-y2)
        B = (x1-x2)
        g = gcd(A,B)
        self.a, self.b = A//g, B//g
        self.c = -(x1*self.a + y1*self.b)

        self.xrange = Range.create(x1, x2)
        self.yrange = Range.create(y1, y2)

    def __contains__(self, point):
        x,y = point
        return self.a * x + self.b*y + self.c == 0

    def intersection_point(self, other):
        return cartesianproduct(self, other)

    def range_intersect(self, other):
        return (self.xrange.intersect(other.xrange),
                self.yrange.intersect(other.yrange))

    def intersect(self, other):
        range_x, range_y = self.range_intersect(other)
        if (bool(range_x) and bool(range_y)):
            x,y,z = self.intersection_point(other)
            if z == 0:
                return None
            if (other.lowp in self or other.highp in self or
                self.lowp in other or self.highp in other):
                return None
            X = (x,z)
            Y = (y,z)
            if (X in range_x and Y in range_y):
                 g = gcd(gcd(x,y),z)
                 return (x//g, y//g, z//g)
        return None

    def __str__(self):
        return str((self.lowp, self.highp))
    __repr__ = __str__

##############  TRIANGLE AREA CALCULATION using LINEAR ALGEBRA    #####################
# I had just described to my precalculus students that the determinant of a 3x3 matrix can be used to
# find the area of a triangle -- specifically, if the vertices are A(x1, y1), B(x2, y2) and C(x3, y3) then the area of the triangle
# is one half of the determinant of the matrix:

#                                                                                x1, y1, 1
#                                                                                x2, y2, 1
#                                                                                x3, y3, 1

def compute_triangle_area(P1, P2, P3):
    import numpy as np
    ''':where:  P1, P2, P3 are the three coord points each given in the form of tuple P(p.x, p.y)
    '''
    # A = np.array( [[P1[0], P1[1], 1], [P2[0], P2[1], 1], [P3[0], P3[1], 1] ])
    A =  [[P1[0], P1[1], 1], [P2[0], P2[1], 1], [P3[0], P3[1], 1]]
    det = np.linalg.det(A)      # determinant of a matrix
    return abs(det/2)

P1, P2, P3 = (-1, 0), (0, 3), (2, 0)
print('\nAREA OF THE TRIANGLE : \t', compute_triangle_area (P1, P2, P3))


################### Angle between two slopes
print('\n------------------- Angle between two slopes ---------------------- ')


def angle_between_two_slopes( slopes ):     # © Made by Bogdan Trif @ 2017-04-10, 12:30
    '''Correct formula with sign convention positive for θ counter-clockwise rotation from
    direction of radius vector 1 to 2 is . Always returns the acute angle  < 90 degrees
        tan(θ)= (m2−m1) / (1+m1*m2)
    :param m1:
    :param m2:
    :return: angle of the two slopes                        '''
    m1, m2 = slopes
    # print(m1, m2)
    try :   theta = math.atan( abs( (m2 -m1) /(1+m1*m2) ) )
    except :
        ZeroDivisionError
        return 90

    return theta * 180 / math.pi

print('\nAngle_between_two_slopes : \t', angle_between_two_slopes( ( -1/1, 1/1.001 ) )   )