#!/usr/bin/python3
# Solved by Bogdan Trif @
#The  Euler Project  https://projecteuler.net
'''
                            Su Doku     -   Problem 96
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept.
Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar,
and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however,
is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column,
and 3 by 3 box contains each of the digits 1 to 9.
Below is an example of a typical starting puzzle grid and its solution grid.

                +-----------------------+         +-----------------------+
                   | 0 0 3 | 0 2 0 | 6 0 0 |         | 4 8 3 | 9 2 1 | 6 5 7 |
                   | 9 0 0 | 3 0 5 | 0 0 1 |         | 9 6 7 | 3 4 5 | 8 2 1 |
                   | 0 0 1 | 8 0 6 | 4 0 0 |         | 2 5 1 | 8 7 6 | 4 9 3 |
                   |-------+-------+-------|         |-------+-------+-------|
                   | 0 0 8 | 1 0 2 | 9 0 0 |         | 5 4 8 | 1 3 2 | 9 7 6 |
                   | 7 0 0 | 0 0 0 | 0 0 8 |         | 7 2 9 | 5 6 4 | 1 3 8 |
                   | 0 0 6 | 7 0 8 | 2 0 0 |         | 1 3 6 | 7 9 8 | 2 4 5 |
                   |-------+-------+-------|         |-------+-------+-------|
                   | 0 0 2 | 6 0 9 | 5 0 0 |         | 3 7 2 | 6 8 9 | 5 1 4 |
                   | 8 0 0 | 2 0 3 | 0 0 9 |         | 8 1 4 | 2 5 3 | 7 6 9 |
                   | 0 0 5 | 0 1 0 | 3 0 0 |         | 6 9 5 | 4 1 7 | 3 8 2 |
                   +-----------------------+         +-----------------------+

A well constructed Su Doku puzzle has a unique solution and can be solved by logic,
although it may be necessary to employ "guess and test" methods in order to eliminate options
(there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle;
the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles
ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid;
for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
'''
# Generate a 9x9 Matrix
from macpath import split
from copy import copy, deepcopy
from itertools import count
from numpy import transpose
import hashlib, time

#  ::::::::::::::::::::::::::::::         DIFFERENT METHODS TO LOAD A FILE          ::::::::::::::::::::::::::::::  #

# filename = "pb096_test_matrix.txt"
filename = "pb096_sudoku.txt"

def load_file_1(filename):
    M=[]
    with open(filename) as f:
        M = [list(map(int, line.rstrip('\n') )) for line in f.readlines()]
    return M

def load_file_2(filename):
    M=[]
    with open(filename, 'r') as f :
        for line in f :
            # print(line, type(line))
            M.append([ int(i) for i in line.rstrip('\n') ])
    return M

def load_file_3(filename) :
    f = open(filename, 'r')
    text = f.read()
    for row in text.split('\n'):
        if row[0] == 'G' :
            matrix = []
            Mall[row] = matrix
        else :
            matrix.append(list(map(int, row)))
    return matrix


Mall = {}
M = load_file_3(filename)
cnt= 0
S = 0
for k, v in Mall.items() :
    cnt+=1
    print(str(cnt)+'.    ' , k,'    ' ,v)


#############        END    DEFINITIONS        ####################

print('\n----------------------------------------------------------- \n')

t1  = time.time()



