import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

'''
We want to solve the 1st order ODEs :
        y'(t) = 3.5 y(t)
        y' - 3.5 y = 0
        Characteristic equation is :    r - 3.5 = 0      =>
gen sol'n is :        y(t) = C0 * e^(3.5*t)
Establishing init cond:      if t = 0 = t0       =>  y(t0=0) =  C0
We consider     y(t0) = 10 = C0     =>
the particular sol'n is     =>      y'(t) = 10 * e^(3.5*t)
'''
#   CODE    IMPLEMENTATION:

def deriv(y, t):
    y_prime = np.array([3.5 * y[0]])
    return y_prime

start = 0
end = 1.5
numsteps = 150
time = np.linspace(start, end, numsteps)

y_0 = np.array([10])

y = integrate.odeint(deriv, y_0, time)

print('Value for test: ', time[8],' --> ', y[8])
for i, j in zip(time, y):
    print ('time:',i,'    -->   ','value: ',j)

plt.plot(time, y[:])
plt.xlabel('t'); plt.ylabel('y')
plt.grid(True)
plt.show()


