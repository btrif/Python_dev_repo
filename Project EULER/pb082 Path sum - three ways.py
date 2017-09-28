#!/usr/bin/python
# Solved by Bogdan Trif @   Completed on Fri, 1 Sep 2017, 22:15
#The  Euler Project  https://projecteuler.net
'''
                            Path sum: three ways        -       Problem 82
NOTE: This problem is a more challenging version of Problem 81.
The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and
finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

                           131 673 234 103 18
                           201 96  342 965 150
                           630 803 746 422 111
                           537 699 497 121 956
                           805 732 524 37  331

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix,
from the top left to the bottom right by only moving right and down.
'''

import time
from numpy import transpose, zeros
from copy import copy, deepcopy

filename = "pb081_matrix.txt"
def load_file(filename):
    with open(filename) as f:
        matrix = [list(map(int, line.split(","))) for line in f.readlines()]
    f.close()
    return matrix

matrix = load_file(filename)
# for i in matrix :    print(i)

# mT = transpose(matrix)
# print('\n',mT)


print('\n----------------- TEST FOR Smaller MaTriX -----------------------\n')

# m =[[150, 650, 250, 100, 50], \
#        [200, 100,  350, 950, 150],\
#        [650, 800, 750, 400, 100],\
#        [550, 700, 500, 150, 950],\
#        [800, 750, 500, 50,  350]]

M=  [[131, 673, 234, 103, 18], \
        [201, 96,  342, 965, 150],\
        [630, 803, 746, 422, 111],\
        [537, 699, 497, 121, 956],\
        [805, 732, 524, 37,  331]]

# M = [ [100,	100,	90,	100,	100],
#         [95,	   80	,   105,	110,	 100],
#         [100,	   20,	   150,	115,	100],
#         [125,   	95,	35,	100,	100],
#         [90,    	95,	100,	95,	100] ]

print('------------------------------------The Original Matrix --------------')
for i in range(len(M)): print(M[i])

print('\n----------------------------------- The Computed PATH ---------------------')

# M = [row[:] for row in mT]     # Making a copy of transposed matrix
# M = deepcopy(mT)          # deepcopy for cloning the transposed matrix
# B = zeros((len(M), len(M)), dtype=int)        # numpy Create a zeroed Matrix the same size
# print(B)


M_test = [ [100,	100,	90,	100,	100],
                    [95,	80	,   105,	110,	100],
                    [100,	20,	150,	115,	100],
                    [125,	95,	35,	100,	100],
                    [90,	95,	100,	95,	100] ]

# min_three_ways_path(M_test)
# min_three_ways_path(matrix)

# FAILED :
# Smallest path cost : 	 312831

# print()
# for i in range(len(B)): print(B[i])
# print()
#
#
# # print(mT[0])
# for i in range(1, len(mT)-1):
#     for j in range(0, len(mT)):
#         if B[i][j] ==1 :
#             if i == 1 or i == len(mT)-1 :        # 2-nd row (#1) and last row
#                 mT[i][j] +=  M[i-1][j]
#
#             #if j%2 == 0 :
#             if i < len(mT)-1 and j < len(mT)-2 :
#                 if M[i-1][j+1] + M[i][j+1] < M[i-1][j] :        # Go To LEFT   __|
#                     mT[i][j] += ( mT[i-1][j+1] + mT[i][j+1] )
#
#                 elif  M[i][j+1] +M[i+1][j+1] < M[i][j+1] :        # Go To RIGHT  |__
#                     mT[i][j] += M[i][j+1] +M[i+1][j+1]
#
#                 else :
#                     mT[i][j] += M[i-1][j]
#
#     print(mT[i])
# print()
# Characters :  ∟ ∟  ┐ ┐  ┐ ∟  ┌ ┌ ┐ _|


# for i in range(len(mT)): print(mT[i])


# matrix = deepcopy(m)        #              You must use deepcopy !!!!!!!!!!!!!!!!!!!!!!
#
# for i in range(1,len(m)):
#     matrix[0][i] += matrix[0][i-1]
#     matrix[i][0] += matrix[i-1][0]
#     print(matrix[i])
#
# print('---------------- ')
#
# for i in range(1,len(m)):
#     for j in range(1,len(m)):
#             matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])
#     print(matrix[i])













#Matrix as it is :
# for i in range(0,len(m)):
#     for j in range(0, len(m)):
#             if j == 0  :
#                 continue
#             if j == len(m)-1 :
#                 m[i][j] += m[i][j-1]
#
#             elif i == 0 and len(m)-1 >  j>0 :
#                 m[i][j] += min(m[i][j-1], m[i+1][j] )
#
#             elif i == len(m)-1 and len(m)-1 >  j > 0 :
#                 m[i][j] += min(m[i][j-1], m[i-1][j] )
#
#             else:
#                 print(m[i-1][j], m[i+1][j], m[i][j-1])
#                 m[i][j] += min( m[i-1][j], m[i+1][j], m[i][j-1] )
#                 if ( j <  len(m)-1 and mtx[i-1][j] < mtx[i+1][j] and  mtx[i-1][j] < mtx[i][j+1]   ) :
#                      print( mtx[i-1][j] , mtx[i+1][j], mtx[i][j+1] )
#                      fix_point = m[i][j]
#                      m = [row[:] for row in mtx]
#                      i = i - 1
#                      m[i][j] +=fix_point
#                      m[i+1][j] = 10**4
#
#             # print(m[i][j])
#             # print(mtx[i][j])
#     print(m[i])

