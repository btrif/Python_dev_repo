#!/usr/bin/python
# Solved by Bogdan Trif @
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
for i in matrix :    print(i)

# mT = transpose(matrix)
# print('\n',mT)


print('\n----------------- TEST FOR Smaller MaTriX -----------------------\n')

# m =[[150, 650, 250, 100, 50], \
#        [200, 100,  350, 950, 150],\
#        [650, 800, 750, 400, 100],\
#        [550, 700, 500, 150, 950],\
#        [800, 750, 500, 50,  350]]

# M=  [[131, 673, 234, 103, 18], \
#         [201, 96,  342, 965, 150],\
#         [630, 803, 746, 422, 111],\
#         [537, 699, 497, 121, 956],\
#         [805, 732, 524, 37,  331]]

M = [ [100,	100,	90,	100,	100],
[95,	80	,105,	110,	100],
[100,	20,	150,	115,	100],
[125,	95,	35,	100,	100],
[90,	95,	100,	95,	100] ]

print('------------------------------------The Original Matrix --------------')
for i in range(len(M)): print(M[i])


# print('\n---------------------------------The Transposed Matrix --------------')
#
# mT = transpose(m)
#
# for i in range(len(mT)): print(mT[i])



print('\n----------------------------------- The Computed PATH ---------------------')
# TRansposed

# M = [row[:] for row in mT]     # Making a copy of transposed matrix
# M = deepcopy(mT)          # deepcopy for cloning the transposed matrix
# B = zeros((len(M), len(M)), dtype=int)        # numpy Create a zeroed Matrix the same size
# print(B)

def make_dict(M) :
    ###### CONSTRUCT DICTIONARY.  We make the path dictionary :
    D={}
    for i in range(0, len(M) ):
        for j in range(0, len(M[i])-1, 1):
            if i==0:        # next pos
                # print( (i,j), M[i][j] ,'     -->  ' , (i+1, j) , M[i+1][j] , '       ', (i, j+1) , M[i][j+1] )
                D[ (i,j) ] = [(i+1, j), (i, j+1)  ]
            if  0< i < len(M) -1 :  # next pos
                # print( (i,j),M[i][j] ,'      --> ' , (i-1, j),M[i-1][j] ,'       ',(i+1,j) ,M[i+1][j] , '        ',(i, j+1) ,M[i][j+1] )
                D[ (i,j) ] = [(i-1, j), (i+1, j), (i, j+1)  ]

            if   i == len(M)-1 :    # next pos
                # print( (i,j),M[i][j] ,'      --> ' , (i-1, j),M[i-1][j] , '        ',(i, j+1) ,M[i][j+1] )
                D[ (i,j) ] = [(i-1, j),  (i, j+1)  ]

    print('\nD = ',D )
    return D

Track = {}
D= make_dict(M)
def next_pos(cur_pos, Track, D, M ) :
    oo = D[cur_pos]
    # print(oo,  [ M[i[0]][i[1]]  for i in oo ])

    for i in oo :
        if i in Track : oo.remove(i)
    L = [ M[i[0]][i[1]] + M[i[0]][i[1]+1]  if i[0] != cur_pos[0]  else M[i[0]][i[1]]  for i in oo   ]
    # print( [ i   for i in oo if i[1] < len(M)-1 ] )
    m = min(L)
    # if L.count(m) > 1 :
    #     ll = max([ (oo[i][1],oo[i][0]) for i in range(len(L)) if L[i] == m  ])
    #     print( 'max col = ', ll  )
    #     ll = ( ll[1], ll[0]  )

    ll = oo[L.index(m)]
    k = M[ll[0]][ll[1]]
    # print('min_index = ',  ll , '       min=', k, L.index(m) , '     ', L,'      ',oo )
    Track[ll] = 0
    return  k, ll



pos = (2, 1)
print('\nnext_pos : \t' ,next_pos( pos, Track, D, M  ) )
print('Track = ',Track ,'\n')







def min_three_ways_path(M) :

    ###### CONSTRUCT DICTIONARY.  We make the path dictionary :

    D = make_dict(M)

    #### PART 2 - find the min value by starting from every row with col = 0
    SS = 10**9
    for i in range( len(M)  ) :
        Track = {}
        pos = (i, 0)
        S = M[pos[0]][pos[1]]
        col = pos[1]
        Track[pos] = 0

        while col < len(M)-1 :
            val, pos = next_pos( pos, Track, D, M )
            print('val =',val, '    pos= ', pos, '      sum=', S, '             ',Track )
            col = pos[1]
            S += val
        print('---------  row =',i , '\t path= ', S ,'\n')
        if SS > S : SS = S

    return print('\nSmallest path cost : \t', SS)

M_test = [ [100,	100,	90,	100,	100],
[95,	80	,105,	110,	100],
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

M = M_test
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

print(sol)
print( min(sol))





print('\n---------TEST----------')

# bck = range(len(m)-1, -1, -1)
# fwd = range(0, len(m), 1)
# flag = 1
# if flag == 1: dir = fwd
# elif flag == -1 : dir = bck
#
# for i in dir :
#     for j in range(0, len(m)) :
#         print(m[i][j],end=',  ')
#         if i > 0 and  m[i][j] > m[i-1][j]:
#             flag = -1
#             dir = bck
#         else:
#             flag = 1
#             dir = fwd

# print('\nBacwards : ',bck)
# print('Forward : ',fwd)







