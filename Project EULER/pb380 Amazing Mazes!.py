#  Created by Bogdan Trif on 21-09-2017 , 3:21 PM.
# © o(^_^)o  Solved by Bogdan Trif  @       Completed on Sat, 26 May 2018, 15:34
#The  Euler Project  https://projecteuler.net
'''
        Amazing Mazes!                  -                   Problem 380

An m×n maze is an m×n rectangular grid with walls placed between grid cells such that
there is exactly one path from the top-left square to any other square.
The following are examples of a 9×12 maze and a 15×20 maze:

p380_mazes.gif

Let C(m,n) be the number of distinct m×n mazes.
Mazes which can be formed by rotation and reflection from another maze are considered distinct.

It can be verified that C(1,1) = 1, C(2,2) = 4, C(3,4) = 2415, and C(9,12) = 2.5720e46
(in scientific notation rounded to 5 significant digits).

Find C(100,500) and write your answer in scientific notation rounded to 5 significant digits.

When giving your answer, use a lowercase e to separate mantissa and exponent.

E.g. if the answer is 1234567891011 then the answer format would be 1.2346e12.


'''
import time, zzz
from math import sin, asin, sqrt, pi, log10, modf

# http://mathworld.wolfram.com/SpanningTree.html

# http://oeis.org/A007341     -       	Number of spanning trees in n X n grid. (Formerly M3721)

# https://oeis.org/A116469
# https://oeis.org/A007341/b007341.txt
#
# FORMULA
# T(m,n) = Product_{k=1..n-1} Product_{h=1..m-1} (4*sin(h*Pi/(2*m))^2 + 4*sin(k*Pi/(2*n))^2); [Kreweras] - N. J. A. Sloane, May 27 2012
#
# Equivalently, T(n,m) = resultant( U(n-1,x/2), U(m-1,(4-x)/2 ) = Product_{k = 1..n-1} Product_{h = 1..m-1} (4 - 2*cos(h*Pi/m) - 2*cos(k*Pi/n)),
#     where U(n,x) denotes the Chebyshev polynomial of the second kind.
#
#     The divisibility properties of the array mentioned in the Comments follow from this representation. - Peter Bala, Apr 29 2014
#
# EXAMPLE
# a(2,2) = 4, since we must have exactly 3 of the 4 possible connections: if we have all 4 there are multiple paths between points;
# if we have fewer some points will be isolated from others.
#
# Array begins:
#
# 1,   1,      1,         1,           1,              1, ...
#
# 1,   4,     15,        56,         209,            780, ...
#
# 1,  15,    192,      2415,       30305,         380160, ...
#
# 1,  56,   2415,    100352,     4140081,      170537640, ...
#
# 1, 209,  30305,   4140081,   557568000,    74795194705, ...
#
# 1, 780, 380160, 170537640, 74795194705, 32565539635200, ...
#
# MAPLE
# Digits:=200;
#
# T:=(m, n)->round(Re(evalf(simplify(expand(
# mul(mul( 4*sin(h*Pi/(2*m))^2+4*sin(k*Pi/(2*n))^2, h=1..m-1), k=1..n-1)))))); # crude Maple program from N. J. A. Sloane, May 27 2012
#
# MATHEMATICA
# T[m_, n_] := Product[4 Sin[h Pi/(2 m)]^2 + 4 Sin[k Pi/(2 n)]^2, {h, m - 1}, {k, n - 1}];
# Flatten[Table[FullSimplify[T[k, r - k]], {r, 2, 10}, {k, 1, r - 1}]] (* Ben Branman, Mar 10 2013 *)

#
# SOLUTIONS :
#  - I found Kirchhof's theorem.
# - Rather than Gaussian elimination, I computed the Cholesky decomposition of the matrix: G = LDLT,
# - Matrix Tree Theorem, which didn't solve the problem completely.
#         The challenge was to calculate the determinant of a 50K x 50K matrix.
#
# -  It's a count of spanning trees of a m*n grid graph.
#       I found a formula for a square grid at http://mathworld.wolfram.com/SpanningTree.html
#             and took a guess at how to change it for rectangular.
#
# -  Found "Spanning Tree" article on wiki, then Matrix Tree Theorem....
# Gaussian elimination to get the determinant of 50k x 50k sparse matrix

# - First this problem reminded me of Problem 289, which could also be transformed into enumarting the forest of trees.
# However, soon it was obvious that this problem is too large for a dynamic programming approach.
# So I noticed that here, it seems to be better to look at a tree connecting the maze cells instead of looking at the walls.
# Every valid maze is a spanning tree. So I learned how to count spanning trees on a square lattice.
# I ended up with Kirchhoff's theorem, where we need to calculate the determinant of the Laplacian matrix.
# Since the matrix is symmetric and has a nice banded form,
# I used Cholesky decomposition to calculate the determinant.

