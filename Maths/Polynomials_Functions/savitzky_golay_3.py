#  Created by Bogdan Trif on 11-02-2018 , 7:45 PM.
from savitzky_golay import Savitzky_Golay
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-4, 4, 500)
y = np.exp( -t**2 ) + np.random.normal(0, 0.05, t.shape)

ysg = Savitzky_Golay(y, window_size=31, order=4, deriv = 0, rate = 1)
import matplotlib.pyplot as plt

plt.figure(figsize=(16,5))
plt.grid(which='both')
plt.plot(t, y, label='Noisy signal')
plt.plot(t, np.exp(-t**2), 'k', lw=1.5, label='Original signal')
plt.plot(t, ysg, 'r', label='Filtered signal')
plt.legend()
plt.show()