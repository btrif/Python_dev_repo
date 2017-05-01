#!/usr/bin/python                   o(^_^)o
# Solved by Bogdan Trif @       Completed on Wed, 8 Mar 2017, 19:15
#The  Euler Project  https://projecteuler.net
'''
Rectangles in cross-hatched grids       -       Problem 147

In a 3x2 cross-hatched grid, a total of 37 different rectangles could be situated within that grid as indicated in the sketch.

There are 5 grids smaller than 3x2, vertical and horizontal dimensions being important,
i.e. 1x1, 2x1, 3x1, 1x2 and 2x2. If each of them is cross-hatched, the following number of different rectangles
could be situated within those smaller grids:

                                        1x1: 1
                                        2x1: 4
                                        3x1: 8
                                        1x2: 4
                                        2x2: 18

Adding those to the 37 of the 3x2 grid, a total of 72 different rectangles could be situated within 3x2 and smaller grids.

How many different rectangles could be situated within 47x43 and smaller grids?
'''

import time
from itertools import combinations
from numpy import prod
from gmpy2 import is_prime
import functools, operator

def factors(a):
    '''Outputs a list of the unique prime factors of its input; The Second Fastest Algorithm
    This Function is splitting a number in its factors, and detects also if the number is a prime. '''
    b = 2
    d = []
    f = a
    while f > 1:
        while f % b != 0:
            b = b + 1
        d = d + [b]
        f = f / b
    if len(d) >1:
        return  d
    else: return print(a,' is prime')

