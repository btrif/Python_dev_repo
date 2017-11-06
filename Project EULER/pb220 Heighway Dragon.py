#!/usr/bin/python
# Solved by Bogdan Trif @       Completed on Tue, 28 Feb 2017, 19:57
#The  Euler Project  https://projecteuler.net
'''
                            Heighway Dragon     -       Problem 220

Let D0 be the two-letter string "Fa". For n≥1, derive Dn from Dn-1 by the string-rewriting rules:

"a" → "aRbFR"
"b" → "LFaLb"

Thus, D0 = "Fa", D1 = "FaRbFR", D2 = "FaRbFRRLFaLbFR", and so on.

These strings can be interpreted as instructions to a computer graphics program,
with "F" meaning "draw forward one unit", "L" meaning "turn left 90 degrees",
"R" meaning "turn right 90 degrees", and "a" and "b" being ignored.
The initial position of the computer cursor is (0,0), pointing up towards (0,1).

Then Dn is an exotic drawing known as the Heighway Dragon of order n.
For example, D10 is shown below; counting each "F" as one step,
the highlighted spot at (18,16) is the position reached after 500 steps.

What is the position of the cursor after 1012 steps in D50 ?
Give your answer in the form x,y with no spaces.
'''

import time
import math

def findnth(source, target, n):
    num = 0
    start = -1
    while num < n:
        start = source.find(target, start+1)
        if start == -1: return -1
        num += 1
    return start

def replacenth(source, old, new, n):
    p = findnth(source, old, n)
    if n == -1: return source
    return source[:p] + new + source[p+len(old):]


def get_next_orientation( current_orientation, operation):
    # Left, Righ, Up, Down - L, R, U, D
    o = 'RULD'
    if operation == 'L' :
        i = o.find(current_orientation)
        return o[ (i+1)%4 ]
    if operation == 'R' :
        i = o.find(current_orientation)
        return o[(i-1)%4]


def path_sequence_gen(iterations) :
    a =  'aRbFR'
    b = 'LFaLb'
    H = 'FaRbFR'

    for d in range(1, iterations) :
        a_cnt = H.count('a')
        ind =1
        for i in range(a_cnt):
            # print('before -- >   ' ,H, len(H))
            H = replacenth(H, "a", a, ind)
            # print(ind,    H, len(H), '   <-- a  after')
            ind+=1
            # print('before -- >   ',  H, len(H) )
            H = replacenth(H, "b", b, ind)
            # print(ind,  H, len(H),  '   <-- b   after')
            ind+=1
    return H

def log_spiral_pow_of_2( power_lim ) :
    LOG2 = { 0 : (0,1) , 1:( 1, 1 ) ,2 : ( 2,0 ) }
    i=2
    x, y = 2, 0
    r = math.sqrt(x**2+y**2 )
    theta = 0*math.pi/180
    # print(str(i)+'.   ( x,y ) = ', x, y, '     angle= ', theta, '    r=', r)

    while i < power_lim :
        theta = (theta - 45)%360
        r *= math.sqrt(2)
        x = round(r * math.cos(theta*math.pi/180))
        y = round(r * math.sin(theta*math.pi/180))
        i+=1
        # print(str(i)+ '.   ( x,y ) = ', x, y, '     ;  theta =', theta, '  ;    r=', r)
        LOG2[i] = (x,y)
    return LOG2


nr = 10**12 - 2**39
print('\nLeft number : ', nr,'\n')

def decompose_in_2_powers(nr):
    X = []
    while nr > 0 :
        l = math.floor(math.log2(nr))
        # print('power = ',l, '     ', nr , '          ',2**l, )
        nr -= 2**l
        X.append(l)
    # print('\nVerification Sum :\t', sum([2**i for i in X]), X,'\n')

    return X

print('decompose_in_2_powers : \t' ,decompose_in_2_powers(10**4) )

