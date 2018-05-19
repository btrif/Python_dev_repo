import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def deriv(y,t):
    u_prime = y[1]
    w_prime = -3 * y[0] - np.sin(t)    # -1/30*u_prime
    y_prime = np.array([u_prime, w_prime])
    return y_prime

time=np.linspace(0, 250, 1000)

y_0 = np.array([0.0005, 0.2])

y = integrate.odeint(deriv, y_0, time)          # Now our diff eqn is solved by the odeint module

plt.plot(time, y[:,0])
plt.show()


