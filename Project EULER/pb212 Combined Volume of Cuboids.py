#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Wed, 12 Dec 2018, 20:55
#The  Euler Project  https://projecteuler.net
'''
                             Combined Volume of Cuboids          -       Problem 212

An axis-aligned cuboid, specified by parameters { (x0,y0,z0), (dx,dy,dz) },
consists of all points (X,Y,Z) such that x0 ≤ X ≤ x0+dx, y0 ≤ Y ≤ y0+dy and z0 ≤ Z ≤ z0+dz.
The volume of the cuboid is the product, dx × dy × dz.
The combined volume of a collection of cuboids is the volume of their union
and will be less than the sum of the individual volumes if any cuboids overlap.

Let C1,...,C50000 be a collection of 50000 axis-aligned cuboids such that Cn has parameters

x0 = S6n-5 modulo 10000
y0 = S6n-4 modulo 10000
z0 = S6n-3 modulo 10000
dx = 1 + (S6n-2 modulo 399)
dy = 1 + (S6n-1 modulo 399)
dz = 1 + (S6n modulo 399)

where S1,...,S300000 come from the "Lagged Fibonacci Generator":

For 1 ≤ k ≤ 55, Sk = [100003 - 200003k + 300007k3]   (modulo 1000000)
For 56 ≤ k, Sk = [Sk-24 + Sk-55]   (modulo 1000000)

Thus, C1 has parameters {(7,53,183),(94,369,56)}, C2 has parameters {(2383,3563,5079),(42,212,344)}, and so on.

The combined volume of the first 100 cuboids, C1,...,C100, is 723581599.

What is the combined volume of all 50000 cuboids, C1,...,C50000 ?


'''
import time, zzz

# http://stackoverflow.com/questions/12769386/how-to-calculate-total-volume-of-multiple-overlapping-cuboids
# http://stackoverflow.com/questions/244452/what-is-an-efficient-algorithm-to-find-area-of-overlapping-rectangles          !!!!!!!!!!!
# https://www.reddit.com/r/projecteuler/comments/lzazf/problem_212_combined_volume_of_cuboids/
# https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle
import sys


def Lagged_Fibonacci_Generator_gen():           # EFFICIENT GENERATOR
    '''
    For 1 ≤ k ≤ 55, Sk = [100003 - 200003*k + 300007*k**3] (modulo 1000000) - 500000
    For 56 ≤ k, Sk = [S_(k-24) + S(k-55)] (modulo 1000000) - 500000                      '''
    tmp=[]
    for k in range(1,56) :
        s = (100003 - 200003*k + 300007*k**3) % 1000000
        # print(k, s)
        tmp.append(s)
        yield s
    while True :
        s = (tmp[-24]+tmp[-55])%1000000
        tmp.append(s)
        tmp.pop(0)
        # print(len(tmp) ,tmp)
        yield s


LFG = Lagged_Fibonacci_Generator_gen()

def generate_cuboids( how_many ) :

    for i in range(how_many) :
        s1, s2, s3, s4, s5, s6 = next(LFG), next(LFG), next(LFG), next(LFG), next(LFG), next(LFG)
        x0, y0, z0  = s1 % 10000, s2 % 10000, s3 % 10000
        dx, dy, dz = 1 + (s4 % 399) , 1 + (s5 % 399) , 1 + (s6 % 399)
        # print(str(i+1) +'.    x0, y0, z0, =', (x0, y0, z0 ) , '       dx, dy, dz =', (dx, dy, dz) )

        yield ( x0, x0+dx, y0, y0+dy, z0 , z0+dz  )



