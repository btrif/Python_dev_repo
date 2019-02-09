#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @     Completed on Sat, 4 Nov 2017, 16:17
#The  Euler Project  https://projecteuler.net
'''
        Maximising a weighted product       -       Problem 190

Let S_m = (x_1, x_2, ... , x_m) be the m-tuple of positive real numbers with : x_1 + x_2 + ... + x_m = m

for which P_m = x_1 * x_2**2 * ... * x_m**m      is maximised.

For example, it can be verified that [P10] = 4112 ([ ] is the integer part function).

Find Σ[P_m] for 2 ≤ m ≤ 15.


'''
import time

import functools, operator
import numpy as np
# from scipy.optimize import minimize
import scipy.optimize

def objective3(X, sign=1.0) :   # X will be a vector with 3 elements
    """ Objective function """
    x1, x2, x3 = X

    return sign *( x1 * x2**2 * x3**3 )


def func_deriv3(X, sign=1.0):
    """ Derivative of objective function """
    dfdx1 = sign *( X[1]**2 * X[2]**3 )
    dfdx2 = sign *( 2 * X[0] * X[1] * X[2]**3 )
    dfdx3 = sign *( 3 * X[0] * X[1]**2 * X[2]**2 )

    return np.array([ dfdx1, dfdx2, dfdx3 ])

def constraint3(X):
    return X[0] + X[1] + X[2] - 3.0

def jacobian3(X) :
    return np.array([  X[0], X[1], X[2] ])

# Bounds
b = (0.1, 3)
bnds3 = (b , b , b)

# Constraints definition

con3 = {'type' : 'eq', 'fun' : constraint3 , 'jac' : jacobian3 }
cons3 = [ con3 ]

X3 = np.array([ 0.5, 1, 1.5 ])

sol3 = scipy.optimize.minimize(objective3, X3, args=(-1.0,) , jac=func_deriv3 ,method='SLSQP' ,
                               bounds=bnds3, constraints=cons3 , options= { 'maxiter':100} )
print(sol3)

Y = sol3.x
print('sum = ', sum(Y) , '     wheighted prod = ',Y[0] * Y[1]**2 * Y[2]**3)

print('\n---------------------------------')




# VERIFICATION, CHECK
print('------------- SOLUTION ---------------')

# P = 0
# for i in range(1, 11):
#     P += i ** i
#     print(str(i), '         ', P)







print('\n--------------------------TESTS------------------------------')
t1  = time.time()



def brute_force_2():
    step = 0.01
    max = 0
    ratio = 1/step
    m = 2
    for x1 in range(int(0*ratio) , int(1*ratio)+1 , 1 ) :
        x1 = x1 * step
        x2 = m - x1
        P_m = x1*x2*x2
        if P_m > max :
            max = P_m
            print(' x1, x2 = ' , x1 , x2,'          P_m = ', P_m  )

# brute_force_2()         #       x1, x2 =  0.67 1.33           P_m =  1.1851630000000002

def brute_force_3():
    step = 0.1
    max = 0
    ratio = 1/step
    m = 3
    for x1 in range(int(0*ratio)+1  , int(1*ratio)+1 , 1 ) :
        # print(x1*step, x1*ratio)
        x1 = x1 * step
        for x2 in range(int(x1) , int((m-x1)*ratio) , 1 ) :
            x2 = x2 * step
            x3 = m - ( x1 + x2 )

            P_m = x1 * x2**2 * x3**3
            if P_m > max :
                max = P_m
                print(' x1, x2, x3 = ' , x1 , x2, x3  ,'          P_m = ', P_m  )

# brute_force_3()


