#!/usr/bin/python
import matplotlib.pyplot as plt1
import numpy as np2
from pylab import *

def xy(r , phi):
  return r*np2.cos(phi), r*np2.sin(phi)

fig = plt1.figure()
ax = fig.add_subplot(111,aspect='equal')  

phis = np2.arange(0,6.28,0.01)
r = 1.1

plt1.ylim([-2.5,2.5])
plt1.xlim([-2.5,2.5])

# Setting spines (orthogonal axes)
ax = gca()
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

# Ploting (drawing) the circles
ax.plot( *xy(r, phis), color='c',  linewidth=2.5, linestyle='-' )
ax.plot( *xy(r+1, phis), color='#11ee11',  linewidth=2.5, linestyle='-' )
plt1.grid(True)
plt1.show()








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