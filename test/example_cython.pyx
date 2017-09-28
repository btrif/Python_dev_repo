cpdef double test_function(int x):
    cdef double y = 0
    cdef int i                      # This line makes a HUGE Difference
    for i in range(x):
        y += i
    return y




