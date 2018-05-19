#  http://sam-marsh.staff.shef.ac.uk/mas115/docs/PYTHON-Lecture10.pdf
import numpy as np

a = np.array([[3, 6, -5], [1, -3, 2], [5, -1, 4]])
b = np.array([12, -2, 10])

# finding matrice X=([x, y, z]) si by multiplying a**-1 with b
x = np.linalg.inv(a).dot(b)

print('Inverse of matrice a is   a**-1:   \n',   np.linalg.inv(a))
print('Solution to the equation is:  X = ',x)

# Let's check whether ax = b
print('Matrices multipliplication a * b = ', np.dot(a, x))
# the last vector is equivalent to b !

'''======================SECOND WAY =========================='''

a = np.array([[1, 2], [3, 5]])
b = np.array([7, 21])
print('Product of the matrices a * b = ', np.dot(a , b))
print('Second way of Product of the matrices a * b = ', a.dot(b))