def get_point_coord(nr_of_steps) :

    N = decompose_in_2_powers(nr_of_steps)
    L = log_spiral_pow_of_2(int(math.log2(nr_of_steps)))
    # print(N, '\n',L)
    x , y = L[N[0]][0],  L[N[0]][1]
    for i in range(1, len(N) ):
        # print('(x , y) = ', (x, y))
        x -= L[N[i]][0]
        y -= L[N[i]][1]
    return x, y

n= 971
print('\n get_point_coord ', n ,'steps : \t' , get_point_coord(n) )




print('log_spiral_pow_of_2 : \t', log_spiral_pow_of_2(40))


def heighway_sequence(degree):
    if degree == 1:
        return 'L'
    else:
        first = heighway_sequence(degree - 1)
        second = ''.join(['L' if turn == 'R' else 'R' for turn in first[::-1]])
        return first + 'L' + second

def heighway(degree):
    directions = [(0,1), (1,0), (0,-1),(-1,0)]
    d = 0  # Initial direction: (1,0) = +1 x axis
    points = [(0,0), (0,1)]
    here = (0,1)
    for turn in heighway_sequence(degree):
        d += 1 if turn == 'L' else -1
        d %= 4
        here = (here[0]+directions[d][0], here[1]+directions[d][1])
        points.append(here)
    return points
# print(sum([ p[0] for p in points ]))
# print(sum([ p[1] for p in points]))


points = heighway(14)
print(points[10**4])

print('\n--------------------------TESTS------------------------------')
t1  = time.time()


def dragon_path(n):
    length = 1
    pos = [0,1]

    while length < n :
        pos = [ pos[0]+pos[1], -pos[0]+pos[1] ]
        length*=2

    if length == n :  return pos

    diff = length - n

    pos2 = dragon_path(diff)

    pos2 = [ -pos2[1], pos2[0] ]

    return [ pos[0]+pos2[0]  , pos[1]+pos2[1] ]

dragon_path(10)

# D15 = the Generated Sequence :  131070


# print('\n-------- Next Orientation Tests ------------')
# print('\nget_next_orientation : \t', get_next_orientation('R', 'L' ))
# print('get_next_orientation : \t', get_next_orientation('R', 'R' ))
# print('get_next_orientation : \t', get_next_orientation('L', 'R' ))
# print('get_next_orientation : \t', get_next_orientation('L', 'L' ))
# print('get_next_orientation : \t', get_next_orientation('D', 'L' ))
# print('get_next_orientation : \t', get_next_orientation('D', 'R' ))
# print('get_next_orientation : \t', get_next_orientation('U', 'L' ))
# print('get_next_orientation : \t', get_next_orientation('U', 'R' ))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n================  My Initial Testing SOLUTION,   ===============\n')
t1  = time.time()


def construct_path(iterations) :
    H = path_sequence_gen(iterations)
    # print('\nthe Generated Sequence : ', len(H) , '\n', H[:1000] ,'\n\n\n')
    # [2, 6, 14, 30, 62, 126, 254, 510, 1022, 2046, 4094]

    orientation = 'U'
    pos = [0, 0]
    cnt = 0
    for s in H :
        if s == 'a' or s=='b' : continue
        if s == 'F' :
            if orientation == 'U' :            pos[1]+=1
            if orientation == 'D' :            pos[1]-=1
            if orientation == 'R' :            pos[0]+=1
            if orientation ==  'L' :            pos[0]-=1
            cnt+=1
            coord = get_point_coord(cnt)
            # if pos[0] != coord[0] or pos[1] != coord[1] :
            # if pos[0] == coord[0] and pos[1] == coord[1] :
            print(str(cnt)+'.    Orientation : ', orientation,'      Correct Position : \t', pos, '   ' ,coord ,' = get_point_coord  ' )
            # if pos == [18,16] :             print(str(cnt)+'.      =====>    Position', pos)

            if cnt == 10000 :
                print(str(cnt)+'.      =====>    Position', pos)
                break

        if s == 'L' or s =='R' :         orientation = get_next_orientation( orientation  , s )


construct_path(10)

