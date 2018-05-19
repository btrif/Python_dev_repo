'''Python – Solving First Order Differential Equations

This presentation outlines how to solve an ordinary differential equation (ode) with python.
The solution is obtained numerically using the python scipy ode engine (integrate module),
the solution is therefore not in analytic form but the output as if the analytic function
 was computed for each time step. We will use a series RC circuit for our example.
'''
'''
Step 1

Get ode and rearrange in the following form:
x'=f(x)

For our RC circuit example from:
V=RCVc'+Vc

we have:
Vc'=(V-Vc)/RC
'''
# Step 2
# Implement a python function that returns the right hand side of the rearranged equation,
#  ie f(x) For our example we have:

from scipy import integrate
from pylab import *
def capVolts(Vc, t):     # f(x) Function
    V = 12
    R = 0.5
    C = 1
    return (V-Vc)/(R*C)

time = linspace(0.0, 5.0, 1000)         # Define the time steps for the solution.
y = integrate.odeint(capVolts, 0, time)         # Call the integrate function to obtain the solution.

plot(time, y); grid(True); xlabel('t'); ylabel('Vc'); show()