def make_rectangles(n) :
    ''' Functions which transform an area into a rectangle
    :param n: is the Area which will be computed. If the number is a prime it just returns [n,1]
    :return: a list with pairs of numbers which represent sides of a rectangle    '''
    lst =[]
    if is_prime(n) == False:
        # print(i, factors(i))
        C = list(combinations(factors(n), 2))
        for k in range(len(C)):
            q = [ n//prod(C[k]),  prod(C[k]) ]
            q = sorted(q)
            if q not in lst : lst.append( q )
        for j in range( len(factors(n))):
            p = ( int(prod(factors(n)[0:j]))  , prod(factors(n)[j::]) )
            p = sorted(p)
            if p not in lst : lst.append( p  )
        return lst
    elif is_prime(n) == True :
        lst = [n , 1]
        return [lst]

# print('\nMake Rectangles Function: ',make_rectangles(2772))

def calc_rectangle(a , b):
    '''    Function which calculates the possible number of sub rectangles in an area
    :param a: is the length of the rectangle
    :param b:  the height of the rectangle
    :return:  returns the number of rectangles that can be formed inside    '''
    S = 0
    for i in range(1, a+1):
        for j in range(1, b+1):
            S += (a-i+1) * (b-j+1)
    return S

def get_one_row_rectangle(a ) :
    return calc_rectangle(a, 1) +a-1


def calculate_rombs( a , b ):
    if a==1 : return b-1
    if b==1 : return a-1
    R = {}
    #######   CASE 1--> a=b    ##########
    if a == b  :
        l_max = 2*a - 2
        group = []
        for i in range(l_max, 0, -2):
            group.append( (i,2) )
        ### Generate blocks :
        BL = []
        if a%2==0 :  max_rect = ( a, a)
        if a%2==1 :  max_rect = ( a+1, a-1)
        S_rect = sum(max_rect)
        R[max_rect] =1

        for i in range(S_rect, 1 ,-1) :
            for j in range(1, i+1 ):
                if i+j > S_rect : break
                if  ( ( i%2 == 0) or (j%2 == 0) ) or ( i+j <S_rect ) :
                    # print(i, j)
                    BL.append( ( i, j) )

     #####   CASE 2  --> a != b   ########
    if a != b  :
        l_max = (min(a, b) - 1)*2 +1
        group = []
        h = abs(a-b)        # How many max lengths
        group.append((l_max, h ))
        for i in range(l_max-1, 0, -2):
            group.append( (i,2) )

        ### Generate blocks :
        BL = []
        for i in range( l_max, min(a,b)-1, -1 ):
            for j in range( l_max-i+1, 0, -1 ):
                BL.append( ( i, j) )
        for i in range( min(a,b)-1, 1, -1):    #we neglect (1, 1)
            for j in range(i, 0, -1):
                BL.append( (i,j))

    ####COMMON OPERATIONS ####
    #### Q: How many k x 1 Rectangles ?
    max_length = group[0][0]


    for i in range(max_length, 1, -1):
        F = [ b[1] for b in group if i <= b[0]  ]
        G = [ c[0]-i+1 for c in group if i <= c[0] ]
        fg = sum ( [ i*j for i,j in zip(F, G)]   )
        R[(i, 1)] = fg
        BL.remove( (i , 1) )
        # print(F, G,   fg )
    # print('\n', max(BL))
    for I in BL :
        g_s_k = [ i for i in R.keys() if sum(i)== sum(I) ][0]  # get_sum_key
        # print(g_s_k,'           ' ,I)
        if ( g_s_k[0]%2 == 1) and ( g_s_k[1]%2 == 1) :  # both ODD
            if I[0]%2 == 1 and I[1]%2 == 1 :
                # print( I,'    =    ' , R[g_s_k]  )
                R[I] = R[g_s_k]
            else :       R[I] = R[g_s_k]+1
        else :
            if I[0]%2 == 1 and I[1]%2 == 1 :
                R[I] = R[g_s_k]-1
            else :      R[I] = R[g_s_k]

    # print('group : \t', group)
    # print('Blocks : \t', BL)
    # print('dict R : \t', R)
    # print( ' blocks of equal elements  : \t',  [ v  for k, v in R.items() if ( k[0] == k[1] )  ]  )
    S = sum([ k[0]*k[1] for k in group ])
    # print( 'Blocks of  1x1 : \t', S)
    for k, v in R.items() :
        # print(S)
        if k[0] != k[1] : S += 2*v
        else : S += v

    return S




def get_squares_rombs(a, b):
    x, y = calc_rectangle(a,b), calculate_rombs(a, b)
    return x+y




print('\n--------------------------TESTS------------------------------')
t1  = time.time()

print('\ncalc_rectangle : \t',calc_rectangle(3, 1) ,'\n')
print('\nget_one_row_rectangle : \t',get_one_row_rectangle(1) ,'\n')

print('\ncalculate_rombs : \t', calculate_rombs( 6 , 3)  )

print('\nget_squares_rombs : \t', get_squares_rombs( 8, 9)  )


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION, SLOW, 3 min  ===============\n')
t1  = time.time()


def cross_hatched_grids(a, b) :
    S = 0
    for i in range(1, a+1) :
        for j in range(1, b+1) :
            mag = get_squares_rombs(i,j)
            print(i,j,'            ', mag)
            S+= mag

    return print('\nAnswer : \t', S)


# cross_hatched_grids(47, 43)             #   Answer : 	 846910284


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, 13 ms  INCREDIBIL --------------------------')
t1  = time.time()

# ==== Fri, 30 Jan 2015, 15:48, boondoggle, USA
# After noticing some patterns and playing around with Wolfram Alpha for a while:


from itertools import product, starmap

def grid(x, y):
    """Returns a list of vertices on a grid of given size."""
    return product(range(1, x+1), range(1, y+1) )

def combined_count(x, y):
    if y > x:
        x, y = y, x
    return int(round(1/12 * y * (3 * x**2 * y + 3 * x**2 + 16 * x * y**2 + 3 * x * y - x - 8 * y**3 + 2 * y - 6)))

def total_count(x, y):
    if y > x:
        x, y = y, x
    return sum(starmap(combined_count, grid(x, y)))

print( total_count(47,43 ) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  6 sec --------------------------')
t1  = time.time()

# === Sun, 14 Oct 2012, 08:51, thedoctar, Australia
# I found an equation for the normal rectangles, x(x+1)(x+2)y(y+1)(y+2)/36,
# and for oblique rectangles with dimensions m, n. The explanation is rather complicated, anyway, here's my code.

def f(x, y):
	limit, output = (min(x, y)-1)*2+1, 0
	for m in range(1, limit+1):
		for n in range(1, limit-m+2):
			output += (x-(m+n-2+(m+n-2)%2)/2)*(y-1-(m-1-(m-1)%2)/2-(n-1-(n-1)%2)/2)+(x-1-(m+n-2-(m+n-2)%2)/2)*(y-(m-1+(m-1)%2)/2-(n-1+(n-1)%2)/2)
	return output

def solution2():
    limitx, limity = 43, 47
    output = 0
    for x in range(1, limitx+1):
        for y in range(1, limity+1):
            output += f(x, y)
    return print (output+limitx*(limitx+1)*(limitx+2)/6*limity*(limity+1)*(limity+2)/6)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  VERY FAST --------------------------')
t1  = time.time()

# === Sun, 2 Jun 2013, 18:27, Hariram, India
# I found a quite different recursive formula number of possible slant rectangles. If B(x, y) is the number of slant rectangles:
# B(x, y) = 2*B(x-1, y-1) - B(x-2, x-2) + 8(x-1)(y-1) + 1
# B(1, z) = B(z, 1) = z-1

h=47
w=43

A = [[0]*w for i in range(h)] # Normal block
B = [[0]*w for i in range(h)] # Diagonal blocks

for i in range(h):
    for j in range(w):
        if i == 0:
            A[0][j] = (j+1)*(j+2)/2
            B[0][j] = j
        elif j == 0:
            A[i][0] = (i+1)*(i+2)/2
            B[i][0] = i
        else:
            A[i][j] = A[i][0] * A[0][j]
            B[i][j] = 2*B[i-1][j-1] + 8*i*j + 1
            if i>1<j :
                B[i][j] -= B[i-2][j-2]

print (sum([sum(i) for i in A]) + sum([sum(i) for i in B]))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# ==== Sat, 6 Jul 2013, 11:38, EdM, France
# A counting problem. Not funny for me...
# PE147 : nombre de rectangles = 846910284 en 0.499 s



# -- Rectangles obliques de largeur i < m interceptant les lignes 1 et m
def b_(n, m, i):
    s = 0
    if i%2 == 1:
        s += 2*(n - m) + 2*(2 + 2*(n - m))
        if i == m - 1:
            return s + (n - m + 2)
        else:
            return s + 2*(n - m + 2)
    else:
        s += 2*(n - m + 1) + 2*(2*(n - m + 1))
        if i == m - 1:
            return s + (n - m + 1)
        else:
            return s + 2*(n - m + 1)
# -------------------------------

# -- Carres obliques de taille m x m interceptant les lignes 1 et m
def c_(n, m):
    return n - m + (m + 1)%2
# -------------------------------

# -- Rectangles interceptant les lignes 1 et m
def t_(n, m):
    s = n*(n + 1)/2
    for i in range(1, m):
        s += b_(n, m, i)
    return s + c_(n, m)
# -------------------------------

# -- Rectangles dans un rectangle de taille n x m
def s_(n, m):
    if n < m:
        return s_(m, n)
    s = 0
    for k in range(1, m + 1):
        s += (m + 1 - k)*t_(n, k)
    return s
# -------------------------------

# -- Routine principale ---------
cpt = 0

for n in range(1, 48):
    for m in range(1, 44):
        cpt += s_(n, m)
# -------------------------------


print ("PE147 : nombre de rectangles =", cpt)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,  Dynamic Programming --------------------------')
t1  = time.time()

# ==== Sat, 7 Sep 2013, 17:32, Oren, USA
# Dynamic programming, although it is clear that the number of rectangles must be a
# symmetric fourth order polynomial in m and n with zero free coefficient (since the count is 0 for m=n=0),
# hence a closed form formula (leading to an O(1) algorithm)
# could be derived from a small number of cases by polynomial interpolation.
# For illustration, the code uses a closed form formula for
# rectangles aligned with the vertical and horizontal axes and DP for tilted rectangles.

import numpy as np

def type1(M, N):
    '''# of rectangles aligned with the vertical and horizontal axes. R[m,n] is the count for a mxn grid,
    m <= M, n <= N.'''
    n, m = np.meshgrid(range(N + 1), range(M + 1))
    return n * (n + 1) * m * (m + 1) // 4

def type2(M, N):
    '''# of tilted rectangles. R[m,n] is the count for a mxn grid, m <= M, n <= N.'''
    R = np.zeros((M + 1, N + 1), dtype=int)
    R[1, 1:N + 1] = np.arange(N)  # Initial Condition
    # Dynamic programming
    for m in range(2, M + 1):
        for n in range(1, min(N, m) + 1):
            R[m, n] = R[m - 1, n] + n * (4 * n * n - 1) // 3
        if m <= N: R[m, m] -= m
        t = m * (4 * m * m - 1) / 3
        for n in range(m + 1, N + 1): R[m, n] = R[m, n - 1] + t
    return R

'''Total number of rectangles in an MxN grid and smaller grids.'''
all_rect = lambda M, N: np.sum(type1(M, N) + type2(M, N))

if __name__ == "__main__":
    print (all_rect(47, 43))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6, RECURSION  --------------------------')
t1  = time.time()

def solution_6():
    g = lambda m, n, x: m+n-abs(m-x)

    # @memoized
    def h(m, n):
        if m == 1: return n-1
        if m > n: return h(n, m)
        s = h(m-1, n)
        for x in range(1, n+1):
            for y in range(n-x, g(m, n, x)):
                s += min(g(m, n, y+1), g(m, n, n-x))-x
                if y > n-x: s += min(g(m, n, y+1), g(m, n, n-x+1))-x
        return s

    t = 0
    for m in range(43):
        for n in range(47):
            t += h(m+1, n+1) + (m+1)*(m+2)*(n+1)*(n+2)//4
    return print (t)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7,  7 sec --------------------------')
t1  = time.time()

# ==== Tue, 30 Dec 2008, 00:40, tolstopuz, Russia

s = 0
for w in range(1, 48):
    for h in range(1, 44):
        s += w * (w + 1) * h * (h + 1) // 4
        for x in range(0, 2 * w):
            xx = 2 * w - x
            for y in range(x % 2, 2 * h, 2):
                yy = 2 * h - y
                minw = max(min(y, xx - yy),0)
                maxw = min(y, xx)
                s += yy * minw + (2 * xx - minw - maxw - 1) * (maxw - minw) // 2

print(s)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')


print('\n--------------------------SOLUTION 8,  14 sec --------------------------')
t1  = time.time()

# ==== Tue, 21 Jul 2009, 08:49, thagg, USA
# The rectilinear rectangles are from problem 85, but the angled ones are a little harder.
# First I wrote a program to draw the rectangle with the the diagonal lines very dark and the horizontal
# and vertical lines very faint, to make it easier to see what was going on.
#
# Dividing the problem into "even" lines where the first square of the block fell completely within one
# of the rectilinear squares, and the "odd" rows than had the initial square bisected by the rectilinear lines,
# it was pretty easy to calculate how many 'w' by 'h' blocks would fit into each line, and the number of even and odd lines.
#
# What took me a while to realize is that in a (say) 4x3 rectangle you can have diagonal blocks 5x1 long --
# I had originally deceived by the smaller test cases that the longest block was at most as long as the longest edge
# of the original rectangle -- but those diagonal blocks are smaller by sqrt(.5)!
#
# Runs in 14 seconds, but more importantly took 58 minutes to write.

sum = 0

for Y in range(1, 43 + 1):
	for X in range(1, 47 + 1):

		# diagonals
		limit = X + Y
		for w in range(1, limit):
			for h in range(1, limit):
				even = X - (w + h + 0) // 2		# how many per even row
				n_even = Y					# how many even rows
				n_even -= h // 2				# subtract those that go off the top
				n_even -= w // 2				# subtract those that go off the bottom
				if(even > 0 and n_even > 0):
					sum += even * n_even
				odd = X - (w + h - 1) // 2		# how many per odd row
				n_odd = Y - 1                               # how many odd rows
				n_odd -= (h - 1) // 2			# subtract those that go off the top
				n_odd -= (w - 1) // 2			# subtract those that go off the bottom
				if(odd > 0 and n_odd > 0):
					sum += odd * n_odd

		# rectilinear
		for w in range(1, X + 1):
			for h in range(1, Y + 1):
				sum += (X - w + 1) * (Y - h + 1)


print (sum)

t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')