# 10**5 = (108, 156)
# 10**6 = (-104, -1008)

print('\n--------------TEST OF FUNCTIONS --------------------\n')

nr_of_steps = 59

N = decompose_in_2_powers(nr_of_steps)
L = log_spiral_pow_of_2(int(math.log2(nr_of_steps)))
print('pow of 2 : \t\t', N , '\ncoord at 2 powers : \t\t', L)

# x , y = L[N[0]][0],  L[N[0]][1]
#
# for i in range(1, len(N) ):
#     print('(x , y) = ', (x, y) )
#     x -= L[N[i]][0]
#     y -= L[N[i]][1]

def dragon_pos(n) :         # Simple Recursive Dragon, with while loops
    length = 1
    pos = [0,1]

    while length < n :          # Main Loop
        pos = [ pos[0]+pos[1]  , -pos[0]+pos[1] ]
        length*=2

    if length == n : return pos

    m = length-n
    pos2 = dragon_pos(m)
    pos2 = [ -pos2[1], pos2[0]  ]

    return [ pos[0]+pos2[0], pos[1]+pos2[1]  ]

dragon_pos(126)

print('\n------------------------------')
#############


# The final steps to complete . Calculations fail for some values. Find why & calibrate :
# @2017-01-25, 11:53   -->  I must calibrate the function
# H = path_sequence_gen(2)		4.      Orientation :  R       Position : 	 [2, 0]
# H = path_sequence_gen(3)		8.      Orientation :  R       Position : 	 [2, -2]
# H = path_sequence_gen(4)		16.      Orientation :  R       Position : 	 [0, -4]
# H = path_sequence_gen(5)		32.      Orientation :  R       Position : 	 [-4, -4]
# H = path_sequence_gen(6)		64.      Orientation :  R       Position : 	 [-8, 0]
# H = path_sequence_gen(7)		128.      Orientation :  R       Position : 	 [-8, 8]
# H = path_sequence_gen(8)		256.      Orientation :  R       Position : 	 [0, 16]
# H = path_sequence_gen(9)		512.      Orientation :  R       Position : 	 [16, 16]
# H = path_sequence_gen(10)		1024.      Orientation :  R       Position : 	 [32, 0]
# H = path_sequence_gen(11)		2048.      Orientation :  R       Position : 	 [32, -32]
# H = path_sequence_gen(12)		4096.      Orientation :  R       Position : 	 [0, -64]
# H = path_sequence_gen(13)		8192.      Orientation :  R       Position : 	 [-64, -64]
# H = path_sequence_gen(14)		16384.      Orientation :  R       Position : 	 [-128, 0]

# @ iter = 549755813888 = 2**39 --> pos = [-524288 , 524288 ]
# need to find the difference : 10**12 - 2**39
# I know how to solve this problem, I work only with differences !!!


print('\n================  My RECURSION SOLUTION,   ===============\n')
t1  = time.time()

D = { 1 : [0,1] }
def dragonM(n) :
    ''':Desciption: Dragon with MEMOIZATION      '''
    global D
    pos = [0,1]
    step = 1
    if n in D :  return D[n]
    if n not in D:
        while step < n :
            step*=2
            pos = [ pos[0] + pos[1], pos[1] - pos[0] ]
            D[step] = pos
            print('step :  ',step,'     position:     ' ,pos)
    if step == n :
        return pos

    diff = step - n
    # Here we make the recursive call which calculates the smaller steps
    d = dragonM(diff)
    print( diff, d )
    # We rotate counterclockwise because we must count for the smaller parts
    # which are rotated clockwise already
    d = [ -d[1], d[0] ]

    final_pos = [ pos[0]+d[0], pos[1]+d[1]   ]
    print(D)
    return final_pos

n = 10**12
print('\nPosition after ',n ,' steps is :   ' ,dragonM(n ) )            #   Answer:     139776,963904

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

