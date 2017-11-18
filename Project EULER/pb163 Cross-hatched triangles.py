#  Created by Bogdan Trif on 08-10-2017 , 11:01 AM.
# © o(^_^)o  Solved by Bogdan Trif  @       Completed on Mon, 6 Nov 2017, 00:13
#The  Euler Project  https://projecteuler.net
'''
                        Cross-hatched triangles     -       Problem 163

Consider an equilateral triangle in which straight lines are drawn from each vertex to the middle
of the opposite side, such as in the size 1 triangle in the sketch below.


Sixteen triangles of either different shape or size or orientation or location can now be observed in that triangle.
Using size 1 triangles as building blocks, larger triangles can be formed, such as the size 2 triangle in the above sketch.
One-hundred and four triangles  (104) of either different shape or size or orientation or location
can now be observed in that size 2 triangle.

It can be observed that the size 2 triangle contains 4 size 1 triangle building blocks.
A size 3 triangle would contain 9 size 1 triangle building blocks and
a size n triangle would thus contain n^2 size 1 triangle building blocks.

If we denote T(n) as the number of triangles present in a triangle of size n, then

T(1) = 16
T(2) = 104

Find T(36).

'''
import time, zzz, math
import itertools, operator, functools
from math import floor

def get_unique_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    print( list( factorise(n)) )
    # return [val for subslist in [[i[0]]*i[1] for i in factorise(n)] for val in subslist]
    return [val[0] for val in factorise(n)]



hatchedT = lambda n : floor( (2* n**3 + 5 * n**2 + 2 * n)/8 ) + \
                                2*floor( (n**3 - 1/3 * n)/2 ) + \
                                6*(  n*(n+1)*(n+2)/6  + floor( (2* n**3 + 5* n**2 + 2 *n)/8 )  +  \
                                floor( (2* n**3 + 3 * n**2 - 3 *n)/18 ) + \
                                floor( (2* n**3 + 3 * n**2 - 3 *n)/10 )  ) + \
                                 3 * floor( (22* n**3 + 45* n**2 - 4 *n)/48 )

print('Cross-hatched triangles =  ', hatchedT(36) )

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

T = { 1: 6, 2: 3 , 3: 6, 6: 1 }

T_ = []
c = 0
for i in range(2, 3) :
    # sqr = lambda i : i+2 if i%2==0 else i+1
    if i%2 ==0 : c+=1

    print(c)
    T_ += [ k*k for k in range( i, i+c+1 ) ]
    print(T_)
    for j, v in T.items() :
        lim = 6*i*i
        # print(str(i)+'.     ',  i*j*i ,'         ', j*j ,'       lim =  ' , 6*i*i )
        # if j*j <= lim and not lim/2 < j*j < lim   :             T_.append(j*j)
        if j*i*i <= lim and not lim/2 < j*i*i < lim :            T_.append(j*i*i)


    # T = list(sorted(set(T+T_)))
    print('level - ', i ,'     ' ,  T)

print()

# n = 16
# for i in range(2, 36+1 ) :
#     print(str(i) +'.       ' ,n  , i*i , math.factorial( i ) , '            Close result =  ',  n*(1+i*i  ) + math.factorial( i+2 )   )



# LINKS
# https://stackoverflow.com/questions/2830505/project-euler-163-understanding
# https://www.math.uni-bielefeld.de/~sillke/SEQUENCES/grid-triangles
# http://www.mathpuzzle.com/bdalytriangles.html
# https://oeis.org/A210687

# ==== GENERAL IDEAS ====
# ==== Sat, 13 Oct 2007, 15:43, shuniu , Canada
# The difficulty is on how to represent the graph...
# I did it by identifying each point as a six-tuple (since there are 6 axis), and storing
# - for each line, what are the valid point on that line
# - for every two lines, is there a valid point on their intersection

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()





# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,  < 1 sec -  graph theory problem --------------------------')
t1  = time.time()


