#!/usr/bin/python                   o(^_^)o         ( ͡° ͜ʖ ͡°)
# © Solved by Bogdan Trif @
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

weighted_product( 15 )

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
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
