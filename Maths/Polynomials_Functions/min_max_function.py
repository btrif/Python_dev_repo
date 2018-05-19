#  Created by Bogdan Trif on 31-01-2018 , 1:00 PM.
import numpy as np
import matplotlib.pyplot as plt



# example data with some peaks:
x = np.linspace(0, 8 , 1e3 )
data = .2*np.sin(10*x)+ np.exp(-abs(2-x)**2) + x**(2/3)

# that's the line, you need:
min_and_max = np.diff(np.sign(np.diff(data))).nonzero()[0] + 1 # local min+max
print('min_and_max : ', min_and_max)
MIN = (np.diff(np.sign(np.diff(data))) > 0).nonzero()[0] + 1 # local min
print('MIN : ', MIN)
MAX = (np.diff(np.sign(np.diff(data))) < 0).nonzero()[0] + 1 # local max



# graphical output...
fig = plt.figure(1, figsize=(18,10))
ax = plt.subplot(111)
plt.title(' MIN & MAX')
plt.grid(which='both')

plt.plot( x, data)
plt.plot(x[MIN], data[MIN], "or", label="min")
plt.plot(x[MAX], data[MAX], "og", label="max")

plt.legend(loc=0)
plt.show()




############### Using scipy         ###################

import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt

y = np.random.random(40)
print('y : ',len(y))
t = np.arange(0, len(y))
print('t : ',len(t))

# for local maxima
MAX = argrelextrema(y, np.greater)
print('MAX :', y[MAX], t[MAX],'\n', MAX)

# for local minima
MIN = argrelextrema(y, np.less)

fig = plt.figure(1, figsize=(10,3))
ax = plt.subplot(111)
plt.plot(t, y,'r.-')
plt.plot( t[MAX], y[MAX],'bo')
plt.plot( t[MIN], y[MIN],'go')


plt.grid(which ='both')
plt.show()