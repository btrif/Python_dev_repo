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
bnds3 = (b,b,b)

# Constraints definition

con3 = {'type' : 'eq', 'fun' : constraint3 , 'jac' : jacobian3 }
cons3 = [ con3 ]

X3 = np.array([ 0.5, 1, 1.5 ])

sol3 = scipy.optimize.minimize(objective3, X3, args=(-1.0,) , jac=func_deriv3 ,method='SLSQP' ,
                               bounds=bnds3, constraints=cons3 , options= { 'maxiter':100} )
print(sol3)

# VERIFICATION, CHECK
print('------------- SOLUTION ---------------')
Y = sol3.x
print('sum = ', sum(Y) , '     wheighted prod = ',Y[0] * Y[1]**2 * Y[2]**3)








print('\n--------------------------TESTS------------------------------')
t1  = time.time()






t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()







# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')


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
