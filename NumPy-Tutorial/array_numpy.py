import numpy as np

# using np to define a numpy array
from sympy.functions.combinatorial.numbers import nP

a = np.array([x for x in range(2,20)], int)
print('The numpy array is: \n', a)

b = np.array([x for x in range(2,50) if x % 2 !=0], float)
print(b)

c = np.array([x for x in range(2,50) if x % 2 !=0 and  x% 3 != 0], int)
print(c)

print('_____'*15)
d = np.array([1,2,3,4,5], float)
print(d)
e = np.array([1,2,3,4,5], int)
print(e)
# Test if a equals b:
print ('Compare two matrices if they are equal: ',d == e)
#Accesing element number from an array:
print('The element number six from array b is :',b[6])
'''
It is often useful, to create an array with the range function. With
the reshape–method you can create the object you want, if
needed:                         '''
print('-----'*20)
f = np.array(range(10), float)
print('Generate a matrix with range', f)
g =f.reshape(2,5)
print('Reshape: ', g)
print('Transpose: \n', g.transpose())
print('Flatten: ', g.flatten())
f = np.array([range(10), range(10,20), range(30,40)])
print(f)
print('_____'*15)

print('---------   Arrays of zeros and ones : -----------------')

h = np.zeros((2,3), dtype=int)
print(h)
m = np.ones((2,3), dtype=float)
print('Ones matrix: \n',m)

'''You can create a N by N identity matrix with the
identity–function. The eye–function returns matrices with ones
along the k-th diagonal:                        '''
#   Identity matrix:
print('Identity matrix: \n',np.identity(3, dtype=int))

print('__'*15,'MATHEMATICAL OPERATIONS', '___'*10)
print(' !!!!!!!!! ------------Attention A*B is not the DOT PRODUCT ------- use A.dot(B) -----------!!!!!!!!!!!!!')
A = np.array(([[1,2,3],[2,5,7],[7,4,2]]))
B = np.array([[8,7,4],[5,7,2],[1,6,2]])

print('\nTHE DOT PRODUCT: \n',np.dot(A,B))

print('\nTHE CROSS PRODUCT: \n',np.cross(A,B))

print('\nDETERMINANT OF MATRIX A: \n',np.linalg.det(A))

print('\nINVERSE OF MATRIX A: \n',np.linalg.inv(A))

#####################################
print('_____'*15)

print('\n------------------ print a single column :  -------------------------' )
A = np.array([[1,2,3,4],[5,6,7,8],[2,4,7,2]])
print(A)
print('A single column : \t' ,A[ : , 2])       # Returns the third column

print('\n-----------Count elements in an numpy array ------------------ : ')
print( np.count_nonzero( A == 2) )      # 2 is the element we want to count


print('\n ============= Diagonals in matrix : ================\n')

# Diagonals in matrix
matrix = np.array(         [[1,   2,   3,  4],      \
                                      [ 5,  6,   7,  8],        \
                                      [ 9,  10,  11,  12],      \
                                      [13,  4,  15,  16]]  )

print('Main diagonal : \n' , np.diagonal(matrix ) )
print('Main diagonal : \n' , matrix.diagonal( )  )
print('Main Secondary diagonal : \n' , matrix.diagonal( -1)  )
print('Main Secondary diagonal : \n' , matrix.diagonal( 1)  )

print(' Main Diagonal 2 : \n' , np.diagonal(matrix[::-1], 0 ) )
print('Main Diagonal 2 : \n' , matrix[ :: -1].diagonal(  )  )
print('Main Secondary diagonals 2: \n' , matrix[::-1].diagonal( -1)  )
print('Main Secondary diagonals 2: \n' , matrix[::-1].diagonal( 1)  )



diags = [matrix[::-1,:].diagonal(i) for i in range(-len(matrix)+1 , len(matrix))]
print('-------------- All the diagonals : --------------\n',diags)
diags.extend( matrix.diagonal(i) for i in range(3,-4,-1))
print ('\nAll the diagonals :',[n.tolist() for n in diags])
#print(diags)

print('\n------------  Product of a list using numpy--------------------')

print(np.prod([[1.,2.],[3.,4.]]))
print('Using Numpy the product of elements within Matrix is :  ',np.prod(matrix))
print('Display the maximum element :',np.max(matrix),'   ;   Display the index of the maximum element :', np.argmax(matrix))
print(np.array(matrix))


print('\n-------------------- Add entire row or columns to an array :----------------------- ')
A = np.array([[0, 1, 2], [0, 2, 0]])
print('----- Initial Matrix A  : \n', A)

new_row = [11, 12, 13]
A = np.row_stack([A, new_row] )
print('----- Matrix A after row insertion : \n', A)

new_col = [7, 8, 9]
A = np.column_stack([A, new_col])
print('----- Matrix A after column insertion : \n', A ,'\n')

T = np.array([])
T = np.column_stack( [4,5,6] )
print(T,'\n')
T = np.row_stack([ T, new_col ])
print(T,'\n')

T = np.row_stack([ T, [8,0,5] ])
print(T,'\n')

print('\n----------------- Insert  ROWS, COLUMNS at the specified location --------------')

import numpy as np
N = 4
a = np.random.rand(N,N)
b = np.zeros((N,N+1))
b[:,:-1] = a
print( a.shape , b.shape )
import timeit

# Method I
c = np.hstack((a, np.zeros((a.shape[0], 1), dtype = int)  ))
print(' c: \n',c)

# Method II
d = np.insert(a, 3, values=[-1,-2,-3,-4], axis=1)
print('d : \n',d)

print('\n----------------- Delete ROWS, COLUMNS at the specified location --------------')
arr = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print('Initial array : \n',arr)

arr = np.delete(arr, 1, 0)
print(' --------- Deletes the row 1 : \n',arr)

arr = np.delete(arr, 2, axis=1)
print(' -------- Deletes the column 2, (axis =1 is column, axis=0 is a row ) :\n', arr)

print('\n--------------- Add single element to a numpy array-----------------')
A = np.array([], dtype = int )
A = np.append(A, [1]) ; A = np.append(A, [2]) ; A = np.append(A, [3]) ; A = np.append(A, [5]) ; A = np.append(A, [7]) ;

print('the numpy array is : \t',A)


print('\n------------------ Find elements in the numpy array -------------------')

M = np.zeros([4,4])
M[0][1] = 1
M[2][2] = 1

# Method I
print(' Get nonzero elements of M : \t',np.nonzero(M))

# Method II
print(' Get elements with condition : \r', np.where(M ==1))
for i in np.where(M ==1) : print(i)
