#  Created by Bogdan Trif on 01-07-2018 , 1:25 PM.

M = [[3, 0, 0, 8, 7, 0, 0, 0, 9], [0, 7, 9, 0, 5, 0, 1, 8, 0], [8, 0, 0, 0, 0, 0, 0, 0, 7], [1, 9, 7, 3, 4, 6, 8, 5, 2], [4, 5, 2, 7, 1, 8, 3, 9, 6], [6, 8, 3, 5, 9, 2, 7, 0, 0], [7, 0, 0, 0, 0, 0, 0, 0, 5], [0, 1, 6, 0, 3, 0, 4, 2, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

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


def solve_Sudoku( M   ) :
