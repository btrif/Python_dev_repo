#  Created by Bogdan Trif on 08-10-2017 , 11:01 AM.
# © o(^_^)o  Solved by Bogdan Trif  @
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
    # return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]
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

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()





# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()



t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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




