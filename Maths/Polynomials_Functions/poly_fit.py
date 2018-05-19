#  Created by Bogdan Trif on 11-02-2018 , 8:36 PM.

import numpy as np
import matplotlib.pyplot as plt
from includes.app_functions import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from scipy.signal import savgol_filter

import numpy as np
import matplotlib.pyplot as plt


n_samples = 30
dataset = np.random.rand(n_samples)
print('dataset : \t', dataset )




fig = plt.figure(1, figsize=(16,8))
ax = plt.subplot(111)
t = np.arange(len(dataset))



plt.plot(t, dataset, "co-.")

p1 = np.polyfit(t, dataset, 1 )
p2 = np.polyfit(t, dataset, 2 )
p3 = np.polyfit(t, dataset, 3 )
p4 = np.polyfit(t, dataset, 4 )




print('p1  =  ', p1)
print('p2  =  ', p2)
print('p3  =  ',  p3)
print('p4  =  ',  p4)


print('polyval(p1, x) = ', np.polyval(p1,t))
print('polyval(p2, x) = ', np.polyval(p2,t))
print('polyval(p3, x) = ', np.polyval(p3,t))
print('polyval(p4, x) = ', np.polyval(p4,t))



plt.plot(t  , np.polyval(p1, t), 'y-.', label='polyn 1')
plt.plot(t  , np.polyval(p2, t), 'b--', label='polyn 2')

plt.plot(t  , np.polyval(p3, t), 'g-', label='polyn 3', color='lightcoral' )
plt.plot(t  , np.polyval(p4, t), 'm-', label='polyn 4')



plt.legend()
plt.grid(which ='both')
plt.show()

