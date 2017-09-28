#                               Comma-separated values (CSV)

from numpy import *

M = random.rand(3,4)
print(M)
# Using numpy.savetxt we can store a Numpy array to a file in CSV format:
savetxt("random-matrix.csv", M)

print('\n-------'*10,'MATRIX OPERATIONS','-------'*10)

print('\n print a single column : ', M[:, 0])

print('\nDescribe the shape of the Matrix:  ',M.shape)

print('\nDescribe the number of object within the matrix:  ',M.size)

print('\nPrint the MIN value of each row: ', amin(M,axis=1))

print('\nPrint the minimum value of each column: ',amin(M,axis=0))

print('\nPrint the max value of each row: ', amax(M,axis=1))

print('\nPrint the MAX value of each column: ',amax(M,axis=0))

print('\nPrint the MEAN value of each column: ',mean(M,axis=0))

print('\nPrint the SUM value of each column: ', sum(M, axis=0))
N = random.rand(3,3)
print(N)
print('\nPrint the TRACE : ', trace(N))

print('\nPrint the MAIN diagonal : ', diagonal(N))
print('\nPrint the SECONDARY diagonal : ', diag(fliplr(M)) )

print('\n---------------Assign columns in a matrix ------------------')
N[:,0] = [3,8,9]
print('\n',N)
N[:,2] = [7,5,3]
print('\n', N )

print(' !!!!!!!!! ------------Attention A*B is not the DOT PRODUCT ------- use A.dot(B) -----------!!!!!!!!!!!!!')

print('\nPrint the TRANSPOSE matrix : ', transpose(N))
print('\nPrint how many bytes has an elemnt: ',N.itemsize)
print('\nPrint total number of bytes of the MaTriX: ',N.nbytes)
print('\nPrint total number of dimensions the MaTriX: ',N.ndim)
print('-------'*10,'END','-------'*10)
savetxt("random-matrix_2.csv", M, fmt='%.5f') # fmt specifies the format

#           Numpy's native file format
#Useful when storing and reading back numpy array data. Use the functions numpy.save and numpy.load:
save("random-matrix_3.npy", M)
load("random-matrix_3.npy")

print('\n ----------------- The power of a matrix, taking the power of a matrix -----------------  ')
from numpy import linalg as LA

Init = array([0.1, 0.9])
Trans = array([[0.6, 0.4],[0.15, 0.85]])

Trans_sq =LA.matrix_power(Trans, 2)
print(' The matrix is : \n', Trans)
print('The matrix taken to the power 2 is : \n', Trans_sq )

