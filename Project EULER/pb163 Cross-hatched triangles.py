#  Created by Bogdan Trif on 08-10-2017 , 11:01 AM.
# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                        Cross-hatched triangles     -       Problem 163

Consider an equilateral triangle in which straight lines are drawn from each vertex to the middle
of the opposite side, such as in the size 1 triangle in the sketch below.


Sixteen triangles of either different shape or size or orientation or location can now be observed in that triangle.
Using size 1 triangles as building blocks, larger triangles can be formed, such as the size 2 triangle in the above sketch.
One-hundred and four triangles  (104) of either different shape or size or orientation or location
can now be observed in that size 2 triangle.

It can be observed that the size 2 triangle contains 4 size 1 triangle building blocks.
A size 3 triangle would contain 9 size 1 triangle building blocks and
a size n triangle would thus contain n^2 size 1 triangle building blocks.

If we denote T(n) as the number of triangles present in a triangle of size n, then

T(1) = 16
T(2) = 104

Find T(36).

'''
import time, zzz, math
import itertools, operator, functools


def get_unique_factors(n):       ### o(^_^)o  FASTEST  o(^_^)o  ###
    ''' Decompose a factor in its prime factors. This function uses the pyprimes module. THE FASTEST  '''
    from pyprimes import factorise
    print( list( factorise(n)) )
    # return [val for sublist in [[i[0]]*i[1] for i in factorise(n)] for val in sublist]
    return [val[0] for val in factorise(n)]




print('\n--------------------------TESTS------------------------------')
t1  = time.time()

T = [1, 2, 3,  6]
T_ = []
for i in range(2, 3) :
    for j in T :
        T_.append(j*i*i)

    T = T+T_
    print(T)

print()

# n = 16
# for i in range(2, 36+1 ) :
#     print(str(i) +'.       ' ,n  , i*i , math.factorial( i ) , '            Close result =  ',  n*(1+i*i  ) + math.factorial( i+2 )   )




t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()





# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')




