import pb390

import time

t1  = time.time()


print( 'test_function cython : \t'  ,  pb390.non_rational_sides_triangles(10**6) )
# print( 'test_function cython : \t'  ,  pb276.Ccombinations(3, [1,2,3,4,5,6] ) )



t2  = time.time()
cy = t2-t1
print('Completed in :', round((cy)*1000,6), 'ms')

#
# t1  = time.time()
#
#
# print( '\ntest_function Python : \t' ,test_python.test_function(10**7) )
#
#
# t2  = time.time()
# py = t2-t1
# print('Completed in :', round((py)*1000,6), 'ms')
#
# print('\nCython is ' , round(py/cy,2) , 'x   faster')