def brute_force_4():
    step = 0.1
    max = 0
    ratio = 1/step
    m = 4
    for x1 in range(int(0*ratio)+1  , int(1*ratio)+1 , 1 ) :
        # print(x1*step, x1*ratio)
        x1 = x1 * step
        for x2 in range(int(x1) , int((m-x1)*ratio) , 1 ) :
            x2 = x2 * step

            for x3 in range(int(x1) , int((m-x1-x2)*ratio) , 1 ) :
                x3 = x3 * step
                x4 = m - ( x1 + x2 + x3 )

                P_m = x1 * x2**2 * x3**3 * x4**4
                if P_m > max :
                    max = P_m
                    print(' x1, x2, x3, x4  = ' , x1 , x2, x3, x4  ,'          P_m = ', P_m  )

brute_force_4()




t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# ============ SOME IDEAS ==========
# ===== Sat, 19 Apr 2008, 00:42, Stijn Duijzer, Netherlands
# https://en.wikipedia.org/wiki/Lagrange_multiplier
# Solved it using Lagrange-Multipliers. The problem can be stated as follows:
# Maximize:
#    f(x1,x2,...,xm) = x11 * x22 * ... * xmm
#
# With constraint:
#    g(x1,x2,...,xm) = x1 + x1 + ... + xm - m = 0
#
# If maximal then the following must hold for i=1..m:
#    df/dxi = L * dg/dxi
#
# Thus:
#    f * i/xi = L
#    xi = i * f/L
#
# Combining this with g = 0 and ∑i = (m+1)*m/2 gives:
#    xi = 2*i/(m+1)


print('\n=============  My FIRST SOLUTION,  1 ms  ===============\n')
t1  = time.time()

def weighted_product(up) :
    S = 0
    for m in range(2, up+1):
        N = [ i*2/(m+1)  for i in range(1, m+1)  ]
        P_m = functools.reduce(operator.mul, [N[j - 1] ** j for j in range(1, len(N) + 1)])
        print('m = ', m,'           P_m = ', P_m  , '          x_1, x_2,..., x_m  =   '  ,N )
        S += int(P_m)

    return print('\nΣ[Pm]  =  ' , S )

weighted_product( 15 )              #   Answer : Σ[Pm]  =   371048281

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1,   --------------------------')
t1  = time.time()

# ====Sat, 24 Dec 2016, 02:41, squidaction, USA
# Want to maximize log(x1)+2*log(x2)+...m*log(xm).
# The derivative wrt x1 = 1/x1 - 2/(m-xr-x1)  (where xr is the sum of the remaining x's)
# m-xr-x1 = x2, so if 1/x1 - 2/x2 = 0, then x2 = 2*x1, and so forth.
#
# Code is basically the same as everyone else's:

from math import floor
def P(m):
    x1, p = 2/(1+m), 1
    for e in range(1,m+1):
        p *= pow(e*x1,e)
    return floor(p)

print (sum(P(m) for m in range(2,16)))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,   --------------------------')
t1  = time.time()

# ==== Mon, 6 Mar 2017, 21:17, Khalid, Saudi Arabia
# I wrote test code for small values until I saw the pattern.

def max_weighted_product(n):
    p = 1
    for i in range(n):
        p *= (float(2 * (i + 1))/(n+1))**(i + 1)
    return int(p)

result = 0

for n in range(2, 16):
    result += max_weighted_product(n)

print (result)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n----------------------SOLUTION 3,  weighted Arithmetic Mean - Geometric Mean --------------------------')
t1  = time.time()

# ==== Sun, 10 May 2015, 15:45, Haroun, Algeria
# Simple weighted Am-Gm, this python code gives the answer in about 0.1 ms

def f(m):
    r=(m*(m+1))/2.;
    p=1.
    for i in range(1,m+1):
        p*=i**i;
    return int((m/(r))**r*p);

sol=sum([ f(i) for i in range(2,16)] )

print( "the answer is " , sol )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 4,   --------------------------')
t1  = time.time()

# === Fri, 12 Jun 2015, 12:49, mmaximus, Portugal
# I played around with numerical optimisation (which exploded around n=12),
# but I gathered enough data to spot the pattern: if X_n is the solution vector for n, then X_n[i] = 2i/(n+1).
#
# Once you spot this the solution can be obtained immediately.

