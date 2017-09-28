#  Created by Bogdan Trif on 10-09-2017 , 6:57 PM.
'''
Given nxn board place n queen on this board so that they dont attack each other. One solution is to find
 * any placement of queens which do not attack each other. Other solution is to find all placements of queen
 * on the board.
 Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' '
 both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:
[ [".Q..",          // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",       // Solution 2
  "Q...",
  "...Q",
  ".Q.."]]

 * Time complexity O(n*n)
 * Space complexity O(n*n)

 https://github.com/mission-peace/interview/blob/master/src/com/interview/recursion/NQueenProblem.java

'''


import numpy as np

M= np.zeros( ( 5 , 5 ), dtype=int)
M[1][1] = 1
M[3][4] = 1
print(M)

def get_free_squares(M ) :
    '''         © Made by Bogdan Trif @ 2017-09-12
        :Description: In the N Queens problem get all the occupied squares as 1 ones
        and unoccupied squares as zeros.

    :param M: Matrix to analyze
    :return: grid 2D,  all the unoccupied squares as zeros, occupied squares as ones    '''
    l = len(M)
    N = np.zeros( (l, l) , dtype=int )
    # print('N :',N)
    # O = np.where(M ==1)
    for i in range(len(N)):
        for j in range(len(N[i])):
            if M[i][j] == 1 :
                # print(i,j)
                I  =  ( i, j )
                # row , col =  i, j

                # Insert corresponding row
                N = np.delete(N, I[0], 0)
                # print('N2 : \n',N)
                # print( np.ones(( N.shape[0] , 1 ), dtype=int )   )
                N = np.insert(N, I[0], values=np.ones((1, l)) , axis=0 )
                # print ('N3 ROW insertion : \n', N )

                # Insert corresponding column
                N = np.delete(N, I[1], axis=1)
                # print('N4 : \n',N)
                # print( np.ones((1, N.shape[1]  ), dtype=int )   )
                N = np.insert(N, I[1], values=np.ones(( 1, l)) , axis=1 )
                # print ('N5  COLUMN insertion : \n', N )

                row , col = I
                # print(' Chosen position : row, col = ', row, col)
                # Diagonal I
                d1 = row - col
                if d1 < 0 :
                    row1 = 0
                    col1 = abs(d1) + row1
                if d1 > 0 :
                    col1 = 0
                    row1 = col1 + d1
                if d1 == 0 :
                    row1 = 0
                    col1 = 0

                # print('\nrow1, col1 = ', row1, col1 , '    d1 = ', d1)
                while col1 < l  and row1 < l :
                    # print( N[row1][col1] , '        row1, col1 = ',row1, col1 )
                    N[row1][col1] = 1
                    col1+=1
                    row1+=1
                # print('N6 : after diagonal 1 : \n', N )

                # Diagonal II
                d2 = (row + col)
                if row + col >= l :
                    col2 = l-1
                    row2 = d2 - col2
                if row + col < l :
                    row2 = 0
                    col2 = d2 - row2
                if row + col == l-1 :
                    row2 = 0
                    col2 = l-1

                # print('\nrow2, col2 = ', row2, col2 , '    d2 = ', d2)
                while col2 >= 0  and  row2 < l :
                    # print( N[row2][col2] , '        row2, col2 = ',row2, col2 )
                    N[row2][col2] = 1
                    col2-=1
                    row2+=1
                # print('N6 : after diagonal 2 : \n', N )

    return N

def is_row_free(M, row) :
    '''Uses the function get_free_squares(M) to find available spots

        :param M: matrix, grid 2D
        :param row: the row we are investigating
        :return: boolean, True or False             '''

    N = get_free_squares(M)
    if  sum(N[row]) == len(N[row]) :
        return False
    return

def next_free_pos(M, pos) :
    ''' :Description: returns the next available position in the same row

    :param M:
    :param row:
    :param pos:
    :return:
    '''
    row = pos[0]
    if is_row_free(M, row) :
        for i in range(len(M[row])):



print(' get_free_squares : \n' , get_free_squares(M) )


print('is_row_free : \t', is_row_free(M, 4) )


def solveQueens(M):
    pos = (0 , 0)