print()
def intersect_volumes( C1, C2) :
    ''':Description: Function which gives the volume intersection of two cuboids they share common volume.
        C1, C2 must have the form : C1 =  (x11, x12, y11, y12, z11, z12) , C2 = (x21, x22, y21, y22, z21, z22) ;
        where x12 > x11, y12> y11 ...and so on ...
        returns False if they do not share a common volume:
    :param C1: cuboid1 with x12 > x11, y12> y11 , z12> z11
    :param C2: cuboid 2 with  x22 > x21, y22> y21, z22> z21
    :return: False or the Common Volume (intersection )  in the form (x1, y1, z1), (x2, y2, z2)                             '''
    x11,  x12, y11, y12, z11, z12 = C1
    x21,  x22, y21, y22, z21, z22 = C2

    # print('C1 :   ', x11, y11, z11,'        ' ,x12, y12, z12 )
    # print('C2 :   ',  x21, y21, z21,'        ' ,x22, y22, z22 )
    dx = min(x12, x22) -  max(x11, x21)
    dy = min(y12, y22) -  max(y11, y21)
    dz = min(z12, z22)  -  max(z11, z21)
    # print('dx = ', dx, '      dy = ', dy , '      dz = ', dz  )
    if dx <=0 or dy <= 0 or dz <= 0 :
        return False
    else :
        x = max(x11, x21)
        y = max(y11, y21)
        z = max(z11, z21)
        # print('(x , dx) = ', x , x+ dx , ' ;     (y , dy) = ', y , y+ dy , ' ;    (z , dz) = ', z , z+ dz  )
        return ( x, x+dx, y, y+dy, z , z+dz )




C1 = ( 7, 1001, 53, 1422, 1183, 1239 )
C2 = ( 83, 2425, 563, 3775, 790, 2423 )

print('\nTest intersect_volumes(C1, C2) :  ' ,intersect_volumes(C1, C2) )

def cuboid_volume( C ) :
    x1, x2, y1, y2, z1 , z2   = C
    return (x2-x1)*(y2-y1)*(z2-z1)

print('Cuboid Volume : ', cuboid_volume( C1 ))

print('\n-----------  TESTS   - BRUTE FORCE,  Exponential Algorithm, INCLUSION - EXCLUSION Principle  ------------------------------')
t1  = time.time()

# This algorithm is only FOR TESTING. STEPS:        @2018-12-12, 19:50
# 1.  Add all the volumes and sum them;
# 2.  Then compares each volume with each other n(n+1)/2 comparisons and find common volumes
#     It makes an innitial list with level 1 common volumes and those will be substracted : odd sign
# 3.  From all the unique volumes found in level 1 it will make another n(n+1)/2 comparison
#     resulting in a level 2 list : even sign, these will be added.
# 4.  Repeat process until only one cuboid remains ...


# CUBOID = [ (9, 20, 2, 18, 1, 22), (12, 29, 3 , 12, 13, 23 ), (13, 25, 7, 22, 15, 21), (23, 29, 17, 25, 18, 26),
#       (27, 32, 11, 20, 16, 31 ), (9, 10, 18, 22, 24, 30 ), (24, 28, 26, 28, 17, 33 ) ]   # Right Cubes


nr_cuboids = 50000

CUBOID = list(generate_cuboids(nr_cuboids))
print('CUBOIDS : ', len(CUBOID) )
print(CUBOID[:30] ,'\n' )

def Combined_volume_exponential( list_of_cubes ) :
    CUB = list_of_cubes
    # print(len(CUB), CUB[:30],'\n')

    ### PART I - First we calculate all the volumes together. including the intersecting volumes (even multiple times )

    VOLUM = sum([ cuboid_volume(C) for C in CUB ])      # First we cumulate all the volumes

    ### PART II - Inclusion-Exclusion Principle

    UNION = set()       # Set to put common parts
    sign = 1
    while len(CUB) > 1 :
        UNION = set()
        for i in range(len(CUB)) :
            # sys.stdout.write('\r' + str(sign)+ '       ' + str(i) )   # Font Segoe UI Semibold
            # sys.stdout.flush()
            # print('sign = ', sign,'      ' , i )
            for j in range(i+1, len(CUB)) :
                if CUB[i] != CUB[j] :
                    C =  intersect_volumes( CUB[i] , CUB[j] )
                    if C :     #   if we have positive cuboid intersection then ... :
                        if C not in UNION :
                            vol = cuboid_volume(C)
                            # print(i ,j, '      C1 = ' , CUB[i],'       C2 =', CUB[j], '     resulting C = ', C ,  '      vol = ',   vol )

                            if sign %2 == 1 : VOLUM -= vol
                            if sign %2 == 0 : VOLUM += vol

                            # print('C = ', C ,'      vol = ',   vol )
                            UNION.add(C)

        print('\nUNION new length : ', len(UNION) )
        CUB = list(UNION)
        print('sign = ', sign )
        print('len(CUB) = ', len(CUB),'    ' , CUB[:30] )

        sign += 1
        # if sign == 10 : break

    print('\nTotal Union of Cuboids = ', VOLUM )
    return VOLUM