######## SOME OTHER GOOD IDEAS #############
# ====Sat, 17 Mar 2012, 07:49, Narasimhan-S., C/C++  , India
#
# This problem is essentially similar to problem 230.
#
# My method to solve this problem is as under:
# (1) Pre-compute the coordinates after 2^n steps for various
#     values of n as follows:
#   (i) x(0) = 0,  y(0) = 1
#   (ii) For n >= 1, coordinates after 2^n steps are:
#        x(n) = x(n-1) + y(n-1)
#        y(n) = y(n-1) - x(n-1)
#
# (2) For computing the coordinates after k steps :
#   (i) Find the value (v) of n for which 2^n just surpasses k:
#       v = ceil(log(k) / log(2))
#       It can be seen that the k-th step will be somewhere near
#       the end of the string Dv.
#   (ii) Find the distance (d) of the required step from the right
#        end of Dv by :
#          d = 2^v - k
#   (iii) From the pre-computed table get the coordinates, x(v) and
#         y(v).
#         Similarly get the coordinates of the turtle for d steps.
#         Let these be x1, y1.
#   (iv) Then the coordinates after k-steps are :
#          x = x(v) - y1
#          y = y(v) + x1
#
# An example will better illustrate the method. Suppose we want to find
# the position after 19 steps.
#
#   19 = 2^5-13 = 2^5 - [2^4-3] = 2^5-[2^4-[2^2-1]].......(1)
#
# Steps   2^5    2^4    2^2    2^0
# ----------------------------------
# x       -4     0      2       0
# ----------------------------------
# y       -4     -4     0       1
# ----------------------------------
# Start from the rightmost end of (1)
#  x(3) = x(4-1) = x(4) - y(1) = 2 - 1 = 1
#  y(3) = y(4) + x(1) = 0 + 0          = 0
#  x(13) = x(16-3) = x(16) - y(3) = 0 - 0 = 0
#  y(13) = y(16) + x(3) = -4 + 1          = -3
#  x(19) = x(32-13) = x(32) - y(13) = -4 -(-3) = -1
#  y(19) = y(32) + x(13) = -4 + 0              = -4
#
# Therefore coordinates after 19 steps = (-1,-4)
#
# It is essentially paper and pencil problem solvable using
# a calculator.
#
# Nevertheless my C code is presented below:


# http://ecademy.agnesscott.edu/~lriddle/ifs/heighway/heighway.htm

print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 0,  ITERATION, SUPER ELEGANT & SIMPLE --------------------------')
t1  = time.time()

# # ====Thu, 11 Dec 2008, 22:27, quilan, USA
# So, I decided to hell with my previous recursive answer, and wrote a really compact & quick iterative algorithm.
# Calculates the answer in log2(n) steps exactly.


def D(n):
    x = y = x2 = y2 = 0;
    s=n;
    if ( n & 1 == 0 ) :
        y2 = -1;
    while ( s>0 ):
        stv = s & 3;
        if (stv == 1) :  x2, y2 = x-y2, x2+y;
        if (stv == 2) : x2, y2 = -y2-1, x2;
        if (stv == 3) : x2, y2 = x2-y-1, y2+x;
        x, y = x+y+1, y-x;
        s >>= 1
    return x2,  y2+1

#================================

from time import time;

start=time();
print ("END: ",list(D(10**12)))
print ("Time taken: ",(1000*(time()-start)) )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 1, RECURSION,  JUST BEAUTIFUL --------------------------')
t1  = time.time()

# ==== Sat, 6 Feb 2016, 00:53, Thierry Machicoane, Switzerland
# Fun! First designed a small automaton computing the travel by walking through the string
# so that to study the arithmetic progression.
# Then found the recursive rule and coded the short program herebelow.

# Result for 10^100: -36933568459161897590895734152376774658622765400064, \
#                    -113193778373761310028664971076732958824136523644928

cache = {}
def Where(n):
    global cache
    if n == 0: return 0,0
    if n == 1: return 0,1
    if n == 2: return 1,1
    if n in cache: return cache[n]

    if n % 2 == 0:
        x,y = Where(n/2)
        cache[n] = x+y,y-x
        return x+y, y-x
    else:
        x,y = Where((n-1)/2)
        X,Y = Where((n+1)/2)
        cache[n] = x+y,Y-X
        return x+y, Y-X

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()