from fractions import Fraction

def sol(n):
    t = Fraction(1,1)
    for i in range(1, n+1):
        t *= Fraction((2*i)**i, (n+1)**i)
    return int(t)

T = 0
for i in range(2,16):
	T += sol(i)

print (T)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------SOLUTION 5, Gradient Ascent, BEAUTIFUL   --------------------------')
t1  = time.time()

# ==== Fri, 21 Aug 2015, 13:18, grauerwolf, Germany
# When I saw that one of the x'es is not a free parameter, so the case m=3 hab to be expressed
# as P3 = (3-x2-x3)1*x22*x33, I made a spreadsheet for m=2 and m=3 and found the maxima to be
# at x1=2/3,x2=4/3 and x1=1/2,x2=2/2,x3=3/2, respectively.
# From there, I tried to continue this sequence of even distribution using this:
# #!/usr/bin/env python3
# if __name__ == '__main__':
#     final_result = 0
#     for m in range(2,16):
#         product = 1
#         for i in range (1,m+1):
#             product *= ((2/(m+1))*i)**i #m/(m*(m+1)/2)==2/(m+1)
#         final_result += int(product)
#     print(final_result)
#
# This worked. But what's wrong with practicing some optimization?
# I used a gradient ascent scheme with step size adjustment.
# The step size adjustment also prevents it from stepping over a restriction, like xi>0. There you go:



def f(x):
    #x1 is a depentent variable, x1 = n-(sum(x2..xn))
    #so the function to optimize is
    #f(x2..xn) = (n-sum(x2..xn)) * x2**2 * x3**3 * ... xn**n
    #since x1 does not appear in the list and list stars at 0, x2 is x[0], x3 is x[1], xi = x[i-2] and so on
    result = len(x)+1-sum(x)
    for i in range(len(x)):
        result *= x[i]**(i+2)
    return result

def f_strich(x,i):
    #partiel derivative with respect to x[i]
    #df/dxi = -1 * x2**2 * x3**3 * ... xn**n + i*(n-sum(x2..xn)) * x2**2 * x3**3 * ... xn**n / xi
    #since x1 does not appear in the list and list stars at 0, x2 is x[0], x3 is x[1], xi = x[i-2] and so on
    result = len(x) + 1 - sum(x)
    result *= (i+2)
    product = 1
    for j in range(len(x)):
        product *= x[j]**(j+2)
    result *= product/x[i]
    result -= product
    return result

def nabla(x):
    #gradient
    return list(f_strich(x,i) for i in range(len(x)))


def main5():
    final_result = 0
    for m in range(1,15):
        alpha = 1e-5 #intial value for step size
        x = [1] * m #initial value, f(x) = 1
        for i in range(10**6): #10 to the sixth will never be reached, but to prevent infinite loop, its always good to have this
            n = nabla(x)
            #determine step size
            #reduce alpha to prevent divergence
            x_try = [x[k]+alpha*n[k] for k in range(len(x))]
            shortened = False
            while (f(x_try)<f(x)):
                shortened = True
                alpha/=2
                x_try = [x[k]+alpha*n[k] for k in range(len(x))]
            # reduce alpha if lower alpha gives higher f(x)
            if not shortened:
                x_try = [x[k]+alpha*n[k] for k in range(len(x))]
                x_s = [x[k]+alpha/2*n[k] for k in range(len(x))]
                while (f(x_try)<f(x_s)):
                    shortened = True
                    alpha/=2
                    x_try = [x[k]+alpha*n[k] for k in range(len(x))]
                    x_s = [x[k]+alpha/2*n[k] for k in range(len(x))]
            #extend if possible
            if not shortened:
                try:
                    x_ext = [x[k]+10*alpha*n[k] for k in range(len(x))]
                    if (f(x_ext)>f(x_try) and (f(x_ext) < 2*f(x_try)) and alpha < 1e-3): #f(x_ext) can diverge seriously, causing a floating point error, better stay inside the try-block
                        alpha*=10
                except:
                    pass #if f(x_ext) did diverge seriously, there is no need to do anything else than carry on
            #eventually, after determining the step size for more than half of the code, do the step
            x = [x[k]+alpha*n[k] for k in range(len(x))]
            if alpha < 10**(min(-7,-m-4)):
                break
        final_result += int(f(x))
    print(final_result)