# ====Sat, 16 Jan 2016, 10:55, jmarot, France
#
# I spent a fair bit of time trying to find a counting formula before I,
# like many others, decided to view this as a graph theory problem.
#
# Since there are a lot fewer lines than vertices, it makes sense to consider the dual graph,
# i.e. the graph whose vertices are the 9n−3 lines, and two lines are linked iff they intersect inside the triangle.
#
# Using an oblique frame where the triangle is defined by x≥0, y≥0 and x+y≤n,
# I worked out the equations to all 6 families of lines, computed intersection points by hand
# (it's a lot less work than it seems, since using symmetry there are really only 4 cases to consider),
#  then made some code that fills up the adjacency matrix MM and computes the trace of M3.
# The result is probably not very enlightening unless you've carried out the calculations yourself. :)
#
# A few complications to this approach:
#  - each triangle is counted 6 times, corresponding to 3 choices of starting side and 2 choices of orientation
#  - whenever k≥3k≥3 lines intersect at a single point, they generate k(k−1)(k−2) "fake" triangles of area zero,
# which have to be removed at the end.

import numpy as np

n=36
M=np.zeros((9*n-3,9*n-3),dtype=int)
M=np.matrix(M)
A=-1
B=n-1
C=2*n-1
Ap=4*n-1
Bp=6*n-2
Cp=8*n-3

def set(i,j):
    global M
    M[i,j]=M[j,i]=1

for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>=n:
            set(A+i,B+j)
            set(A+i,C+j)
            set(B+i,C+j)

for i in range(1,n+1):
    for j in range(-n+1,n):
        if abs(j)<=i:
            set(A+i,Ap+j)
            set(B+i,Bp+j)
            set(C+i,Cp+j)

for i in range(1,n+1):
    for j in range(-n+1,n):
        if 2*i+j>=n and i+j<=n:
            set(A+i,Bp+j)
            set(B+i,Cp+j)
            set(C+i,Ap+j)
        if 2*i-j>=n and i-j<=n:
            set(A+i,Cp+j)
            set(B+i,Ap+j)
            set(C+i,Bp+j)

for i in range(-n+1,n):
    for j in range(-n+1,n):
        if n-2*i-j>=0 and n+i-j>=0 and -i-2*j<=n:
            set(Ap+i,Bp+j)
            set(Bp+i,Cp+j)
            set(Cp+i,Ap+j)

T=(M**3).trace()
T=T[0,0]

