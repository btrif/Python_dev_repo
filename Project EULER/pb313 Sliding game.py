#  Created by Bogdan Trif on 19-12-2018 , 10:28 AM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                                    Sliding game      -       Problem 313

In a sliding game a counter may slide horizontally or vertically into an empty space.
The objective of the game is to move the red counter from the top left corner of a grid
to the bottom right corner; the space always starts in the bottom right corner.

For example, the following sequence of pictures show how the game can be completed in five moves on a 2 by 2 grid.

p313_sliding_game_1.gif

Let S(m,n) represent the minimum number of moves to complete the game on an m by n grid.

For example, it can be verified that S(5,4) = 25.

p313_sliding_game_2.gif

There are exactly 5482 grids for which S(m,n) = p2, where p < 100 is prime.

How many grids does S(m,n) = p^2, where p < 10^6 is prime?


'''
import time, zzz


print('\n--------------------------TESTS------------------------------')
t1  = time.time()

def slides(m, n) :
    S = m - 2 + n - 1 - 3   #   Move only white space from bottom left to top right
    print('only white moves = ', S )
    S += 1      # first red move to white space
    print('white + red :  S = ', S)
    ####   RULES :      ####
    #   1.     For an horizontal move RED needs 4 white displacements, without the RED 1 move
    #   2.      For a diagonal movement RED needs 2 moves for the vertical displacement + another
    #            2 moves for the horizontal displacement, without the RED 2 own moves.
    #   3.      For the vertical move RED needs 4 white displacements, without the RED 1 own move
    ###   Convention: we will consider always m >= n ( cols >= rows )
    diag = (n-1) * (4+1+1)
    S += diag
    print('diag = ', diag, ' ;    S=', S )
    horiz = (m-n)*5
    S += horiz
    print('horiz = ', horiz )

    print('S= ', S)
    return S


slides(5, 5)

# @2018-12-19 --  I need to properly adjust this function. Work not completed !


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