# main5()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 6,  Newton  root-finding method in n dimensions  --------------------------')
t1  = time.time()

# ==== Fri, 10 Jun 2016, 07:09, sO3SrLCr4Rqb00Zr.., Japan
# Being an engineer and not a mathematician, I suppose I am the only person who actually did
# this by using Newton's root-finding method in n dimensions.  ' \
#     (Doing it in 1-dimension at a time, iterating over each dimension.)
#
# Although, I realized at first glance that the answer would be when dP/dx_n = 0 for all n,
#     I thought it would be easier to solve numerically than it would to actually go about writing a function
#     for analytically solving dP/dx_n for all n.  (More about programming time than mathematical difficulty.
#     Again, being an engineer, I do more numerical than analytical solutions.)
#
# Of course, the first few versions of the program bugged out because I forgot that you might
# e.g. have a positive dy/dx and a d2y/dx2 yielding to no clearly visible maximum,
# and in those cases it would attempt to find the minimum. (!!!)
#
# Runs in 10.75s, but that's only because I have no clearly defined termination for accuracy.
# But it does have the saving grace that this approach would work for
# any arbitrary function P(X), not just the given one.


def P(xs):
    prod = 1.0
    for power, x_m in enumerate(xs, start=1):
        prod *= x_m**power
    return prod


def add_value(old_xs, n, to_add):
    to_sub = to_add / (len(old_xs) - 1)
    new_xs = []
    for index, x in enumerate(old_xs):
        if index != n:
            new_xs.append(x - to_sub)
        else:
            new_xs.append(x + to_add)
    return tuple(x * len(new_xs) / sum(new_xs) for x in new_xs)


def dPdX(xs0, n, delta=0.0000001):
    xs1 = add_value(xs0, n, delta)
    return (P(xs1) - P(xs0)) / delta


def d2PdX2(xs1, n, delta=0.0000001):
    xs0 = add_value(xs1, n, -1 * delta)
    xs2 = add_value(xs1, n, delta)
    return (P(xs2) + P(xs0) - 2*P(xs1)) / (delta**2)


def get_max_S(m):
    xs = (1.0) * m
    return sum(xs)


def main6():
    m = 10
    # print(P(xs))
    # print(dPdX(xs, 0))
    # print(dPdX(xs, 1))
    # print(dPdX(xs, 2))
    # print(dPdX(xs, 3))

    # print(d2PdX2(xs, 0))
    # print(d2PdX2(xs, 1))
    # print(d2PdX2(xs, 2))
    # print(d2PdX2(xs, 3))

    sums = 0
    for m in range(2, 15+1):
        xs = (1.0, ) * m
        print(xs, P(xs))
        while True:
            changes = 0
            for n in range(m):
                dydx2 = d2PdX2(xs, n)
                dydx  = dPdX(xs, n)
                print(dydx, dydx2)
                if dydx > 0 and dydx2 > 0:
                    approx_to_max = 1
                elif dydx < 0 and dydx2 <0 :
                    approx_to_max = -1
                else:
                    try:
                        approx_to_max = -dydx/dydx2
                    except ZeroDivisionError:
                        approx_to_max = 0.0
                if approx_to_max > 0:
                    approx_to_max = min(min(xs)/2, approx_to_max)
                else:
                    approx_to_max = max(-min(xs)/2, approx_to_max)
                print("adding", approx_to_max, "to", n)
                new_xs = add_value(xs, n, approx_to_max)
                if P(new_xs) > P(xs):
                    xs = new_xs
                    print(xs, P(new_xs))
                    changes += 1
            if changes == 0:
                sums += int(P(xs))
                break
    print(sums)

