"""
A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)  # x-array
line, = ax.plot(x, np.sin(x)*np.exp(-0.1 * x) )

def animate(i):
    line.set_ydata(np.sin(x +i )*np.exp(-0.10* x +i))  # the speed to update the data
    return line,

# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1,2000), init_func=init, interval=125, blit=True)

plt.plot([1, 2, 3, 4,5], [1, 4, 3, 2,-1], 'ms--')
plt.grid(True)
plt.ylim([-5,5])
plt.xlim([0,20])
plt.show()
