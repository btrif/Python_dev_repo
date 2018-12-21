#                               Comma-separated values (CSV)

import numpy as np

M = np.random.rand(3,4)
print(M)
# Using numpy.savetxt we can store a Numpy array to a file in CSV format:
np.savetxt("random-matrix.csv", M)

print('\n-------'*10,'MATRIX OPERATIONS','-------'*10)

print('\n print a single column : ', M[:, 0])

print('\nDescribe the shape of the Matrix:  ',M.shape)

print('\nDescribe the number of object within the matrix:  ',M.size)

print('\nPrint the MIN value of each row: ', np.amin(M,axis=1))

print('\nPrint the minimum value of each column: ',np.amin(M,axis=0))

print('\nPrint the max value of each row: ', np.amax(M,axis=1))

print('\nPrint the MAX value of each column: ', np.amax(M,axis=0))

print('\nPrint the MEAN value of each column: ', np.mean(M,axis=0))

print('\nPrint the SUM value of each column: ', np.sum(M, axis=0))
N = np.random.rand(3,3)
print(N)
print('\nPrint the TRACE : ', np.trace(N))

print('\nPrint the MAIN diagonal : ', np.diagonal(N))
print('\nPrint the SECONDARY diagonal : ', np.diag(np.fliplr(M)) )

print('\n---------------Assign columns in a matrix ------------------')
# Insert to the 1-st Column
N[:,0] = [3,8,9]
print('\n',N)
# Insert to the 3-rd Column
N[:,2] = [7,5,3]
print('\n', N )


print('\n---------------Assign row in a matrix ------------------')
# Insert to the 2-nd ROW
N[1] =  [ 13, 18, 19 ]
print('\n', N )


print('\n------     How to “embed” a small numpy array into a predefined block of a large numpy array?  -----------')
# https://stackoverflow.com/questions/7115437/how-to-embed-a-small-numpy-array-into-a-predefined-block-of-a-large-numpy-arra
# I have a small NXN array "block" that I want to plug into a specified region (i.e., a diagonal region at "start")
# of a large array "wall". Is there an efficient method to archive this?

wall = np.zeros((10,10), dtype=np.int )
block = np.arange(1,7).reshape(2,3)

print('wall : \n', wall)
print('block : \n', block)

#We want to insert at the position :
x = 2
y = 3

wall[ x : x + block.shape[0], y : y + block.shape[1]] = block       ### GREAT FEATURE !!

print('wall : \n', wall )



print(' !!!!!!!!! ------------Attention A*B is not the DOT PRODUCT ------- use A.dot(B) -----------!!!!!!!!!!!!!')

print('\nPrint the TRANSPOSE matrix : ', np.transpose(N))
print('\nPrint how many bytes has an elemnt: ',N.itemsize)
print('\nPrint total number of bytes of the MaTriX: ',N.nbytes)
print('\nPrint total number of dimensions the MaTriX: ',N.ndim)
print('-------'*10,'END','-------'*10)
np.savetxt("random-matrix_2.csv", M, fmt='%.5f') # fmt specifies the format

#           Numpy's native file format
#Useful when storing and reading back numpy array data. Use the functions numpy.save and numpy.load:
np.save("random-matrix_3.npy", M)
np.load("random-matrix_3.npy")

print('\n ----------------- The power of a matrix, taking the power of a matrix -----------------  ')
from numpy import linalg as LA

Init = np.array([0.1, 0.9])
Trans = np.array([[0.6, 0.4],[0.15, 0.85]])

Trans_sq =LA.matrix_power(Trans, 2)
print(' The matrix is : \n', Trans)
print('The matrix taken to the power 2 is : \n', Trans_sq )