# Combined_volume_exponential(CUBOID)

t2  = time.time()
print('\nCompleted in :', round((t2-t1), 4 ), 's\n\n')


print('--------------------     Testing for small list of cubes ----------------')



# @2018-05-16 :
# https://www.hackerearth.com/practice/math/geometry/line-sweep-technique/tutorial/       !!!!!!!!!!
# https://pdfs.semanticscholar.org/presentation/b904/8991fc6dceb30da2db063194ffa0bdab8d06.pdf
# https://courses.csail.mit.edu/6.006/spring11/lectures/lec24.pdf     !!!
# https://www.youtube.com/watch?v=phrSBwaBs7o
#
# https://stackoverflow.com/questions/32216606/python-program-to-detect-intersection-of-one-dimensional-line-segments
# https://stackoverflow.com/questions/244452/what-is-an-efficient-algorithm-to-find-area-of-overlapping-rectangles
# https://github.com/adrianN/line_intersection/blob/master/README.md
# http://jeffe.cs.illinois.edu/teaching/373/notes/x06-sweepline.pdf



print('---------------------    2D  Sweep Line Algorithm Simulation ------------------------')
t1  = time.time()



print('------------                 Function TESTS              -----------')

test_quad_collection =  [ (24, 28, 26, 28), (23, 29, 17, 25), (12, 29, 3, 12), (13, 25, 7, 22)]
y_segments = sorted( [ (i[2],i[3]) for i in test_quad_collection ] )

def segment_colinear_intersect(segments):
    ''' :Description: Function which will intersect collinear segments and make a
     list with resulting common segments having x1= min and x2 = max . There will be
     no intersection any more, only the common parts.
    :Observation: The segments is a collection of (x1, x2) segments sorted . If not sorted => ERROR !
      '''
    try :
        A = [ list(segments[0]) ]
        # print('segments = ', segments, '   A = ', A ,'\n')

        for j in segments :
            Last_segm = A[-1]
            # print('BEFORE :   j = ', j, ' Last_segm = ', Last_segm, '  A :', A)

            if j[0] > Last_segm[1] :
                A.append([ j[0], j[1] ])

            if  j[0] <= Last_segm[1] :
                if j[1] > Last_segm[1] :
                    Last_segm[1] = j[1]

            # print('AFTER :   j = ', j, ' Last_segm = ', Last_segm, '  A :', A)
        # print('Final A : ', A)
        return A
    except IndexError :
        return IndexError

segment_colinear_intersect(y_segments)


Q = [ (9, 20, 2, 18), (12, 29, 3 , 12 ), (13, 25, 7, 22), (23, 29, 17, 25), (27, 32, 11, 20 ), (9, 10, 18, 22 ), (24, 28, 26, 28 ) ]   # Right quadrilaterals
# Q = [ (9, 20, 2, 18), (27, 32, 11, 20 ), (24, 28, 26, 28 ) ]   # Right quadrilaterals



def mapping_pair_of_elem( lst_tuples, k ):
    '''     Takes 2 elements from the quadruple or cuboid and do a mapping between k1, k+1 elem and all the
        quadrilateral, cuboid, ... etc ... It returns a dictionary of mappings in the form x1 :{x1,x2,y1,y2}, x2 :{x1,x2,y1,y2} ...etc...
        :Example:   Mapping between x1 & x2 values and the quadrilateral.
    '''
    Q = sorted(lst_tuples, key=lambda x: x[k])      # Sorts tuples after the specified elem within the tuple: 1-st, 2-nd, 3-rd, etc...
    # print('Q : ', Q )
    Qx=dict()
    for quad in Q :
        if not quad[k] in Qx :
            Qx[quad[k]] = { quad }
        else : Qx[quad[k]].add(quad)

        if not quad[k+1] in Qx :
            Qx[quad[k+1]] = { quad }
        else : Qx[quad[k+1]].add(quad)
    # print('Qx : ', Qx)

    return Qx


