#!/usr/bin/python

# DIAGONAL of matrix
print('-------------  List of type MATRIX MANIPULATION, Print DIAGONAL   -------------')

def get_diagonal(m, i0, j0, d):     #m - matrix ;  i0 - start row  ; j0 - start column ;   d - directions
    return [m[(i0 + i - 1)%len(m)][(j0 + d*i - 1)%len(m[0])] for i in range(len(m))]


m = [[1,    2,    3,    4],\
         [5,    6,    7,    8],\
         [9,   10,  11,  12],\
        [13,  14,  15,  16]]

print (get_diagonal(m, 1, 1, 1))    # [1, 6, 11]
print (get_diagonal(m, 1, 2, 1))    # [2, 7, 12]
print (get_diagonal(m, 1, 4,-1))   # [4, 7, 10]  This goes in the other direction

# It even wraps around the matrix to get diagonals:

print( get_diagonal(m, 1, 4, 1))    # [4, 5, 10]
print (get_diagonal(m, 1, 1,-1) )   # [1, 8, 11]        This goes in the other direction
print (get_diagonal(m, 3, 1, 1) )   # [9, 2, 7 ]
print('------------ OTHER TESTS ------------ ')

mtx = [[1,    2,    3,    4],\
           [5,    6,    7,    8],\
           [9,   10,   11,  12],\
          [13,  14,   15,  16]]

def get_diag(m, i0, j0, d):     #m - matrix ;  i0 - start row  ; j0 - start column ;   d - directions
    #return [m[(i0 + i - 1)%len(m)][(j0 + d*i - 1)%len(m[0])] for i in range(len(m)-1)]
    return [m[(i0 + i - 4)%len(m)][(j0 + d*i - 4)%len(m[0])] for i in range(len(m)-1)]

diagonal=[]
# this Diagonal method works :
print('------------------Only 3 elements taken from the DIRECT diagonal : -------------------')
for x in range(len(mtx)-2):
    for y in range(len(mtx)-2):
        print (get_diag(mtx, x, y, 1) )
        diagonal.append(get_diag(mtx, x, y, 1))
print('-------------This works fine !  --------------------\n')
print(type(diagonal),'  ;  Your test matrix is :',diagonal)

print('\n------------------Only 3 elements taken from the INVERSE diagonal : -------------------')

for g in range(len(mtx)-2):
    for h in range(len(mtx)-1, 1,-1):
        print (get_diag(mtx, g, h, -1) )
print('-------------This works fine too !  --------------------\n')
#print('This is perfect, it works !',len(mtx), mtx[0][0], mtx[3][3])

print('------------COLUMN OF A MATRIX -------------')
A = [[1,2,3,4], [5,6,7,8]]
def column(matrix, i):
    return [row[i] for row in matrix]

print(column(A,1))

print('------------------TRANSPOSE SQUARE GRID, TRANSPOSE MATRIX--------------------')
for i in range(len(mtx)):
    print([row[i] for row in mtx])

##########################################################
print('===='*20)
print('---------------- ACCESS MATRIX IN ALL DIRECTIONS  ---------------------\n')

# Open and read the file
f = open('matrix_file.txt', 'r')
text = f.read()

# Initialize and populate grid
grid = []

for row in text.split('\n'):
    grid.append(list(map(int, row.split(' '))))

maxprod = 0

# Display rows
print(' ------------  ROWS   :    ------------ ')
for i in range(6):
    for j in range(3):
        print(grid[i][j],grid[i][j+1],grid[i][j+2],grid[i][j+3], end=' ;   ')

# Find highest product in columns
print('\n ------------ COLUMNS   :    ------------ ')
for j in range(6):
    for i in range(3):
        print(grid[i][j] , grid[i+1][j] , grid[i+2][j], grid[i+3][j], end = ' ;   ')

# Find highest product in downward-right diagonal
print('\n ------------ DOWNWARD-RIGHT DIAGONAL   :    ------------ ')
for i in range(3):
    for j in range(3):
        print(grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3], end=' ;   ')