# -  Created my own banded sparse matrix and just did Gaussian Elimination to compute the determinant
#
# - Here's a link to a paper with the formula for number of spanning trees of a rectangular grid.  ' \
#       'I used Sage rather than Python to handle the large numbers properly.
# http://arxiv.org/pdf/cond-mat/0001408.pdf

'''
Beautiful problem.
It took me a while to figure out how to solve it until some googling led me to Kirchhoff's theorem. 
Next step: how do I compute the determinant of this huge sparse Laplacian matrix where one row/column has been omitted? 
Or the product of nonzero eigenvalues?

Right before going to bed I realized that I had seen this before: We are dealing with a discrete Laplacian (as in finite differences), 
and its eigenvectors are sine/cosine curves, which can be treated independently for the two axes! 
What about the boundary? I was thinking of cosines evaluated at i+½ for integer i, so cos(a*(-½)) = cos(a*½) 
would properly account for the vertex at the low border, and cos(a*(n-½)) = cos(a*(n+½)) at the high border.
(Basically, a boundary vertex is missing a neighbor, so the corresponding entry on the diagonal of the matrix is decreased by 1, 
and a "-1" is missing in the corresponding row/column. 
These equalities make sure that the corresponding terms of the finite differences would cancel out, 
so I can ignore the fact that they're not there.)

With a little experimenting I ended up with coefficients a=π*k/n, k=0..n-1, 
with corresponding eigenvalues 2*(1-cos(a)) (easily derived from the angle sum identities of the cosine).

In two dimensions, any eigenvalue of the discrete Laplacian is an eigenvalue in the x-axis plus an eigenvalue in the y-axis. 
The least one is zero. Multiply all others, divide by nx*ny, and you have the result.

In the end the solution is the same as usrbin's and others, the thought process was just a little longer. 
This is the first time I have a pretty compact solution for a problem with a high ID. :)

Language is R.
'''
# - Source: http://www.combinatorics.org/Volume_7/PDF/v7i1r25.pdf
#
# - http://www.iwriteiam.nl/Cst.html      - Facts about spanning trees

'''
It didn't take me long to find out about spanning trees and that the
result is the determinant of a 50,000 square matrix.
I used a Gauss elimination in Python for a sparse matrix and it
started trashing. Then I programmed it myself  straightforwardly using
lists. This promises to take 50 hours (It is still running).
Using dicts in Python was no improvement, it would take about
ten times as long. Trying to use one of the sparse libraries available in
whatever language failed me. It took too long to select one and then
it seemed that the matrix can only be filled in from a disk file in the Boeing format.

Using good old C was the solution. It takes about one second.
I make use of the fact that non-zero elements are in a band with
size 100.

I visited the spanningtree page at Wolfram, and overlooked the explicit
formula. That would have felt like cheating. At least I learned more now.

- Kirchhoff's Matrix Tree Theorem, like many other of you. I used matlab_bgl to generate the adjacency matrix 
and a logarithm-determinant from Matlab central.
 I am pretty much an opportunist, using Python for integers, Matlab for matrices and 
 Mathematica for high-precision numbers. I should learn to get by with only one tool. :)
 
 
 -
 Used matrix tree theorem. Then gaussian elimination. Instead of calculating log,just devided the result by 1e100 at each row, and counted it. :-) 

'''



print('\n--------------------------TESTS------------------------------')
t1  = time.time()



t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()



def _sigma(k, n) :
    x = 4* (sin( ((k* pi) / (2*n)) ))**2
    return x

def mazes(m, n) :

    P = 0
    for k in range(1, n ) :
        M = _sigma(k, n)
        for h in range(1, m) :
            N = _sigma(h, m)
            P += log10(N+M)
            # print(P,'       N=', N, '      M=', M)

    print('\n log = ', P )
    d, f = modf(P)
    print('\n decimals  : ',  d, f,'     ' , 10**(d )   )
    print('\n RES  = ', "{0:.5g}".format(10**(d) )+'e'+str( int( f) )  )

    return P

mazes( 100, 500 )           #       Answer :  6.3202e25093


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')            # Completed in : 147.01 ms


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ==== Sun, 15 Apr 2012, 00:15, st1974, Python  , Germany
# First this problem reminded me of Problem 289, which could also be transformed into enumarting the forest of trees.
# However, soon it was obvious that this problem is too large for a dynamic programming approach.
# So I noticed that here, it seems to be better to look at a tree connecting the maze cells instead of looking at the walls.
# Every valid maze is a spanning tree. So I learned how to count spanning trees on a square lattice.
# I ended up with Kirchhoff's theorem, where we need to calculate the determinant of the Laplacian matrix.
# Since the matrix is symmetric and has a nice banded form,
# I used Cholesky decomposition to calculate the determinant.
#
# Not very efficient Python code, but it gives the correct result after about 5 min:


