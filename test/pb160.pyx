cpdef double pb160_BF( double lim ) :
    cdef double P = 1
    for n in range(1, lim+1) :
        P *= n
        m = n
        while m%5 == 0 :
            P //= 10
            m //= 5

        # print(n, '    ' , P)

        P %= 10**13

    print('\n ANSWER = ', P%10**5 )
    return P%10**5