# main6()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 7, inequality of arithmetic and geometric mean  --------------------------')
t1  = time.time()

# === Wed, 13 Jul 2016, 08:05, Moai, South Korea
#
# To get SmSm, used the inequality of arithmetic and geometric mean.
#
# x1/1 ×(x2/2×x2/2) ×... ×(xm/m×xm/m×...×xm/m)  ≤(∑xk/n)^n = (m/n)^n  ,      where n=m(m+1)/2
#
# with equality if and only if x1/1=x2/2=...=xm/m = m/(m(m+1)/2)

from functools import reduce

def prod(iterable):
    return reduce(lambda x, y: x*y, iterable)

def s(m):
    n = m*(m+1)//2
    return [k * m/n for k in range(1, m+1)]

def p(m):
    return prod(x**k for x, k in zip(s(m), range(1, m+1)))

assert int(p(10)) == 4112
print(sum(int(p(m)) for m in range(2, 16)))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 8, Mathematica Multivariable Calculus , Lagrange Multiplier --------------------------')
t1  = time.time()

# ==== Tue, 19 Nov 2013, 19:03, dcterr, Mathematica , USA

# This is a nice exercise in multivariable calculus which can be rather easily solved using a Lagrange multiplier.
#
# For a fixed positive integer m, we define the function pm(x1, x2,⋯,xm) as follows:
# pm(x1,x2,⋯,xm)=∏{k=1, m }xk^k.
#
#
# Now we wish to compute the maximum Pm of pm(x1,x2,⋯,xm) subject to the constraint
# x1+x2+⋯xm=mx1+x2+⋯xm=m. This is most easily done if we let :
#
# f(x1,x2,⋯,xm) = log [ pm(x1,x2,⋯,xm) ] = ∑{k=1, m} k* log (xk)
#
# Then we wish to maximize ff subject to the constraint
#
# g(x1,x2,⋯,xm )= ∑{k=1, m} xk = m.
#
# This is equivalent to maximizing the function
# F(x1,x2,⋯,xm,λ) == f (x1,x2,⋯,xm) + λ * g(x1,x2,⋯,xm)  = ∑{k=1, m} ( k* log (xk) + λ * xk ).
#
#
# Taking the partial derivative of both sides of the above equation with respect to xk
# and setting the result equal to zero, we obtain
#
# ∂F/ ∂xk  = k/ xk + λ = 0 ,
#
# whence xk=−k/λ . Thus we have :
#
# m = ∑{k=1,m} xk = −1/λ * ∑{k=1, m} k = −m(m+1)/ (2λ)
#
#
# whence λ=−(m+1)/2  and hence
# xk=−k/ λ = 2k / (m+1)
#
#
# Thus we have the solution
# Pm = ∏{k=1,m} (2k / (m+1))^k= (2/(m+1)) ^(m(m+1)/2) * ∏{k=1,m} k^k
#
#
# I finally used Mathematica to compute [Pm][Pm] for 2≤m≤15 and computed their sum. The code is given below:
#
# In[21]:= P = Table[Floor[(2/(m + 1))^((m (m + 1))/2) \!\*UnderoverscriptBox[\(\[Product]\*UnderoverscriptBox[\(\[Product], k=1k=1, mm]
# \*SuperscriptBox[kk, kk]\)], {m, 2, 15}]

# Out[21]= {1, 1, 2, 6, 15, 46, 169, 759, 4112, 26998, 214912, 2074179, 24273249, 344453832}
# In[22]:= Plus @@ P
# Out[22]= 371048281

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 9,  Lagrange multipliers --------------------------')
t1  = time.time()

# ===Sat, 8 Sep 2012, 03:56, ephemeral, USA
# Easy with Lagrange multipliers.
# One liner in Python