# Find highest product in upward-right diagonal
print('\n ------------ UPWARD-RIGHT DIAGONAL   :   ------------ ')
for i in range(3,6):
    for j in range(3):
        print(grid[i][j],grid[i-1][j+1],grid[i-2][j+2],grid[i-3][j+3], end=' ;   ')

# Find highest product in downward-left diagonal
print('\n ------------ DOWNWARD-LEFT DIAGONAL   :    ------------ ')
for i in range(3):
    for j in range(3,6):
        print(grid[i][j],grid[i+1][j-1],grid[i+2][j-2],grid[i+3][j-3], end=' ;   ')

# Find highest product in downward-left diagonal
print('\n ------------ UPWARD-LEFT DIAGONAL   :    ------------ ')
for i in range(3,6):
    for j in range(3,6):
        print(grid[i][j],grid[i-1][j-1],grid[i-2][j-2],grid[i-3][j-3], end=' ;   ')

f.close()

print('\n ================= COMPLEX MATRIX MANIPULATIONS ==============')
print('\n------------------ Get custom columns from a matrix -----------------')
M=[[0, 0, 3, 0, 2, 0, 6, 0, 0],
       [9, 0, 0, 3, 0, 5, 0, 0, 1],
       [0, 0, 1, 8, 0, 6, 4, 0, 0],
       [0, 0, 8, 1, 0, 2, 9, 0, 0],
       [7, 0, 0, 0, 0, 0, 0, 0, 8],
       [0, 0, 6, 7, 0, 8, 2, 0, 0],
       [0, 0, 2, 6, 0, 9, 5, 0, 0],
       [8, 0, 0, 2, 0, 3, 0, 0, 9],
       [0, 0, 5, 0, 1, 0, 3, 0, 0]]
print('Get last 3 columns of a matrix : ',  [row[-3:] for row in M])
print('Get columns 4:6 of a matrix : ',  [row[3:6] for row in M])

print('\n -------------   Performs a cut of a 3x3 sub matrix based on coord, find the ninant ')
def SubMatrix_3x3(x, y ):
    '''Function which cuts a given matrix  in 3x3 SubMatrices. In a 9x9 matrix there will be 9 3x3 matrices called Ninants
     Based on the position coordinate (x,y) returns the corresponding Ninant.
     Note: x, y values go from 1 up. 0 is excluded. Don't confuse with referencing matrix like M[0]
    :returns
    Returns the Ninant where the coordinate (x,y) lies in.    '''
    N =  M[((x-1)//3)*3 : ((x-1)//3)*3+3 ]      # This complicated expression do the work of slicing
    return [row[((y-1)//3)*3 : ((y-1)//3)*3+3] for row in N]

print('\n SubMatrix :   ',SubMatrix_3x3(5,6),'\n')


print('\n--------------- Get the index of a searched element from a matrix ------------')
matrix=[[1,2,19],[4,19,6],[7,8,9]]
val = 9
print([(index, row.index(val)) for index, row in enumerate(matrix) if val in row])

print('\n--------------- Returns TRUE if an element is in a matrix, Else return FALSE ------------')
print( [val in row for row in matrix])
print( True  if  True in [ val in row for row in matrix ]  else False)    # Nice List Comprehension Construction, by Bogdan Trif, 2016-11-01


print('\n--------------------Hash of a Matrix ----------------')
import hashlib

M = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 7, 9, 0, 5, 0, 1, 8, 0],
     [8, 0, 0, 0, 0, 0, 0, 0, 7],
     [0, 0, 7, 3, 0, 6, 8, 0, 0],
     [4, 5, 0, 7, 0, 8, 0, 9, 6],
     [0, 0, 3, 5, 0, 2, 7, 0, 0],
     [7, 0, 0, 0, 0, 0, 0, 0, 5],
     [0, 1, 6, 0, 3, 0, 4, 2, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]

signature = hashlib.md5(b'My Hello World !')
print('The Test of Hellow World :  ',  signature.hexdigest() )

X = M.copy() ;  Y = str(X)
print(' The initial  X Matrix Hash Signature :',  hashlib.md5( Y.encode() ).hexdigest())
X[8][8]= 10 ;  Y = str(X)
print(X)
print(' The MODIFIED  X Matrix Hash:',  hashlib.md5(Y.encode()).hexdigest() )