def main_sweep_line_algo():

    # Take ONLY the x elements from the tuples  : i[0] and i[1]
    # Flatten only first two elements of the tuples contained within the list
    X = sorted( { item for sublist in Q for item in sublist[0:2] } )
    print('\nX events : ', X)

    Qx = mapping_pair_of_elem(Q, 0)

    Y, queue = [], []
    SUM = 0

    for i in range(len(X)) :
        # print('\nstart quad : ', [ k[0] for k in Qx[ X[i]] if k[0] == X[i]  ])            #   Determine if it is a x1 event ( bottom left of square )
        # print('end quad : ',[ k[1] for k in Qx[ X[i]] if k[1] == X[i]  ])            #   Determine if it is a x2 event ( up right of square )

        ###     QUEUE   MANAGEMENT      ###
        for k in Qx[ X[i]] :
            if k[0] == X[i] :           # if is a START quad event : APPEND to queue
                queue.append(k )

            if k[1] == X[i] :          # if is an END quad event : POP from the queue
                queue.remove(k)

        ###   Y Part :
        y_segments = sorted( [ (i[2],i[3]) for i in queue ] )
        if len(y_segments) > 0 :
            Y = segment_colinear_intersect(y_segments)

            dy = sum( k[1]-k[0] for k in Y )
            dx = X[i+1]-X[i]

            print('queue : ', queue)
            print('x1 = ', X[i], '   x2 =', X[i+1], '    dx =', dx,  '   y_segments :', y_segments  ,'     Y:', Y, '   dy=', dy)
            SUM +=dy*dx

    print('SUM = ', SUM )

    return SUM                   # @2018-12-10, 18:05        !!!     BINGO !!!!      Algo works


# main_sweep_line_algo()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n============  My FIRST SOLUTION, 15 min Sweep Plane Algo   ===============\n')
t1  = time.time()

# @2018-12-12, 20:20    -   Algo can be improved

# Q = [ (9, 20, 2, 18, 17, 29), (27, 32, 11, 20, 4, 23 ), (24, 28, 26, 28, 24, 31 ) ]   # Right Cubes
# CUBOID = [ (9, 20, 2, 18, 1, 22), (12, 29, 3 , 12, 13, 23 ), (13, 25, 7, 22, 15, 21), (23, 29, 17, 25, 18, 26),
#       (27, 32, 11, 20, 16, 31 ), (9, 10, 18, 22, 24, 30 ), (24, 28, 26, 28, 17, 33 ) ]   # Right Cubes

