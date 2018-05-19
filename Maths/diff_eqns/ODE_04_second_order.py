import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
'''
For example, you want to solve the following differential equation:
z
00(t) = −z(t).
For a second order differential equation, you need to specify z(tini)
and z(tini)! In the example, lets assume z(0) = 0.0005 and z'(0) = 0.2.
The trick is to not to consider one second-order differential
equation, but two first-order differential equations! Lets introduce
the following variables: z(t) = u(t) and z'(t) = w(t). Then the differential equation
z''(t) = −z(t)
can be written as:
            w'(t) = −u(t)
            u'(t) = w(t).

So, from our original z(t) and z'(t) we went to two variables u(t)
and w(t) and instead of having one differential equation, we have
to solve two differential equations, but they are now of first order.
These are coupled, i.e. u(t) and w(t) are not independent (since
they are just z(t) and z'(t)).
This sounds more complicated, but it is not! You know how to
solve first–order differential equations. We just have to extend our
solution array: y = [u(t),w(t)]. Note that y[0] = u(t) and
y[1] = w(t), so your array does now contain the information about
u(t) = z(t) and w(t) = z'(t). In your script you define now the
differential equations as follows:
'''

def deriv(y,t):
    u_prime = y[1]
    w_prime = -y[0]
    y_prime = np.array([u_prime, w_prime])
    return y_prime

'''
As usual, you define your start time, end time, the number of
points in between and create a Numpy array with the help of the
linspace function. Finally, define a Numpy array which contains
the initial conditions, but this time the array is two dimensional
(initial condition for u and w):
'''
time=np.linspace(0, 10, 1000)       #   Define the time range

y_0 = np.array([0.0005, 0.2])           #       Array which contain initial conditions

y = integrate.odeint(deriv, y_0, time)          # Now our diff eqn is solved by the odeint module

'''To plot this, you call again pyplot, but this time, you need to
specify whether you want to plot y[0] = z(t) or y[1] = z'(t). Lets plot z(t):
'''
plt.plot(time, y[:,0]);  plt.grid(True); plt.show()


