#!/usr/bin/env python

# Jonathan Senning <jonathan.senning@gordon.edu>
# Gordon College
# January 1999
# Revised August 2000
# Revised April 27, 2006 to update graphing commands
# Converted to Python May 2008
#
# This python program does essentially the same thing as the sequence
# of MatLab commands given on page 25 of "Numerical Mathematics and
# Computing", 4th edition, by Cheney and Kincaid, Brooks/Cole, 1999.

from pylab import *

x = pi * arange( -120, 121 ) / 100.0
y1 = x
y2 = x - (x**3) / 6.0
y3 = x - (x**3) / 6.0 + (x**5) / 120.0
y4 = sin( x )

plot( x, y1, x, y2, x, y3, x, y4 )
xlabel( '$x$' )
ylabel( '$y$' )
grid()
title( 'Partial sums of the Taylor series for $\sin(x)$' )
legend( ( '$y = T_1(x)$', '$y = T_3(x)$', '$y = T_5(x)$', '$y = \sin(x)$' ), \
            loc='upper center' )

show()

# End of File