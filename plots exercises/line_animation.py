__author__ = 'trifb'    #2014-12-19
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()              #defining the figure
ax = plt.axes(xlim=(0, 10), ylim=(-8, 8))        # x-axes limits and y-axes limits
line, = ax.plot([], [], lw=4, )       # establishing two lists and lw = linewidth

# initialization function: plot the background of each frame
def init():
#    line.set_data([], [])
    return line,
'''The next piece is the animation function.
 It takes a single parameter, the frame number i, and draws a sine wave with a shift that depends on i:'''
# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, 1+ 0.09*i, 100)
    y = (1    - 0.02 * i)          #  the 'i' variable makes the sine function flow
    line.set_data(x, y)
    return line,

print(line)
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

plt.grid(); plt.show()