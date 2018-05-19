import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

a = 2

def f(y, t):
    return a * y

y0 = 1.0
t_output = np.arange(0, 6, 0.1)

y_result = integrate.odeint(f, y0, t_output)
y_result = y_result[:, 0]   # convert the returned 2D array to a 1D array

plt.plot(t_output, y0 * np.exp(a * t_output))
plt.grid(True)
plt.show()