# ====Thu, 14 Jan 2016, 04:51, mattmadi, Australia
# The number of steps can be expressed as the sum of powers of two.
#
# The position after n steps be calculated from the sum of the (possibly negated) positions after 2k steps,
# where k are the powers of two used in the binary expansion of n.
# These 'positions after 2k steps' are calculated easily as follows.
# The position after 2k steps will be (√2)**k from the origin and rotated clockwise by k×(45∘))
#
# In my code I implemented this by generating the coordinates of the position after 2k2k steps:
#  (x,y)=(2**⌊k/2⌋,−(n mod 2)×2**⌊k/2⌋)
#
# The hardest part was figuring out which ones to negate.
# What I eventually realised was that a pair of coordinates had the same sign
# as the next bigger pair of coordinates only if there was no 'gap' between them.
# In other words, consider the number of steps as a binary number and swap signs only if there is a '0' between two '1's.

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3, RECURSION  --------------------------')
t1  = time.time()

# ==== Fri, 20 Jan 2012, 08:06, Turing Machine, USA
# D_n is D_(n-1) doubled with a rotation in the middle.
# This gives you a recurrence for powers of 2. Rather than apply this to the binary representation of 10**12
# I just looked at the positions up to 20 moves and found it generalized to any n.

# (X(n), Y(n)) = ( X(p)+Y(p), Y(q)-X(q) )
#
# p = floor (n/2)
# q = ceiling (n/2)

def pos(n):

	if n in cache:
		return cache[n]

	if n % 2 == 0:
		cache[n] = (sum(pos(n/2)), pos(n/2)[1] - pos(n/2)[0])
	else:
		cache[n] = (sum(pos(n/2)), pos(n/2 + 1)[1] - pos(n/2 + 1)[0])

	return cache[n]

if __name__ == "__main__":
	cache = {0:(0,0), 1:(0,1)}
        print (pos(10**12))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,  ITERATION --------------------------')
t1  = time.time()

# ==== Mon, 3 Jun 2013, 13:24, tom.wheldon, England
# To calculate the position after 2^n moves I used a different recurrence to most:
# using a complex coordinate, zn = -2j*zn-2, with z0 = j and z1 = 1+j.
# I then used the binary expansion of 10^12 to get the result - if a digit is '1' the corresponding value of z_n
# is added or subtracted according to the following rule:
# for the first digit of each block of '1's the sign alternates, starting with positive, the sign
# for the second and subsequent '1's in a block is minus the sign for the first '1'.
# Runs instantly in Python.

N = 10**12

D = {0: complex(0,1), 1: complex(1,1)}
for n in range(2, 41 ):
    D[n] = D[n-2]*complex(0,-2)

bn = format(N, 'b')
size = len(bn)-1
sgn = -1
ones = False
res = 0
for i in range(size+1):
    if bn[i] == '1':
        if not ones:
            sgn = -sgn
            ones = True
            res += sgn*D[size-i]
        else:
            res += -sgn*D[size-i]
    else:
        ones = False

print(res)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 5,   --------------------------')
t1  = time.time()

# ====   Fri, 16 Aug 2013, 12:08, hackleberry, Germany
# If we represent the state of the pointer by a vector of two complex numbers
#
# (z,e**iϕ)
#
# with the position z=x+iy
# and the direction ϕ∈{0,π2,π,3π2}, the basic moves are linear operators
#
# L=[ [1, 0], [ 0, i]] , R=([1,0],[0,−i]), F=([1,0],[1,1])
#
# and can be chained together using straight matrix multiplication.
# python, 2ms


from numpy import array, dot, eye

def LRF_matrices():
    L = array([[1, 0],[0, 1j]])
    R = array([[1, 0],[0,-1j]])
    F = array([[1, 1],[0, 1+0j]])
    return L,R,F

