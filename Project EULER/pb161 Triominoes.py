#  Created by Bogdan Trif on 18-12-2018 , 12:10 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                    Triominoes                  -                   Problem 161

A triomino is a shape consisting of three squares joined via the edges. There are two basic forms:

If all possible orientations are taken into account there are six:

Any n by m grid for which nxm is divisible by 3 can be tiled with triominoes.
If we consider tilings that can be obtained by reflection or rotation from another tiling as different there are 41 ways a 2 by 9 grid can be tiled with triominoes:

In how many ways can a 9 by 12 grid be tiled in this way by triominoes?

'''
import time, zzz
import numpy as np

print('\n--------------------------TESTS------------------------------')
t1  = time.time()


# @2018-12-18, 12:11 : I think this problem can be solved via Backtracking by using matrices blocks
# We remark that there are only 6 shapes which can be represented with 2x2 matrices , 1x3 and 3x1

ur = np.array([ [1, 1], [1, 0] ])        #   UP-RIGHT
ul = np.array([ [1, 1], [0, 1] ])        # UP-LEFT
dr = np.array([ [1, 0], [1, 1] ])        # DOWN-RIGHT
dl = np.array([ [0, 1], [1, 1] ])        # DOWN-LEFT
ve = np.array([ [1], [1], [1] ])        # VERTICAL
ho = np.array([ 1, 1, 1] )        # HORIZONTAL

print('ur : \n', ur)
print('ul : \n', ul)
print('dr : \n', dr)
print('dl : \n', dl)
print('ve : \n', ve)
print('ho : \n', ho)

grid = np.zeros(( 9, 2 ), dtype=int )
print('grid : ', grid)

# def match_shape(shape , pos) :


###      How to “embed” a small numpy array into a predefined block of a large numpy array :
grid[ 0 : 0 + ur.shape[0], 0 : 0 + ur.shape[1]] = ur
print(grid)

# @2018-12-19, 13:21, Must continue the problem. A Recursive backtracking algorithm







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

