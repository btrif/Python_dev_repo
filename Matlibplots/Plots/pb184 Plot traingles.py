#  Created by Bogdan Trif on 09-10-2017 , 9:56 PM.

from pylab import *
import itertools
import random

Colors = ['mediumturquoise',  'darkslategrey', 'springgreen', 'saddlebrown', 'olivedrab', 'wheat', 'brown',
          'chocolate', 'lightslategrey', 'palegreen', 'darkorange', 'darkorchid', 'hotpink', 'yellowgreen', 'silver', 'palevioletred',
          'oldlace', 'navy', 'peachpuff', 'orangered', 'mediumorchid', 'burlywood', 'tan', 'forestgreen', 'yellow', 'darksage',
          'darkslategray', 'bisque', 'indigo', 'lightsteelblue', 'aquamarine', 'blue', 'lightgrey', 'khaki', 'slategrey', 'darkred', 'lime', 'peru',
          'darkmagenta', 'midnightblue', 'lightslategray', 'darkgrey', 'lightcoral', 'teal', 'lightsage', 'deepskyblue', 'limegreen', 'skyblue',
          'aqua', 'mediumpurple', 'dodgerblue', 'plum', 'indianred', 'mediumslateblue', 'darkturquoise', 'violet',
          'darkgoldenrod', 'thistle', 'lawngreen', 'palegoldenrod', 'lightsalmon', 'lightpink', 'coral', 'rosybrown', 'goldenrod', 'lemonchiffon',
          'mediumseagreen',  'mediumblue', 'crimson', 'darksalmon', 'cornflowerblue', 'red', 'magenta', 'mistyrose',
          'mediumspringgreen', 'green', 'lightblue', 'lightgreen', 'darkgreen', 'purple', 'royalblue', 'sandybrown',
          'gray', 'blanchedalmond', 'turquoise', 'paleturquoise', 'blueviolet', 'darkslateblue', 'lightseagreen', 'orange', 'pink',
          'darkcyan',  'steelblue', 'gold', 'darkkhaki', 'black', 'papayawhip', 'lightskyblue', 'sienna', 'sage', 'cornsilk', 'dimgrey',
          'darkgray', 'deeppink', 'moccasin', 'chartreuse', 'fuchsia', 'darkviolet', 'honeydew', 'olive', 'mediumvioletred', 'powderblue',
          'lightgoldenrodyellow', 'grey', 'gainsboro', 'firebrick', 'slateblue', 'greenyellow', 'cadetblue', 'seagreen',
          'lavender', 'slategray', 'darkblue', 'dimgray', 'beige', 'mediumaquamarine', 'salmon',
          'cyan', 'orchid', 'darkseagreen', 'darkolivegreen', 'maroon', 'tomato', 'lightgray']

def grid(major,minor, x1, x2, y1, y2):
    # major ticks every 5, minor ticks every 1
    major_ticks = np.arange(x1, x2, major)
    minor_ticks = np.arange(y1, y2, minor)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)

    # and a corresponding grid
    # ax.grid(which='both')

    # or if you want differnet settings for the grids:
    # ax.grid(which='minor', alpha=0.2)
    ax.grid(which='minor', alpha=0.8)
    ax.grid(which='major', alpha=1)


fig = plt.figure(figsize=(11, 10))
ax = fig.add_subplot(1,1,1 ) #, aspect='equal')

ax.grid(which='both')
ax.axis('equal')

x1 , x2, y1, y2 = -5, 5, -5, 5
# ax.set_ylim([-x1, x2])
# ax.set_xlim([-y1, y2])
# ax.autoscale_view(True, True ,True)
plt.xlim([x1 , x2])
plt.ylim([y1, y2])

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

grid(1 , 5, x1, x2, y1, y2)

TRIANGL =   [((0, 3), (4, 0), (-3, -2)), ((0, 3), (4, 2), (-1, -4)), ((0, 4), (3, 2), (-4, -3)), ((0, 4), (4, 1), (-3, -1)), ((0, 4), (4, 3), (-1, -3)), ((1, 3), (4, 1), (-3, -4)), ((1, 4), (4, 2), (-3, -3))]

for triangle in TRIANGL :
    culoare = random.choice( Colors )
    plt.plot(*zip(*itertools.chain.from_iterable(itertools.combinations(triangle, 2)))  , color = culoare, marker = 'o',  linewidth=2.5 )


plt.ylabel('Triangle points')
plt.show()