def dot_chain(*matrices):
    ''' given (a1,..,an) return the dot-product a1*...*an. '''
    res=1*matrices[0]
    for a in matrices[1:]:
        res = dot(res,a)
    return res

def apply_a(n, length, x, a, b, L, R, F):
    ''' apply operation a_n, but only up to length steps. '''

    if length==(2**n)-1:
        return dot(a[n], x)
    elif length==0:
        return x
    elif length<=(2**(n-1)-1):
        return apply_a(n-1, length, x, a, b, L, R, F)
    elif length<(2**n)-1:
        x_ = dot_chain(R,a[n-1],x)
        return apply_b(n-1, length-2**(n-1)+1, x_, a, b, L, R, F)

def apply_b(n, length, x, a, b, L, R, F):
    ''' apply operation b_n, but only up to length steps. '''
    if length==(2**n)-1:
        return dot(b[n], x)
    elif length==0:
        return x
    elif length<=(2**(n-1)):
        return apply_a(n-1, length-1, dot_chain(F,L,x), a, b, L, R, F)
    elif length<(2**n)-1:
        x_ = dot_chain(L,a[n-1],F,L,x)
        return apply_b(n-1, length-2**(n-1), x_, a, b, L, R, F)

def solution(pos, n):
    L,R,F = LRF_matrices()

    # write a dictionary containing the matrix-operations
    # for the iterates of a and b
    unit = eye(2, dtype=complex)
    a= {0: unit}
    b= {0: unit}

    n=1
    while 2**n<=pos:
        a[n] = dot_chain(R,F,b[n-1],R,a[n-1])
        b[n] = dot_chain(b[n-1],L,a[n-1],F,L)
        n += 1

    # define the initial state
    x=array([0j,1j])
    # go one step F(orward)
    x1=dot(F,x)
    # compute the final state from that using a
    # with iteration depth n
    X = apply_a(n, pos-1, x1, a, b, L, R, F)
    return (X[0].real, X[0].imag)

print solution(1e12,50)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,   --------------------------')
t1  = time.time()

# ====Thu, 7 Nov 2013, 14:43, inamori, Japan
# Let Sn be the position after n steps.
#
# We can easily find S2m.
#
# S2m=([1,1], [-1, 1])**m*(0, 1)
#
# In general, we can compute Sn recursively. For example, let us find S22.
# We walk 32 ssteps and back up 10 steps. Here, 10 steps is like S10, but the steps turn 90 degrees. Let us be denote it
#
# S22=S32⊖S10S22=S32⊖S10
#
# Similarly, S10=S16⊖S6S10=S16⊖S6, and S6=S8⊖S2S6=S8⊖S2. Then, we can express S22 in S2m.
# 10 **  100 0.001sec
# 10 **  200 0.001sec
# 10 **  500 0.004sec
# 10 ** 1000 0.012sec
# 10 ** 2000 0.034sec
# 10 ** 5000 0.156sec
# 10 ** 6000 <- crash!
#
# I tried to compute S106000 in Python. But Python crashed. Probably, due to recursion, it occurred.
#
#
# Let us have a think about a non-recursive algorithm.
# Expressing 22 in binary, (10110)2. First, we find 1 from right. It is found in 2nd bit. Then, S <- S2.
# Next time, we find 0. It is found in 4th bit. Then, S←S8⊖SS←S8⊖S. The next is 6th bit. S←S32⊖SS←S32⊖S.


from itertools import *
import sys
import time

def step(n):
    def subtract((x0, y0), (x1, y1)):
        return (x0 - y1, y0 + x1)

    def twice((x, y)):
        return (x + y, -x + y)

    Step = (0, 0)
    S = (0, 1)
    first = True
    while n > 0:
        if first:
            if (n & 1) == 1:
                Step = S
                first = False
            S = twice(S)
        else:
            S = twice(S)
            if (n & 1) == 0:
                Step = subtract(S, Step)
        n >>= 1
    return subtract(S, Step)

