#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

def xy(a, b , phi):
  return a*np.cos(phi), b*np.sin(phi)

fig = plt.figure()
ax = fig.add_subplot(111,aspect='equal')

phis = np.arange(0,6.28,0.01)           # Definition of the angle
a = 1.1
b = 1.8


plt.ylim([-2.5,2.5])
plt.xlim([-2.5,2.5])

# Setting spines (orthogonal axes)
ax = gca()
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

# Ploting (drawing) the circles
#ellipse = xy(1, 1.2, phis)
ax.plot( *xy(a, b, phis), color='c',  linewidth=2.5, linestyle='-' )

plt.grid(True)
plt.show()








'''

from pylab import *

figure(figsize=(8,8))
ax=subplot(aspect='equal')

#plot one circle (the biggest one on bottom-right)
circles(1, 0, 0.5, 'r', alpha=0.2, lw=5, edgecolor='b', transform=ax.transAxes)

#plot a set of circles (circles in diagonal)
a=arange(11)
out = circles(a, a, a*0.2, c=a, alpha=0.5, edgecolor='none')
colorbar(out)

xlim(0,10)
ylim(0,10)

'''