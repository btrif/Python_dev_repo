import numpy as np
np.set_printoptions(precision=16)       # Set precision, how many digits of numpy

print('\n------------ roots - Find the Roots of a polynomial --------------')
# Here the bellow are the coefficients of the polynomial : x**3 - 3 x**2 + 3 x**2 - 1
print('Roots  : ' ,np.roots( ( 1., -3.,  3. ,-1. ) ) )

# Here the bellow are the coefficients of the polynomial : x**3 - 4 x**2 + 2
print('\nRoots  : ' ,np.roots((1., -4., 0 , 2. )) )
# Here the bellow are the coefficients of the polynomial : x**3 - 8 x**2 + 3
print('\nRoots  : ' ,np.roots((1., -8., 0 , 3. )) )


print('\n----- poly - Find the coefficients of a polynomial with the given sequence of roots. ---------')
# Returns the coefficients of the polynomial whose leading coefficient
# is one for the given sequence of zeros (multiple roots must be included in the sequence
# as many times as their multiplicity; see Examples).
# A square matrix (or array, which will be treated as a matrix) can also be given,
# in which case the coefficients of the characteristic polynomial of the matrix are returned.

# The line above represents z**3 + 0*z**2 + 0*z + 0
print(' Polynomial with the roots : \t' ,np.poly((-1./2, 0, 1./2))  )

# The line above represents z**3 - 6*z**2 + 11*z - 6
print('\nPolynomial with the roots : \t' ,np.poly((1, 2, 3))  )

# The line above represents z**3 - 8*z**2 - 1*z + 8
print('\nPolynomial with the roots : \t' ,np.poly((1., -1., 8.  ))  )

print('\n----- polyal - Evaluate a polynomial at specific values. ---------')
# Evaluate a polynomial at specific values.
# Horner’s scheme [R65] is used to evaluate the polynomial.
# Even so, for polynomials of high degree the values may be inaccurate due to rounding errors. Use carefully.

# Teh following  polynomial 3 * 5**2 + 0 * 5**1 + 1 will be evaluated at the x=5
print('polynomial at specific values : \t', np.polyval([3, 0,1], 5)   )