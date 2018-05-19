#  Created by Bogdan Trif on 11-02-2018 , 7:45 PM.
from savitzky_golay import Savitzky_Golay
import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import savgol_filter

x =  np.arange(60+1)
y =  np.array([-0.06, -0.06, -0.06, -0.06, -0.06, -0.05, -0.05, -0.05, -0.04, -0.04, -0.04, -0.05,
               -0.04, -0.04, -0.03, -0.04, -0.03, -0.03, -0.03, -0.03, -0.04, -0.03, -0.04, -0.03,
               -0.02, -0.02, -0.02, -0.02, -0.02, -0.02, -0.01, -0.01, -0.02, -0.03, -0.01, -0.05,
               -0.02, -0.02, -0.02, -0.02, -0.03, -0.03, -0.02, -0.02, -0.02, -0.02, -0.02, -0.02,
               -0.02, -0.02, -0.03, -0.02, -0.03, 0.01, 0.02, 0.02, 0.03, 0.02, 0.02, 0.03, 0.01])

yhat = Savitzky_Golay(y, window_size=31, order=3) # window size 51, polynomial order 3
time_series_savgol = savgol_filter(y, window_length=57, polyorder=3)

p1 = np.polyfit(x, y, 1 )
p2 = np.polyfit(x, y, 2 )
p3 = np.polyfit(x, y, 3 )
print('p1, p2, p3 =  ', p1, p2, p3)
print('polyval(p1, x) = ', np.polyval(p1,x))

print(yhat)
plt.figure(figsize=(16,5))
plt.grid(which='both')
plt.plot(x,y, 'yo-.' )
plt.plot(x, yhat, color='red')
# plt.plot(x, time_series_savgol, color='blue')
plt.plot(x , np.polyval(p1, x), 'm-')
plt.plot(x , np.polyval(p2, x), 'gv')
plt.plot(x , np.polyval(p3, x), 'r--')



plt.show()