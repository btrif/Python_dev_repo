"""
Simple demo of the fill function.
"""
import numpy as np
import matplotlib.pyplot as plt

t1 = np.arange(0, 2 * np.pi, 0.1)
t2 = np.arange(0, 2 * np.pi, 0.001)

def f(t, a=1, b=2):
    return np.exp(-a * t) * np.cos(b  * t)


plt.figure(1)
#plt.subplot(211)
plt.plot(t1, f(t1, a=0.5), 'bo', t2, f(t2, b=4), 'r')
plt.plot(t1, f(t1, a=0.3, b=5), 'g--')
plt.grid(True)



plt.show()
