#  Created by Bogdan Trif on 12-02-2018 , 11:31 AM.

import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

N = 100


x = np.linspace(0,2*np.pi,100)
y = np.sin(x) + np.random.random(100) * 0.8

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth


w = scipy.fftpack.rfft(y)
f = scipy.fftpack.rfftfreq(N, x[1]-x[0])
spectrum = w**2

cutoff_idx = spectrum < (spectrum.max()/5)
w2 = w.copy()
w2[cutoff_idx] = 0

y2 = scipy.fftpack.irfft(w2)


fig = plt.figure(1, figsize=(18,10))
plt.title( ' FAST FOURIER TRANSFORM ')
ax = plt.subplot(111)


plt.plot(x, y2,'-' ,  linewidth = 2 ,label = 'Fast Fourier Transfrom' )
plt.plot( x, smooth(y, 3), 'r-' , lw=1 , label = 'smooth 3' )
plt.plot(x, smooth(y , 19 ), 'g-', lw=1 , label = 'smooth 19')



plt.legend(loc = 0)
plt.grid(which ='both')
plt.show()


plt.plot(x,spectrum, 'm-', lw=1 , label = 'spectrum')
plt.show()