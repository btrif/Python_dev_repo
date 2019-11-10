#  Created by Bogdan Trif on 03-11-2019 , 12:28 PM.


'''

Use fsolve to find the solution of the following two equations :

f(x,y) = 2*x^(2/3) + y^(2/3) − 9^(1/3)
g(x,y) = x^2/4 + y^(1/2) − 1


Use the initial guess (init conds. ) :  x_0=1, y_0=1

'''


from scipy.optimize import linprog
from numpy.linalg import solve
from scipy.optimize import minimize
import scipy.optimize
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
import time

t1  = time.time()

# https://stackoverflow.com/questions/19843116/passing-arguments-to-fsolve

def func( init_cond , *x_y_z ):
    '''     per             https://www.veltech.edu.in/wp-content/uploads/2016/04/Paper-09-15.pdf    -    section I
    '''
    p, q, r = init_cond
    a, b, c = x_y_z
    f = np.zeros(3)
    f[0] =  p**2 + q**2 - r**2 -1
    f[1] = (a+p)**2 + (b+q)**2 - (c+r)**2 - 1
    f[2] = (2*a-p)**2 + (2*b-q)**2 - (2*c-r)**2 - 1

    return f

#############           HERE IS THE PATTERN      !!!!!!!!!         ################
x_y_z = ( 3, 4, 5 )        # works         p, q, r  =  1.0 3.0 3.0
# x_y_z = ( 5, 12, 13 )        # works         p, q, r  =  1.0 5.0 5.0
# x_y_z = ( 7, 24, 25 )      # works           p, q, r  =  1.0 7.0 7.0
# x_y_z = ( 9, 40, 41 )          # works          p, q, r  =  1.0 9.0 9.0
# x_y_z = ( 11, 60, 61)              # works      p, q, r  =  1.0 11.0 11.0
# x_y_z = ( 13, 84 ,85)              # works      p, q, r  =  1.0 13.0 13.0
# x_y_z = ( 15, 112, 113)              # works      p, q, r  =  1.0 15.0 15.0
# x_y_z = ( 17, 144 ,145)              # works      p, q, r  =  1.0 17.0 17.0


a, b, c = x_y_z
A = fsolve( func, [ 0 , a  , a  ],  args=x_y_z )


# As we see bellow  the computed values of the fnct func(x,y,z) = 0,0,0 pretty close to 0 which means that
# fsolve evaluated our problem correctly
print('GENERAL SOLUTION : ' , A, '    ;              Evaluation of soln :   ',func( A, *x_y_z )  )

p, q, r = np.round(A)
print(' Solution :  ', A , '  ;        Soln.  rounded :       p, q, r  = '  , p, q, r  )


X= lambda p, q, r : p**2 + q**2 - r**2 -1
X2= lambda p, q, r, a, b, c : (a+p)**2 + (b+q)**2 - (c+r)**2 -1
X3= lambda p, q, r, a, b, c : (2*a-p)**2 + (2*b-q)**2 - (2*c-r)**2 -1



# (1, 3, 3) & (2, 1, 2) ---->  BOTH are valid solutions !! with a, b, c = 3, 4, 5
print(' Function 1 check :   ', X(p, q, r) ,'       ',   X(p, q, r) == 0 )
print(' Function 2 check :   ', X2(p, q, r, a, b, c) ,'       ',   X2(p, q, r, a, b, c) == 0 )
print(' Function 3 check :   ', X3(p, q, r, a, b, c) ,'       ',   X3(p, q, r, a, b, c) == 0 )





t2  = time.time()
print('\nCompleted in :', round((t2-t1),6), 's\n\n')