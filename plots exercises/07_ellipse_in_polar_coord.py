import numpy as np
import matplotlib.pyplot as plt
cos = np.cos
pi = np.pi

a = 10
e = 0.3
theta = np.linspace(0,2*pi, 360)
r = (a*(1-e**2))/(1+e*cos(theta))

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.set_yticklabels([])
ax.plot(theta,r)

print(np.c_[r,theta])
plt.show()