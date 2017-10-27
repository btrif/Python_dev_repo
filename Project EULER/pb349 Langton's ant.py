#  Created by Bogdan Trif on 27-09-2017 , 6:04 PM.
# © o(^_^)o  Solved by Bogdan Trif  @       Completed on Wed, 25 Oct 2017, 19:03
#The  Euler Project  https://projecteuler.net
'''
                Langton's ant           -           Problem 349

An ant moves on a regular grid of squares that are coloured either black or white.
The ant is always oriented in one of the cardinal directions (left, right, up or down) and moves from square
to adjacent square according to the following rules:

- if it is on a black square, it flips the color of the square to white,
rotates 90 degrees counterclockwise and moves forward one square.

- if it is on a white square, it flips the color of the square to black,
rotates 90 degrees clockwise and moves forward one square.

Starting with a grid that is entirely white, how many squares are black after 10^18 moves of the ant ?


'''
import time, zzz
import matplotlib.pyplot as plt
import numpy as np



def turn_clockwise(orientation) :
    '''  U, R, D, L - up, right, down, left'''
    O = 'URDL'
    p = O.find(orientation)
    return O[ (p+1)%4 ]

print('turn_clockwise : \t' ,turn_clockwise('L') )


def turn_counterclockwise(orientation) :
    '''  U, R, D, L - up, right, down, left'''
    O = 'URDL'
    p = O.find(orientation)
    return O[ (p-1)%4 ]

print('turn_counterclockwise : \t' ,turn_counterclockwise('U') )

def move(pos, orientation) :
    if orientation == 'U' : return  ( pos[0], pos[1]+1 )
    if orientation == 'R' : return  ( pos[0]+1, pos[1] )
    if orientation == 'D' : return  ( pos[0], pos[1]-1 )
    if orientation == 'L'  : return  ( pos[0]-1, pos[1] )




print('\n--------------------------TESTS------------------------------')
t1  = time.time()



def get_the_overall_picture( nr_of_moves ) :
    Black = [] #set()
    pos, orientation = (0,0), 'U'

    for i in range(nr_of_moves) :

        if pos not in Black :
            Black.append(pos)    #   add(pos)
            orientation = turn_clockwise(orientation)
            pos = move(pos, orientation )
        elif pos in Black :
            Black.remove(pos)
            orientation = turn_counterclockwise(orientation)
            pos = move(pos, orientation )

        print(str(i+1)+'.        ',orientation, pos ,'    ', len(Black) , '        '  , Black[-20::] )

    # print('\nBlack squares : \n',len(Black), Black )
    return len(Black), Black


def make_the_plot( lim) :
    B = list(get_the_overall_picture(lim))[1]
    hmax, vmax = 0 , 0
    for i, j in B:
        if hmax < abs(i) :
            hmax = abs(i)
        if vmax < abs(j) :
            vmax = abs(j)

    print('hmax , vmax = ', hmax, vmax)

    fig = plt.figure(num=None, figsize=(5, 5), dpi=80, facecolor='w', edgecolor='k')
    ax = fig.add_subplot(1,1,1)

    def grid(hmax , vmax):
        # major ticks every 5, minor ticks every 1
        major_ticks = np.arange(-hmax, hmax, 5)
        minor_ticks = np.arange(-vmax, vmax, 1)

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

    grid(hmax , vmax)

    plt.axis([-hmax-1, hmax+1, -vmax-1, vmax+1 ])
    plt.grid(True)

    for k in B :
        plt.scatter(k[0], k[1], s=50 , c='black' , marker="s")

    plt.show()

make_the_plot( 11000 )

# get_the_overall_picture(12432)




t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
t1  = time.time()

# SOLUTION :
# We observe that the ant has a period of 104 moves and completing only 12 black squares
# Therefore we fix some small value and we choose 10648
# 10648.         U (-30, -6)      796          [(-26, -4), (-25, -3), (-25, -2), (-26, -2), (-27, -5), (-30, -2), (-27, -2),
#                                               (-27, -3), (-28, -3), (-29, -3), (-31, -4), (-31, -3), (-30, -3), (-30, -5), (-30, -4),
#                                               (-29, -4), (-28, -5), (-28, -6), (-29, -7), (-30, -7)]
# We choose 10648 because 10**18%104 = 10648%104 = 40
# Now all we have to do is  :
# (10**18-10648)/104 , ((10**18-10648)//104)*12,
# and we must add now the remainder left from 10648 moves which is = 796
#
# ((10**18-10648)//104)*12 + 796      <<---- AND WE HAVE THE CORRECT ANSWER !!!!!
# @2017-10-25, 19:00 - IT WORKED FROM THE FIRST TIME !!!!


print(10**18 % 104, 10664%104, (10648)%104)
print((10**18-10648)/104 , ((10**18-10648)//104)*12, ((10**18-10648)//104)*12 + 796)

print('\nResult = ', ( (10**18-10648)//104)*12 + 796 )          #   Answer:     115384615384614952


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')




