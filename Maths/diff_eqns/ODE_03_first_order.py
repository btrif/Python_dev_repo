import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def f(y, t):
    return 2 * y

y0 = np.array([1.0])
time = np.arange(0, 6, 0.1)

y_result = integrate.odeint(f, y0, time)
#y_result = y_result[:, 0]   # convert the returned 2D array to a 1D array

plt.plot(time, y0 * np.exp(time))
plt.grid(True)

for i, j in zip(time, y_result):
    print ('time:',i,'    -->   ','value: ',j)
plt.show()

