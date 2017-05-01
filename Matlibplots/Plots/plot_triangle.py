from pylab import *
import itertools

def plot_triangle(A, B, C):
    fig = plt.figure()
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

    ax.grid(which='both')

    x1 , x2, y1, y2 = -1000, 1000, -1000, 1000
    # ax.set_ylim([-x1, x2])
    # ax.set_xlim([-y1, y2])
    ax.autoscale_view(True, True ,True)

    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

    grid(200,50, x1, x2, y1, y2)

    all_data = [ A, B, C ]
    plt.plot(*zip(*itertools.chain.from_iterable(itertools.combinations(all_data, 2)))  , color = 'red', marker = 'o',  linewidth=2.5 )

    # plt.plot([1, 2, 3, 4], linestyle='--', color='m')
    # plt.scatter(10, 10 , s=20 ,  marker='o' , linewidths=2.5  )
    # plt.scatter(-15, 20 , s=20 ,  marker='o' , linewidths=2.5  )
    # plt.plot( [ 15, 20], [-10, -15]   ,'bo-' , linewidth=2.5  )
    # plt.plot([3, 1.2, 1, 3], linestyle='--',  linewidth=4.5)
    # plt.plot([8, 3, 1, 5], 'ro-.')
    plt.ylabel('Triangle points')
    plt.show()

lst = [-100, 200, 900, 100, -100, -700]
A, B, C = [lst[0], lst[1]],  [lst[2], lst[3]],  [lst[4], lst[5]]
# A, B, C = [129, 169], [576, 651], [-87, -458]
plot_triangle(A, B, C)