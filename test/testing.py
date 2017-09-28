import example_cython , test_python
import  test_python
# from example_cython import test_function

import time

t1  = time.time()


print( 'test_function cython : \t'  ,example_cython.test_function(10**7) )



t2  = time.time()
cy = t2-t1
print('Completed in :', round((cy)*1000,6), 'ms')


t1  = time.time()


print( '\ntest_function Python : \t' ,test_python.test_function(10**7) )


t2  = time.time()
py = t2-t1
print('Completed in :', round((py)*1000,6), 'ms')

print('\nCython is ' , round(py/cy,2) , 'x   faster')






