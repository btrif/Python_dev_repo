print('\n================  My FIRST SOLUTION,   ===============\n')

from libc.math cimport sin, cos, acos, exp, sqrt, fabs, M_PI
from libcpp cimport bool

# import math


# cpdef bool is_square(long x) :
#     long(sqrt(x))**2 == x

# def  is_square(x) :
#     return (sqrt(x))**2 == x



cpdef long non_rational_sides_triangles( long  constraint ) :
    cdef int cnt = 0
    cdef long Suma = 0
    cdef int b
    cdef long c
    cdef double Q
    cdef long Area
    for b in range(2, int( sqrt(constraint) )//2 , 2) :
        for c in range(b, constraint*2 // b, 2 ) :
            # Q = (b*b+1)*c*c + b*b
            Q = sqrt( ((b*b+1)*c*c + b*b ) )
            if Q%2 == 0 :
                Area = long( Q/2)


            # if is_square(Q) and Q%2 == 0 :
            #     Area = sqrt(Q)//2
                if Area <= constraint :

                    cnt+=1
                    print(str(cnt)+'.     b =  ', b ,'    c =  ', c ,  '         Area = ' , Area, '      Q= ', Q  )
                    Suma += Area

    print('Suma finala = ', Suma)
    return Suma