# Fake triangle removal:
# n^2 points at the center of the small triangles
T=T-6*n**2
# The summits of the small triangle, except for the 3 main summits
T=T-120*(((n+1)*(n+2))//2-3)
# The 3 main summits
T=T-18
assert T%6==0
print(T//6)


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 2, BRUTE FORCE , 101 sec  --------------------------')
t1  = time.time()

# ===== Sun, 29 May 2016, 03:36, thorfax , USA
# I used brute-force to generate all the lines, and then find the ones that formed a triangle.
# I ended up having to subtract out all the triple intersections,
# but I found the counting formula n^2+3+20((n+1)(n+2)/2−3) for triple intersections.
# I also wrote a function to plot all of the lines so I could ensure that I was generating them correctly.
#
# My Python code takes 101s :(.

from functools import reduce
import numpy as np
from numpy import pi
import numpy.linalg as la
import pylab as pl
from matplotlib import collections  as mc
from itertools import combinations, product

"""
Project Euler problem 163: Cross-hatched triangles.
"""

def anchor_transform(anchor, mat, point):
    return anchor + mat.dot(point-anchor)

class lineSegment:
    def __init__(self, start, finish):
        self.a = np.array(start)
        self.b = np.array(finish)

    def __repr__(self):
        return str(tuple(self.a)) +","+str(tuple(self.b))
    def __str__(self):
        return str(tuple(self.a)) +","+str(tuple(self.b))


    def intersects(self, other):
        #l1*a + (1-l1) *b = l2 * oa + (1-l2) * ob
        A = np.array([self.a-self.b, other.b-other.a]).T
        lambdas = la.solve(A, other.b - self.b)
#        print lambdas
        return (lambdas[0] > 0 and lambdas[0] < 1) and (lambdas[1] > 0 and lambdas[1] < 1)

    def anchor_transform(self, anchor, mat):
        return lineSegment(anchor_transform(anchor, mat, self.a), anchor_transform(anchor, mat, self.b))

    def elongate(self, distance):
        vec = self.b - self.a
        delta = distance * vec / la.norm(vec)
        return lineSegment(self.a-delta, self.b + delta)


#L1 = lineSegment(np.array([27, 44]), np.array([12, 32]))
#L2 = lineSegment(np.array([46, 53]), np.array([17, 62]))
#L3 = lineSegment(np.array([46, 70]), np.array([22, 40]))

#print L1.intersects(L3)

def rot(theta):
    c,s = np.cos(theta), np.sin(theta)
    return np.array([[c, s],[-s, c]])

def plot_lines(lines):
    lines = map(lambda s: [tuple(s.a), tuple(s.b)], reduce(lambda a,b: a+b,lines))
    lc = mc.LineCollection(lines,  linewidths=2)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    pl.show()


def solve(n):
    """
    Any triangle is result of three intersections. Three lines, with each intersecting the other.
    There are 2 classes of lines, with each class containing 3 lines each (all 120-degree rotations of each other).
    The first class contains the lines forming the sides of the great (or host) triangle. There are n such lines of each type in this class.
    In the other class (containing orientations 90 deg, 210 deg, and 330 deg) have 2*n - 1 copies each.
    Thus we see that each class of triangles corresponds three types of lines.
    """

    theta1 = pi/6
    h = np.cos(theta1)

    #let the corner be at the bottom left
    lines = []
    #first do horizontal lines
    horiz = []
    for i in range(n):
        horiz.append(lineSegment(np.array([.5*(i),i*h]), np.array([n-.5*i,i*h])))
    lines.append(horiz)

    vert = []
    for i in range(1,2*n):
        vert.append(lineSegment([i*.5, 0],[i*.5, min(i,2*n-i)*h]))
    lines.append(vert)

    center = np.array([n*.5, n*h/3])

    r1 = rot(2*pi / 3)
    r2 = rot(-2*pi / 3)
    lines.append([s.anchor_transform(center, r1) for s in horiz])
    lines.append([s.anchor_transform(center, r2) for s in horiz])
    lines.append([s.anchor_transform(center, r1) for s in vert])
    lines.append([s.anchor_transform(center, r2) for s in vert])


    lines = map(lambda t: map(lambda s: s.elongate(.1), t), lines)
#    plot_lines(lines)
    tot = 0
    for a,b,c in combinations(lines, 3):
        for l1, l2, l3 in product(a, b, c):
            if l1.intersects(l2) and l2.intersects(l3) and l3.intersects(l1):
                tot += 1
    #now count all triple intersections
    extras = n*n + 3 + ((n+1)*(n+2)/2 -3) * 20
    return tot - extras

# print (solve(36))


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 3,  NICE,  Graph, 38 sec --------------------------')
t1  = time.time()

# ==== Fri, 3 Oct 2008, 18:18, eterevsky, Russia
# I've got a relatively simple solution. ' \
#  All the points have integer coordinates in the coordinate system with the basis (1/6, 0), (1/12, sqrt(3)/12)
# (basically those are the two sides of the triangle.
# In these coordinates all the points could be grouped by mod 6.
# For points from each group we know the vectors by which the lines are going through that point.
# The following is pretty obvious:

vects = {(0, 0): [(3, 0), (0, 3), (1, 1), (-1, 2), (-3, 3), (-2, 1)],
         (3, 0): [(3, 0), (-1, 2)],
         (0, 3): [(0, 3), (-2, 1)],
         (3, 3): [(1, 1), (-3, 3)],
         (2, 2): [(1, 1), (-1, 2), (-2, 1)],
         (4, 4): [(1, 1), (-1, 2), (-2, 1)]}

def count(n):
  total = 0
  for xb in range(n + 1):
    for yb in range(n - xb + 1):
      for (s, vs) in vects.items():
        x0 = 6*xb + s[0]
        y0 = 6*yb + s[1]
        if x0 + y0 <= 6*n:
          for v1 in vs:
            (x1, y1) = (x0, y0)
            while True:
              x1 += v1[0]
              y1 += v1[1]
              if x1 < 0 or y1 < 0 or x1 + y1 > 6*n: break
              if (x1 % 6, y1 % 6) in vects:
                for v2 in vs:
                  if v2 > v1:
                    (x2, y2) = (x0, y0)
                    while True:
                      x2 += v2[0]
                      y2 += v2[1]
                      if x2 < 0 or y2 < 0 or x2 + y2 > 6*n: break
                      if (x2 % 6, y2 % 6) in vects:
                        (dx, dy) = (x2 - x1, y2 - y1)
                        for v in vects[(x1 % 6, y1 % 6)]:
                          if dx*v[1] - dy*v[0] == 0:
                            total += 1

  return total

print (count(36))

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 4,  BRUTE FORCE, 72 sec --------------------------')
t1  = time.time()


# === Tue, 20 Jun 2017, 09:47, philiplu, USA
# My solution is on the slow side, 40 seconds in Python, but I'm actually kind of pleased with it.
# It's too complicated when compared to others who scaled the triangles so all the interesting points were lattice points, ' \
#   'but I like the labeling method I came up with.
#
# The basic idea is to label each point with (x,y,z) coordinates, where each is the "distance"
# from the three sides of the overall triangle, with the X side at the bottom, Y at left, Z at right.
# Rather than keep exact distances and deal with quadratic surds,
# I instead treat each unit triangle as having side lengths of 2, and treat all points interior to the unit triangles
# as having an odd coordinate.
# Thus, for instance, for n = 2, the center point in the small triangle in the lower-left corner has coordinates (1,1,3),
# since it is half a triangle away from the X and Y sides, and 1 1/2 triangles away from the Z side.
#
# Here's a diagram labeling all the points for n = 2 (built with GeoGebra, which has been very useful for some problems,
# like the Torricelli point one):
#
# Image can be found at http://i.imgur.com/m99Vgd4.png?1, until I can figure out how to directly embed a full image.
#
# Once I had a labeling scheme, the brute-force is pretty simple.
# First, recurse on previous sizes - for size n, solve for n-1 first, then add the new nth row of unit triangles at the bottom of the large triangle, and walk just the newly-added points, which will have x coordinates of 0 and 1.  For each of those, walk up pairs of lines that intersect in each new point, and for each pair of points on those lines, see if they are connected by a third line.
#
# Like I said, the labeling scheme makes the walking of lines and testing for connectedness more expensive
# then necessary (never mind I'm still just doing a brute-force search),
# but I like the way I was able to parameterize the walking through points and lines.


import sys
import itertools as it



#               p1 gen   radial lines   offsets in lines
GenPoints = ( ( (0,0,0), (0,1,2,3,4,5), (0,0,0,0,0,0)),
              ( (0,1,1), (0,6),         (0,0)),
              ( (1,0,1), (2,5),         (1,2)),
              ( (1,1,1), (1,6,5),       (1,1,1)),
              ( (1,1,2), (1,4),         (2,1)),
              ( (1,1,3), (1,3,5),       (3,1,3)) )

# delta x,y,z to generate next point along radial lines
GenLines = ( ( (0,1,-1), ),
             ( (1,1,-1), (0,0,-1), (0,0,-1), (1,1,-1) ),
             ( (1,0,-1), ),
             ( (1,-1,-1), (1,0,0), (1,0,0), (1,-1,-1) ),
             ( (1,-1,0), ),
             ( (1,-1,1), (0,-1,0), (0,-1,0), (1,-1,1) ),
             ( (1,0,0), (1,-1,-1), (1,-1,-1), (1,0,0) ) )

def p1_generator(n, x, init_y, init_z_offset):
    y, z = init_y, n - init_z_offset
    while z >= 0:
        yield x, y, z
        y, z = y+2, z-2

def gen_line_points(n, p1, index, offset):
    x, y, z = p1
    for dx, dy, dz in it.islice(it.cycle(GenLines[index]), offset, None):
        x, y, z = x+dx, y+dy, z+dz
        if not (0 <= y <= n and 0 <= z <= n):
            break
        yield x, y, z

def indiff(p):
    return (p[0]-p[1], p[1]-p[2], p[2]-p[0])

def connected(p1, p2):
    if any(a == b and a % 2 == 0 for a, b in zip(p1, p2)):
        return True
    if any(a == b and a % 2 == 0 for a, b in zip(indiff(p1), indiff(p2))):
        return True
    return False

def solve(n):
    count = solve(n-1) if n > 1 else 0

    n *= 2
    for p1_gen, lines, offsets in GenPoints:
        for p1 in p1_generator(n, *p1_gen):
            for i, p2_line in enumerate(lines[:-1]):
                for p2 in gen_line_points(n, p1, p2_line, offsets[i]):
                    for j, p3_line in enumerate(lines[i+1:], i+1):
                        for p3 in gen_line_points(n, p1, p3_line, offsets[j]):
                            if connected(p2, p3):
                                count += 1

    return count

def p163(n = 36):
    return solve(n)

print(p163(*(int(arg) for arg in sys.argv[1:])))


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n---------------------SOLUTION 5,  Each line by its set of intersection points  --------------------------')
t1  = time.time()

# === Tue, 11 Jun 2013, 19:21, tom.wheldon, England
# I represent each line by its set of intersection points, then use set intersection to find the triangles.
# Straightforward, but a bit long-winded as it takes 32 lines of code to generate the lines.
# Runs in 3 seconds in Python.

from itertools import accumulate, combinations

def solution5(N):


    offsets = {n: [0] for n in range(1,2*N)}
    for i in range(1,N+1):
        for j in range(1,i+1):
            offsets[i].extend([2,1] if (i-j)%2 else [1,2])
        offsets[i] = list(accumulate(offsets[i]))
    for i in range(1,N):
        offsets[N+i] = offsets[N-i]


    lines = {n: dict() for n in range(6)}

    for i in range(N):
        lines[0][i] = set()
        for j in range(2*(N-i)+1):
            lines[0][i].add((8*i + 2*j, 3*j))

    for i in range(N):
        lines[1][i] = set()
        for j in range(2*(N-i)+1):
            lines[1][i].add((8*(N-i) - 2*j, 3*j))

    for i in range(N):
        lines[2][i] = set()
        for j in range(4*i, 8*N - 4*i + 1, 4):
            lines[2][i].add((j,6*i))

    for i in range(1,2*N):
        lines[3][i] = set()
        for k in offsets[i]:
            lines[3][i].add((2*(i+k), 3*i - k))

    for i in range(1,2*N):
        lines[4][i] = set()
        for k in offsets[i]:
            lines[4][i].add((8*N - 2*(i+k), 3*i - k))

    for i in range(1,2*N):
        lines[5][i] = set()
        for k in offsets[i]:
            lines[5][i].add((4*i,2*k))

    triangles = 0
    for (i,j,k) in combinations(range(6),3):
        for a in lines[i].values():
            for b in lines[j].values():
                ab = a&b
                if len(ab) != 1: continue
                for c in lines[k].values():
                    if len(ab|a&c|b&c) == 3:
                        triangles += 1

    return print(triangles)



t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 6,  PATTERN  --------------------------')
t1  = time.time()

# === Mon, 12 Jan 2009, 22:21, tolstopuz, Russia
# Long and tedious paper work.
# I also wrote bruteforce program to help debugging for small n and then threw it away.

n = 36
s = 0

for h in range(n):
    for x in range(1, n - h + 1):
        s += 6 * (x + (3 * x // 2))
        s += 3 * x
        s += 6 * (x // 2)
        s += x

        b = min(x, n - h - x)
        s += 6 * (min(x, 2 * b) + min(2 * x, 3 * b))
        s += 3 * min(x, 3 * b)
        s += 6 * min(3 * x // 2, 3 * b) - 4 * min(x // 2, b)
        s += 2 * min((x - 1) // 2, b)
        s += 2 * min((x - 1) // 2, max(b - 1, 0))
        s += b

print(s)

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()



t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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




