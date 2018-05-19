# -*- coding: utf-8 -*-
'''
Python – Solving Second Order Differential Equations
Posted on March 6, 2013

This presentation outlines how to solve a second order ordinary differential equation (ode) with python.
The solution is obtained numerically using the python scipy ode engine (integrate module),
 the solution is therefore not in analytic form but the output as if the analytic function was computed for each time step.
 The method is generally applicable to a higher order ode as well.
We will use a series RLC circuit for our example.

'''
'''
Step 1

Get ODEs and split into only first order ODEs
Eg, if ode is:

ax'' + bx' + c=k                 (1)

and we let

q=x'                                   (2)

We now have:

aq' + bq + c=k                  (3)

 Eqns (2) and (3) for a "system" of first order ODEs that represent eqn (1)

For our series RLC circuit we have:

VL + VR + VC = Vs        (4)

Now:

VC = v                             (5)

Eqn (4) becomes:

LCv'' + RCv'+v=Vs        (6)

Which is a second order ODEs in the capacitor voltage v
If we let:
x=v'                                (7)

substitute this value in eqn (6) gives:

LCx' + RCx+v=Vs        (8)

we now have two first order ODEs to represent eqn (6)

Step 2:

Rearrange first order ODEs in the following form:

x' = f(x)                         (9)

For our RLC example we have:

v' = x                               (10)
x' = (Vs - v - RCx)/LC       (11)

Step 3:

Implement a python function that returns the right hand sides of the rearranged equations.
For our example we have:
'''

from scipy import integrate
from pylab import * # for plotting commands

def rlc(A,t):
    Vc,x=A
    V = 1.0 #voltageSource
    R = 5.0
    L=100.0e-9 #100nH
    C = 1.0e-9 #1nF
    res=array([x, (V-Vc-(x*R*C)) / (L*C)])
    return res

time = linspace(0.0, 0.6e-6, 1001)          #Define the time steps for the solution.
vc, x = integrate.odeint(rlc, [0.0,0.0], time).T        #Call the integrate function to obtain the solution.

i=1.0e-9 * x

figure(); grid(True); plot(time,vc); xlabel('t'); ylabel('Vc'); show()