import math

class marray(object):
    def __init__(self,mod):
        self.mod=mod
        self.A=[[0.]*mod for i in range(mod)]
    def vset(self,i,j,value):
        self.A[i%self.mod][j%self.mod]=value
    def __call__(self,i,j):
        return self.A[i%self.mod][j%self.mod]

class KirchhoffMatrix(object):
    def __init__(self,m,n):
        self.m=m
        self.n=n
        self.diag=[4.]*(n*m-1)
        self.u1=[-1.]*(n*m-2)

        self.diag[0]=2.
        for j in range(1,m-1):
            self.diag[j]=3.
        self.diag[m-1]=2.
        self.u1[m-1]=0.
        for i in range(1,n-1):
            self.diag[i*m]=3.
            self.diag[i*m+m-1]=3.
            self.u1[i*m+m-1]=0.
        self.diag[(n-1)*m]=2.
        for j in range(1,m-1):
            self.diag[(n-1)*m+j]=3.
    def __call__(self,i,j):
        if i==j :
            return self.diag[i]
        elif j==i+1 :
            return self.u1[i]
        elif i==j+1 :
            return self.u1[j]
        elif i==j+self.m or j==i+self.m :
            return -1.
        else:
            return 0.
    def det(self):
        """calculate determinat using Cholesky decomposition"""
        d,e=1.,0
        G=marray(self.m+2)
        for i in range(self.n*self.m-1):
            gii=float(self(i,i))
            for j in range(max((0,i-self.m-1)),i):
                gij=float(self(i,j))
                for k in range(max((0,i-self.m-1)),j):
                    gij-=G(i,k)*G(j,k)
                gij/=G(j,j)
                gii-=gij*gij
                G.vset(i,j,gij)
            d*=gii
            while d>10.:
                d/=10.
                e+=1
            G.vset(i,i,math.sqrt(gii))
        return d,e

def C(m,n):
    return "%.4fe%i" % KirchhoffMatrix(m,n).det()

print( C(2,2))
print( C(3,4) )
print( C(9,12) )
# print( C(100,500))

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()


# === Thu, 19 Apr 2012, 01:24, Obergscheidle, Luxembourg
# While contemplating how to compute the determinant of the Laplacian I found the same page as umu, which made it very easy.
# Still wondering why this formula works. Has anyone seen a proof?

from math import pi,sin,log,exp

def nst(n,m):
    logs = 0
    sq1 = [sin(i*pi/(2*n))**2 for i in range(n)]
    sq2 = [sin(i*pi/(2*m))**2 for i in range(m)]
    for s1 in sq1:
        for s2 in sq2:
            if s1+s2>0:
                logs += log(4*(s1+s2))
    log10 = (logs-log(n*m))/log(10)
    e = int(log10)
    m = 10**(log10-e)
    return "%.4fe%s"%(m,e)

print( nst(100,500) )

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


print('\n--------------------------SOLUTION 3,   --------------------------')
t1  = time.time()

# ===Sun, 15 Apr 2012, 01:46, brg, Python, England
# I found the formula for the number of spanning trees for a rectangular grid as others have done
# after which it was fairly easy to compute the result in Python
# count of the number of spanning trees in an m by n grid:
#
#   product{a = 0 .. m - 1, b =  0 .. n - 1, (a * b > 0):
#   2 * (2 - cos(a * pi / m) - cos(b * pi / n))} / (m * n)
#
# keep track of powers of 2 in its calculation and return
# (m, e) where the count value is m * 2 ** e.

from math import pi, cos, log10, frexp, fmod

def maze_count(m, n):
  cm, cn = pi / m, pi / n
  p = 1.0
  p2 = 0
  for a in range(m):
    for b in range(n):
      if a or b:
        p *= 2.0 * (2.0 - cos(a * cm) - cos(b * cn))
        while p < 0.5:
          p *= 2.0
          p2 -= 1
        while p >= 2.0:
          p /= 2.0
          p2 += 1
  return p / (m * n), p2

m, e = maze_count(100, 500)
# now convert from powers of 2 to powers of 10
man, exp = frexp(m)
man, exp = 2 * man, (exp + e - 1) * log10(2)
man *= 10 ** fmod(exp, 1)
print(str(round(man, 4)) + 'e' + str(int(exp)))


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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