def main_sweep_plane_algo() :

    print('CUBOIDS : ', len(CUBOID))
    print(CUBOID[-30:])

    VOL = 0
    Z_map = mapping_pair_of_elem(CUBOID, 4)

    # print('Z_mapping : ', Z_map )

    #   Z represents ALL the list of values of z values within the cuboids
    Z = sorted( { item for sublist in CUBOID for item in sublist[4:] } )
    print('Z : ', Z[-100:] )

    Zqueue =[]          #  queue of cuboids which are present at a speciffic z

    for z in range(len(Z)-1) :
        dz = Z[z+1] - Z[z]
        print('\n----------' +str(z)+'.    z = ', Z[z] , '     dz = ', dz , '         -----------')

        # print('     start cuboid : ', [ k[4] for k in Z_map[ Z[z]] if k[4] == Z[z]  ])            #   Determine if it is a x1 event ( bottom left of square )
        # print('     end cuboid : ',[ k[5] for k in Z_map[ Z[z]] if k[5] == Z[z]  ])            #   Determine if it is a x2 event ( up right of square )

        ###    Z QUEUE   MANAGEMENT      ###
        for a in Z_map[ Z[z]] :
            if a[4] == Z[z] :           # if is a START cuboid event : APPEND to queue
                Zqueue.append(a )

            if a[5] == Z[z] :           # if is an END cuboid event : POP from the queue
                Zqueue.remove(a)

        # print('Zqueue : ', Zqueue[:100] )
        ###     END Z QUEUE   MANAGEMENT      ###


        X_map = mapping_pair_of_elem(Zqueue, 0)
        # print('X_map : ', X_map)

        #   get ALL the values of "x"  found in the present Z queue
        X = sorted( { item for sublist in Zqueue for item in sublist[0:2] } )

        # print('\nX : ', X)


        Y, Xqueue  = [], []
        Area_section = 0

        for i in range(len(X)) :

            # print('     start quad : ', [ k[0] for k in X_map[ X[i]] if k[0] == X[i]  ])            #   Determine if it is a x1 event ( bottom left of square )
            # print('     end quad : ',[ k[1] for k in X_map[ X[i]] if k[1] == X[i]  ])            #   Determine if it is a x2 event ( up right of square )

            ###     START X QUEUE   MANAGEMENT      ###
            for k in X_map[ X[i]] :
                if k[0] == X[i] :       # if is a START cuboid event : APPEND to X queue
                    Xqueue.append(k )

                if k[1] == X[i] :           # if is an END cuboid event : POP from the X queue
                    Xqueue.remove(k)

            ###     END X QUEUE   MANAGEMENT      ###


            ###   Y Part :
            y_segm = sorted( [ (i[2],i[3]) for i in Xqueue ] )

            # print(str(i)+ '.    x = ', X[i], '      X queue = ', Xqueue )
            if len(y_segm) > 0:
                Y = segment_colinear_intersect(y_segm)
                dy = sum( y[1]-y[0] for y in Y )
                dx = X[i+1]-X[i]
                Area_section += dx *dy

                # print( '   dx=', dx,  ' ;   y_segm :', y_segm  ,'     Y:', Y, '   dy=', dy, '     Area_section = ', Area_section)

        # print(' Final Area_section = ', Area_section)

        VOL += Area_section* dz

    print('Combined Volume = ', VOL )
    return VOL


# main_sweep_plane_algo()         #   ANSWER  Combined Volume =  328968937309            Completed in : 989.6146 s










t2  = time.time()
print('\nCompleted in :', round((t2-t1),4), 's\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------- SOLUTION 1, INCLUSION-EXCLUSION PRINCIPLE, 2 MIN   --------------------------')
t1  = time.time()

# ====Tue, 14 Oct 2008, 10:48, gianchub, England
# Very nice and tricky problem. As everyone else I used inc/exc principle here.
# I made the cubes array, then sorted by x,y,z coordinates respectively and assigned an id to each cube,
# 0 being the leftmost cube and 49999 being the rightmost cube.
# Then I calc intersections of 2,3,4,... cubes and add/substract them to the whole sum, respectively.
# Sorting speeds things up since if you're checking for an intersection between cube a and b, and see that (a.x+a.dx < b.x), ' \
# you can avoid checking the cubes to the right of b.
#
# Here's my C# code (about 2.5 secs):
# Same algo, 24 secs with python.

def cube_sum(cubes):
    s = 0
    for x in cubes:
        s += x[3]*x[4]*x[5]
    return s

def get_intersections(cubes, inters):
    ret = []
    for i in range(len(inters)):
        a = inters[i]
        for j in range(a[9]+1, len(cubes)):
            b = cubes[j]
            if cube_intersect(a, b):
                inter = get_intersection(a, b)
                inter[9] = j
                ret.append(inter)
            else:
                if a[6] < b[0]:
                    break
    return ret

def get_intersection(a, b):
    x = max(a[0], b[0])
    rx = min(a[6], b[6])
    y = max(a[1], b[1])
    ry = min(a[7], b[7])
    z = max(a[2], b[2])
    rz = min(a[8], b[8])
    return [x, y, z, rx - x, ry - y, rz - z, rx, ry, rz, 0]

