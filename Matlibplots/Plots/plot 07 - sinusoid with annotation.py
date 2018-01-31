import matplotlib.pyplot as plt
import numpy as np


# ax = plt.subplot(111)
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
line = plt.plot(t, s, lw=2)

plt.grid(which='both')
plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),    arrowprops=dict(facecolor='black', shrink=0.05),            )
plt.annotate('local min', xy=(1.5, -1), xytext=(3, -1.5),    arrowprops=dict(facecolor='red', shrink=0.05),            )


plt.ylim(-2, 2)
plt.xlim(-0.5, 7)
plt.show()
