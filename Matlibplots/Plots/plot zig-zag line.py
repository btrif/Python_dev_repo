#  Created by Bogdan Trif on 20-11-2017 , 3:52 PM.
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(1,1,1 ) #, aspect='equal')

def grid(major,minor, x1, x2, y1, y2):
        # major ticks every 5, minor ticks every 1
        major_ticks = np.arange(x1, x2, major)
        minor_ticks = np.arange(y1, y2, minor)

        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        ax.set_yticks(major_ticks)
        ax.set_yticks(minor_ticks, minor=True)

        # and a corresponding grid
        ax.grid(which='both')

        # or if you want differnet settings for the grids:
        # ax.grid(which='minor', alpha=0.2)
        ax.grid(which='minor', alpha=0.8)
        ax.grid(which='major', alpha=1)

# ax.grid(which='both')
# ax.axis('equal')

x1 , x2, y1, y2 = 0, 200, -20, 20
# ax.set_ylim([-x1, x2])
# ax.set_xlim([-y1, y2])
# ax.autoscale_view(True, True ,True)
plt.xlim([x1 , x2])
plt.ylim([y1, y2])

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

grid(1 , 10, x1, x2, y1, y2 )





V = [(0, 0), (2, 2), (5, -1), (10, 4), (17, -3), (28, 8), (41, -5), (58, 12), (77, -7), (100, 16), (129, -13), (160, 18), (197, -19), (238, 22), (281, -21), (328, 26), (381, -27), (440, 32), (501, -29), (568, 38), (639, -33)]

x = [ i[0] for i in V ]
y = [ i[1] for i in V ]

print(x, y)



for i in range(0, len(x), 2):
    print( x[i:i+2], y[i:i+2] )
    plt.plot(x[i:i+2], y[i:i+2], 'ro-')
    plt.plot(x[i+1:i+3], y[i+1:i+3], 'ro-')
#     plt.plot(x[i+1:i+3:2], y[i+1,i+3:2], 'b-')

plt.plot([x[1], x[5] ], [y[1],y[5]], 'b-')

plt.show()