def cube_intersect(a, b):
    if a[6] < b[0] or b[6] < a[0]:
        return False # x doesn't overlap
    if a[7] < b[1] or b[7] < a[1]:
        return False # y doesn't overlap
    if a[8] < b[2] or b[8] < a[2]:
        return False # z doesn't overlap
    # x, y, z overlap
    return True


def p212():
    target = 50000
    fg = [0] * (target * 6 + 1)
    for k in range(6 * target + 1):
        if k <= 55:
            fg[k] = (100003 - 200003 * k + 300007 * k ** 3) % 1000000
        else:
            fg[k] = (fg[k - 24] + fg[k - 55]) % 1000000
    cubes = []
    for i in range(target):
        n = 6 * (i + 1)
        x, y, z, dx, dy, dz = fg[n-5]%10000, fg[n-4]%10000, fg[n-3]%10000, 1 + fg[n-2]%399, 1 + fg[n-1]%399, 1 + fg[n]%399
        cubes.append([x, y, z, dx, dy, dz, x+dx, y+dy, z+dz, i])

    # sorting on x, y, z
    cubes = sorted(cubes, key = lambda x:(x[0], x[1], x[2]))
    for i in range(len(cubes)):
        cubes[i][9] = i
    s = cube_sum(cubes)
    inters = cubes[:]
    m = -1
    while len(inters) > 0:
        inters = get_intersections(cubes, inters)
        print('Found %d intersections' % len(inters))
        s = s + m * cube_sum(inters)
        m *= -1
    print(s)


# p212()                  #  Completed in : 137.264 s

# Found 77168 intersections
# Found 34282 intersections
# Found 8289 intersections
# Found 1594 intersections
# Found 392 intersections
# Found 120 intersections
# Found 28 intersections
# Found 3 intersections
# Found 0 intersections
# 328968937309

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')       #  Completed in : 137.264 s


print('\n--------------------------SOLUTION 2,  Inclusion - Exclusion on 26x26x26 cubes  --------------------------')
t1  = time.time()

# =====   Tue, 26 Oct 2010, 22:42, cousin_it, Russia
# Python, divided the volume into 26x26x26 smaller cubes of size 400x400x400, used inclusion-exclusion principle.

def make_cuboid(x0, y0, z0, dx, dy, dz):
    return (x0, y0, z0, x0 + dx, y0 + dy, z0 + dz, 0)

s = [(100003 - 200003*k + 300007*k*k*k)%1000000 for k in range(56)]
for i in range(300000 - 55):
    s.append((s[-24] + s[-55])%1000000)

cuboids = [make_cuboid(
	s[6*n + 1]%10000,
	s[6*n + 2]%10000,
	s[6*n + 3]%10000,
	1 + s[6*n + 4]%399,
	1 + s[6*n + 5]%399,
	1 + s[6*n + 6]%399
) for n in range(50000)]

little_cubes = []

for i in range(26):
    for j in range(26):
		for k in range(26):
			little_cubes.append([make_cuboid(i*400, j*400, k*400, 400, 400, 400)])

for c in cuboids:
	for i in range(c[0]//400, c[3]//400 + 1):
		for j in range(c[1]//400, c[4]//400 + 1):
			for k in range(c[2]//400, c[5]//400 + 1):
				lc = little_cubes[i*26*26 + j*26 + k]
				for l in range(len(lc)):
					p = lc[l]
					if (c[0] < p[3]) and (c[1] < p[4]) and (c[2] < p[5]) and (p[0] < c[3]) and (p[1] < c[4]) and (p[2] < c[5]):
						lc.append((
							max(c[0], p[0]),
							max(c[1], p[1]),
							max(c[2], p[2]),
							min(c[3], p[3]),
							min(c[4], p[4]),
							min(c[5], p[5]),
							p[6] + 1
						))

total_volume = 0
for c in little_cubes:
	for p in c:
		if p[6] > 0:
			total_volume += (p[3] - p[0])*(p[4] - p[1])*(p[5] - p[2])*((-1)**(p[6] + 1))
print( total_volume)



t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


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

