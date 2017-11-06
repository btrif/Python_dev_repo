#  Created by Bogdan Trif on 01-11-2017 , 7:59 PM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                Path sum: four ways             -               Problem 83

NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
by moving left, right, up, and down, is indicated in bold red and is equal to 2297.


Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
a 31K text file containing a 80 by 80 matrix,
from the top left to the bottom right by moving left, right, up, and down.


'''
import time, zzz

filename = "pb081_matrix.txt"
def load_file(filename):
    with open(filename) as f:
        matrix = [list(map(int, line.split(","))) for line in f.readlines()]
    f.close()
    return matrix

matrix = load_file(filename)



print('\n--------------------------TESTS------------------------------')
t1  = time.time()

M=  [[131, 673, 234, 103, 18], \
        [201, 96,  342, 965, 150],\
        [630, 803, 746, 422, 111],\
        [537, 699, 497, 121, 956],\
        [805, 732, 524, 37,  331]]


def three_ways_path( matrix ) :

    M = matrix
    gridSize = len(M)
    sol = [0 for i in range(gridSize)]

    #   initialise solution :
    for i in range(0, gridSize ) :
        sol[i] = M[i][gridSize - 1]

    for i in range(gridSize-2,-1, -1 ) :
        #   Traverse down :
        sol[0] += M[0][i]
        for j in range(1, gridSize) :
           sol[j] = min ( sol[j - 1] + M[j][i], sol[j] + M[j][i] )

        #   Traverse up :
        for j in range(gridSize -2, -1, -1) :
            sol[j] = min( sol[j], sol[j+1] + M[j][i] )

    print('The Complete path is : ',sol)
    return print('\nThe minimal path is : \t', min(sol))

three_ways_path(M)


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




