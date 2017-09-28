import numpy as np
from scipy.optimize import brentq
import matplotlib.pyplot as plt

def f(x):
    return x**3 - x**2 - 1

x = np.linspace(0, 2, 100)
plt.plot(x, f(x))
plt.axhline(color = 'k')

root, info = brentq(f, 0.5, 2, full_output=True)
plt.axvline(x=root, color = 'r', **{'linestyle': 'dashed'})
print (root, info.converged)

plt.show()

from math import pi
from numpy import sin, cos, linspace

def g(x):
    return (x**2. * sin(20*x) + cos(x-pi))**3 + 1

x = linspace(-1, 1, 100)
plt.plot(x, g(x))
plt.show()

#   We can zoom in to get a better idea of the interval of interest.
x = linspace(-0.05, 0.05, 100)
plt.plot(x, g(x))
plt.show()