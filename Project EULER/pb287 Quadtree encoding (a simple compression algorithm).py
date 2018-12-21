#  Created by Bogdan Trif on 02-11-2017 , 11:36 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
Quadtree encoding (a simple compression algorithm)          -           Problem 287

The quadtree encoding allows us to describe a 2N×2N black and white image as a sequence of bits (0 and 1).
Those sequences are to be read from left to right like this:

-   the first bit deals with the complete 2N×2N region;
-   "0" denotes a split:
the current 2n×2n region is divided into 4 sub-regions of dimension 2^(n-1) × 2^(n-1),
the next bits contains the description of the top left, top right, bottom left and bottom right sub-regions - in that order;
-   "10" indicates that the current region contains only black pixels;
-   "11" indicates that the current region contains only white pixels.

Consider the following 4×4 image (colored marks denote places where a split can occur):

p287_quadtree.gif

This image can be described by several sequences, for example : "001010101001011111011010101010", of length 30, or
"0100101111101110", of length 16, which is the minimal sequence for this image.

For a positive integer N, define DN as the 2N×2N image with the following coloring scheme:

=   the pixel with coordinates x = 0, y = 0 corresponds to the bottom left pixel,
=   if (x - 2^(N-1))^2 + (y - 2^(N-1))^2 ≤ 2^(2N-2) then the pixel is black,
=   otherwise the pixel is white.
What is the length of the minimal sequence describing D_24 ?


'''
import time, zzz
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

def generate_pixels( N, plot = False ):
    cnt = 0
    X, Y = [], []
    for x in range(0, 2**N) :
        Z = []      # used to display y max
        for y in range(0, 2**N) :
            if  ( x- 2**(N-1) )**2 + ( y - 2**(N-1) )** 2 <= ( 2**(2*N-2)) :
            # if  ( x )**2 + ( y  )** 2 <= ( 2**(2*N-2)) :
                cnt += 1
                X.append(x+0.5) ; Y.append(y+0.5)
                Z.append(y)
            # if  ( x- 2**(N-1) )**2 + ( y - 2**(N-1) )** 2 == ( 2**(2*N-2)) :
        y_max = max(Z)
        print( str(cnt)+ '.      x, y =  ', x , y_max ,'        x^2= ', ( x - 2**(N-1) )**2,  '       y^2=' , ( y_max - 2**(N-1) )** 2 , '        R^2 = '  ,( 2**(2*N-2))  )

    if plot == True :
        ######     START PLOT    ###########
        fig = plt.figure(figsize=(12 , 12))
        ax = fig.add_subplot( 1,1,1    ) #, aspect='equal')
        plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)


        major, minor, x1, x2, y1, y2 = 1, 10, 0, 2**N, 0, 2**N

        # major ticks every 5, minor ticks every 1
        major_ticks = np.arange(x1, x2, major)
        minor_ticks = np.arange(y1, y2, minor)

        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        ax.set_yticks(major_ticks)
        ax.set_yticks(minor_ticks, minor=True)


        plt.xlim([x1 , x2])
        plt.ylim([y1, y2])

        # and a corresponding grid
        # ax.grid(which='both')

        # or if you want differnet settings for the grids:
        # ax.grid(which='minor', alpha=0.2)
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=1.5)

        ax.grid(which='both')
        # ax.axis('equal')
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')

        plt.grid(True)

        plt.scatter(X, Y, color = 'slateblue', marker = 's' , s = 500  )

        plt.show()


generate_pixels( 6 , True )

print('\n--------------------------TESTS------------------------------')
t1  = time.time()

uncompressed = lambda N : sum([ 2**(2*i) for i in range(0, N)  ]) + 2*2**(2*N)          # CORRECT !

print('uncompressed : ', uncompressed(5)  )

N = 5
for x in range( 2**N):
    z = int(sqrt( ( 2**(2*N-2)) - ( x- 2**(N-1) )**2  ))
    y_max = z + 2**(N-1)
    y_min = 2**N - y_max
    pix = min( y_max-y_min+1, 2**N  )
    print('x = '  ,x, '     y_min = ' ,y_min, '     y_max = ' ,y_max, '      pixels =  ' , pix )


# @2017-11-13,  It remains to solve this problem via recursion when I will master it better than
# I am right now ! When it will come that day ? I AM curious !

### STUDY CASE :
# D5 :  minimal length =  499

t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()





# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


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