for E in (100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000):
    N = 10 ** E
    print ( "10 ** %6d" % E)
    print ("%d,%d" % step(N))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




print('\n--------------------------SOLUTION 7,   --------------------------')
t1  = time.time()

# # ====Wed, 14 Jan 2009, 16:27, jorendorff, USA
# My solution builds a tree representation of D50.  The tree has around 3*2^50 nodes, but only 105 distinct nodes!
#
# I like this code because it's such an explicit copy of the problem statement.
# I think the code for building the tree is especially pretty.  :)

def problem220():
    N = 50
    GAS = 10**12

    # a move is a 4-tuple (submoves, totalCost, totalVec, totalTurn)
    def compose(moves):
        p = 0  # position
        h = 1  # heading
        cost = 0
        for (submoves, mcost, mvec, mturn) in moves:
            cost += mcost
            p += h * mvec
            h *= mturn
        return (moves, cost, p, h)

    # a state is a triple (position, heading, gas)
    def walk(state, move):
        p, h, gas = state
        submoves, cost, vec, turn = move
        if cost <= gas:
            return (p + h * vec, h * turn, gas - cost)
        for m in submoves:
            if state[2] == 0:
                break
            state = walk(state, m)
        return state

    F = ([], 1, 1, 1)
    L = ([], 0, 0, 1j)
    R = ([], 0, 0, -1j)
    # here be dragons
    a = ([], 0, 0, 1)
    b = ([], 0, 0, 1)
    for i in range(1, N+1):
        a, b = (compose([a, R, b, F, R]),
                compose([L, F, a, L, b]))
    DN = compose([F, a])  #don't print this :)

    endpos, endh, endgas = walk((0, 1j, GAS), DN)
    assert endgas == 0
    print("%d,%d" % (endpos.real, endpos.imag))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 8,   --------------------------')
t1  = time.time()

# ====Sun, 7 Dec 2008, 00:42, jfrio, Spain
# Trickier than I first thought...
#
# I finally solved it based on the fact that, after 2^n steps, you can get the next 2^n steps by adding
# the same curve rotated 90º around the endpoint.
# So if the desired point is of the form 2^n + a, it reduces to folding it back around 2^n,
# and so calculating 2^n - a, which in turn is of the form 2^m + b... The iterative solution...
#
# ...could be made faster by caching the positions for values of the form 2^n,
# or by working out a closed solution for them, but I'm feeling lazy, and my code runs in 15ms...


def pos2n(n) :
    if n == 0 :
        return [1,0]
    r = pos2n(n-1)
    return [r[0]+r[1],r[1]-r[0]]

def pos(n,verbose=False) :
    t = time()
    fold = int(log(n,2))
    newN = 2**(fold+1) - n
    if newN == n :
        return pos2n(fold)
    r = pos2n(fold)
    a = pos(newN)
    if verbose :
        print ("Calculated",n,"in",time()-t,"sec.")
    return [r[0]+r[1]-a[1],r[1]+a[0]-r[0]]


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')



print('\n--------------------------SOLUTION 9,   --------------------------')
t1  = time.time()

# ====Mon, 8 Dec 2008, 09:59, grep, Ukraine
# The n-th dragon curve is a composition of the n-1-th curve with itself reversed and turned counter-clockwise
#
# Dn = Dn-1((Dn-1)-1)CCW
#
# So, we can easily find the position on the dragon curve after u steps (in complex numbers)
#
# P(0)=0, P(1)=i
#
# P(2**N)=P(2**(N-1)) - i P(2**((N-1)) = i (1-i)**N
#
# If 2**N<u<2**(N+1))
#
# P(u)=P(2**(N+1))+i(P(2**)N+1)-u))


def ilog2(n):
	r=0
	while n>1:
		r=r+1
		n=n//2
	return r

def P(u):
	n=ilog2(u)
	if u==1<<n:
		return 1j*(1-1j)**n
	else:
		return P(1<<(n+1))+1j*P((1<<(n+1))-u)

print P(10**12)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')





