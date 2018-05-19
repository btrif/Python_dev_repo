#!/usr/bin/env python

# Jonathan Senning <joanthan.senning@gordon.edu>
# Gordon College
# March 19, 1999
# Converted to Python October 2008
#
# This program demonstrates the use of Taylor Series to solve the initial
# value problem x'(t) = t*sin(t), x(0) = 1.

from pylab import *

# Set desired order of Taylor Series

m = 8

# Set interval and initial condition

a, b = ( 0, 20 )
x0 = 1

# Desired number of subintervals

n = 20

# Begin the solution process...

h = float( b - a ) / float( n )
t = a
x = x0

# T and X are arrays that will contain each t value and each x value
# computed.  They are not necessary for the final solution, but are used
# to produce a plot of the solution curve.

T = [ t ]
X = [ x ]

# Enter the main loop.  Since the equation we are solving is
# x'(t) = t*sin(t) we will need to evaluate both cos(t) and sin(t)
# repeatedly for each value of t.  We compute them once ahead of time.

for i in range( n ):

    c = cos( t )
    s = sin( t )

    # The following is the pattern for the derivatives of x(t). The
    # subscript in each case is the order of differentiation.  Notice
    # the pattern of negative signs and the uniform increments of the
    # coefficient of the second term.
    #
    #   dx(0) =   t * s;
    #   dx(1) =   t * c + s;
    #   dx(2) = - t * s + 2 * c;
    #   dx(3) = - t * c - 3 * s;
    #   dx(4) =   t * s - 4 * c;
    #   dx(5) =   t * c + 5 * s;
    #   dx(6) = - t * s + 6 * c;
    #
    # In the loop below, s1 and s2 are used to figure the signs of the
    # first and second terms; s0 is used as an intermediate variable.
    # It's kind of a mess, but all this loop does is compute the values
    # of dx in the pattern shown above.

    dx = []
    ( s0, s1, s2 ) = ( 1, -1, -1 )
    for k in range( m ):
        s0 = -s0
        s1 =  s0 * s1
        s2 = -s0 * s2
        if k % 2 == 0:
             dx.append( s1 * t * s + s2 * k * c )
        else:
             dx.append( s1 * t * c + s2 * k * s )

    # Now compute the sum of the first m+1 terms of the Taylor series.
    # Using a nested form of the truncated series saves many operations.

    sum = dx[m-1]
    for j in range( m, 1, -1 ):
        sum = h * sum / float( j ) + dx[j-2]

    x = x + h * sum

    # At this point x contains the value x(t+h) so we need to compute the
    # new t value.  This could be done with either t = t+h or the form below.
    # The from below is preferred to avoid accumulated roundoff error from
    # the repeated addition of h.

    t = a + ( i + 1 ) * h

    # Now we can save the current values of t and x(t) for plotting.

    T.append( t )
    X.append( x )
    
# Done -- plot to compare with true solution: x(t) = sin(t) - t*cos(t) + 1.

T2 = linspace( a, b, 5 * n + 1 )
Y = sin(T2) - T2 * cos(T2) + 1

plot( T, X, "o", T2, Y, "-" )
xlabel( '$t$' )
ylabel( '$x$' )
title( 'Taylor Series Solution of $x\'(t) = t\sin(t)$, $x(0) = 1$' )
legend( ( 'Taylor Solution (order %d)' % m, 'Exact Solution' ), \
            loc='lower center' )

show()

# End of File
