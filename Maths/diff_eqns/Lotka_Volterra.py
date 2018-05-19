from scipy.integrate import odeint
import numpy as np
from matplotlib import pyplot as plt

alpha=0.1
beta=0.015
gamma=0.0225
delta=0.02

def system(z, t):
    x,y=z[0], z[1]
    dxdt= x*(alpha - beta*y)
    dydt=-y*(gamma - delta*x)
    return [dxdt, dydt]

t = np.linspace(0, 300, 1000)
x0, y0=1.0, 1.0

sol = odeint(system,[x0, y0] , t)
X, Y = sol[:,0], sol[:,1]

plt.plot(X,Y)
plt.show()