import matplotlib.pyplot as plt
import numpy as np
from math import sqrt


def toRadians(degrees):
    return (degrees / 180.0) * math.pi

def polar_to_X(theta, r):
    x = r * math.cos(theta)
    return x

def polar_to_Y(theta, r):
    y = r * math.sin(theta)
    return y

def draw_Circle(x):
    return sqrt(1-x**2)

t1 = np.arange(0.0, 1.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)


plt.figure(1)

plt.plot(t1, f(t1), 'b--')
plt.grid(True)



plt.show()