print('\n================  My FIRST SOLUTION,  DP ===============\n')
t1  = time.time()

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

three_ways_path(matrix)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')




print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
print('\n--------------------------SOLUTION 1, Dynamic Programming   --------------------------')
t1  = time.time()

# ====== Fri, 25 Aug 2017, 00:18 FergusonTG  ,
# Another python solution, using DP and sweeping backwards from right to left. Comments in line
#
# Biggest problem for me was realising I had to scan downwards and upwards on each column in order to
# get costs for moving down and up respectively.


import math

def costValue(row, col):
    if row<0 or row > len(costs)-1:
        return math.inf
    if col < 0 or col > len(costs[row])-1:
        return math.inf
    return costs[row][col]

def leastCost () :
    # start at last column: this is copy of matrix column
    for row in range(len(matrix)): costs[row][-1] = matrix[row][-1]

    # next, look to the previous column and get cost of coming
    # from the left
    # then we go down looking for cost of moving upards
    # and afterwards sweep up looking at cost of moving down
    for col in range(len(matrix[0])-2,-1,-1):
        # scanning downwards
        for row in range(len(matrix)):
            # cost of going right
            costs[row][col] = matrix[row][col] + costValue(row,col+1)
            # cost of going up
            costs[row][col] = min(costValue(row,col),
                        matrix[row][col]+costValue(row-1,col))
        # scanning upwards
        for row in range(len(matrix[row])-1,-1,-1):
            costs[row][col] = min(costValue(row,col),
                        matrix[row][col]+costValue(row+1,col))
        # helps with debugging
        # showCosts()

    return min(row[0] for row in costs)

def showCosts():
    for row in costs:
        print(row)
    print()


if __name__ == "__main__":
    with open("pb081_matrix.txt","r") as matrixFile:
        matrix = [[int(w) for w in line.split(",")] for line in matrixFile]


    costs = [[math.inf]*len(row) for row in matrix]

    answer = leastCost()
    print(answer)


t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 2,  --------------------------')
t1  = time.time()

# ==== Tue, 15 Nov 2016, 01:14, rtoscani, Netherlands

# First, the matrix is stored in a nested (2D-)list.
# Then, starting with the second column and working top-down, each subsequent value is gradually replaced
# by a minimum path sum value. For each cell, this is done by determining all possible sums through adjacent cells underneath,
# until one cell in the neighbouring column on the left is reached (which is also included in the sum).
# Of the values on top, only the one immediately above is added, this is already a replaced minimal value!
# The smallest of the sums found is then used to replace the original value in the cell.
# This procedure is repeated in the next column and so on until the last column is reached.
# Finally, the smallest value in the last column yields the answer to the problem.


minimum = 1000000
matrix = []
f = open(filename,'r')
for line in f.readlines():
    if not line:
        break
    lis = [int(i) for i in line.split(',')]
    matrix.append(lis)
f.close()
for i in range(1,len(matrix[0])):
    for j in range(len(matrix)):
        min_sum = minimum
        col_sum = 0
        for k in range(j,len(matrix)):
            col_sum += matrix[k][i]
            _sum = col_sum + matrix[k][i-1]
            if _sum < min_sum:
                min_sum = _sum
        if j > 0:
            _sum = matrix[j][i] + matrix[j-1][i]
            if _sum < min_sum:
                min_sum = _sum
        matrix[j][i] = min_sum
min_path = minimum
for m in range(len(matrix)):
    if matrix[m][i] < min_path:
        min_path = matrix[m][i]
print (min_path)

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

print('\n--------------------------SOLUTION 3,  Recursive solutions --------------------------')
t1  = time.time()

from functools import reduce

def euler82():
    f = open(filename, 'r' ).read()
    f = list( map(lambda x:  map( int, x.split(',')), f.splitlines() ) )
    f =  map( list, zip(*f))[::-1]
    def func(x,y):
        s = map(reduce.add,x,y)
        def part(s,x):
            smin = min(s)
            k = s.index(smin)
            if k == 0:
                left = []
            else:
                temp = min(x[k-1],smin)
                s[k-1] += temp - x[k-1]
                x[k-1] = temp
                left = part(s[:k],x[:k])
            if k == len(s)-1:
                right = []
            else:
                temp = min(x[k+1],smin)
                s[k+1] += temp - x[k+1]
                x[k+1] = temp
                right = part(s[k+1:],x[k+1:])
            return left + [smin] + right
        return part(s,x)
    return min(reduce(func,f))

euler82()

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')

# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')
#







