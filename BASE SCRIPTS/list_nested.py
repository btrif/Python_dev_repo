#!/usr/bin/python

#import numpy as np

my_array=[['1', '2', '3', '7'], ['0', '1', '6', '9'], ['0', '1', '3', '9'], ['1', '2', '5', '8'], ['0', '1', '5', '8']]
my_array[3][2]
my_array.append(['2', '5'])
my_array.append([i for i in range(2,7,2)])
print(my_array)
my_array.append(['3','2',['1','4',['9','7','0','1']],'2','5','8'])
my_array.append(['3','2',['1','4',['9','7','0','1']],'2','5','8'])
my_array.append(['3','2',['1','4',['9','7','0','1']],'2','5','8'])
my_array.append(['3','2',['1','4',['9','7','0','1']],'2','5','8'])
my_array.append(['3','2',['1','4',['9','7','0','1']],'2','5','8'])

#Delete an element of the my_array
my_array.pop(8)
print(my_array[9][2][1])

# Removing items from a nested list Python
print(' -----------    This removes the i-th, i-th element from the array, e.g. : 2,2  3,3   and so on  ---------------')
families = [[0, 1, 2, 3, 4, 5, 6],[0, 1, 2, 3, 4, 5, 6],[0, 1, 2, 3, 4, 5, 6],[0, 1, 2, 3, 4, 5, 6],[0, 1, 2, 3, 4, 5, 6],[0, 1, 2, 3, 4, 5, 6],[0, 1, 2, 3, 4, 5, 6]]
print(families)
[x.remove(ind) for ind,x in enumerate(families) ]
print(families)

print('\n -----------    Removing a single item from a nested list Python  ---------------')
# Removing a single item from a nested list Python
lst = [['x',6,5,4],[4,5,6]]
print(lst)
lst[0].pop(0)       # the [0] access the first general element
print (lst)  #should print [[6, 5, 4], [4, 5, 6]]

print('-------'*20)
# Another way, more complicated
def nested_remove(L, x):
    if x in L:
        L.remove(x)
    else:
        for element in L:
            if type(element) is list:
                nested_remove(element, x)

m=[[34,345,232],[23,343,342]]
print(m)
nested_remove(m, 345)
print(m)

print('==============   MATRIX MANIPULATION ===================')
print('-------------  List of type MATRIX MANIPULATION, Print COLUMN   -------------')

#   If you have an array like

matrix = [[1, 2], [2, 3], [3, 4]]
#   Then you extract the first column like that:

print([row[0] for row in matrix])

A = [[1,2,3,4], [5,6,7,8]]
def column(matrix, i):
    return [row[i] for row in matrix]

print(column(A,1))

#import numpy as np
#B = np.array([[1,2,3,4],[5,6,7,8]])
#print(B[:,2])       # Returns the third column


# DIAGONAL of matrix
print('-------------  List of type MATRIX MANIPULATION, Print DIAGONAL   -------------')

def get_diagonal(m, i0, j0, d):     #m - matrix ;  i0 - start row  ; j0 - start column ;   d - directions
    return [m[(i0 + i - 1)%len(m)][(j0 + d*i - 1)%len(m[0])] for i in range(len(m))]

m = [[1,  2,   3,   4],\
         [5,  6,   7,   8],\
         [9, 10, 11, 12]]

print (get_diagonal(m, 1, 1, 1))    # [1, 6, 11]
print (get_diagonal(m, 1, 2, 1))    # [2, 7, 12]
print (get_diagonal(m, 1, 4,-1))   # [4, 7, 10]  This go in the other direction

# It even wraps around the matrix to get diagonals:

print( get_diagonal(m, 1, 4, 1))    # [4, 5, 10]
print (get_diagonal(m, 1, 1,-1) )   # [1, 8, 11]
print (get_diagonal(m, 3, 1, 1) )   # [9, 2, 7 ]