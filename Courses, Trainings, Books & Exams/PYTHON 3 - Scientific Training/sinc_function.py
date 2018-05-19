from math import sin, pi

from pylab import *  # plotting routines
from scipy.integrate import odeint  # routine for ODE integration



"""Right hand side of the differential equation.
Here y = [phi, v].
"""
def derivative(y, t):
    return array([y[1], sin(y[0]) + 0.25 * cos(t)])  # (\dot{\phi}, \dot{v})

def compute_trajectory(y0):
# Integrate the ODE for the initial point y0 = [phi_0, v_0]
    t = arange(0.0, 100.0, 0.1)  # array of times
    y_t = odeint(derivative, y0, t)  # integration of the equation
    return y_t[:, 0], y_t[:, 1]  # return arrays for phi and v

# compute and plot for two different initial conditions:
phi_a, v_a = compute_trajectory([1.0, 0.9])
phi_b, v_b = compute_trajectory([0.9, 0.9])
plot(phi_a, v_a)

plot(phi_b, v_b, 'r--')

xlabel(r"$\varphi$")
ylabel(r"v")
show()


'''
def sinc(x):
#Compute the sinc function:
    sin(pi*x)/(pi*x)
    try:
        val = (x*pi)
        return sin(val)/val
    except ZeroDivisionError:
        return 1.0
output = [sinc(x) for x in input]

'''
