#  Created by Bogdan Trif on 31-01-2018 , 1:00 PM.
from numpy import *
import matplotlib.pyplot as plt



# example data with some peaks:
x = linspace(0, 8 , 1e3 )
data = .2*sin(10*x)+ exp(-abs(2-x)**2) + x**(2/3)

# that's the line, you need:
a = diff(sign(diff(data))).nonzero()[0] + 1 # local min+max
b = (diff(sign(diff(data))) > 0).nonzero()[0] + 1 # local min
c = (diff(sign(diff(data))) < 0).nonzero()[0] + 1 # local max



# graphical output...
# from pylab import *
plt.grid(which='both')

plt.plot( x, data)
plt.plot(x[b], data[b], "or", label="min")
plt.plot(x[c], data[c], "og", label="max")

plt.legend()
plt.show()