M = [[3, 0, 0, 8, 7, 0, 0, 0, 9], [0, 7, 9, 0, 5, 0, 1, 8, 0], [8, 0, 0, 0, 0, 0, 0, 0, 7], [1, 9, 7, 3, 4, 6, 8, 5, 2], [4, 5, 2, 7, 1, 8, 3, 9, 6], [6, 8, 3, 5, 9, 2, 7, 0, 0], [7, 0, 0, 0, 0, 0, 0, 0, 5], [0, 1, 6, 0, 3, 0, 4, 2, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
#     [[3, 4, 5, 8, 7, 1, 2, 6, 9], [2, 7, 9, 6, 5, 3, 1, 8, 4], [8, 6, 1, 4, 2, 9, 5, 3, 7], [1, 9, 7, 3, 4, 6, 8, 5, 2], [4, 5, 2, 7, 1, 8, 3, 9, 6], [6, 8, 3, 5, 9, 2, 7, 4, 1], [7, 3, 8, 2, 6, 4, 9, 1, 5], [5, 1, 6, 9, 3, 7, 4, 2, 8], [9, 2, 4, 1, 8, 5, 6, 7, 0]]
# M = [[6, 3, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 5, 0, 0, 0, 0, 8], [0, 0, 5, 6, 7, 4, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0, 0], [0, 0, 3, 4, 0, 1, 0, 2, 0], [0, 0, 0, 0, 0, 0, 3, 4, 5], [0, 0, 0, 0, 0, 7, 0, 0, 4], [0, 8, 0, 3, 0, 0, 9, 0, 2], [9, 4, 7, 1, 0, 0, 0, 8, 0]]
# M = [[0, 0, 4, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 3, 0, 0, 0, 2], [3, 9, 0, 7, 0, 0, 0, 8, 0], [4, 0, 0, 0, 0, 9, 0, 0, 1], [2, 0, 9, 8, 0, 1, 3, 0, 7], [6, 0, 0, 2, 0, 0, 0, 0, 8], [0, 1, 0, 0, 0, 8, 0, 5, 3], [9, 0, 0, 0, 4, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 8, 0, 0]]





# A Utility Function to print the Grid ---> NOT USED !!!
def print_grid( arr ) :
    for i in range(9):
        for j in range(9):
            print (arr[i][j], end='   ')
        print ()


def show_complete(M, grid_nr) :
        print('=='*6+'   '+str(grid_nr)+'   '+'=='*6)
        # print('=='*15 )
        for i in range(len(M)):
            print('  +++++   ', M[i] ,'   +++++  ')
        print('=='*15 )
        # print('\nCONGRATULATIONS !! SUDOKU Magic Puzzle has been Correctly Solved ! \n ')

# if solve_sudoku(M) :
#     show_complete(M, 16)


# Function to Find the entry in the Grid that is still  not used
# Searches the grid to find an entry that is still unassigned. If
# found, the reference parameters row, col will be set the location
# that is unassigned, and true is returned. If no unassigned entries
# remain, false is returned.
# 'l' is a list  variable that has been passed from the solve_sudoku function
# to keep track of incrementation of Rows and Columns
def find_empty_location(arr, l):        # FIND EMPTY LOCATION
    for row in range(9):
        for col in range(9):
            if(arr[row][col]==0):
                l[0]=row
                l[1]=col
                return True
    return False

# Returns a boolean which indicates whether any assigned entry
# in the specified row matches the given number.
def used_in_row(arr, row, num):         # ROW
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False

# Returns a boolean which indicates whether any assigned entry
# in the specified column matches the given number.
def used_in_col(arr, col, num):         # COLUMN
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False

# Returns a boolean which indicates whether any assigned entry
# within the specified 3x3 box matches the given number
def used_in_box(arr, row, col, num):            # 3x3 BOX
    for i in range(3):
        for j in range(3):
            if(arr[i+row][j+col] == num):
                return True
    return False

# Checks whether it will be legal to assign num to the given row,col
#  Returns a boolean which indicates whether it will be legal to assign
#  num to the given row,col location.
def check_location_is_safe(arr, row, col, num):         # ALL THREE COMBINED !!!!!!!!!!
    # Check if 'num' is not already placed in current row,
    # current column and current 3x3 box
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) \
           and not used_in_box(arr, row - row%3, col - col%3, num)


# Takes a partially filled-in grid and attempts to assign values to
# all unassigned locations in such a way to meet the requirements
# for Sudoku solution (non-duplication across rows, columns, and boxes)

print('\n-----------------------------------------------')

###### ============= THE MAIN BACKTRACKING ALGORITHM ======== ########
def solve_sudoku(M) :
    # 'l' is a list variable that keeps the record of row and col in find_empty_location Function
    l =[ 0, 0 ]
    # If there is no unassigned location, we are done, THIS SOLVES SUDOKU !!!
    if not find_empty_location(M, l )  :
        return True

    # We assign list values to row and col that we got from find_empty_location function
    row, col = l[0], l[1]

    for num in range(1,10) :
        # print(num, (row, col) , M)
            # if it looks promising :
        if (check_location_is_safe(M, row, col, num ) ) :
                # make tentative assignment
            M[row][col] = num
                    # Return If Success
            if solve_sudoku(M) :
                return True
                # IF failure, unmake & try again, this TRIGGERS BACKTRACKING !!!!
                # This resets the row, col of the matrix and removes the previous assignment M[row][col] = num
                # else IF FALSE :
            M[row][col] = 0
        print(num, (row, col) , M)

    return False





def main_solve_all_sudokus() :
    cnt= 0
    S = 0
    for g, M in Mall.items() :
        if solve_sudoku(M) :
            show_complete(M, g)
            res = int(''.join([str(i) for i in M[0][:3]]))
            S += res
            cnt+=1
            print(str(cnt)+'.    ' , g ,'       res = ' ,res ,'       M=   ',M)

    return print('\nAnswer : \t ', S)


# main_solve_all_sudokus()            #       Answer : 	  24702


solve_sudoku(M)

# if solve_sudoku(M) :
#     show_complete(M, 12)


t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')            #   Completed in : 69.630983 s