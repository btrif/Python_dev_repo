#  Created by Bogdan Trif on 27-09-2017 , 6:04 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                Langton's ant           -           Problem 349

An ant moves on a regular grid of squares that are coloured either black or white.
The ant is always oriented in one of the cardinal directions (left, right, up or down) and moves from square
to adjacent square according to the following rules:

- if it is on a black square, it flips the color of the square to white, rotates 90 degrees counterclockwise and moves forward one square.
- if it is on a white square, it flips the color of the square to black, rotates 90 degrees clockwise and moves forward one square.

Starting with a grid that is entirely white, how many squares are black after 10^18 moves of the ant ?


'''
import time, zzz




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
    Black = set()
    pos, orientation = (0,0), 'U'
    for i in range(nr_of_moves) :

        if pos not in Black :
            Black.add(pos)
            orientation = turn_clockwise(orientation)
            pos = move(pos, orientation )
        elif pos in Black :
            Black.remove(pos)
            orientation = turn_counterclockwise(orientation)
            pos = move(pos, orientation )

        print(orientation, pos ,'    ', Black)

    print('\nBlack squares : \n',len(Black), Black )
    return print('\nBlack Squares : \t', len(Black))

get_the_overall_picture(2**5)


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