from operator import mul
from functools import reduce

def euler_190():
    return sum([int(reduce(mul, [pow((2 * i) / (m + 1), i) for i in range(1, m + 1)])) for m in range(2, 16)])

print( euler_190() )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 10,  annealing --------------------------')
t1  = time.time()

# === Mon, 24 Sep 2012, 22:41, guyru, Israel
# Simply used annealing, works pretty fast:

import random
from itertools import count

def annealing(m):
    THRES = 0.000001
    step = 0.5
    max_tuple = [1]*m
    cur_tuple = [1]*m
    max_p = 1
    for j in count():
        if  (j % 100*m) == 0:
            step /= 2
        cur_tuple = max_tuple[:]
        cur_p = 1
        x,y = random.sample(range(m), 2)
        if cur_tuple[x] < step:
            continue
        cur_tuple[x] = max_tuple[x] - step
        cur_tuple[y] = max_tuple[y] + step
        for i,x in enumerate(cur_tuple):
            cur_p *= x**(i+1)
        if cur_p > max_p:
            max_tuple = cur_tuple[:]
            if cur_p - max_p < THRES:
                return cur_p
            max_p = cur_p

print (sum([int(annealing(i)) for i in range(2,16)]))


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 11, subgradient projection method, Beautiful  --------------------------')
t1  = time.time()

# ==== Sat, 6 Apr 2013, 03:35, OldCigarette, USA
# Pretty cool. I didn't know a lot about optimization problems but implemented the subgradient projection method.
# It converges to the solutions very quickly

import math
import numpy

def main11():
    L = 15
    sum = 0
    for m in range(2, L+1):
        hplane_normal = numpy.array([1]*m)
        hplane_normal = hplane_normal / numpy.linalg.norm(hplane_normal)
        hplane_d = -m / math.sqrt(m)

        def project(z):
            dfp = numpy.inner(z, hplane_normal)+hplane_d
            pv = dfp*hplane_normal
            z = z - pv
            return z

        def f(x):
            product = 1
            for j in range(1, m+1):
                product *= x[j-1]**-j
            return product

        def gradient(x):
            eps = 1e-3
            for j in range(1, m+1):
                if x[j-1] <= eps:
                    g = numpy.array([0]*m)
                    g[j-1] = -1
                    return g

            def partial_derivative(x, i):
                product = 1
                for j in range(1, m+1):
                    if j == i:
                        product *= -j*x[j-1]**(-j-1)
                    else:
                        product *= x[j-1]**-j
                return product
            return numpy.array([partial_derivative(x, i) for i in range(1, m+1)])
        x = numpy.array([1]*m)
        for i in range(0, m//2):
            x[i] = 0.5
            x[m-i-1] = 1.5
        step_size = 0.25
        best = 1.0
        best_x = x
        for step in range(1, 500):
            g = gradient(x)
            g = g/numpy.linalg.norm(g)
            x = project(x - step_size*g)
            if f(x) < best:
                best = f(x)
                best_x = x
        print(m, 1/best, best_x)
        sum += int(1/best)
    print(sum)
main11()


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


print('\n--------------------------SOLUTION 12, Brute Force - BINARY SEARCH  --------------------------')
t1  = time.time()

# ====Fri, 31 Oct 2008, 16:13, Axel Brzostowski, Argentina
# I brute-forced it, but using a binary movement.


def Pm(x):
    p = 1
    for i in range(len(x)):
        p *= x[i]**(i+1)
    return p

ss = 0
for nn in range(2, 16):
    x = [1.0] * nn
    chg = 0.5
    for k in range(100):
        for i in range(len(x)):
            for j in range(len(x)):
                x2 = x[:]
                x2[i] -= chg
                x2[j] += chg
                if Pm(x2) > Pm(x):
                    x = x2
        chg /= 2.0
    ss += int(Pm(x))

print (ss)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

