import sympy

print(help(sympy))
print('-----------------------------------')

A = dir(sympy)
print( A )

print('------------------ Number Theory, Totient, Binomial Coeff ------------------------')

print(sympy.ntheory.totient(510510))
print(sympy.ntheory.totient(4))
print(sympy.ntheory.totient(6))
print(sympy.ntheory.totient(8))
print(sympy.ntheory.binomial_coefficients_list(15))

print('------------------ Divisors ------------------------')
print(sympy.ntheory.divisors(12))
print(sympy.ntheory.divisor_count(12))
print(sympy.ntheory.divisor_sigma(12))

print(sympy.ntheory.primefactors(90))



print(sympy.ntheory.multinomial_coefficients(2,3))
print(sympy.ntheory.multinomial_coefficients(2,2))

print('----------------------- Primes ------------------------')

print(sympy.ntheory.primerange(3,18))
print(sympy.ntheory.primepi(100))
print(sympy.ntheory.primorial(2))


print('----------------------- Partitions ------------------------')

print(sympy.ntheory.npartitions(4))

print('  ----------------------- Continued Fractions ------------------------')

print(sympy.ntheory.continued_fraction_reduce([1,1,2,4]))
print(sympy.ntheory.continued_fraction_periodic(13,6))


print(sympy.ntheory.is_nthpow_residue(2,3, 8))
print(sympy.ntheory.is_primitive_root(12,23))

from sympy import symbols, expand_mul, exp, log, sin
x, y, z = symbols('x,y,z', positive=True)
print(sympy.expand_mul(sympy.exp(x+y)*(x+y)*sympy.log(x*y**2)))
print(sympy.expand_power_base((x*y)**z))
print(sympy.expand_trig( sin(x+y)*(x+y)) )

from sympy import factor, sqrt
from sympy.abc import x, y
print(sympy.factor(2*x**5 + 2*x**4*y + 4*x**3 + 4*x**2*y + 2*x + 2*y))

from sympy.abc import x, y
from sympy.core.evaluate import evaluate
print( '\nEvaluate : \t ' ,  ( (x-1/2 )**2 + (y-1/2)**2 - 1/4 ) )
print('Simplify : ' , sympy.simplify(  ( (x-1/2 )**2 + (y-1/2)**2 - 1/4 ) ) )


################################
print('\n---------------------------------------------')

from sympy import *
x, y, z = symbols("x y z")

expr = cos(x) + 1
print( expr.subs(x, y) )

print (expr.subs(x, 0) )

print('\n---------------- Equation Manipulations, Math variable Substitution, Lambdify ')

# The main equation, we substitute y=f(x) = x into it
expr = (x- (1/2))**2 + (y-(1/2))**2 - (1/4)
v1 = expr.subs( x, y )
print( 'The SUBSTITUTED expression : \t'  ,v1 )
v2 = sympy.expand (v1)
print('The expanded expression : \t' ,v2 )
# we find the roots of the quadratic equation :
y = sympy.Symbol('y')
print('Solving quadratic, finding its roots : \t', sympy.solve( v2, y ) )


print('\n-----Second example, more detailed : -------\n')
# The main equation, we substitute y=f(x) = x/2 into it, ##### actually we do x=2*y
w1 = expr.subs( y, x/2 )
print('The SUBSTITUTED expression : \t' , v2 )

#Expand, Put in standard form
w2 = sympy.expand (w1)
print('The EXPANDED expression : \t' ,  w2 )
# Lambdify, which means that we create a function from the previous expression
J =  sympy.lambdify(x, w2)
print('We simply test the function with some values : \t',J(0), J(1), J(1/2))

# we find the roots of the quadratic equation :
x = sympy.Symbol('x')
print('Solving quadratic, finding its roots : \t', sympy.solve( w2, x ) )
min_root = min ( sympy.solve( w2, x ) )
print('The smallest root is : \t', min_root)








