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

Backtracking Algorithm
The idea is to place queens one by one in different columns, starting from the leftmost column.
When we place a queen in a column, we check for clashes with already placed queens.
In the current column, if we find a row for which there is no clash,
we mark this row and column as part of the solution.
If we do not find such a row due to clashes then we backtrack and return false.

1) Start in the leftmost column
2) If all queens are placed
    return true
3) Try all rows in the current column.  Do following for every tried row.
    a) If the queen can be placed safely in this row then mark this [row,
        column] as part of the solution and recursively check if placing
        queen here leads to a solution.
    b) If placing queen in [row, column] leads to a solution then return
        true.
    c) If placing queen doesn't lead to a solution then umark this [row,
        column] (Backtrack) and go to step (a) to try other rows.
3) If all rows have been tried and nothing worked, return false to trigger
    backtracking.

'''


import numpy as np
import time

M= np.zeros( ( 5 , 5 ), dtype=int)
# Here we place two queens
M[1][1] = 1
M[3][4] = 1
print(M)

def get_free_squares(M ) :
    '''         © Made by Bogdan Trif @ 2017-09-12
        :Description: In the N Queens problem get all the occupied squares as 1 ones
        and AVAILABLE squares as zeros.

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
    return True

# def next_free_pos(M, pos) :
#     ''' :Description: returns the next available position in the same row
#
#     :param M:
#     :param row:
#     :param pos:
#     :return:
#     '''
#     row = pos[0]
#     if is_row_free(M, row) :
#         for i in range(len(M[row])):



print(' get_free_squares : \n' , get_free_squares(M) )


# print('is_row_free : \t', is_row_free(M, 4) )


# def solveQueens(M):
#     pos = (0 , 0)


################################   BACKTRACKING ALGORITHM #################
print('\n-------------------BACKTRACKING ALGORITHM ----------------------- ')
t1  = time.time()


dim = 10
M= np.zeros( ( dim , dim ), dtype=int)

def print_board(board):
    for i in range(len(M)):
        print(M[i])

print_board(M)

# An utility function to check if a queen can be placed on board[row][col]. Note that this
# function is called when "col" queens are  already placed in columns from 0 to col -1.
# So we need to check only left side for  attacking queens

def is_location_safe(board, row, col):
    # Check row
    if  sum(board[row]) > 0 :
        return False

    # Check column
    if sum(M[ : , col ] ) > 0 :
        return False

    # Check diagonal 1
    if sum( M.diagonal(col-row)) > 0 :
        return False

    # Check diagonal 2 -> M[::-1] is the transpose matrix
    if sum( M[::-1].diagonal(row+col-len(board)+1)) > 0 :
        return False

    return True

def find_empty_row(board, pos ):

    for row in range(len(board)):
        if sum(board[row]) == 0:
            pos[0], pos[1] = row, 0
            return True
    return False


def solve_Queens( M ):
    pos = [0,0]
    #   If all queens are placed    return true
    if not find_empty_row(M, pos):
        return True

    row, col = pos

    for col in range(len(M[row])) :
        if is_location_safe(M, row, col):
            M[row][col] = 1

            if solve_Queens(M):
                return True

            # Backtracking
            M[row][col] = 0

    return False


N = solve_Queens(M)     # VICTORY . IT works !!!!! I made it @ 2017-10-27, 16:51
print('\n')
print_board(M)


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')            #   Completed in : 69.63 s






