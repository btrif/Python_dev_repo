"""
Matplotlib Animation Example

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

'''Here we create a figure window, create a single axis in the figure,
 and then create our line object which will be modified in the animation.
 Note that here we simply plot an empty line: we'll add data to the line later.'''
# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()              #defining the figure
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))        # x-axes limits and y-axes limits
line, = ax.plot([], [], lw=5)       # establishing two lists and lw = linewidth

'''Next we'll create the functions which make the animation happen.
init() is the function which will be called to create the base frame upon which the animation takes place.
Here we use just a simple function which sets the line data to nothing.
 It is important that this function return the line object,
 because this tells the animator which objects on the plot to update after each frame:'''
# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,
'''The next piece is the animation function.
 It takes a single parameter, the frame number i, and draws a sine wave with a shift that depends on i:'''
# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()